[English](Step-3-Fill-the-form) · **Dansk** · [Bahasa Malaysia](Step-3-Fill-the-form-ms)

# Trin 3: Udfyld formularen med Selenium

Vi åbnede formularen med Selenium, skrev adresse, pris og link og trykkede på Send, én gang pr. annonce. Skærmbilledet viser bekræftelsen på ét registreret svar.

![Trin 3: Udfyld formularen med Selenium](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/03-response-recorded.png)

## Hvad vi fik ud af det

- Eksplicitte ventetider (`WebDriverWait`) er nødvendige: at skrive, før et felt vises, giver `ElementNotInteractableException`.
- Browseren kører headless i en Docker-container, så en test aldrig tager computerens mus og tastatur.
- En port (`FormSubmitter`) skjuler Selenium for resten af programmet, så udfylderen testes med en falsk driver.
- Alle locators ligger i `constants.py`.

Tilbage til [Hjem](Home-da)
