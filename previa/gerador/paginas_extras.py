"""Páginas institucionais: Sobre, Avaliar imóvel e Política de Privacidade."""

EMAIL = "emanoelajba@gmail.com"
ATUALIZADA = "6 de novembro de 2026"

CSS = """
.pg-narrow{max-width:820px}
.inst h2{font-size:clamp(1.3rem,2.2vw,1.6rem);margin:34px 0 10px}
.inst p,.inst li{color:var(--muted);max-width:70ch}
.inst ul{padding-left:20px}
.inst ul.facts,.inst ul.why{padding-left:0}
.inst li{margin:6px 0}
.about-hero{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:44px;align-items:center;padding-block:34px 10px}
.about-hero img{width:100%;aspect-ratio:4/5;object-fit:cover;object-position:50% 20%;border-radius:24px;background:var(--surface)}
@media (max-width:760px){.about-hero{grid-template-columns:1fr;gap:22px}.about-hero img{max-width:320px;aspect-ratio:1/1}}
.steps{list-style:none;padding:0;margin:18px 0 0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.steps li{background:var(--bg);border:1px solid var(--line);border-radius:16px;padding:18px;margin:0;max-width:none}
.steps b{display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--brand);color:var(--accent-hi);font-family:var(--display);margin-bottom:10px}
.steps strong{display:block;color:var(--ink);margin-bottom:4px}
.steps span{font-size:.92rem;color:var(--muted)}
@media (max-width:900px){.steps{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.steps{grid-template-columns:1fr}}
.cta-band{display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;background:var(--brand);color:#F3EBDA;border-radius:22px;padding:26px 28px}
.cta-band strong{display:block;font-family:var(--display);font-size:1.3rem;color:#fff}
.cta-band .acts{display:flex;gap:10px;flex-wrap:wrap}
.eval{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,380px);gap:40px;align-items:start;padding-block:26px 10px}
@media (max-width:900px){.eval{grid-template-columns:1fr}}
.eval-form{background:var(--bg);border:1px solid var(--line);border-radius:20px;padding:22px;display:grid;gap:12px;box-shadow:var(--shadow)}
.eval-form h2{font-size:1.2rem;margin:0}
.eval-form .row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.eval-form textarea{width:100%;border:1px solid var(--line);background:var(--surface);border-radius:12px;padding:11px 12px;min-height:84px;resize:vertical;font:inherit}
.eval-form .btn{width:100%}
.eval-form small{color:var(--muted);font-size:.8rem}
.why{list-style:none;padding:0;margin:16px 0 0;display:grid;gap:12px}
.why li{display:flex;gap:12px;align-items:flex-start;color:var(--muted)}
.why li::before{content:"";flex:none;width:22px;height:22px;margin-top:2px;border-radius:50%;background:var(--accent-soft) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%238A6A2E' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m5 12 5 5 9-10'/%3E%3C/svg%3E") center/14px no-repeat}
.why strong{color:var(--ink)}
"""


def sobre(e, wa_link):
    return f'''
<div class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › Sobre</nav>
  <div class="about-hero">
    <img src="/manu.jpg" alt="Manu, corretora de imóveis em Joaçaba" loading="eager">
    <div class="inst">
      <span class="creci">CORRETORA DE IMÓVEIS · CRECI/SC 54977 F</span>
      <h1 style="font-size:clamp(1.9rem,3.6vw,2.7rem);margin-top:12px">Oi, eu sou a Manu.</h1>
      <p>Sou corretora de imóveis há mais de 3 anos e pós-graduada em Gestão Empresarial pela UNOESC Joaçaba. Nesse caminho, já ajudei dezenas de famílias a encontrar um lugar para chamar de seu.</p>
      <p>Atendo em Joaçaba, Herval d'Oeste, Luzerna e região, com foco em casas e apartamentos. Meu trabalho é entender o que você procura, apresentar só o que faz sentido e acompanhar cada etapa da negociação até a entrega das chaves.</p>
      <ul class="facts">
        <li><strong>+3 anos</strong><span>no mercado imobiliário</span></li>
        <li><strong>Dezenas</strong><span>de famílias atendidas</span></li>
        <li><strong>Pós-graduada</strong><span>em Gestão Empresarial</span></li>
      </ul>
    </div>
  </div>
</div>
<section class="block alt"><div class="wrap inst">
  <div class="sec-head"><div><h2>Como eu trabalho</h2></div></div>
  <ol class="steps">
    <li><b>1</b><strong>Conversa inicial</strong><span>Entendo o que você precisa: região, tamanho, faixa de valor e forma de pagamento.</span></li>
    <li><b>2</b><strong>Seleção e visitas</strong><span>Apresento só os imóveis que combinam com você e acompanho as visitas com hora marcada.</span></li>
    <li><b>3</b><strong>Negociação</strong><span>Cuido da proposta e da negociação, com transparência dos dois lados.</span></li>
    <li><b>4</b><strong>Financiamento e contrato</strong><span>Oriento sobre o financiamento, com apoio de correspondente bancário de confiança, até a assinatura.</span></li>
  </ol>
</div></section>
<section class="block"><div class="wrap">
  <div class="cta-band">
    <div><strong>Vamos encontrar seu próximo imóvel?</strong><span>Me conte o que você procura ou peça uma avaliação do seu imóvel.</span></div>
    <div class="acts">
      <a class="btn btn-accent" href="{e(wa_link)}" target="_blank" rel="noopener">Falar no WhatsApp</a>
      <a class="btn btn-call" href="/avaliar-imovel/">Avaliar meu imóvel</a>
    </div>
  </div>
</div></section>'''


