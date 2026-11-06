"""Gera a prévia em _site/previa/ e ajusta os links internos para ficarem dentro de /previa/."""
import os, re, subprocess, sys
saida = sys.argv[1] if len(sys.argv) > 1 else "_site/previa"
args = [sys.executable, os.path.join(os.path.dirname(__file__), "gerador", "gerar.py"), "--saida", saida] + sys.argv[2:]
subprocess.run(args, check=True)
PAGINAS = r"(?:imovel/|imoveis-[a-z-]+/|casas-a-venda/|apartamentos-a-venda/|terrenos-a-venda/|simulador-financiamento/|sobre/|avaliar-imovel/|politica-de-privacidade/|#|\")"
for raiz, _, arqs in os.walk(saida):
    for a in arqs:
        if not a.endswith(".html"):
            continue
        f = os.path.join(raiz, a)
        s = open(f, encoding="utf-8").read()
        s = re.sub(r'href="/(?=' + PAGINAS[3:], 'href="/previa/', s)
        s = s.replace('fetch("/imoveis.json"', 'fetch("/previa/imoveis.json"').replace("`/imovel/${", "`/previa/imovel/${")
        s = s.replace("/simulador-financiamento/?imovel=", "/previa/simulador-financiamento/?imovel=").replace("/previa/previa/", "/previa/")
        if 'name="robots"' not in s:
            s = s.replace("<head>", '<head>\n<meta name="robots" content="noindex">', 1)
        s = s.replace("<body", '<body data-previa="1"', 1)
        s = s.replace("</body>", '<div style="position:fixed;left:12px;bottom:12px;z-index:40;background:#C9A15A;color:#0E2A14;font:700 12px system-ui;padding:5px 10px;border-radius:999px">PRÉVIA · não publicada</div></body>', 1)
        open(f, "w", encoding="utf-8").write(s)
for x in ("sitemap.xml", "robots.txt", "CNAME", "google96cde1483d736429.html", "montar_previa.py"):
    try: os.remove(os.path.join(saida, x))
    except FileNotFoundError: pass
print("prévia pronta em", saida)
