#!/usr/bin/env python3
"""Maakt privacy/index.html uit de privacyverklaring van de app.

De bron is app/assets/privacy/privacyverklaring_nl.md in de repository van Jensen; daar wijzig je de tekst.
Daarna:  python3 build.py [pad naar de Jensen-repository]   (standaard ../Jensen)

Ondersteunt alleen wat de verklaring gebruikt: # en ## koppen, alinea's en lijsten met "- ".
Adressen (https://..., e-mail) worden vanzelf een link.
"""
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "Jensen"
SOURCE = REPO / "app/assets/privacy/privacyverklaring_nl.md"

LINK = re.compile(r"(https://[^\s,)]+[^\s,).]|[\w.+-]+@[\w-]+(?:\.[\w-]+)+)")


def inline(text: str) -> str:
    out, last = [], 0
    for m in LINK.finditer(text):
        out.append(html.escape(text[last:m.start()]))
        target = m.group(0)
        href = target if target.startswith("https://") else f"mailto:{target}"
        out.append(f'<a href="{html.escape(href)}">{html.escape(target)}</a>')
        last = m.end()
    out.append(html.escape(text[last:]))
    return "".join(out)


def convert(md: str) -> tuple[str, str]:
    title, parts, para, items = "Privacyverklaring", [], [], []

    def flush():
        if para:
            parts.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()
        if items:
            parts.append("<ul>\n" + "\n".join(f"  <li>{inline(i)}</li>" for i in items) + "\n</ul>")
            items.clear()

    for line in md.splitlines():
        line = line.rstrip()
        if not line:
            flush()
        elif line.startswith("## "):
            flush()
            parts.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            flush()
            title = line[2:]
            parts.append(f"<h1>{inline(title)}</h1>")
        elif line.startswith("- "):
            if para:
                flush()
            items.append(line[2:])
        elif items:
            items[-1] += " " + line.strip()
        else:
            para.append(line.strip())
    flush()
    body = "\n".join(parts)
    # De regel met de versie direct onder de titel krijgt de stijl van metagegevens
    body = re.sub(r"(</h1>\n)<p>(Versie [^<]*)</p>", r'\1<p class="meta">\2</p>', body, count=1)
    return title, body


PAGE = """<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="icon" href="/icon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
</head>
<body>
<main>
  <header class="site"><a href="/"><img src="/icon.svg" alt="">Jensen</a></header>
<!-- Gemaakt door build.py uit app/assets/privacy/privacyverklaring_nl.md. Niet met de hand wijzigen. -->
{body}
  <footer>
    <a href="/">Jensen</a> · Contact: <a href="mailto:hiltopdevs@gmail.com">hiltopdevs@gmail.com</a>
  </footer>
</main>
</body>
</html>
"""


def main():
    title, body = convert(SOURCE.read_text(encoding="utf-8"))
    out = HERE / "privacy" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(PAGE.format(title=html.escape(title), body=body), encoding="utf-8")
    print(f"{out.relative_to(HERE)} gemaakt uit {SOURCE}")


if __name__ == "__main__":
    main()
