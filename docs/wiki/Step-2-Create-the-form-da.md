[English](Step-2-Create-the-form) · **Dansk** · [Bahasa Malaysia](Step-2-Create-the-form-ms)

# Trin 2: Opret formularen og arket

Vi lavede en Google-formular med tre korte svar (adresse, pris, link) og koblede et Google Sheet på, så hvert svar bliver en række. Skærmbilledet viser den tomme formular.

![Trin 2: Opret formularen og arket](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/02-empty-form.png)

## Hvad vi fik ud af det

- En formular er et mål, vi ikke styrer: dens opbygning er fast, så programmet må følge den.
- Google viser formularen på sproget fra den besøgendes placering. Tilføj `?hl=en` til linket, så de engelske tekster altid passer.
- Formularen skal være åben for alle med linket, fordi den browser, programmet starter, ikke er logget ind.
- Linket ligger i miljøvariablen `FORM_URL` og aldrig i repositoriet.

Tilbage til [Hjem](Home-da)
