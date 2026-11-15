"""Blog do site da Manu Corretora.

Para publicar um artigo novo: acrescente um dicionário em POSTS (o mais novo primeiro),
com o texto em HTML no campo "corpo". O gerador cria /blog/ (lista) e /blog/<slug>/
(uma página por artigo) e inclui tudo no sitemap.

- "capa": imagem do topo do artigo (foto horizontal)
- "og": imagem de compartilhamento (WhatsApp, Facebook), 1200x630
"""

AUTORA = {"@type": "Person", "name": "Manu", "jobTitle": "Corretora de imóveis (CRECI/SC 54977 F)",
          "url": "https://manucorretora.com.br/sobre/"}

CSS = """
.post-wrap{max-width:780px}
.post-head{padding-block:28px 6px}
.post-kicker{display:inline-block;font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--accent-ink)}
.post-head h1{font-size:clamp(1.85rem,4.2vw,2.75rem);line-height:1.12;margin:10px 0 14px;letter-spacing:-.01em}
.post-lead{font-size:1.14rem;line-height:1.6;color:var(--muted);margin:0 0 18px;max-width:62ch}
.post-meta{display:flex;align-items:center;gap:12px;color:var(--muted);font-size:.9rem;line-height:1.45}
.post-meta span{min-width:0}
.post-meta img{flex:none;width:44px;height:44px;border-radius:50%;object-fit:cover;object-position:50% 15%}
.post-meta strong a{color:var(--ink)}
.post-cover{margin:26px 0 8px}
.post-cover img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;border-radius:20px;background:var(--surface)}
.post-cover figcaption{font-size:.74rem;color:var(--muted);margin-top:6px}
.post-cover figcaption a{color:inherit}
.post{font-size:1.07rem;line-height:1.75;color:var(--ink)}
.post>p,.post li{color:var(--ink)}
.post h2{font-size:clamp(1.35rem,2.8vw,1.7rem);line-height:1.25;margin:44px 0 12px;letter-spacing:-.01em}
.post ul,.post ol{padding-left:22px}
.post li{margin:7px 0}
.post a{color:var(--accent-ink);text-decoration:underline;text-underline-offset:3px}
.post a.btn{text-decoration:none}
.post a.btn-accent{color:var(--on-accent)}
.tldr{background:var(--surface);border-radius:16px;padding:20px 22px;margin:26px 0 8px;border-left:4px solid var(--accent)}
.tldr strong{display:block;font-family:var(--display);font-size:1.05rem;margin-bottom:6px}
.tldr p{margin:0}
/* gráfico de barras */
.chart{border:1px solid var(--line);border-radius:18px;padding:22px 22px 16px;margin:22px 0;background:var(--bg)}
.chart h3{font-size:1rem;margin:0 0 4px}
.chart .sub{font-size:.86rem;color:var(--muted);margin:0 0 18px}
.bar{display:grid;grid-template-columns:92px 1fr 64px;align-items:center;gap:12px;margin:12px 0}
.bar span{font-size:.92rem;color:var(--muted)}
.bar i{display:block;height:14px;border-radius:999px;background:linear-gradient(90deg,var(--brand),#2E5A36)}
.bar.hl i{background:linear-gradient(90deg,var(--accent-ink),var(--accent))}
.bar b{font-family:var(--display);font-size:1.05rem;text-align:right;font-variant-numeric:tabular-nums}
.chart small{display:block;font-size:.78rem;color:var(--muted);margin-top:12px}
/* tabela */
.tbl{border:1px solid var(--line);border-radius:18px;overflow-x:auto;margin:22px 0}
.tbl table{width:100%;border-collapse:collapse;font-size:1rem}
.tbl th,.tbl td{padding:13px 16px;text-align:left;border-bottom:1px solid var(--line)}
.tbl tr:last-child td{border-bottom:0}
.tbl th{background:var(--surface);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.tbl .n{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.tbl .up{color:#A2552F;font-weight:600}
.post .note{font-size:.86rem;color:var(--muted);margin-top:-8px}
/* destaque */
.callout{display:flex;gap:16px;align-items:flex-start;background:var(--brand);color:#EEE7D8;border-radius:18px;padding:22px 24px;margin:26px 0}
.callout b{font-family:var(--display);font-size:2rem;line-height:1;color:var(--accent-hi);white-space:nowrap}
.callout p{margin:0;color:#EEE7D8}
/* cartões */
.post .cards2,.post .steps2{padding:0}
.cards2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:20px 0;padding:0;list-style:none}
.cards2 li{background:var(--surface);border-radius:16px;padding:18px 18px 16px;margin:0}
.cards2 strong{display:block;font-family:var(--display);font-size:1.02rem;margin-bottom:4px}
.cards2 span{font-size:.95rem;color:var(--muted);line-height:1.55;display:block}
.steps2{counter-reset:s;list-style:none;padding:0;margin:20px 0;display:grid;gap:12px}
.steps2 li{counter-increment:s;position:relative;border:1px solid var(--line);border-radius:16px;padding:18px 18px 16px 70px;margin:0;background:var(--bg)}
.steps2 li::before{content:counter(s);position:absolute;left:18px;top:16px;width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:var(--brand);color:var(--accent-hi);font-family:var(--display);font-weight:700}
.steps2 strong{display:block;font-family:var(--display);margin-bottom:2px}
.steps2 span{color:var(--muted);font-size:.97rem;line-height:1.55;display:block}
@media (max-width:620px){.tbl th,.tbl td{padding:11px 10px;font-size:.9rem}.tbl th{font-size:.7rem}.cards2{grid-template-columns:1fr}.bar{grid-template-columns:78px 1fr 56px;gap:10px}.callout{flex-direction:column;gap:8px}.post{font-size:1.03rem}}
.post-cta{margin:44px 0 10px}
.post-src{font-size:.86rem;color:var(--muted);border-top:1px solid var(--line);margin-top:34px;padding-top:16px}
.post-src ul{padding-left:18px}
.post-src a{color:var(--muted)}
/* lista */
.blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;padding-block:20px 10px}
.blog-card{display:flex;flex-direction:column;background:var(--bg);border:1px solid var(--line);border-radius:18px;overflow:hidden;color:inherit;text-decoration:none;box-shadow:var(--shadow)}
.blog-card img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover}
.blog-card div{padding:16px 18px 20px}
.blog-card h2{font-size:1.15rem;line-height:1.3;margin:6px 0 8px}
.blog-card p{color:var(--muted);font-size:.94rem;margin:0}
"""

