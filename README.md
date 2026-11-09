# Website van Jensen

Openbare pagina's van Jensen op https://jensen.wilhil.nl, via GitHub Pages: de voorpagina en de privacyverklaring.

- `privacy/index.html` wordt gemaakt door `build.py` uit `app/assets/privacy/privacyverklaring_nl.md` in de repository van de app. Wijzig de tekst daar, en draai dan `python3 build.py` (verwacht de app-repository in `../Jensen`, of geef het pad mee).
- Kleuren in `style.css` zijn gelijk aan `JensenPalette` in de app. Lettertype Outfit staat in `fonts/` (OFL-licentie).
- `CNAME` vertelt GitHub Pages het domein. DNS bij Mijndomein: een CNAME-record `jensen.wilhil.nl` naar `hiltopdevs-hash.github.io.` (GitHub weigert A-records op een subdomein, InvalidARecordError). Naast een CNAME kan niets anders op dezelfde naam staan. Mail van Jensen komt van `noreply@wilhil.nl`; de records daarvoor staan op `wilhil.nl` zelf.
- Lokaal bekijken: `python3 -m http.server 8080` en open http://localhost:8080.
