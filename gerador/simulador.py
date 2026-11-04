"""Página /simulador-financiamento/ — simulador de financiamento imobiliário (SAC e Price).

As taxas abaixo são REFERÊNCIAS para a estimativa. Atualize a lista e as datas quando houver dados novos.
- Bancos (linha SBPE, taxa de balcão + TR): tabelas de setembro/2026 divulgadas pelos bancos e compiladas pela imprensa.
- Sicoob e Sicredi: taxas médias de novas operações divulgadas pelo Banco Central (julho/2026).
- Minha Casa, Minha Vida: regras válidas a partir de 22/04/2026 (Portaria MCID). Usamos a taxa MAIS ALTA de cada faixa
  para não prometer parcela menor do que a real; cotistas do FGTS podem conseguir taxa menor.
"""
import json

TAXAS_DATA = "setembro/2026"
BANCOS = [
    {"id": "caixa", "nome": "Caixa Econômica Federal", "taxa": 11.19},
    {"id": "itau", "nome": "Itaú", "taxa": 11.60},
    {"id": "santander", "nome": "Santander", "taxa": 11.69},
    {"id": "bradesco", "nome": "Bradesco", "taxa": 11.70},
    {"id": "bb", "nome": "Banco do Brasil", "taxa": 12.00},
    {"id": "sicoob", "nome": "Sicoob", "taxa": 9.87, "ref": "média BC jul/2026"},
    {"id": "sicredi", "nome": "Sicredi", "taxa": 10.27, "ref": "média BC jul/2026"},
]
# Minha Casa, Minha Vida (área urbana). teto = valor máximo do imóvel; nas faixas 1 e 2 varia por município (até R$ 275 mil).
MCMV = [
    {"faixa": 1, "renda": 3200, "teto": 275000, "taxa": 5.25},
    {"faixa": 2, "renda": 5000, "teto": 275000, "taxa": 7.00},
    {"faixa": 3, "renda": 9600, "teto": 400000, "taxa": 8.16},
    {"faixa": 4, "renda": 13000, "teto": 600000, "taxa": 10.50},
]

CSS = """
.sim{display:grid;grid-template-columns:minmax(0,380px) minmax(0,1fr);gap:28px;padding-block:8px 40px;align-items:start}
@media (max-width:860px){.sim{grid-template-columns:minmax(0,1fr)}}
.res,.sim-form{min-width:0}
.sim-form{background:var(--surface);border-radius:20px;padding:20px;display:grid;gap:14px}
.sim-form .field input,.sim-form .field select{background:var(--bg);font-variant-numeric:tabular-nums}
.sim-form .row{display:grid;grid-template-columns:1fr 1fr;gap:10px;align-items:start}
.sim-form .hint{font-size:.78rem;color:var(--muted);margin-top:2px}
.seg{display:grid;grid-template-columns:1fr 1fr;background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:3px;gap:3px}
.seg button{border:0;background:transparent;padding:9px;border-radius:9px;font-weight:600;cursor:pointer;color:var(--muted)}
.seg button[aria-pressed="true"]{background:var(--accent);color:#1F1B17}
.res{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;min-width:0}
.res>*,.sim>*{min-width:0}
.res-main{background:#1F1B17;color:#fff;border-radius:20px;padding:22px;display:grid;gap:14px}
.res-main small{color:rgba(255,255,255,.7);display:block;font-size:.8rem}
.res-big{font-family:var(--display);font-size:clamp(2rem,5vw,2.6rem);font-weight:700;color:var(--accent);line-height:1.05}
.res-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media (max-width:520px){.res-grid{grid-template-columns:1fr 1fr}}
.res-grid b{font-size:1.05rem;font-variant-numeric:tabular-nums}
.res-main .btn{width:100%;white-space:normal;text-align:center}
.res-main,.res-grid>div{min-width:0}
.fit{font-size:.85rem;font-weight:600;border-radius:10px;padding:8px 10px}
.fit.ok{background:rgba(52,199,89,.16);color:#7EE2A0}
.fit.no{background:rgba(255,99,71,.16);color:#FFB4A6}
.tag{display:inline-block;font-size:.7rem;font-weight:700;background:var(--accent);color:#1F1B17;border-radius:6px;padding:1px 6px;margin-left:6px;vertical-align:middle}
.alert{background:var(--accent-soft);border-radius:14px;padding:12px 14px;font-size:.9rem}
.cmp-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:16px}
.cmp{width:100%;border-collapse:collapse;font-size:.9rem;font-variant-numeric:tabular-nums;min-width:520px}
.cmp th,.cmp td{padding:11px 12px;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}
.cmp th:first-child,.cmp td:first-child{text-align:left}
.cmp thead th{background:var(--surface);font-size:.78rem;color:var(--muted);font-weight:600}
.cmp tr.sel td{background:var(--accent-soft);font-weight:700}
.cmp tbody tr{cursor:pointer}
.aviso{font-size:.8rem;color:var(--muted);max-width:80ch}
.faq details{border-bottom:1px solid var(--line);padding:12px 0}
.faq summary{font-weight:600;cursor:pointer}
.faq p{color:var(--muted);margin:8px 0 0}
"""


