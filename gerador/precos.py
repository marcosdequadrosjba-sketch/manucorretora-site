"""Bloco de preços, perguntas frequentes e páginas de bairro, calculados a partir dos imóveis anunciados.

Tudo aqui é refeito a cada geração do site (a cada push e 2x por dia), então os números acompanham
os imóveis ativos no My Home. São os imóveis anunciados pela Manu, não uma pesquisa do mercado inteiro,
e os textos deixam isso claro.
"""
import re
import statistics
import unicodedata

CIDADES = {"joacaba": "Joaçaba", "hervaldoeste": "Herval d'Oeste", "luzerna": "Luzerna"}
CIDADE_SLUG = {"joacaba": "imoveis-em-joacaba", "hervaldoeste": "imoveis-em-herval-doeste", "luzerna": "imoveis-em-luzerna"}

# Texto opcional sobre cada bairro (2 ou 3 frases). Bairro sem texto aqui usa só os números.
SOBRE_BAIRRO = {
    "centro": "O Centro de Joaçaba reúne comércio, bancos, serviços e escolas a poucos passos, e concentra boa parte dos prédios residenciais da cidade. É a escolha de quem quer resolver tudo a pé.",
}

TIPO_TXT = {  # singular, plural, gênero
    "casa": ("casa", "casas", "f"),
    "apartamento": ("apartamento", "apartamentos", "m"),
    "terreno": ("terreno", "terrenos", "m"),
    None: ("imóvel", "imóveis", "m"),
}


def norm(s):
    return unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode().lower()


def ckey(s):
    """Chave de cidade sem acento, espaço nem apóstrofo: "Herval d Oeste" e "Herval d'Oeste" viram "hervaldoeste"."""
    return re.sub(r"[^a-z]", "", norm(s))


def bkey(s):
    return re.sub(r"\s+", " ", norm(s)).strip()


def slug_bairro(bairro, cidade):
    cid = {"joacaba": "joacaba", "hervaldoeste": "herval-doeste", "luzerna": "luzerna"}.get(ckey(cidade), norm(cidade))
    return re.sub(r"[^a-z0-9]+", "-", f"imoveis-{norm(bairro)}-{cid}").strip("-")


def prep(bairro):
    """"no Centro", "na Cidade Alta", "na Vila Pedrini"."""
    return "na" if norm(bairro).split(" ")[0] in ("cidade", "vila", "linha", "rua", "avenida") else "no"


def plural(n, sing, pl):
    return sing if n == 1 else pl


def lista_e(itens):
    itens = list(itens)
    return itens[0] if len(itens) == 1 else ", ".join(itens[:-1]) + " e " + itens[-1]


def onde(p):
    return p.get("neighborhood") or p.get("city") or "Joaçaba"


def resumo_txt(lista, tipo, local, brl, m2_preco=True):
    """Frase com a faixa de preço. Ex.: "Hoje, as 5 casas anunciadas pela Manu em Joaçaba custam de R$ 350.000 (Cidade Alta) a ..."."""
    sing, pl, g = TIPO_TXT.get(tipo, TIPO_TXT[None])
    com = [p for p in lista if p.get("price")]
    if not com:
        return ""
    anun = "anunciada" if g == "f" else "anunciado"
    if len(com) == 1:
        p = com[0]
        art = "uma" if g == "f" else "um"
        return f"No momento, há {art} {sing} {anun} pela Manu {local}: {p['title'].strip()} ({onde(p)}), por {brl(p['price'])}."
    art = "as" if g == "f" else "os"
    barato = min(com, key=lambda p: float(p["price"]))
    caro = max(com, key=lambda p: float(p["price"]))
    med = statistics.median(float(p["price"]) for p in com)
    txt = (f"Hoje, {art} {len(com)} {pl} {anun}s pela Manu {local} custam de {brl(barato['price'])} ({onde(barato)}) "
           f"a {brl(caro['price'])} ({onde(caro)}). Metade del{'as' if g == 'f' else 'es'} custa até {brl(med)}.")
    por_m2 = [float(p["price"]) / float(p["area"]) for p in com if p.get("area") and p.get("type") != "terreno"]
    if m2_preco and len(por_m2) >= 3:
        txt += f" Considerando a área construída informada, o metro quadrado fica em torno de {brl(round(statistics.median(por_m2), -2))}."
    return txt


def tabela(linhas, cab, e):
    n = ' class="n"'
    head = "".join(f'<th{n if i else ""}>{e(c)}</th>' for i, c in enumerate(cab))
    body = "".join("<tr>" + "".join(f'<td{n if i else ""}>{c}</td>' for i, c in enumerate(l)) + "</tr>" for l in linhas)
    return f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def faixa(grupo, brl):
    v = sorted(float(p["price"]) for p in grupo if p.get("price"))
    if not v:
        return "Consulte", "–"
    return (brl(v[0]) if len(v) == 1 else f"{brl(v[0])} a {brl(v[-1])}"), str(len(grupo))


