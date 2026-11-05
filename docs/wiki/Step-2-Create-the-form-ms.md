[English](Step-2-Create-the-form) · [Dansk](Step-2-Create-the-form-da) · **Bahasa Malaysia**

# Langkah 2: Cipta borang dan Sheet

Kami membuat borang Google dengan tiga soalan jawapan pendek (alamat, harga, pautan) dan memautkan Google Sheet kepadanya, supaya setiap jawapan menjadi satu baris. Tangkapan skrin menunjukkan borang kosong.

![Langkah 2: Cipta borang dan Sheet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/02-empty-form.png)

## Apa yang kita peroleh

- Borang ialah sasaran yang tidak kita kawal: strukturnya tetap, jadi program mesti mengikutinya.
- Google memaparkan borang dalam bahasa lokasi pelawat. Tambah `?hl=en` pada pautan supaya label Inggeris sentiasa sepadan.
- Borang mesti terbuka kepada sesiapa yang mempunyai pautan, kerana pelayar yang dimulakan program tidak log masuk.
- Pautan disimpan dalam pemboleh ubah persekitaran `FORM_URL`, tidak pernah dalam repositori.

Kembali ke [Utama](Home-ms)
