#!/usr/bin/env python3
"""Gera as páginas estáticas do site da Manu Corretora a partir dos imóveis do My Home.

- /imovel/<slug>/        uma página por imóvel ativo (com prévia para WhatsApp e dados para o Google)
- /imoveis-em-joacaba/ … páginas de busca por cidade e por tipo de imóvel
- /imoveis.json          mapa id -> slug usado pela página inicial
- /sitemap.xml           lista de todas as páginas para o Google

Roda no GitHub Actions (sem custo). Uso local de teste:  python3 gerador/gerar.py --dados teste.json --saida /tmp/site
"""
import argparse, datetime as dt, html, json, os, re, shutil, sys, unicodedata, urllib.parse, urllib.request

SB_URL = "https://hfirfbdpgjakinagjwcr.supabase.co"
SB_KEY = "sb_publishable_oSMuelGGnzQfIG5w4HF6yQ_Km5N8-AD"  # chave pública, só lê anúncios ativos
OWNER = "3e07538e-7a7b-4455-bede-f387bd3e528a"              # perfil Manu Corretora no My Home
SITE = "https://manucorretora.com.br"
WHATS = "5549988987121"
FONE = "(49) 98898-7121"
TYPES = {"casa": "Casa", "apartamento": "Apartamento", "terreno": "Terreno", "rural": "Imóvel rural", "comercial": "Imóvel comercial"}
TYPES_PL = {"casa": "Casas", "apartamento": "Apartamentos", "terreno": "Terrenos"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------- dados
def sb(path):
    req = urllib.request.Request(f"{SB_URL}/rest/v1/{path}", headers={"apikey": SB_KEY})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def carregar(arquivo=None):
    if arquivo:
        d = json.load(open(arquivo, encoding="utf-8"))
        return d["properties"], d["photos"]
    props = sb(f"properties?owner_id=eq.{OWNER}&status=eq.ativo&select=id,title,type,price,city,neighborhood,bedrooms,suites,parking,site_featured,area,description,cover_url,created_at&order=created_at.desc")
    photos = []
    if props:
        ids = ",".join(p["id"] for p in props)
        photos = sb(f"property_photos?property_id=in.({ids})&select=property_id,url,position,is_cover&order=position.asc")
    return props, photos


def norm(s):
    return unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode().lower()


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", norm(s)).strip("-") or "imovel"


W = {"um": 1, "uma": 1, "dois": 2, "duas": 2, "tres": 3, "quatro": 4}


def from_desc(desc, words):
    t = norm(desc)
    total, found = 0, False
    for w in words:
        for m in re.finditer(r"(\d+|um|uma|dois|duas|tres|quatro)\s*" + w, t):
            v = m.group(1)
            total += int(v) if v.isdigit() else W[v]
            found = True
    return total if found else None


def preparar(props, photos):
    usados = set()
    out = []
    for p in props:
        ph = [x for x in photos if x["property_id"] == p["id"]]
        cover = next((x["url"] for x in ph if x.get("is_cover")), None) or (ph[0]["url"] if ph else None) or p.get("cover_url")
        urls = [x["url"] for x in ph] or ([cover] if cover else [])
        suites = p.get("suites") if p.get("suites") is not None else from_desc(p.get("description"), ["suite"])
        dorms = from_desc(p.get("description"), ["dormitorio", "quarto"])
        beds = p.get("bedrooms") or ((suites or 0) + (dorms or 0)) or None
        parking = p.get("parking") if p.get("parking") is not None else from_desc(p.get("description"), ["vagas?", "garage"])
        base = slugify(p["title"])
        slug = base if base not in usados else f"{base}-{p['id'][:6]}"
        usados.add(slug)
        out.append({**p, "cover": cover, "photos": urls, "beds": beds, "suites": suites, "parking": parking, "slug": slug})
    return out


# ---------------------------------------------------------------- formatação
e = lambda s: html.escape(str(s if s is not None else ""), quote=True)


def brl(v):
    if v is None:
        return "Consulte"
    return "R$ " + f"{float(v):,.0f}".replace(",", ".")


def m2(v):
    if not v:
        return ""
    n = float(v)
    s = f"{n:,.0f}" if n == int(n) else f"{n:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".") + " m²"


def wa(msg):
    return f"https://wa.me/{WHATS}?text=" + urllib.parse.quote(msg)


def loc(p):
    return ", ".join(x for x in [p.get("neighborhood"), p.get("city")] if x)


def resumo(p):
    partes = []
    if p["type"] != "terreno":
        if p["beds"]: partes.append(f"{p['beds']} dorm.")
        if p["suites"]: partes.append(f"{p['suites']} suíte" + ("s" if p["suites"] > 1 else ""))
        if p["parking"]: partes.append(f"{p['parking']} vaga" + ("s" if p["parking"] > 1 else ""))
    if p.get("area"): partes.append(m2(p["area"]))
    partes.append(loc(p))
    return " · ".join(x for x in partes if x)


# ---------------------------------------------------------------- pedaços do layout (copiados da página inicial)
def partes_do_index():
    s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    style = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    header = re.search(r'<header class="top">.*?</header>', s, re.S).group(0)
    header = header.replace('href="#inicio"', 'href="/"').replace('href="#', 'href="/#')
    footer = re.search(r"<footer>.*?</footer>", s, re.S).group(0)
    footer = re.sub(r'\s*<div class="wrap credit-row">.*?</div>', "", footer, flags=re.S)
    wafloat = re.search(r'<a class="wa-float js-wa".*?</a>', s, re.S).group(0)
    seo = re.search(r'<nav class="seo-links".*?</nav>', s, re.S).group(0)
    return style, header, footer, wafloat, seo


def fixar_whats(html_txt, msg_padrao):
    def rep(m):
        tag = m.group(0)
        dm = re.search(r'data-msg="([^"]*)"', tag)
        msg = html.unescape(dm.group(1)) if dm else msg_padrao
        return re.sub(r'href="#"', f'href="{e(wa(msg))}"', tag, count=1)
    return re.sub(r'<a [^>]*class="[^"]*js-wa[^"]*"[^>]*>', rep, html_txt)


ICON = {
    "bed": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18V7"/><path d="M3 14h18v4"/><path d="M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.6"/></svg>',
    "bath": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h16v3a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4Z"/><path d="M6 12V6a2 2 0 0 1 4 0"/><path d="M7 19l-1 2M17 19l1 2"/></svg>',
    "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 16V11l2-5h10l2 5v5"/><path d="M3 16h18v2H3z"/><circle cx="7.5" cy="13" r="1"/><circle cx="16.5" cy="13" r="1"/></svg>',
    "area": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.4"/></svg>',
    "cam": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h3l2-3h6l2 3h3v11H4Z"/><circle cx="12" cy="13" r="3.5"/></svg>',
    "prev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>',
    "next": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>',
}


def feats(p):
    if p["type"] == "terreno":
        itens = [(ICON["area"], m2(p.get("area")) or "–", "Terreno")]
        estilo = ' style="grid-template-columns:1fr"'
    else:
        a = p.get("area")
        itens = [(ICON["bed"], p["beds"] if p["beds"] is not None else "–", "Dorm."),
                 (ICON["bath"], p["suites"] if p["suites"] is not None else "–", "Suítes"),
                 (ICON["car"], p["parking"] if p["parking"] is not None else "–", "Vagas"),
                 (ICON["area"], (m2(a).replace(" m²", "") if a else "–"), "Área m²")]
        estilo = ""
    return f'<div class="feats"{estilo}>' + "".join(f'<div class="feat-i">{i}<b class="num">{e(v)}</b><small>{l}</small></div>' for i, v, l in itens) + "</div>"


def foto(url, alt, eager=False):
    if not url:
        return ""
    lz = "" if eager else ' loading="lazy"'
    return (f'<span class="ph"><img class="ph-bg" src="{e(url)}" alt="" aria-hidden="true"{lz}>'
            f'<img class="ph-fg" src="{e(url)}" alt="{e(alt)}"{lz} onload="window.__fit&&window.__fit(this)"></span>')


def card(p):
    return f'''<a class="card" href="/imovel/{p["slug"]}/">
  <div class="card-img">{foto(p["cover"], p["title"])}<span class="tag">{TYPES.get(p["type"], "Imóvel")}</span>{f'<span class="card-photos">{ICON["cam"]}{len(p["photos"])}</span>' if len(p["photos"]) > 1 else ""}</div>
  <div class="card-body">
    <div class="card-title">{e(p["title"])}</div>
    <div class="card-loc">{ICON["pin"]}{e(loc(p))}</div>
    {feats(p)}
    <div class="card-price"><small>Valor de venda</small><strong class="num">{brl(p.get("price"))}</strong></div>
    <span class="btn btn-accent">Ver detalhes</span>
  </div>
</a>'''


EXTRA_CSS = """
a.card{color:inherit;text-decoration:none}
.crumbs{font-size:.85rem;color:var(--muted);padding-block:18px 0}
.crumbs a{color:inherit}
.pg-head{padding-block:14px 8px}
.pg-head h1{font-size:clamp(1.6rem,3.6vw,2.4rem)}
.pg-head p{color:var(--muted);max-width:70ch;margin:10px 0 0}
.gal2{position:relative;border-radius:20px;overflow:hidden;background:#111;margin-top:16px}
.gal2-track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none}
.gal2-track::-webkit-scrollbar{display:none}
.gal2-track img{flex:0 0 100%;width:100%;aspect-ratio:16/10;max-height:72vh;object-fit:contain;scroll-snap-align:center;background:#111}
@media (max-width:760px){.gal2{border-radius:14px}.gal2-track img{aspect-ratio:4/3}}
.gal2 .arrow{position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,.9);border:0;color:#1F1B17}
.gal2 .arrow.prev{left:12px}.gal2 .arrow.next{right:12px}
@media (hover:none){.gal2 .arrow{display:none}}
.gal2 .gal-count{position:absolute;bottom:12px;left:12px;background:rgba(0,0,0,.6);color:#fff;font-size:.8rem;padding:4px 10px;border-radius:999px}
.prop{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:32px;padding-block:24px 40px}
@media (max-width:860px){.prop{grid-template-columns:1fr}.prop .side{order:-1;position:static}}
.prop h1{font-size:clamp(1.6rem,3.4vw,2.3rem);margin-top:10px}
.prop .side{position:sticky;top:90px}
.prop .side .card-price strong{font-size:1.7rem}
.prop .side .btn{width:100%}
.desc{white-space:pre-line;color:var(--muted);margin-top:16px}
.seo-links{display:flex;flex-wrap:wrap;gap:8px}
.seo-links a{border:1px solid var(--line);background:var(--bg);padding:8px 14px;border-radius:999px;font-size:.9rem;font-weight:500;text-decoration:none}
.seo-links a:hover{border-color:var(--accent)}
.empty a{color:var(--accent-ink)}
"""

FIT_JS = """<script>
window.__fit=function(img){var b=img.parentElement,bw=b.clientWidth,bh=b.clientHeight;if(!img.naturalWidth||!bw||!bh)return;var d=Math.abs((img.naturalWidth/img.naturalHeight)/(bw/bh)-1);b.classList.toggle("fit",d>0.18)};
document.getElementById("yr")&&(document.getElementById("yr").textContent=new Date().getFullYear());
</script>"""


def pagina(titulo, descricao, url, corpo, style, header, footer, wafloat, og_img=None, jsonld=None, msg_whats="Olá, Manu! Vi seu site e gostaria de mais informações."):
    og_img = og_img or f"{SITE}/joacaba-2.jpg"
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titulo)}</title>
<meta name="description" content="{e(descricao)}">
<link rel="canonical" href="{e(url)}">
<meta name="theme-color" content="#FFA41B">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Manu Corretora">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(descricao)}">
<meta property="og:url" content="{e(url)}">
<meta property="og:image" content="{e(og_img)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{style}{EXTRA_CSS}</style>
{ld}
</head>
<body class="m2">
{header}
<main>
{corpo}
</main>
{footer}
{wafloat}
{FIT_JS}
</body>
</html>
'''
    return fixar_whats(doc, msg_whats)


AGENTE = {"@type": "RealEstateAgent", "name": "Manu Corretora", "url": SITE + "/", "telephone": "+55 49 98898-7121",
          "areaServed": ["Joaçaba", "Herval d'Oeste", "Luzerna"],
          "address": {"@type": "PostalAddress", "addressLocality": "Joaçaba", "addressRegion": "SC", "addressCountry": "BR"}}


def pagina_imovel(p, todos, partes):
    style, header, footer, wafloat, seo = partes
    url = f"{SITE}/imovel/{p['slug']}/"
    tipo = TYPES.get(p["type"], "Imóvel")
    cidade = p.get("city") or "Joaçaba"
    titulo = f"{p['title']} · {tipo} à venda em {cidade} · {brl(p.get('price'))} | Manu Corretora"
    desc_txt = re.sub(r"\s+", " ", p.get("description") or "").strip()
    descricao = f"{tipo} à venda em {loc(p)}: {resumo(p)}. {brl(p.get('price'))}. " + desc_txt
    descricao = descricao[:300]
    msg = f'Olá, Manu! Tenho interesse no imóvel "{p["title"]}" ({brl(p.get("price"))}) que vi no seu site.'
    lz = ' loading="lazy"'
    fotos = "".join(f'<img src="{e(u)}" alt="{e(p["title"])} – foto {i+1}"{"" if i == 0 else lz}>' for i, u in enumerate(p["photos"]))
    nav = (f'<button type="button" class="arrow prev" aria-label="Foto anterior">{ICON["prev"]}</button>'
           f'<button type="button" class="arrow next" aria-label="Próxima foto">{ICON["next"]}</button>') if len(p["photos"]) > 1 else ""
    outros = [x for x in todos if x["id"] != p["id"]][:4]
    cards_outros = "".join(card(x) for x in outros)
    bloco_outros = ('<section class="block alt"><div class="wrap"><div class="sec-head"><div><h2>Outros imóveis da Manu</h2></div></div>'
                    f'<div class="grid" id="grid">{cards_outros}</div></div></section>') if outros else ""
    cidade_slug = {"joacaba": "imoveis-em-joacaba", "herval d'oeste": "imoveis-em-herval-doeste", "luzerna": "imoveis-em-luzerna"}.get(norm(cidade), "imoveis-em-joacaba")
    corpo = f'''