CREDITO_JBA = 'Joaçaba (SC). Foto: Suhaibharraka, <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>, via <a href="https://commons.wikimedia.org/w/index.php?curid=133214067" target="_blank" rel="noopener">Wikimedia Commons</a>'

POSTS = [
    {
        "slug": "vale-a-pena-comprar-imovel-agora",
        "titulo": "Vale a pena comprar imóvel agora ou esperar? O que os números mostram em 2026",
        "titulo_seo": "Vale a pena comprar imóvel agora ou esperar? Números de 2026 | Manu Corretora",
        "resumo": "Os imóveis valorizaram entre 5% e 8% ao ano no Brasil desde 2024. Veja quanto custa esperar, quando faz sentido adiar a compra e como se preparar para comprar imóvel em Joaçaba e região.",
        "lead": "Desde 2024, os imóveis subiram entre 5% e 8% ao ano no Brasil. Entenda o que isso significa no seu bolso, quando esperar faz sentido e como se preparar para comprar com segurança em Joaçaba e região.",
        "kicker": "Comprar imóvel",
        "data": "2026-11-15",
        "data_br": "15 de novembro de 2026",
        "capa": "/joacaba-2.jpg",
        "capa_alt": "Vista da cidade de Joaçaba, em Santa Catarina, com prédios residenciais e morros ao fundo",
        "capa_credito": CREDITO_JBA,
        "og": "/blog/img/vale-a-pena-comprar-imovel-agora.jpg",
        "leitura": "7 min de leitura",
        "corpo": """
<div class="tldr"><strong>Resposta curta</strong><p>Esperar sem um plano costuma sair caro, porque o preço médio dos imóveis tem subido acima da inflação. Mas comprar por impulso também é um erro. Vale a pena comprar imóvel agora quando você sabe quanto pode pagar, o que procura e quanto vai gastar além do preço.</p></div>

<h2>Valorização dos imóveis: o que os dados mostram</h2>
<p>O Índice FipeZAP acompanha o preço de venda de imóveis residenciais em 56 cidades brasileiras. Nos últimos três períodos, a alta ficou acima da inflação em todos eles:</p>
<div class="chart" role="img" aria-label="Valorização dos imóveis residenciais no Brasil: 7,73% em 2024, 6,52% em 2025 e 5,44% nos 12 meses até outubro de 2026">
  <h3>Alta do preço médio dos imóveis residenciais</h3>
  <p class="sub">Brasil, Índice FipeZAP de venda</p>
  <div class="bar"><span>2024</span><i style="width:100%"></i><b>7,73%</b></div>
  <div class="bar"><span>2025</span><i style="width:84%"></i><b>6,52%</b></div>
  <div class="bar hl"><span>12 meses*</span><i style="width:70%"></i><b>5,44%</b></div>
  <small>*Acumulado até outubro de 2026. Fonte: FipeZAP.</small>
</div>
<p>Joaçaba, Herval d'Oeste e Luzerna não fazem parte do índice. Os números mostram a tendência do país, mas o preço de um imóvel aqui depende muito do bairro, do tipo e do estado de conservação. Para saber quanto vale um imóvel específico, o caminho é uma <a href="/avaliar-imovel/">avaliação</a> com base em vendas reais da região.</p>

<h2>E a renda, acompanhou?</h2>
<p>É comum ouvir que “o salário nunca acompanha o preço dos imóveis”. Os dados recentes mostram um quadro mais equilibrado: segundo o IBGE, o rendimento médio real do brasileiro <strong>cresceu 5,4% em 2025</strong>, já descontada a inflação.</p>
<p>A pergunta mais útil, então, não é se a renda sobe. É se você está se preparando no mesmo ritmo em que o imóvel que você quer fica mais caro: juntando a entrada, organizando o crédito e acompanhando o mercado.</p>

<h2>Quanto custa esperar para comprar</h2>
<p>Veja o efeito da valorização em um imóvel de R$ 400 mil, considerando 6% ao ano, próximo da média recente:</p>
<div class="tbl"><table>
<thead><tr><th>Se você esperar</th><th class="n">Valor do imóvel</th><th class="n">A mais</th></tr></thead>
<tbody>
<tr><td>Hoje</td><td class="n">R$ 400.000</td><td class="n">–</td></tr>
<tr><td>1 ano</td><td class="n">R$ 424.000</td><td class="n up">R$ 24.000</td></tr>
<tr><td>2 anos</td><td class="n">R$ 449.440</td><td class="n up">R$ 49.440</td></tr>
<tr><td>3 anos</td><td class="n">R$ 476.406</td><td class="n up">R$ 76.406</td></tr>
</tbody></table></div>
<p class="note">Simulação ilustrativa. A valorização real varia por cidade, bairro e tipo de imóvel.</p>
<div class="callout"><b>≈ R$ 50 mil</b><p>é quanto o mesmo imóvel pode custar a mais em dois anos. Muitas vezes, é justamente o valor da entrada que a pessoa estava juntando. E quem paga aluguel enquanto espera ainda tem esse gasto todo mês.</p></div>

<h2>Por que os imóveis tendem a ficar mais caros</h2>
<ul class="cards2">
<li><strong>Terreno bem localizado é limitado</strong><span>As melhores regiões não aumentam de tamanho, e a procura por elas continua.</span></li>
<li><strong>Construir fica mais caro</strong><span>Material e mão de obra sobem todo ano, e isso chega ao preço de imóveis novos e usados.</span></li>
<li><strong>O aluguel também é reajustado</strong><span>Enquanto espera, quem aluga segue pagando por um patrimônio que não é seu.</span></li>
<li><strong>A demanda segue firme</strong><span>Com a renda em alta, mais famílias buscam a casa própria, o que sustenta os preços.</span></li>
</ul>

<h2>Quando vale a pena esperar</h2>
<p>Esperar nem sempre é um erro. Em algumas situações, adiar a compra é a decisão mais sensata:</p>
<ul>
<li>Você ainda não tem uma reserva de emergência separada do dinheiro da entrada.</li>
<li>Sua renda está instável ou deve mudar em breve.</li>
<li>Existe chance real de você mudar de cidade nos próximos anos.</li>
<li>Você tem dívidas com juros altos, como cartão de crédito ou cheque especial. Quitar essas dívidas antes costuma render mais do que qualquer valorização.</li>
</ul>
<p>O problema não é esperar. É esperar sem saber pelo quê.</p>

<h2>Custos além do preço: ITBI, escritura e registro</h2>
<p>Quem vai comprar imóvel precisa reservar dinheiro para os custos da compra, que não entram no financiamento na maioria dos casos:</p>
<ul>
<li><strong>ITBI:</strong> imposto municipal sobre a transmissão do imóvel. A alíquota e a base de cálculo são definidas por cada prefeitura, então o ITBI em Joaçaba pode ser diferente do de Herval d'Oeste ou Luzerna.</li>
<li><strong>Escritura e registro:</strong> taxas de cartório que variam com o valor do imóvel. No financiamento bancário, o contrato do banco costuma substituir a escritura, mas o registro continua obrigatório.</li>
<li><strong>Avaliação e taxas do banco:</strong> no financiamento, o banco cobra a avaliação do imóvel e pode ter tarifas de contratação.</li>
</ul>
<p>Antes de fazer uma proposta, peça uma estimativa desses custos para o imóvel e a cidade que você escolheu.</p>

<h2>Como se preparar para comprar: financiamento, FGTS e entrada</h2>
<ol class="steps2">
<li><strong>Conheça seu poder de compra</strong><span>Some renda, FGTS e entrada, e veja quanto o banco aprova. Comece pelo <a href="/simulador-financiamento/">simulador de financiamento imobiliário</a>, que compara SAC e Price entre os principais bancos.</span></li>
<li><strong>Defina suas prioridades</strong><span>Bairro, tamanho, número de quartos e prazo. Saber o que é essencial evita visitas que não fazem sentido.</span></li>
<li><strong>Compare parcela e aluguel</strong><span>Em muitos casos, a parcela do financiamento fica próxima do aluguel, com a diferença de que você está construindo patrimônio.</span></li>
<li><strong>Negocie com informação</strong><span>Preço de mercado, histórico da região e documentação em dia dão segurança para fazer uma proposta justa.</span></li>
</ol>

<h2>Comprar imóvel em Joaçaba com acompanhamento</h2>
<p>Comprar um imóvel é uma das maiores decisões financeiras da vida. Um acompanhamento próximo ajuda a evitar os dois extremos: esperar demais ou comprar sem planejamento. Do primeiro cálculo à entrega das chaves, eu acompanho cada etapa com você em Joaçaba, Herval d'Oeste, Luzerna e região.</p>
<p>Quer ver o que está disponível agora? Confira os <a href="/#imoveis">imóveis à venda</a>.</p>
""",
        "fontes": [
            ("Índice FipeZAP: preços de imóveis sobem 6,52% em 2025 (InfoMoney)", "https://www.infomoney.com.br/?p=3162261"),
            ("FipeZAP: preço dos imóveis sobe 0,48% em outubro de 2026 (BP Money)", "https://bpmoney.com.br/educacao-financeira/preco-imoveis-sobe-048-outubro-cidades-mais-caras-fipezap/"),
            ("IBGE: rendimento médio da população atinge R$ 3.367 em 2025", "https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2012-agencia-de-noticias/noticias/46579-rendimento-medio-da-populacao-brasileira-atinge-r-3-367-em-2025.html"),
        ],
    },
]


