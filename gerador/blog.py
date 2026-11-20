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
/* motivos numerados, citação, checklist, quadro do simulador e perguntas frequentes */
.motivo{display:grid;grid-template-columns:56px minmax(0,1fr);gap:4px 16px;border:1px solid var(--line);border-radius:18px;padding:20px 22px 6px;margin:16px 0;background:var(--bg)}
.motivo .mn{display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--brand);color:var(--accent-hi);font-family:var(--display);font-weight:700;font-size:1.2rem}
.motivo h3{font-size:1.12rem;margin:8px 0 6px}
.motivo p{margin:0 0 12px}
.motivo .pr{color:var(--muted);font-size:.98rem}
.post blockquote{margin:28px 0;padding:4px 0 4px 22px;border-left:4px solid var(--accent);font-family:var(--display);font-size:1.3rem;line-height:1.4;color:var(--ink)}
.post .check{list-style:none;padding:0}
.post .check li{position:relative;padding-left:32px}
.post .check li::before{content:"";position:absolute;left:0;top:5px;width:22px;height:22px;border-radius:50%;background:var(--accent-soft) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%238A6A2E' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m5 12 5 5 9-10'/%3E%3C/svg%3E") center/14px no-repeat}
.simu{display:flex;gap:18px;align-items:center;justify-content:space-between;flex-wrap:wrap;background:var(--surface);border-radius:18px;padding:20px 22px;margin:22px 0}
.simu div{flex:1;min-width:240px}
.simu strong{display:block;font-family:var(--display);font-size:1.1rem;margin-bottom:4px}
.simu p{margin:0;color:var(--muted);font-size:.98rem;line-height:1.6}
.faq details{border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:10px 0;background:var(--bg)}
.faq summary{cursor:pointer;font-weight:700;list-style:none;display:flex;justify-content:space-between;gap:12px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:var(--accent-ink);font-size:1.3rem;line-height:1}
.faq details[open] summary::after{content:"–"}
.faq details p{margin:10px 0 0;color:var(--muted)}
@media (max-width:620px){.motivo{grid-template-columns:1fr;padding:18px 18px 4px}.post blockquote{font-size:1.15rem}}
"""

CREDITO_JBA = 'Joaçaba (SC). Foto: Suhaibharraka, <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>, via <a href="https://commons.wikimedia.org/w/index.php?curid=133214067" target="_blank" rel="noopener">Wikimedia Commons</a>'

POSTS = [
    {
        "slug": "visitou-imoveis-com-varios-corretores",
        "titulo": "Visitou imóveis com vários corretores e ainda não encontrou o que busca? Veja por quê",
        "titulo_seo": "Visitou imóveis com vários corretores e não encontrou? Veja por quê | Manu Corretora",
        "resumo": "Visitar imóveis com vários corretores nem sempre ajuda. Entenda exclusividade, parceria entre imobiliárias, a documentação do imóvel e como escolher um corretor de imóveis de confiança em Joaçaba e região.",
        "lead": "Três motivos comuns que levam a esse cansaço, o que a lei diz sobre exclusividade e parceria entre imobiliárias, e como escolher um corretor de imóveis de confiança em Joaçaba e região.",
        "kicker": "Comprar imóvel",
        "data": "2026-11-19",
        "data_br": "19 de novembro de 2026",
        "capa": "/blog/img/visitou-imoveis-com-varios-corretores.jpg",
        "capa_alt": "Visitou imóveis com vários corretores e ainda não encontrou o que busca? Artigo da Manu, corretora de imóveis em Joaçaba",
        "og": "/blog/img/visitou-imoveis-com-varios-corretores-og.jpg",
        "leitura": "8 min de leitura",
        "cta_titulo": "Deseja uma assessoria imobiliária com seriedade e compromisso?",
        "cta_texto": "É só me chamar. Começamos pelo diagnóstico do que você quer e precisa.",
        "corpo": """
<div class="tldr"><strong>Resposta curta</strong><p>Na maioria das vezes, o problema não é a falta de imóveis à venda, e sim a falta de direção na busca. Falar com vários corretores ao mesmo tempo costuma repetir os mesmos imóveis e enfraquecer a negociação. Um corretor de confiança, que trabalha em parceria com outras imobiliárias, dá acesso ao mercado com uma estratégia só.</p></div>

<p>Você separou um sábado, visitou três casas com um corretor, dois apartamentos com outro, recebeu uma lista no WhatsApp de um terceiro… e voltou para casa com a sensação de que o imóvel ideal não existe. Se isso soa familiar, você não está sozinho.</p>

<h2>Por que tanta gente procura imóvel com vários corretores</h2>
<p>Comprar um imóvel é, para a maioria das famílias, a maior decisão financeira da vida. É natural querer ver tudo e não deixar nenhuma oportunidade escapar. E a internet facilita: hoje dá para olhar dezenas de anúncios de casas e apartamentos à venda antes mesmo de marcar a primeira visita.</p>
<p>O interesse pela casa própria continua alto. Uma pesquisa da Brain Inteligência Estratégica apontou, no início de 2026, que <strong>49% das famílias pretendem comprar um imóvel</strong>, o maior patamar em um ano. Muita gente procurando ao mesmo tempo significa mais concorrência pelos bons imóveis e mais pressa na hora de decidir.</p>

<div class="callout"><b>88%</b><p>dos compradores de imóveis nos Estados Unidos fecharam negócio por meio de um corretor ou imobiliária, segundo a National Association of Realtors (2025). Mesmo com todos os anúncios na internet, quase todo comprador ainda recorre a um profissional para filtrar, negociar e conferir a documentação.</p></div>

<h2>Os três motivos mais comuns</h2>
<p>No dia a dia como corretora de imóveis em Joaçaba, escuto quase sempre as mesmas três razões de quem já visitou imóveis com vários corretores.</p>

<div class="motivo"><span class="mn">1</span><div>
  <h3>Medo de perder o imóvel que acha ser o ideal</h3>
  <p>O comprador acredita que o corretor tem uma “carteira exclusiva” e que falar com mais gente aumenta as chances de achar algo bom.</p>
  <p class="pr"><strong>Na prática:</strong> os mesmos imóveis aparecem várias vezes, por corretores diferentes, às vezes com preços e condições diferentes. Isso confunde o comprador e passa insegurança ao proprietário.</p>
</div></div>

<div class="motivo"><span class="mn">2</span><div>
  <h3>Desejo de comparar condições</h3>
  <p>Existe a ideia de que corretores diferentes podem oferecer valores, prazos ou poder de barganha distintos para o mesmo imóvel.</p>
  <p class="pr"><strong>Na prática:</strong> quem define o preço e as condições é o proprietário. Quando vários corretores levam propostas diferentes para o mesmo vendedor, o comprador perde força na negociação em vez de ganhar.</p>
</div></div>

<div class="motivo"><span class="mn">3</span><div>
  <h3>Uma péssima experiência com um corretor ruim</h3>
  <p>Demora na resposta, atendimento “genérico”, falta de condução clara. Quem já passou por isso tende a não confiar em ninguém e a falar com todo mundo.</p>
  <p class="pr"><strong>Na prática:</strong> a solução não é ter mais corretores, e sim o corretor certo: alguém que escuta, responde e conduz o processo do começo ao fim.</p>
</div></div>

<h2>Exclusividade e parceria entre imobiliárias: o que muda para você</h2>
<p>Um corretor pode, sim, trabalhar com <strong>imóveis em exclusividade</strong>: o proprietário autoriza por escrito um único profissional ou imobiliária a vender o imóvel. O Código Civil trata do contrato de corretagem nos artigos 722 a 729 e, no art. 726, garante ao corretor com exclusividade a remuneração integral mesmo que o negócio seja fechado sem a sua mediação, salvo se for comprovada a sua inércia ou ociosidade.</p>
<p>Isso é bom para o proprietário, porque o corretor investe de verdade na venda. E é bom para o comprador, porque há um responsável claro pelas informações do imóvel.</p>
<p>Mas exclusividade não significa que só aquele corretor pode mostrar o imóvel. É aí que entra a <strong>parceria entre imobiliárias sérias</strong>: corretores fazem acordos entre si e dividem a comissão. Assim, o seu corretor apresenta imóveis captados por outros profissionais, e você não precisa falar com todo mundo para ter acesso ao mercado imobiliário da região.</p>

<div class="tbl"><table>
<thead><tr><th></th><th>Vários corretores ao mesmo tempo</th><th>Um corretor de confiança com parcerias</th></tr></thead>
<tbody>
<tr><td><strong>Imóveis</strong></td><td>Os mesmos, repetidos</td><td>A carteira própria e a dos parceiros</td></tr>
<tr><td><strong>Negociação</strong></td><td>Propostas soltas, sem estratégia</td><td>Uma proposta bem fundamentada</td></tr>
<tr><td><strong>Seu tempo</strong></td><td>Muitas visitas que não fazem sentido</td><td>Poucas visitas, mais certeiras</td></tr>
<tr><td><strong>Documentação</strong></td><td>Ninguém assume por inteiro</td><td>Um responsável do começo ao fim</td></tr>
</tbody></table></div>

<blockquote>A parceria entre imobiliárias sérias viabiliza condições e flexibiliza a negociação. Você ganha alcance sem perder o comando da busca.</blockquote>

<h2>O diagnóstico que vem antes da visita</h2>
<p>Diagnosticar o que você quer e precisa é primordial. É isso que direciona as melhores oportunidades, antes de qualquer visita.</p>
<ol class="steps2">
<li><strong>Momento de vida</strong><span>Casal, família crescendo, filhos saindo de casa ou investimento? Cada momento pede um tipo de imóvel.</span></li>
<li><strong>Localização</strong><span>Quais bairros de Joaçaba, Herval d'Oeste ou Luzerna fazem sentido para a sua rotina de trabalho, escola e deslocamento.</span></li>
<li><strong>Orçamento real</strong><span>Quanto de entrada você tem, se vai usar financiamento imobiliário ou FGTS e qual parcela cabe no mês sem apertar.</span></li>
<li><strong>Inegociável e desejável</strong><span>Garagem para dois carros é obrigatória ou seria bom ter? Separar as duas listas evita visitas perdidas.</span></li>
</ol>

<div class="simu"><div><strong>Descubra quanto você pode financiar</strong><p>Antes de visitar, use o <a href="/simulador-financiamento/">simulador de financiamento imobiliário</a> gratuito: informe renda, entrada e FGTS e veja a parcela nos sistemas SAC e Price, comparando Caixa, Banco do Brasil, Santander, Bradesco, Itaú e cooperativas.</p></div><a class="btn btn-accent" href="/simulador-financiamento/">Simular financiamento</a></div>

<p>Com isso claro, a busca deixa de ser “ver tudo o que aparece” e passa a ser ver só o que tem chance real de virar o seu imóvel.</p>

<h2>Como escolher um corretor de imóveis de confiança</h2>
<ul class="check">
<li><strong>Tem CRECI ativo.</strong> Pela Lei 6.530/1978, só pode exercer a corretagem quem é inscrito no Conselho Regional de Corretores de Imóveis. Peça o número e confira no site do CRECI do estado.</li>
<li><strong>Conhece a região.</strong> Saber o histórico dos bairros e a valorização de cada região faz diferença no preço e na escolha.</li>
<li><strong>Escuta antes de oferecer.</strong> Se o primeiro contato já é uma lista de imóveis, sem nenhuma pergunta sobre você, desconfie.</li>
<li><strong>Responde com clareza e no tempo combinado.</strong> O atendimento é o primeiro sinal de como será a negociação.</li>
<li><strong>Trabalha em parceria.</strong> Pergunte se ele apresenta imóveis de outras imobiliárias. Um profissional sério vai dizer que sim.</li>
<li><strong>Explica a documentação.</strong> Matrícula, certidões, financiamento, ITBI e escritura não podem ser um mistério para você.</li>
</ul>

<h2>Documentação: o que conferir antes de comprar imóvel</h2>
<p>Encontrar o imóvel é só metade do caminho. O documento mais importante é a <strong>certidão de matrícula atualizada</strong>, emitida pelo Registro de Imóveis. Pela Lei 13.097/2015 (arts. 54 a 58), ônus e ações judiciais que possam afetar o imóvel devem constar da matrícula para ter efeito contra o comprador de boa-fé.</p>
<p>Mesmo assim, uma boa assessoria imobiliária confere também:</p>
<ul>
<li>Certidões pessoais do vendedor (cíveis, trabalhistas e fiscais);</li>
<li>Débitos de IPTU e, se houver, de condomínio;</li>
<li>Regularidade da construção (habite-se e averbação da área construída);</li>
<li>Custos da compra, como ITBI, escritura e registro. Veja mais em <a href="/blog/vale-a-pena-comprar-imovel-agora/">vale a pena comprar imóvel agora ou esperar?</a></li>
</ul>

<h2>Comprar imóvel em Joaçaba com assessoria</h2>
<p>Encontre o corretor confiável. O imóvel ideal será consequência. Do diagnóstico à entrega das chaves, eu acompanho cada etapa com você em Joaçaba, Herval d'Oeste, Luzerna e região.</p>
<p>Quer ver o que está disponível agora? Confira os <a href="/#imoveis">imóveis à venda</a>.</p>
""",
        "faq": [
            ("É ruim visitar imóveis com vários corretores ao mesmo tempo?", "Não é proibido, mas costuma gerar visitas repetidas, informações desencontradas e pouca força na negociação. Com um corretor de confiança que trabalha em parceria com outras imobiliárias, você tem acesso às mesmas opções com uma estratégia única de busca e negociação."),
            ("Se eu falar com um corretor só, vou perder opções de imóveis?", "Não necessariamente. Corretores e imobiliárias sérios fazem parcerias e dividem a comissão entre si, de modo que o seu corretor consegue apresentar imóveis captados por outros profissionais."),
            ("O que é exclusividade na venda de imóveis?", "É quando o proprietário autoriza por escrito um único corretor ou imobiliária a intermediar a venda. O art. 726 do Código Civil garante a remuneração integral do corretor com exclusividade, mesmo que o negócio seja fechado sem a sua mediação, salvo se for comprovada a sua inércia ou ociosidade."),
            ("Como saber se um corretor de imóveis é regularizado?", "Peça o número do CRECI e confira a inscrição no site do Conselho Regional de Corretores de Imóveis do estado. Pela Lei 6.530/1978, só pode exercer a corretagem quem é inscrito no CRECI."),
            ("Como saber quanto posso financiar antes de visitar imóveis?", "Use o simulador de financiamento imobiliário do site com a sua renda, a entrada e o FGTS. Ele calcula a parcela nos sistemas SAC e Price e compara Caixa, Banco do Brasil, Santander, Bradesco, Itaú e cooperativas."),
        ],
        "fontes": [
            ("National Association of Realtors: 2025 Profile of Home Buyers and Sellers", "https://www.nar.realtor/news/economists-outlook/top-10-takeaways-from-nars-2025-profile-of-home-buyers-and-sellers"),
            ("Intenção de compra de imóveis atinge maior nível em um ano (Exame)", "https://exame.com/mercado-imobiliario/intencao-de-compra-de-imoveis-atinge-maior-nivel-em-um-ano/"),
            ("Código Civil, Lei 10.406/2002, arts. 722 a 729 (corretagem)", "https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm"),
            ("Lei 6.530/1978: profissão de corretor de imóveis", "https://www.planalto.gov.br/ccivil_03/leis/l6530.htm"),
            ("Lei 13.097/2015, arts. 54 a 58 (concentração dos atos na matrícula)", "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13097.htm"),
        ],
    },
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
  <figure class="post-cover"><img src="{e(p["capa"])}" alt="{e(p["capa_alt"])}" width="1920" height="1080" fetchpriority="high">{f'<figcaption>{p["capa_credito"]}</figcaption>' if p.get("capa_credito") else ""}</figure>
  <article class="post">
    {p["corpo"]}
    {faq_html(p, e)}
    <div class="post-cta cta-band"><div><strong>{e(p.get("cta_titulo", "Quer montar seu plano de compra?"))}</strong>{e(p.get("cta_texto", "Acompanhamento imobiliário exclusivo, do primeiro cálculo à entrega das chaves."))}</div>
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


def faq_ld(p):
    """Perguntas frequentes do artigo (campo opcional "faq": lista de (pergunta, resposta)) para o Google."""
    if not p.get("faq"):
        return []
    return [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}]


def faq_html(p, e):
    """Bloco visível das perguntas frequentes, com o mesmo texto do faq_ld."""
    itens = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in p.get("faq", []))
    return f'<h2>Perguntas frequentes</h2>\n<div class="faq">{itens}</div>' if itens else ""