def avaliar(e):
    cidades = "".join(f"<option>{c}</option>" for c in ["Joaçaba", "Herval d'Oeste", "Luzerna", "Erval Velho", "Lacerdópolis", "Ibicaré", "Outra"])
    tipos = "".join(f"<option>{t}</option>" for t in ["Casa", "Apartamento", "Terreno", "Sala ou loja comercial", "Outro"])
    return f'''
<div class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › Avaliar imóvel</nav>
  <div class="eval">
    <div class="inst">
      <h1 style="font-size:clamp(1.9rem,3.6vw,2.7rem)">Avalie seu imóvel com a Manu</h1>
      <p>Quer vender ou só saber quanto vale o seu imóvel? Preencha os dados do imóvel e a Manu retorna pelo WhatsApp para combinar a avaliação, sem compromisso.</p>
      <ul class="why">
        <li><span><strong>Preço de acordo com o mercado local.</strong> A avaliação considera imóveis parecidos na mesma região de Joaçaba e arredores.</span></li>
        <li><span><strong>Divulgação completa.</strong> Fotos, anúncio no site e nas redes, e atendimento aos interessados.</span></li>
        <li><span><strong>Acompanhamento até o fim.</strong> Negociação, documentação e apoio no financiamento do comprador.</span></li>
      </ul>
    </div>
    <form class="eval-form" id="eval">
      <h2>Dados do imóvel</h2>
      <div class="row">
        <div class="field"><label for="ev-tipo">Tipo</label><select id="ev-tipo" required>{tipos}</select></div>
        <div class="field"><label for="ev-cid">Cidade</label><select id="ev-cid" required>{cidades}</select></div>
      </div>
      <div class="field"><label for="ev-bai">Bairro</label><input id="ev-bai" placeholder="Ex.: Centro, Frei Bruno" required></div>
      <div class="row">
        <div class="field"><label for="ev-area">Área aprox. (m²)</label><input id="ev-area" inputmode="numeric" placeholder="Ex.: 120"></div>
        <div class="field"><label for="ev-q">Quartos</label><select id="ev-q"><option value="">—</option><option>1</option><option>2</option><option>3</option><option>4 ou mais</option></select></div>
      </div>
      <div class="field"><label for="ev-obj">Objetivo</label><select id="ev-obj"><option>Quero vender</option><option>Quero saber quanto vale</option></select></div>
      <div class="field"><label for="ev-obs">Algo mais? (opcional)</label><textarea id="ev-obs" placeholder="Ex.: garagem para 2 carros, reformado em 2023"></textarea></div>
      <div class="field"><label for="ev-nome">Seu nome</label><input id="ev-nome" autocomplete="name" required></div>
      <button class="btn btn-accent" type="submit">Enviar pelo WhatsApp</button>
      <small>Ao enviar, o WhatsApp abre com a mensagem pronta. Nada fica salvo no site.</small>
    </form>
  </div>
</div>
<script>
document.getElementById("eval").addEventListener("submit",function(ev){{ev.preventDefault();
var v=function(id){{return (document.getElementById(id).value||"").trim()}};
var m="Olá, Manu! Gostaria de uma avaliação do meu imóvel.\\n\\nNome: "+v("ev-nome")+"\\nObjetivo: "+v("ev-obj")+"\\nTipo: "+v("ev-tipo")+"\\nCidade: "+v("ev-cid")+"\\nBairro: "+v("ev-bai")
 +(v("ev-area")?"\\nÁrea aprox.: "+v("ev-area")+" m²":"")+(v("ev-q")?"\\nQuartos: "+v("ev-q"):"")+(v("ev-obs")?"\\nObservações: "+v("ev-obs"):"");
if(window.gtag)gtag("event","pedido_avaliacao",{{tipo:v("ev-tipo"),cidade:v("ev-cid")}});
window.open("https://wa.me/5549988987121?text="+encodeURIComponent(m),"_blank","noopener");}});
</script>'''