def artigo(p, e, wa_link, site):
    fontes = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' for t, u in p["fontes"])
    return f'''
<div class="wrap post-wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › <a href="/blog/">Blog</a> › {e(p["kicker"])}</nav>
  <header class="post-head">
    <span class="post-kicker">{e(p["kicker"])}</span>
    <h1>{e(p["titulo"])}</h1>
    <p class="post-lead">{e(p["lead"])}</p>
    <div class="post-meta"><img src="/manu.jpg" alt="Manu, corretora de imóveis" width="44" height="44"><span>Por <strong><a href="/sobre/">Manu</a></strong> · CRECI/SC&nbsp;54977&nbsp;F<br>{e(p["data_br"])} · {e(p["leitura"])}</span></div>
  </header>
  <figure class="post-cover"><img src="{e(p["capa"])}" alt="{e(p["capa_alt"])}" width="1920" height="1080" fetchpriority="high"><figcaption>{p["capa_credito"]}</figcaption></figure>
  <article class="post">
    {p["corpo"]}
    <div class="post-cta cta-band"><div><strong>Quer montar seu plano de compra?</strong>Acompanhamento imobiliário exclusivo, do primeiro cálculo à entrega das chaves.</div>
      <div class="acts"><a class="btn btn-accent" href="{e(wa_link)}" target="_blank" rel="noopener">Falar com a Manu</a><a class="btn btn-line" href="/simulador-financiamento/" style="color:#fff;border-color:rgba(255,255,255,.5)">Simular financiamento</a></div></div>
    <div class="post-src"><strong>Fontes</strong><ul>{fontes}</ul></div>
  </article>
</div>'''


