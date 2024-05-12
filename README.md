# Scraping-Shopee-Produk-Review

## Nomenklatur Dataset ##
Atribut       | Penjelasan
------------- | -------------
nama pengguna         | nama user yang memberikan review
produk         | nama produk dari toko
review       | isi text review
rating       | rating yang diberikan pada produk
waktu transaksi       | waktu user transaksi
## Cara Mendapatkan URL Page Review ##
1. Buka toko mana yang ingin diambil review nya, kemudian klik bagian penilaian
![image](https://github.com/fflah/Scraping-Shopee-Produk-Review/assets/32528100/a13540f4-0a28-4747-a4fe-924275a7986b)
1. Copy urlnya, Example `https://shopee.co.id/buyer/#########/rating?shop_id=#########`

## Setup main.py ##

- Buat virtual environment -> python -m venv env
- Activate environment -> source env/bin/activate (linux dan mac)
- Install requirement.txt ->  pip install -r requirements.txt
- Cara mendapatkan cookies.json (Ref https://fajrulfalah18.medium.com/melewati-sistem-auth-website-di-selenium-emang-bisa-8d88a8a177e8)
- Jalankan -> python main.py