<div class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › <a href="/{cidade_slug}/">Imóveis em {e(cidade)}</a> › {e(p["title"])}</nav>
  <div class="gal2" id="gal">
    <div class="gal2-track" id="track">{fotos}</div>
    {nav}
    <span class="gal-count num" id="gcount">1 / {len(p["photos"])}</span>
  </div>
  <div class="prop">
    <div>
      <span class="tag">{tipo} à venda</span>
      <h1>{e(p["title"])}</h1>
      <div class="card-loc" style="margin-top:6px">{ICON["pin"]}{e(loc(p))}</div>
      <div class="desc">{e(p.get("description"))}</div>
    </div>
    <aside class="side">
      <small>Valor de venda</small>
      <div class="card-price"><strong class="num">{brl(p.get("price"))}</strong></div>
      {feats(p)}
      <a class="btn btn-accent" href="{e(wa(msg))}" target="_blank" rel="noopener">Tenho interesse</a>
      <a class="btn btn-line" href="{e(wa('Olá, Manu! Gostaria de agendar uma visita ao imóvel "' + p["title"] + '".'))}" target="_blank" rel="noopener">Agendar visita</a>
      <button type="button" class="btn btn-ghost" id="share">Compartilhar imóvel</button>
      <small>Manu Corretora · CRECI 54977 F · WhatsApp {FONE}</small>
    </aside>
  </div>
