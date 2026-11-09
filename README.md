# Website van Jensen

Openbare pagina's van Jensen op https://jensen.wilhil.nl, via GitHub Pages: de voorpagina en de privacyverklaring.

- `privacy/index.html` wordt gemaakt door `build.py` uit `app/assets/privacy/privacyverklaring_nl.md` in de repository van de app. Wijzig de tekst daar, en draai dan `python3 build.py` (verwacht de app-repository in `../Jensen`, of geef het pad mee).
- Kleuren in `style.css` zijn gelijk aan `JensenPalette` in de app. Lettertype Outfit staat in `fonts/` (OFL-licentie).
- `CNAME` vertelt GitHub Pages het domein. DNS: vier A-records op `jensen.wilhil.nl` naar 185.199.108.153 t/m 185.199.111.153 (geen CNAME, zodat er ook TXT-records voor de mail op kunnen).
- Lokaal bekijken: `python3 -m http.server 8080` en open http://localhost:8080.