def tabela_bairros(lista, e, brl, links=None):
    """Bairro | Imóveis | Faixa de preço. Mostra a cidade junto quando há mais de uma."""
    links = links or {}
    varias = len({ckey(p.get("city")) for p in lista}) > 1
    grupos = {}
    for p in lista:
        if not p.get("neighborhood"):
            continue
        grupos.setdefault((bkey(p["neighborhood"]), ckey(p.get("city"))), []).append(p)
    if len(grupos) < 2:
        return ""
    linhas = []
    for (bk, ck), g in sorted(grupos.items(), key=lambda kv: min(float(p.get("price") or 0) for p in kv[1])):
        nome = g[0]["neighborhood"] + (f" ({g[0].get('city')})" if varias else "")
        url = links.get((bk, ck))
        nome_html = f'<a href="{url}">{e(nome)}</a>' if url else e(nome)
        fx, n = faixa(g, brl)
        linhas.append([nome_html, n, fx])
    return tabela(linhas, ["Bairro", "Imóveis", "Faixa de preço"], e)


def tabela_tipos(lista, e, brl):
    grupos = {}
    for p in lista:
        grupos.setdefault(p["type"], []).append(p)
    if len(grupos) < 2:
        return ""
    linhas = []
    for t in ("casa", "apartamento", "terreno"):
        if t in grupos:
            fx, n = faixa(grupos[t], brl)
            linhas.append([TIPO_TXT[t][1].capitalize(), n, fx])
    return tabela(linhas, ["Tipo", "Imóveis", "Faixa de preço"], e)


def bloco(lista, tipo, local, titulo_h2, e, brl, data_br, links=None):
    """Seção "Quanto custa..." com a frase-resumo e as tabelas. Devolve ("", "") se não houver preços."""
    txt = resumo_txt(lista, tipo, local, brl)
    if not txt:
        return "", ""
    tabs = (tabela_tipos(lista, e, brl) if tipo is None else "") + tabela_bairros(lista, e, brl, links)
    html_txt = f'''<section class="block"><div class="wrap post-wrap" style="margin-inline:0">
  <div class="sec-head"><div><h2>{e(titulo_h2)}</h2></div></div>
  <p>{e(txt)}</p>
  {tabs}
  <p class="note" style="margin-top:8px">Valores dos imóveis anunciados no site, atualizados em {e(data_br)}. Para saber quanto vale um imóvel específico, peça uma <a href="/avaliar-imovel/">avaliação</a>.</p>
</div></section>'''
    return html_txt, txt


def faq(lista, tipo, local, txt_preco, sing_pergunta=None):
    """Perguntas frequentes geradas com os dados da página. sing_pergunta: "uma casa", "um apartamento"…"""
    sing, pl, g = TIPO_TXT.get(tipo, TIPO_TXT[None])
    sp = sing_pergunta or (("uma " if g == "f" else "um ") + sing)
    out = []
    if txt_preco:
        out.append((f"Quanto custa {sp} {local}?", txt_preco + " O preço varia com o bairro, o tamanho, a garagem e o estado de conservação."))
    bairros = sorted({p["neighborhood"].strip() for p in lista if p.get("neighborhood")})
    if len(bairros) >= 2:
        anun = "anunciadas" if g == "f" else "anunciados"
        out.append((f"Em quais bairros há {pl} à venda {local}?",
                    f"Hoje há {pl} {anun} pela Manu em {lista_e(bairros)}. A lista muda conforme os imóveis são vendidos e novos chegam; se você procura outro bairro, fale com a Manu pelo WhatsApp."))
    if tipo != "terreno":
        out.append((f"Dá para comprar {sp} {local} com financiamento e FGTS?",
                    "Sim, desde que o imóvel tenha a documentação regular e o comprador atenda às regras do banco. O FGTS pode ser usado na entrada ou para amortizar quando o comprador e o imóvel cumprem as regras do Fundo. O simulador de financiamento do site mostra a parcela nos sistemas SAC e Price em vários bancos."))
    out.append(("A Manu atende só em Joaçaba?",
                "Não. A Manu (CRECI/SC 54977 F) atende Joaçaba, Herval d'Oeste, Luzerna e região, e trabalha em parceria com outras imobiliárias, então pode apresentar também imóveis que ainda não estão no site."))
    return out


def faq_html(itens, e):
    if not itens:
        return ""
    det = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in itens)
    return f'''<section class="block alt"><div class="wrap post-wrap" style="margin-inline:0">
  <div class="sec-head"><div><h2>Perguntas frequentes</h2></div></div>
  <div class="faq">{det}</div>
</div></section>'''


def faq_ld(itens):
    if not itens:
        return []
    return [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in itens]}]


def bairros(todos):
    """Bairros com pelo menos um imóvel. Devolve {(bkey, ckey): {"nome", "cidade", "slug", "imoveis"}}."""
    out = {}
    for p in todos:
        if not p.get("neighborhood"):
            continue
        k = (bkey(p["neighborhood"]), ckey(p.get("city")))
        if k not in out:
            out[k] = {"nome": p["neighborhood"].strip(), "cidade": p.get("city") or "Joaçaba",
                      "slug": slug_bairro(p["neighborhood"], p.get("city") or "Joaçaba"), "imoveis": []}
        out[k]["imoveis"].append(p)
    return out


def tipos_titulo(lista):
    tipos = {p["type"] for p in lista}
    if tipos == {"casa"}:
        return "Casas", "casa"
    if tipos == {"apartamento"}:
        return "Apartamentos", "apartamento"
    if tipos == {"terreno"}:
        return "Terrenos", "terreno"
    if tipos == {"casa", "apartamento"}:
        return "Casas e apartamentos", None
    return "Imóveis", None