def lista(e):
    cards = "".join(f'''<a class="blog-card" href="/blog/{p["slug"]}/"><img src="{e(p["capa"])}" alt="" width="1920" height="1080" loading="lazy">
<div><span class="post-kicker">{e(p["kicker"])} · {e(p["data_br"])}</span><h2>{e(p["titulo"])}</h2><p>{e(p["resumo"])}</p></div></a>''' for p in POSTS)
    return f'''
<div class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › Blog</nav>
  <header class="post-head" style="max-width:760px"><span class="post-kicker">Blog</span>
    <h1>Dicas e análises sobre o mercado imobiliário</h1>
    <p class="post-lead">Comprar, vender e financiar imóveis em Joaçaba, Herval d'Oeste, Luzerna e região, explicado de forma simples.</p></header>
  <div class="blog-grid">{cards}</div>
</div>'''


def jsonld(p, site):
    return {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["titulo"], "description": p["resumo"],
            "image": [site + p["og"], site + p["capa"]], "datePublished": p["data"], "dateModified": p.get("atualizado", p["data"]),
            "author": AUTORA, "publisher": {"@type": "Organization", "name": "Manu Corretora", "logo": {"@type": "ImageObject", "url": site + "/logo-manu-g.png"}},
            "mainEntityOfPage": f"{site}/blog/{p['slug']}/", "inLanguage": "pt-BR"}
