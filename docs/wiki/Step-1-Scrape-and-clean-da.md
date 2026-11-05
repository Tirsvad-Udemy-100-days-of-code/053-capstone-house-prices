[English](Step-1-Scrape-and-clean) · **Dansk** · [Bahasa Malaysia](Step-1-Scrape-and-clean-ms)

# Trin 1: Hent og rens

Vi hentede siden med `requests` og sendte headerne `User-Agent` og `Accept-Language`, så siden svarer som til en browser, og læste den med BeautifulSoup. Vi rensede teksten: priser bliver til `$1,234`, og adresser mister linjeskift, lodrette streger og ekstra mellemrum. Skærmbilledet viser resultatet af `python -m house_prices --scrape-only`.

![Trin 1: Hent og rens](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/01-scrape-output.png)

## Hvad vi fik ud af det

- Headers afgør, hvad en hjemmeside sender tilbage.
- CSS-selectorer finder links, adresser og priser i HTML'en.
- Rensning er en lille ren funktion (`clean_price`, `clean_address`), så den er let at teste med en gemt kopi af siden.
- Listerne bruger opgavens navne: `get_links`, `get_addresses`, `get_prices`.

Tilbage til [Hjem](Home-da)
