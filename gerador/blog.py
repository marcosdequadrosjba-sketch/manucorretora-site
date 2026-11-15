"""Blog / Conteúdos do site da Manu Corretora.

Para publicar um artigo novo: acrescente um dicionário em POSTS (o mais novo primeiro),
com o texto em HTML no campo "corpo" e as imagens em /blog/img/. O gerador cria
/blog/ (lista) e /blog/<slug>/ (artigo) e inclui tudo no sitemap.
"""

AUTORA = {"@type": "Person", "name": "Manu", "jobTitle": "Corretora de imóveis (CRECI/SC 54977 F)",
          "url": "https://manucorretora.com.br/sobre/"}

CSS = """
.post-wrap{max-width:760px}
.post-head{padding-block:30px 8px}
.post-kicker{display:inline-block;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--accent-ink)}
.post-head h1{font-size:clamp(1.9rem,4vw,2.8rem);line-height:1.12;margin:10px 0 14px}
.post-meta{display:flex;align-items:center;gap:12px;color:var(--muted);font-size:.92rem}
.post-meta img{width:42px;height:42px;border-radius:50%;object-fit:cover;object-position:50% 15%}
.post-meta strong{color:var(--ink)}
.post-hero{width:100%;height:auto!important;aspect-ratio:auto!important;object-fit:contain;border-radius:20px;margin:22px 0 6px;background:var(--surface);display:block}
.post{font-size:1.06rem;line-height:1.75;color:var(--ink)}
.post p,.post li{color:var(--ink);opacity:.92}
.post h2{font-size:clamp(1.35rem,2.6vw,1.7rem);margin:40px 0 10px;line-height:1.25}
.post h3{font-size:1.12rem;margin:26px 0 6px}
.post ul,.post ol{padding-left:22px}
.post li{margin:6px 0}
.post a{color:var(--accent-ink);text-decoration:underline;text-underline-offset:3px}
.post .tldr{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:14px;padding:18px 20px;margin:22px 0}
.post .tldr strong{display:block;margin-bottom:4px}
.post table{width:100%;border-collapse:collapse;margin:16px 0;font-size:.98rem}
.post th,.post td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line)}
.post th{font-weight:700;color:var(--muted);font-size:.85rem;text-transform:uppercase;letter-spacing:.06em}
.post td.num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.post figure{margin:26px 0;text-align:center}
.post figure img{width:100%;max-width:440px;height:auto!important;aspect-ratio:auto!important;object-fit:contain;border-radius:16px;box-shadow:var(--shadow)}
.post figcaption{font-size:.86rem;color:var(--muted);margin-top:8px}
.post .note{font-size:.9rem;color:var(--muted)}
.post-cta{margin:40px 0 10px}
.post-src{font-size:.88rem;color:var(--muted);border-top:1px solid var(--line);margin-top:34px;padding-top:16px}
.post-src a{color:var(--muted)}
.blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;padding-block:20px 10px}
.blog-card{display:flex;flex-direction:column;background:var(--bg);border:1px solid var(--line);border-radius:18px;overflow:hidden;color:inherit;text-decoration:none;box-shadow:var(--shadow)}
.blog-card img{width:100%;height:auto!important;aspect-ratio:auto!important;object-fit:cover;display:block}
.blog-card div{padding:16px 18px 20px}
.blog-card h2{font-size:1.15rem;line-height:1.3;margin:6px 0 8px}
.blog-card p{color:var(--muted);font-size:.94rem;margin:0}
"""

