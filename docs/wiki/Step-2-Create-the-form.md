**English** · [Dansk](Step-2-Create-the-form-da) · [Bahasa Malaysia](Step-2-Create-the-form-ms)

# Step 2: Create the form and the Sheet

We made a Google Form with three short-answer questions (address, price, link) and linked a Google Sheet to it, so every response becomes a row. The screenshot shows the empty form.

![Step 2: Create the form and the Sheet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/02-empty-form.png)

## What we gained

- A form is a target we do not control: its structure is fixed, so the program must follow it.
- Google shows the form in the language of the visitor's location. Add `?hl=en` to the link so the English labels always match.
- The form must be open to anyone with the link, because the browser the program starts is not signed in.
- The link is kept in the environment variable `FORM_URL`, never in the repository.

Back to [Home](Home)