</div>
{bloco_outros}
<section class="block"><div class="wrap">
  <div class="sec-head"><div><h2>Mais buscas em Joaçaba e região</h2></div></div>
  {seo}
</div></section>
<script>
(function(){{
  var t=document.getElementById("track"),c=document.getElementById("gcount"),n=t.children.length;
  function at(){{return Math.round(t.scrollLeft/t.clientWidth)}}
  t.addEventListener("scroll",function(){{c.textContent=(at()+1)+" / "+n}},{{passive:true}});
  var g=document.getElementById("gal"),pv=g.querySelector(".prev"),nx=g.querySelector(".next");
  function go(i){{i=(i+n)%n;t.scrollTo({{left:i*t.clientWidth,behavior:"smooth"}})}}
  if(pv)pv.onclick=function(){{go(at()-1)}};if(nx)nx.onclick=function(){{go(at()+1)}};
  document.getElementById("share").onclick=function(){{
    var u=location.href.split("#")[0],b=this;
    if(navigator.share){{navigator.share({{title:document.title,url:u}}).catch(function(){{}});return}}
    if(navigator.clipboard){{navigator.clipboard.writeText(u).then(function(){{b.textContent="Link copiado!"}},function(){{prompt("Copie o link:",u)}})}}else prompt("Copie o link:",u);
  }};
}})();
</script>'''
    oferta = {"@context": "https://schema.org", "@type": "RealEstateListing", "name": p["title"], "url": url,
              "description": desc_txt[:500], "image": p["photos"][:6],
              "datePosted": (p.get("created_at") or "")[:10] or None,
              "offers": {"@type": "Offer", "price": float(p["price"]) if p.get("price") is not None else None, "priceCurrency": "BRL", "availability": "https://schema.org/InStock", "seller": AGENTE}}
    trilha = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": f"Imóveis em {cidade}", "item": f"{SITE}/{cidade_slug}/"},
        {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]}
    return pagina(titulo, descricao, url, corpo, style, header, footer, wafloat, og_img=p["cover"], jsonld=[oferta, trilha], msg_whats=msg)


# Páginas de busca: cidade e tipo. Textos próprios para cada uma (nada de repetir palavras-chave à toa).
BUSCAS = [
    {"slug": "imoveis-em-joacaba", "h1": "Imóveis à venda em Joaçaba",
     "title": "Imóveis à venda em Joaçaba (SC) · Casas, apartamentos e terrenos | Manu Corretora",
     "intro": "Casas, apartamentos e terrenos à venda em Joaçaba, selecionados pela corretora Manu (CRECI 54977 F). Se você procura imóvel no Centro, no Frei Bruno, no Anzolin ou em outro bairro da cidade, fale comigo pelo WhatsApp que eu te ajudo a encontrar a melhor opção.",
     "filtro": lambda p: True},
    {"slug": "imoveis-em-herval-doeste", "h1": "Imóveis em Herval d'Oeste e região",
     "title": "Imóveis à venda em Herval d'Oeste (SC) e região | Manu Corretora",
     "intro": "Atendo quem quer comprar ou vender imóvel em Herval d'Oeste, cidade vizinha de Joaçaba, com o mesmo cuidado na negociação e na documentação. Abaixo estão os imóveis disponíveis agora na região. Se você procura algo específico em Herval d'Oeste, me chame no WhatsApp: muitas oportunidades chegam antes de serem anunciadas.",
     "filtro": lambda p: True},
    {"slug": "imoveis-em-luzerna", "h1": "Imóveis em Luzerna e região",
     "title": "Imóveis à venda em Luzerna (SC) e região | Manu Corretora",
     "intro": "Também atendo Luzerna, para quem busca casa, apartamento ou terreno com a tranquilidade de uma cidade menor perto de Joaçaba. Veja os imóveis disponíveis na região e me conte o que você procura em Luzerna.",
     "filtro": lambda p: True},
    {"slug": "casas-a-venda", "h1": "Casas à venda em Joaçaba, Herval d'Oeste e Luzerna",
     "title": "Casas à venda em Joaçaba, Herval d'Oeste e Luzerna | Manu Corretora",
     "intro": "Casas à venda em Joaçaba e região, de casas prontas para morar a opções com terreno amplo. Toque em uma casa para ver todas as fotos, a metragem e o valor.",
     "filtro": lambda p: p["type"] == "casa"},
    {"slug": "apartamentos-a-venda", "h1": "Apartamentos à venda em Joaçaba, Herval d'Oeste e Luzerna",
     "title": "Apartamentos à venda em Joaçaba, Herval d'Oeste e Luzerna | Manu Corretora",
     "intro": "Apartamentos à venda em Joaçaba e região, com opções no Centro, perto de comércio, escolas e serviços. Veja suítes, vagas de garagem e área de cada um e agende sua visita pelo WhatsApp.",
     "filtro": lambda p: p["type"] == "apartamento"},
    {"slug": "terrenos-a-venda", "h1": "Terrenos à venda em Joaçaba, Herval d'Oeste e Luzerna",
     "title": "Terrenos à venda em Joaçaba, Herval d'Oeste e Luzerna | Manu Corretora",
     "intro": "Terrenos à venda em Joaçaba e região para construir sua casa ou investir. Veja a metragem e a localização de cada terreno e fale comigo para saber sobre documentação e viabilidade de construção.",
     "filtro": lambda p: p["type"] == "terreno"},
]


def pagina_busca(b, todos, partes):
    style, header, footer, wafloat, seo = partes
    url = f"{SITE}/{b['slug']}/"
    lista = [p for p in todos if b["filtro"](p)]
    vazio = (f'<div class="empty">No momento não há imóveis deste tipo anunciados no site. '
             f'<a href="{e(wa("Olá, Manu! Estou procurando: " + b["h1"].lower() + ". Pode me ajudar?"))}" target="_blank" rel="noopener">Me chame no WhatsApp</a> '
             f'e eu procuro para você.</div>')
    corpo = f'''