POSTS = [
    {
        "slug": "esperar-para-comprar-imovel-compensa",
        "titulo": "Esperar o momento certo para comprar imóvel compensa? O que os números mostram em 2026",
        "titulo_seo": "Esperar para comprar imóvel compensa? Valorização e planejamento em 2026 | Manu Corretora",
        "resumo": "Os imóveis valorizaram entre 5% e 8% ao ano no Brasil desde 2024. Veja o que isso significa na prática, quando vale a pena esperar e como se preparar para comprar em Joaçaba e região.",
        "kicker": "Mercado imobiliário",
        "data": "2026-11-15",
        "data_br": "15 de novembro de 2026",
        "imagem": "/blog/img/esperar-para-comprar-imovel.jpg",
        "leitura": "6 min de leitura",
        "corpo": """
<div class="tldr"><strong>Resposta rápida</strong>
Esperar sem um plano costuma sair caro: o preço médio dos imóveis no Brasil subiu entre 5% e 8% ao ano desde 2024. Mas comprar por impulso também é um erro. O que funciona é saber exatamente quanto você pode pagar e o que procura, e então decidir com informação.</div>

<h2>O que os dados mostram sobre a valorização dos imóveis</h2>
<p>O Índice FipeZAP, que acompanha o preço de venda de imóveis residenciais em 56 cidades brasileiras, registrou alta de <strong>7,73% em 2024</strong> e de <strong>6,52% em 2025</strong>. Nos 12 meses até outubro de 2026, a alta acumulada foi de <strong>5,44%</strong>. Nos três períodos, os imóveis subiram acima da inflação.</p>
<p>Um ponto importante: Joaçaba e as cidades vizinhas não fazem parte do índice. Os números mostram a tendência nacional, mas o preço de um imóvel aqui depende muito do bairro, do tipo e do estado de conservação. Para saber o valor real de um imóvel específico, o caminho é uma <a href="/avaliar-imovel/">avaliação</a> com base em vendas da região.</p>

<h2>E a renda, acompanhou?</h2>
<p>Muita gente afirma que “o salário nunca acompanha o preço dos imóveis”. Os dados recentes contam uma história mais equilibrada: segundo o IBGE, o rendimento médio real do brasileiro <strong>cresceu 5,4% em 2025</strong>, já descontada a inflação.</p>
<p>Ou seja, a questão não é só se a renda sobe. É se você está se preparando no mesmo ritmo em que o imóvel que você quer fica mais caro: juntando a entrada, organizando o crédito e entendendo o mercado.</p>

<h2>Na prática: quanto custa esperar</h2>
<p>Veja um exemplo simples com um imóvel de R$ 400 mil e valorização de 6% ao ano, próxima da média recente:</p>
<table>
<thead><tr><th>Tempo de espera</th><th class="num">Valor do imóvel</th><th class="num">Diferença</th></tr></thead>
<tbody>
<tr><td>Hoje</td><td class="num">R$ 400.000</td><td class="num">–</td></tr>
<tr><td>1 ano</td><td class="num">R$ 424.000</td><td class="num">+ R$ 24.000</td></tr>
<tr><td>2 anos</td><td class="num">R$ 449.440</td><td class="num">+ R$ 49.440</td></tr>
<tr><td>3 anos</td><td class="num">R$ 476.406</td><td class="num">+ R$ 76.406</td></tr>
</tbody></table>
<p class="note">Valores ilustrativos. A valorização real varia por cidade, bairro e tipo de imóvel.</p>
<p>Em dois anos, são quase R$ 50 mil a mais pelo mesmo imóvel. Muitas vezes, é justamente o valor da entrada que a pessoa estava juntando. E, se durante esse tempo você paga aluguel, esse valor também sai do bolso todo mês.</p>
<figure><img src="/blog/img/exemplo-valorizacao.jpg" alt="Exemplo: imóvel de R$ 400 mil passa a valer R$ 449 mil em 2 anos com valorização de 6% ao ano" width="810" height="1013" loading="lazy"><figcaption>O mesmo exemplo, no carrossel do Instagram da Manu.</figcaption></figure>

<h2>Por que os imóveis tendem a ficar mais caros</h2>
<ul>
<li><strong>Terreno bem localizado é limitado.</strong> As melhores regiões não aumentam de tamanho, e a procura por elas continua.</li>
<li><strong>Construir fica mais caro todo ano.</strong> Material e mão de obra sobem, e isso chega ao preço dos imóveis novos e usados.</li>
<li><strong>O aluguel também é reajustado.</strong> Enquanto espera, quem aluga continua pagando por um patrimônio que não é seu.</li>
</ul>

<h2>Quando faz sentido esperar</h2>
<p>Esperar nem sempre é um erro. Em algumas situações, adiar a compra é a decisão mais sensata:</p>
<ul>
<li>Você ainda não tem uma reserva de emergência separada do dinheiro da entrada.</li>
<li>Sua renda está instável ou deve mudar em breve.</li>
<li>Existe chance real de você mudar de cidade nos próximos anos.</li>
<li>Você tem dívidas com juros altos, como cartão ou cheque especial. Quitar essas dívidas antes costuma valer mais do que qualquer valorização.</li>
</ul>
<p>O problema não é esperar. É esperar sem saber pelo quê.</p>

<h2>Como se preparar para comprar com estratégia</h2>
<ol>
<li><strong>Conheça seu poder de compra.</strong> Some renda, FGTS e entrada, e veja quanto o banco aprova. Você pode começar pelo nosso <a href="/simulador-financiamento/">simulador de financiamento</a>, que compara SAC e Price entre os principais bancos.</li>
<li><strong>Defina suas prioridades.</strong> Bairro, tamanho, número de quartos e prazo. Saber o que é essencial evita perder tempo com visitas que não fazem sentido.</li>
<li><strong>Compare parcela e aluguel.</strong> Em muitos casos, a parcela do financiamento fica próxima do valor do aluguel, com a diferença de que você está construindo patrimônio.</li>
<li><strong>Negocie com informação.</strong> Preço de mercado, histórico da região e documentação em dia dão segurança para fazer uma proposta justa.</li>
</ol>
<figure><img src="/blog/img/como-se-preparar.jpg" alt="Quatro passos para comprar imóvel com estratégia: poder de compra, prioridades, parcela e aluguel, negociação" width="810" height="1013" loading="lazy"><figcaption>Os quatro passos, em resumo.</figcaption></figure>

<h2>Você não precisa decidir sozinho</h2>
<p>Comprar um imóvel é uma das maiores decisões financeiras da vida. Um acompanhamento próximo ajuda a evitar os dois extremos: esperar demais ou comprar sem planejamento. Do primeiro cálculo à entrega das chaves, eu acompanho cada etapa com você, em Joaçaba, Herval d'Oeste, Luzerna e região.</p>
<p>Se quiser ver opções disponíveis agora, confira os <a href="/#imoveis">imóveis à venda</a>.</p>
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
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › <a href="/blog/">Conteúdos</a> › {e(p["kicker"])}</nav>
  <header class="post-head">
    <span class="post-kicker">{e(p["kicker"])}</span>
    <h1>{e(p["titulo"])}</h1>
    <div class="post-meta"><img src="/manu.jpg" alt="Manu" width="42" height="42"><span>Por <strong><a href="/sobre/" style="color:inherit">Manu</a></strong>, corretora de imóveis · {e(p["data_br"])} · {e(p["leitura"])}</span></div>
  </header>
  <img class="post-hero" src="{e(p["imagem"])}" alt="{e(p["titulo"])}" width="1200" height="630">
  <article class="post">
    {p["corpo"]}
    <div class="post-cta cta-band"><div><strong>Quer montar seu plano de compra?</strong>Acompanhamento imobiliário exclusivo, do primeiro cálculo à entrega das chaves.</div>
      <div class="acts"><a class="btn btn-accent" href="{e(wa_link)}" target="_blank" rel="noopener">Falar com a Manu</a><a class="btn btn-line" href="/simulador-financiamento/" style="color:#fff;border-color:rgba(255,255,255,.5)">Simular financiamento</a></div></div>
    <div class="post-src"><strong>Fontes</strong><ul>{fontes}</ul></div>
  </article>
</div>'''


def lista(e):
    cards = "".join(f'''<a class="blog-card" href="/blog/{p["slug"]}/"><img src="{e(p["imagem"])}" alt="" width="1200" height="630" loading="lazy">
<div><span class="post-kicker">{e(p["kicker"])} · {e(p["data_br"])}</span><h2>{e(p["titulo"])}</h2><p>{e(p["resumo"])}</p></div></a>''' for p in POSTS)
    return f'''
<div class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › Conteúdos</nav>
  <header class="post-head" style="max-width:760px"><span class="post-kicker">Conteúdos</span>
    <h1>Dicas e análises sobre o mercado imobiliário</h1>
    <p style="color:var(--muted)">Comprar, vender e financiar imóveis em Joaçaba, Herval d'Oeste, Luzerna e região, explicado de forma simples.</p></header>
  <div class="blog-grid">{cards}</div>
</div>'''


def jsonld(p, site):
    return {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["titulo"], "description": p["resumo"],
            "image": site + p["imagem"], "datePublished": p["data"], "dateModified": p.get("atualizado", p["data"]),
            "author": AUTORA, "publisher": {"@type": "Organization", "name": "Manu Corretora", "logo": {"@type": "ImageObject", "url": site + "/logo-manu-g.png"}},
            "mainEntityOfPage": f"{site}/blog/{p['slug']}/", "inLanguage": "pt-BR"}
