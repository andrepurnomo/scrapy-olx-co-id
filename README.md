# Scrapy OLX

Scraper dengan framework scapy untuk mengoleksi data dari olx, dibuat karena kegabutan yang hqq. Mungkin bisa berguna bagi yang ingin belajar atau data mining

### Fitur yang tersedia

Berikut data yang dapat dikoleksi



| Data | Nama Fitur | Url |
| ------ | ------ | ------|
| Mobil Bekas | otomotif_bekas | https://www.olx.co.id/mobil/bekas/ |
| Motor Bekas | otomotif_bekas | https://www.olx.co.id/motor/bekas/ |

### Teknologi yang digunakan

* [Python 2.7](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively.
* [Scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way.


### Cara Penggunaan

Pastikan sudah menginstall teknologi yang digunakan, langsung sadja guys

Clone Repo

```sh
$ git clone https://github.com/andrepurnomo/scrapy-olx-co-id.git
$ cd scrapy-olx-co-id
```

Cara menjalankannya...

```sh
// scrapy crawl [nama_fitur] -o [nama_file_output].json
// contoh :
$ scrapy crawl otomotif_bekas -o motor.json
$ Masukkan url (default mobil) : https://www.olx.co.id/motor/bekas/
$ Jumlah Halaman (default 1) : 5
```

Hasil dari motor (Setiap fitur berbeda - beda hasil)

| Field | Keterangan | Tipe Data |
| ---- | ---- | ---- |
| Tahun | Tahun motor | String |
| Jarak tempuh | Jarak tempuh motor | String |
| Model | Model motor | String |
| Harga | Harga | Float |
| Nama | Judul dari iklan | String |
| Lokasi | Lokasi iklan | String |
| Penjual | Nama penjual | String |
| Tanggal | Tanggal iklan di posting | Datetime |
| Kontak | Nomor telepon penjual | String |
| Dilihat | Jumlah penonton iklan | Float |

### NB
Fitur akan terus bertambah, silahkan hubungi saya untuk fitur yang ingin ditambahkan.

License
----

MIT


**Free Software, Hell Yeah!**