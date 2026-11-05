**English** · [Dansk](Step-3-Fill-the-form-da) · [Bahasa Malaysia](Step-3-Fill-the-form-ms)

# Step 3: Fill the form with Selenium

We opened the form with Selenium, typed address, price and link, and pressed Submit, once per listing. The screenshot shows the confirmation of one recorded response.

![Step 3: Fill the form with Selenium](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/03-response-recorded.png)

## What we gained

- Explicit waits (`WebDriverWait`) are needed: typing before an input is shown fails with `ElementNotInteractableException`.
- The browser runs headless in a Docker container, so a test never takes the mouse and keyboard of the computer.
- A port (`FormSubmitter`) hides Selenium from the rest of the program, so the filler is tested with a fake driver.
- All locators live in `constants.py`.

Back to [Home](Home)