def privacidade(e):
    return f'''
<div class="wrap pg-narrow inst">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › Política de Privacidade</nav>
  <div class="pg-head"><h1>Política de Privacidade</h1><p>Última atualização: {ATUALIZADA}.</p></div>
  <p>Esta política explica como o site <strong>manucorretora.com.br</strong>, da Manu Corretora de Imóveis (CRECI/SC 54977 F), trata as informações de quem o visita, de acordo com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018, LGPD).</p>

  <h2>1. Quais dados são coletados</h2>
  <ul>
    <li><strong>Dados que você envia por vontade própria:</strong> quando você clica em um botão de WhatsApp, usa o formulário "Avaliar imóvel" ou envia um e-mail, as informações que você escreve (como nome, telefone e dados do imóvel) chegam diretamente à Manu pelo WhatsApp ou por e-mail. O site não armazena essas informações.</li>
    <li><strong>Dados de navegação:</strong> páginas visitadas, tempo no site, tipo de aparelho, navegador, cidade aproximada e origem do acesso (por exemplo, Google ou Instagram). Esses dados são coletados por ferramentas de medição, descritas abaixo.</li>
    <li><strong>Simulador de financiamento:</strong> os valores digitados no simulador são calculados no seu próprio navegador e não são enviados nem guardados, a menos que você escolha enviá-los pelo WhatsApp.</li>
  </ul>

  <h2>2. Ferramentas de terceiros e cookies</h2>
  <p>O site usa cookies e tecnologias semelhantes das seguintes ferramentas:</p>
  <ul>
    <li><strong>Google Analytics</strong> (Google): para medir visitas e entender quais páginas e imóveis interessam mais.</li>
    <li><strong>Pixel da Meta</strong> (Facebook e Instagram): para medir os resultados de anúncios e mostrar anúncios a pessoas que já visitaram o site.</li>
    <li><strong>Google Ads</strong>: para medir os resultados de anúncios na pesquisa do Google, quando houver.</li>
  </ul>
  <p>Você pode bloquear ou apagar cookies nas configurações do seu navegador, e ajustar suas preferências de anúncios nas configurações da sua conta Google e da Meta. Bloquear cookies não impede o uso do site.</p>

  <h2>3. Para que os dados são usados</h2>
  <ul>
    <li>Responder ao seu contato, apresentar imóveis e combinar visitas ou avaliações;</li>
    <li>Melhorar o site e entender quais imóveis e conteúdos são mais procurados;</li>
    <li>Medir e direcionar anúncios da Manu Corretora.</li>
  </ul>
  <p>Os dados não são vendidos nem cedidos a terceiros para fins próprios deles.</p>

  <h2>4. Compartilhamento</h2>
  <p>Quando necessário para a negociação de um imóvel, informações podem ser compartilhadas, com o seu conhecimento, com proprietários, outros corretores parceiros, cartórios e correspondentes bancários, apenas no limite do que for preciso para o atendimento.</p>

  <h2>5. Por quanto tempo</h2>
  <p>As conversas e informações recebidas são mantidas pelo tempo necessário ao atendimento e ao cumprimento de obrigações legais. Os dados de navegação seguem os prazos de retenção das ferramentas citadas.</p>

  <h2>6. Seus direitos</h2>
  <p>Pela LGPD, você pode pedir a qualquer momento: confirmação de que tratamos seus dados, acesso, correção, exclusão, informação sobre compartilhamento e revogação do consentimento. Para isso, entre em contato pelos canais abaixo.</p>

  <h2>7. Contato</h2>
  <p>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>WhatsApp: (49) 98898-7121</p>

  <h2>8. Alterações</h2>
  <p>Esta política pode ser atualizada. A data da última atualização fica sempre no topo desta página.</p>
</div>
<div style="height:40px"></div>'''
