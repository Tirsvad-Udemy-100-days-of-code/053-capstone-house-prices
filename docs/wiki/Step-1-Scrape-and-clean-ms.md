[English](Step-1-Scrape-and-clean) · [Dansk](Step-1-Scrape-and-clean-da) · **Bahasa Malaysia**

# Langkah 1: Ambil dan bersihkan

Kami memuat turun halaman dengan `requests`, menghantar pengepala `User-Agent` dan `Accept-Language` supaya laman web menjawab seperti kepada pelayar, dan membacanya dengan BeautifulSoup. Kami membersihkan teks: harga menjadi `$1,234`, dan alamat kehilangan baris baharu, garis menegak dan ruang tambahan. Tangkapan skrin menunjukkan hasil `python -m house_prices --scrape-only`.

![Langkah 1: Ambil dan bersihkan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/01-scrape-output.png)

## Apa yang kita peroleh

- Pengepala permintaan menentukan apa yang dihantar semula oleh laman web.
- Pemilih CSS mencari pautan, alamat dan harga dalam HTML.
- Pembersihan ialah fungsi tulen yang kecil (`clean_price`, `clean_address`), jadi mudah diuji dengan salinan halaman yang disimpan.
- Senarai menggunakan nama tugasan: `get_links`, `get_addresses`, `get_prices`.

Kembali ke [Utama](Home-ms)