<div class="wrap">
  <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a> › {e(b["h1"])}</nav>
  <div class="pg-head"><h1>{e(b["h1"])}</h1><p>{e(b["intro"])}</p></div>
</div>
<section class="block"><div class="wrap">
  <div class="sec-head"><div><h2>{len(lista)} imóve{"is" if len(lista) != 1 else "l"} disponíve{"is" if len(lista) != 1 else "l"}</h2></div></div>
  <div class="grid" id="grid">{"".join(card(p) for p in lista) or vazio}</div>
</div></section>
<section class="block alt"><div class="wrap">
  <div class="sec-head"><div><h2>Outras buscas</h2></div></div>
  {seo}
  <p style="color:var(--muted);margin-top:18px">Corretora Manu · CRECI 54977 F · Atendimento em Joaçaba, Herval d'Oeste, Luzerna e região pelo WhatsApp {FONE}.</p>
</div></section>'''
    itens = {"@context": "https://schema.org", "@type": "ItemList", "name": b["h1"], "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": f"{SITE}/imovel/{p['slug']}/"} for i, p in enumerate(lista)]}
    return pagina(b["title"], b["intro"][:300], url, corpo, style, header, footer, wafloat, jsonld=[itens])


# ---------------------------------------------------------------- gravação
def gravar(caminho, conteudo):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dados", help="arquivo JSON local (só para teste)")
    ap.add_argument("--saida", default=ROOT)
    a = ap.parse_args()

    props, photos = carregar(a.dados)
    todos = preparar(props, photos)
    partes = partes_do_index()
    out = a.saida
    if os.path.abspath(out) != ROOT:
        shutil.copytree(ROOT, out, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git", "gerador", ".github", "_site"))

    shutil.rmtree(os.path.join(out, "imovel"), ignore_errors=True)
    for p in todos:
        gravar(os.path.join(out, "imovel", p["slug"], "index.html"), pagina_imovel(p, todos, partes))
    for b in BUSCAS:
        gravar(os.path.join(out, b["slug"], "index.html"), pagina_busca(b, todos, partes))
    gravar(os.path.join(out, "imoveis.json"), json.dumps({p["id"]: p["slug"] for p in todos}, ensure_ascii=False))

    hoje = dt.date.today().isoformat()
    urls = [(SITE + "/", "1.0")] + [(f"{SITE}/{b['slug']}/", "0.8") for b in BUSCAS] + [(f"{SITE}/imovel/{p['slug']}/", "0.9") for p in todos]
    gravar(os.path.join(out, "sitemap.xml"), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "".join(f"  <url><loc>{u}</loc><lastmod>{hoje}</lastmod><priority>{pr}</priority></url>\n" for u, pr in urls) + "</urlset>\n")
    print(f"{len(todos)} imóveis, {len(BUSCAS)} páginas de busca, {len(urls)} endereços no sitemap")


if __name__ == "__main__":
    sys.exit(main())
