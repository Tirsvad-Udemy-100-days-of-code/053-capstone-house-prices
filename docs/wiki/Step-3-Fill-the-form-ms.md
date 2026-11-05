[English](Step-3-Fill-the-form) · [Dansk](Step-3-Fill-the-form-da) · **Bahasa Malaysia**

# Langkah 3: Isi borang dengan Selenium

Kami membuka borang dengan Selenium, menaip alamat, harga dan pautan, dan menekan Hantar, sekali bagi setiap penyenaraian. Tangkapan skrin menunjukkan pengesahan satu jawapan yang direkodkan.

![Langkah 3: Isi borang dengan Selenium](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/03-response-recorded.png)

## Apa yang kita peroleh

- Penantian eksplisit (`WebDriverWait`) diperlukan: menaip sebelum medan dipaparkan menyebabkan `ElementNotInteractableException`.
- Pelayar berjalan tanpa kepala dalam bekas Docker, jadi ujian tidak pernah mengambil tetikus dan papan kekunci komputer.
- Satu port (`FormSubmitter`) menyembunyikan Selenium daripada bahagian program yang lain, jadi pengisi diuji dengan pemacu palsu.
- Semua penentu lokasi berada dalam `constants.py`.

Kembali ke [Utama](Home-ms)