def corpo(ICON_PIN, e, wa_link_padrao, imoveis_js):
    return f'''
<div class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › Simulador de financiamento</nav>
  <div class="pg-head">
    <h1>Simulador de financiamento de imóvel</h1>
    <p>Calcule a parcela, a entrada e a renda necessária para financiar sua casa, apartamento ou terreno em Joaçaba e região. Compare Caixa, Banco do Brasil, Santander, Bradesco, Itaú e cooperativas em segundos.</p>
  </div>
  <div class="sim">
    <form class="sim-form" id="simf" autocomplete="off">
      <div class="field"><label for="s-imovel">Imóvel (opcional)</label><select id="s-imovel"><option value="">Digitar o valor</option></select></div>
      <div class="field"><label for="s-valor">Valor do imóvel</label><input id="s-valor" inputmode="numeric" value="R$ 500.000"></div>
      <div class="row">
        <div class="field"><label for="s-entrada">Entrada</label><input id="s-entrada" inputmode="numeric" value="R$ 100.000"><span class="hint" id="s-entpct">20% do imóvel</span></div>
        <div class="field"><label for="s-fgts">FGTS (opcional)</label><input id="s-fgts" inputmode="numeric" value="R$ 0"></div>
      </div>
      <div class="field"><label for="s-renda">Renda familiar bruta (por mês)</label><input id="s-renda" inputmode="numeric" placeholder="R$ 0"><span class="hint">Some a renda de quem vai financiar junto. Usamos para escolher a taxa e ver se a parcela cabe.</span></div>
      <div class="field"><label for="s-banco">Banco</label><select id="s-banco"></select></div>
      <div class="row">
        <div class="field"><label for="s-taxa">Juros ao ano (%)</label><input id="s-taxa" inputmode="decimal" value="11,19"><span class="hint" id="s-taxahint">Taxa escolhida automaticamente. Pode ajustar.</span></div>
        <div class="field"><label for="s-prazo">Prazo (anos)</label><select id="s-prazo"></select></div>
      </div>
      <div class="field"><label>Tabela de amortização</label>
        <div class="seg" role="group" aria-label="Tabela"><button type="button" data-t="sac" aria-pressed="true">SAC</button><button type="button" data-t="price" aria-pressed="false">Price</button></div>
        <span class="hint" id="s-tabhint">SAC: parcelas começam maiores e diminuem com o tempo.</span>
      </div>
    </form>

    <div class="res" aria-live="polite">
      <div class="res-main">
        <div><small id="r-lbl">Primeira parcela estimada</small><div class="res-big num" id="r-parc">—</div></div>
        <div class="fit" id="r-fit" hidden></div>
        <div class="res-grid">
          <div><small id="r-lbl2">Última parcela</small><b id="r-ult">—</b></div>
          <div><small>Valor financiado</small><b id="r-fin">—</b></div>
          <div><small>Renda mínima*</small><b id="r-renda">—</b></div>
          <div><small>Total de juros</small><b id="r-juros">—</b></div>
          <div><small>Total pago</small><b id="r-total">—</b></div>
          <div><small>Prazo</small><b id="r-prazo">—</b></div>
        </div>
        <a class="btn btn-accent" id="r-wa" href="{e(wa_link_padrao)}" target="_blank" rel="noopener">Quero simular oficialmente com a Manu</a>
      </div>
      <div class="alert" id="r-alert" hidden></div>
      <div>
        <h2 style="font-size:1.25rem;margin:6px 0 10px">Compare os bancos</h2>
        <div class="cmp-wrap"><table class="cmp" id="cmp">
          <thead><tr><th>Banco</th><th>Juros a.a. (+TR)</th><th>1ª parcela SAC</th><th>Parcela Price</th><th>Renda mínima*</th></tr></thead>
          <tbody></tbody>
        </table></div>
        <p class="aviso" style="margin-top:8px">Toque em um banco para simular com ele.</p>
      </div>
      <p class="aviso">* Renda mínima considerando que a parcela compromete até 30% da renda bruta familiar, regra usada pela maioria dos bancos.
      Esta é uma <b>estimativa</b> para ajudar no planejamento. As taxas dos bancos são as de balcão da linha tradicional (SBPE), divulgadas em {TAXAS_DATA}; as do Sicoob e do Sicredi são médias do Banco Central (julho/2026). No Minha Casa, Minha Vida usamos a taxa mais alta de cada faixa (regras de abril/2026); cotistas do FGTS podem conseguir taxa menor, e nas faixas 1 e 2 o valor máximo do imóvel varia por município. Clientes com relacionamento no banco (salário, seguros, investimentos) podem conseguir taxas menores. Os valores não incluem TR, seguros obrigatórios (MIP e DFI) nem tarifas, que fazem parte do Custo Efetivo Total (CET).
      A taxa, a entrada mínima e a aprovação dependem da análise de crédito de cada banco. Para uma simulação oficial, fale com a Manu.</p>
    </div>
  </div>
</div>

<section class="block alt"><div class="wrap faq">
  <div class="sec-head"><div><h2>Dúvidas sobre financiamento</h2></div></div>
  <details><summary>Qual a diferença entre SAC e Price?</summary><p>Na tabela SAC a parcela começa maior e diminui todo mês, e no total você paga menos juros. Na Price a parcela é praticamente fixa, começa menor, mas o total de juros é maior.</p></details>
  <details><summary>Quanto preciso de entrada?</summary><p>Na maioria dos bancos, o financiamento cobre até 80% do valor do imóvel, então a entrada mínima costuma ser de 20%. Em programas como o Minha Casa, Minha Vida a entrada pode ser menor. O FGTS pode ser usado como parte da entrada se você cumprir as regras.</p></details>
  <details><summary>Quanto de renda preciso para financiar?</summary><p>Os bancos costumam aceitar parcelas de até 30% da renda bruta familiar. É possível somar a renda de mais de uma pessoa, como casais.</p></details>
  <details><summary>Posso usar o Minha Casa, Minha Vida?</summary><p>Famílias com renda bruta de até R$ 13 mil por mês podem se enquadrar. Faixa 1: renda até R$ 3.200; faixa 2: até R$ 5.000 (imóveis de até R$ 275 mil, conforme o município); faixa 3: até R$ 9.600 (imóveis de até R$ 400 mil); faixa 4: até R$ 13.000 (imóveis de até R$ 600 mil). Os juros são menores que os da linha tradicional e, nas faixas iniciais, pode haver subsídio. Informe sua renda no simulador para ver a taxa estimada. Fale com a Manu para saber se o seu caso se encaixa.</p></details>
  <details><summary>A corretora ajuda com o financiamento?</summary><p>Sim. A Manu dá apoio e orientação durante todo o processo, da simulação à assinatura do contrato, e indica um correspondente bancário de confiança, que é quem encaminha a documentação ao banco e acompanha a análise de crédito.</p></details>
</div></section>

<script>
(function(){{
  var BANCOS = {json.dumps(BANCOS, ensure_ascii=False)};
  var MCMV = {json.dumps(MCMV)};
  var IMOVEIS = {imoveis_js};
  var WHATS = "5549988987121";
  var $ = function(id){{return document.getElementById(id)}};
  var tab = "sac", userBank = false, curList = [];
  function pctf(t){{return String(t.toFixed(2)).replace(".",",")}}
  function faixa(renda, valor){{
    if (!renda) return null;
    for (var k=0;k<MCMV.length;k++){{var f=MCMV[k]; if (renda<=f.renda) return valor<=f.teto ? f : null;}}
    return null;
  }}
  function lista(f){{
    var l = BANCOS.slice();
    if (f) l.unshift({{id:"mcmv", nome:"Caixa · Minha Casa, Minha Vida (faixa "+f.faixa+")", curto:"MCMV faixa "+f.faixa, taxa:f.taxa}});
    return l;
  }}
  function fillBanks(l, keep){{
    var s=$("s-banco"), ids=l.map(function(b){{return b.id}}).join();
    if (s.dataset.ids!==ids){{
      s.innerHTML = l.map(function(b){{return '<option value="'+b.id+'">'+b.nome+' · '+pctf(b.taxa)+'% a.a.</option>'}}).join("");
      s.dataset.ids=ids;
    }}
    if (l.some(function(b){{return b.id===keep}})) s.value=keep;
  }}
  function num(s){{return Number(String(s).replace(/[^0-9,]/g,"").replace(",","."))||0}}
  function brl(v){{return v.toLocaleString("pt-BR",{{style:"currency",currency:"BRL",maximumFractionDigits:0}})}}
  function brl2(v){{return v.toLocaleString("pt-BR",{{style:"currency",currency:"BRL",minimumFractionDigits:2,maximumFractionDigits:2}})}}
  function fmtInput(el){{var v=num(el.value);el.value=brl(Math.round(v))}}
  function calc(P, taxa, n){{
    var i = Math.pow(1+taxa/100,1/12)-1;
    var amort = P/n;
    var sac1 = amort + P*i, sacN = amort + amort*i, sacTot = P + i*P*(n+1)/2;
    var pr = i===0 ? P/n : P*i/(1-Math.pow(1+i,-n));
    return {{sac1:sac1, sacN:sacN, sacTot:sacTot, price:pr, priceTot:pr*n}};
  }}
  // imóveis da Manu
  var sel = $("s-imovel");
  IMOVEIS.forEach(function(im){{var o=document.createElement("option");o.value=im.slug;o.textContent=im.title+" · "+brl(im.price);sel.appendChild(o)}});
  for (var a=5;a<=35;a+=5){{var o=document.createElement("option");o.value=a;o.textContent=a+" anos ("+a*12+" meses)";$("s-prazo").appendChild(o)}}
  $("s-prazo").value=30;
  // valores vindos de um imóvel (?imovel=slug ou ?valor=)
  var q = new URLSearchParams(location.search);
  if (q.get("imovel")) {{ sel.value = q.get("imovel"); var im = IMOVEIS.find(function(x){{return x.slug===sel.value}}); if (im) {{ $("s-valor").value = brl(im.price); $("s-entrada").value = brl(Math.round(im.price*0.2)); }} }}
  else if (q.get("valor")) {{ var v=num(q.get("valor")); $("s-valor").value=brl(v); $("s-entrada").value=brl(Math.round(v*0.2)); }}

  function choose(){{
    // escolhe banco/taxa automaticamente conforme renda e valor
    var valor=num($("s-valor").value), renda=num($("s-renda").value), f=faixa(renda,valor);
    var prev=$("s-banco").value||"caixa";
    curList=lista(f);
    var want = prev;
    if (!userBank || prev==="mcmv") want = f ? "mcmv" : (prev==="mcmv" ? "caixa" : prev);
    if (!curList.some(function(b){{return b.id===want}})) want="caixa";
    var changed = want!==prev || $("s-banco").dataset.ids===undefined;
    fillBanks(curList, want);
    var b=curList.find(function(x){{return x.id===want}});
    if (changed || want==="mcmv") $("s-taxa").value=pctf(b.taxa);
    $("s-taxahint").textContent = want==="mcmv" ? "Taxa do Minha Casa, Minha Vida (faixa "+f.faixa+"). Pode ajustar." : (renda ? "Taxa de balcão do banco. Pode ajustar." : "Informe a renda para ver se o Minha Casa, Minha Vida se aplica.");
    return f;
  }}
  function run(track){{
    var f=choose();
    var valor=num($("s-valor").value), entrada=num($("s-entrada").value), fgts=num($("s-fgts").value), rendaF=num($("s-renda").value);
    var taxa=num($("s-taxa").value), anos=Number($("s-prazo").value), n=anos*12;
    var P=Math.max(valor-entrada-fgts,0);
    var pct = valor ? (entrada+fgts)/valor*100 : 0;
    $("s-entpct").textContent = Math.round(pct)+"% do imóvel"+(fgts?" (com FGTS)":"");
    var r = calc(P,taxa,n);
    var first = tab==="sac"?r.sac1:r.price, last = tab==="sac"?r.sacN:r.price, tot = tab==="sac"?r.sacTot:r.priceTot;
    $("r-lbl").textContent = tab==="sac"?"Primeira parcela estimada":"Parcela fixa estimada";
    $("r-lbl2").textContent = tab==="sac"?"Última parcela":"Última parcela";
    $("r-parc").textContent = P?brl2(first):"—";
    $("r-ult").textContent = P?brl2(last):"—";
    $("r-fin").textContent = brl(P);
    $("r-renda").textContent = P?brl(first/0.30):"—";
    $("r-juros").textContent = P?brl(tot-P):"—";
    $("r-total").textContent = P?brl(tot+entrada+fgts):"—";
    $("r-prazo").textContent = anos+" anos";
    // cabe na renda?
    var fit=$("r-fit"), al=[];
    if (rendaF && P){{
      var comp=first/rendaF*100, i=Math.pow(1+taxa/100,1/12)-1;
      fit.hidden=false;
      if (comp<=30){{ fit.className="fit ok"; fit.textContent="✓ Cabe na renda: a parcela compromete "+Math.round(comp)+"% da renda informada."; }}
      else {{
        var maxP = tab==="sac" ? 0.3*rendaF/(1/n+i) : 0.3*rendaF*(1-Math.pow(1+i,-n))/i;
        var entNec = Math.max(valor-fgts-maxP,0);
        fit.className="fit no"; fit.textContent="A parcela compromete "+Math.round(comp)+"% da renda (os bancos aceitam até 30%).";
        al.push("Para a parcela caber em 30% da renda, o valor financiado deve ficar em até "+brl(maxP)+", ou seja, entrada de cerca de "+brl(entNec)+(fgts?" além do FGTS":"")+". Também dá para aumentar o prazo ou somar a renda de outra pessoa.");
      }}
    }} else fit.hidden=true;
    if (valor && pct<20) al.push("A maioria dos bancos financia até 80% do imóvel. Com entrada de "+Math.round(pct)+"%, talvez seja preciso aumentar a entrada"+(f?" (no Minha Casa, Minha Vida a entrada pode ser menor, conforme a faixa).":" ou usar um programa habitacional."));
    if (f) al.push("Pela renda e pelo valor do imóvel, você pode se enquadrar no <b>Minha Casa, Minha Vida (faixa "+f.faixa+")</b>, com juros de até cerca de "+pctf(f.taxa)+"% ao ano (cotistas do FGTS podem ter taxa menor). A confirmação depende da análise da Caixa.");
    else if (rendaF && rendaF<=13000){{ var fx=MCMV.find(function(x){{return rendaF<=x.renda}}); al.push("Pela renda, você estaria na faixa "+fx.faixa+" do Minha Casa, Minha Vida, mas o imóvel passa do valor máximo da faixa ("+brl(fx.teto)+(fx.faixa<3?", conforme o município":"")+"). Por isso usamos as taxas da linha tradicional."); }}
    else if (!rendaF && valor && valor<=600000) al.push("Informe a renda familiar para saber se você se enquadra no Minha Casa, Minha Vida, que tem juros menores.");
    $("r-alert").hidden = !al.length; $("r-alert").innerHTML = al.join("<br>");
    // comparação
    var bid=$("s-banco").value;
    $("cmp").tBodies[0].innerHTML = curList.map(function(b){{var c=calc(P,b.taxa,n);return '<tr data-b="'+b.id+'"'+(b.id===bid?' class="sel"':'')+'><td>'+(b.id==="mcmv"?'Caixa<span class="tag">'+b.curto+'</span>':b.nome)+'</td><td>'+pctf(b.taxa)+'%</td><td>'+brl2(c.sac1)+'</td><td>'+brl2(c.price)+'</td><td>'+brl(c.sac1/0.30)+'</td></tr>'}}).join("");
    Array.prototype.forEach.call($("cmp").tBodies[0].rows,function(tr){{tr.onclick=function(){{$("s-banco").value=tr.dataset.b;userBank=true;setBank();run(true);window.scrollTo({{top:$("simf").getBoundingClientRect().top+scrollY-90,behavior:"smooth"}})}}}});
    // WhatsApp com os dados
    var bn=(curList.find(function(b){{return b.id===bid}})||{{}}).nome||"";
    var im = IMOVEIS.find(function(x){{return x.slug===sel.value}});
    var msg = "Olá, Manu! Fiz uma simulação de financiamento no seu site e quero uma simulação oficial."
      + (im?"\\nImóvel: "+im.title:"")
      + (rendaF?"\\nRenda familiar: "+brl(rendaF):"")
      + "\\nValor do imóvel: "+brl(valor)+"\\nEntrada: "+brl(entrada)+(fgts?" + FGTS "+brl(fgts):"")
      + "\\nBanco: "+bn+" ("+String(taxa).replace(".",",")+"% a.a.), "+anos+" anos, tabela "+tab.toUpperCase()
      + "\\nParcela estimada: "+brl2(first);
    $("r-wa").href = "https://wa.me/"+WHATS+"?text="+encodeURIComponent(msg);
    if (track && window.gtag) gtag("event","simulacao_financiamento",{{valor:valor,banco:bn,prazo:anos,tabela:tab}});
  }}
  function setBank(){{var b=curList.find(function(x){{return x.id===$("s-banco").value}});if(b){{$("s-taxa").value=pctf(b.taxa)}}}}
  sel.onchange=function(){{var im=IMOVEIS.find(function(x){{return x.slug===sel.value}});if(im){{$("s-valor").value=brl(im.price);$("s-entrada").value=brl(Math.round(im.price*0.2))}}run(true)}};
  $("s-banco").onchange=function(){{userBank=true;setBank();run(true)}};
  ["s-valor","s-entrada","s-fgts","s-renda"].forEach(function(id){{var el=$(id);el.addEventListener("input",function(){{run(false)}});el.addEventListener("blur",function(){{fmtInput(el);run(true)}})}});
  $("s-taxa").addEventListener("input",function(){{run(false)}});
  $("s-prazo").onchange=function(){{run(true)}};
  document.querySelectorAll(".seg button").forEach(function(b){{b.onclick=function(){{tab=b.dataset.t;document.querySelectorAll(".seg button").forEach(function(x){{x.setAttribute("aria-pressed",x===b)}});$("s-tabhint").textContent=tab==="sac"?"SAC: parcelas começam maiores e diminuem com o tempo.":"Price: parcelas fixas, mas o total de juros é maior.";run(true)}}}});
  $("simf").addEventListener("submit",function(ev){{ev.preventDefault()}});
  run(false);
}})();
</script>'''
