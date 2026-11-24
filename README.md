# Latihan Dasar Python dan Pemrograman Berorientasi Objek

Kumpulan latihan Python yang tersusun secara bertahap, mulai dari sintaks dasar hingga pemrograman berorientasi objek (OOP). Setiap topik dibuat sebagai skrip mandiri dan dilengkapi screenshot hasil eksekusinya, sehingga setiap latihan dapat ditinjau tanpa harus menjalankan kodenya.

## Daftar Isi

- [Gambaran Umum](#gambaran-umum)
- [Prasyarat](#prasyarat)
- [Struktur Proyek](#struktur-proyek)
- [Memulai](#memulai)
- [Penggunaan](#penggunaan)
- [Daftar Materi](#daftar-materi)
- [Rincian Topik](#rincian-topik)
- [Pengujian Environment](#pengujian-environment)
- [Catatan dan Keterbatasan](#catatan-dan-keterbatasan)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)
- [Penulis](#penulis)

## Gambaran Umum

Repositori ini mendokumentasikan alur belajar Python yang progresif. Terdapat 21 topik yang diurutkan dari materi pengantar hingga konsep OOP tingkat lanjut:

- Dasar bahasa: sintaks, variabel, konstanta, tipe data, dan operator
- Alur program: percabangan dan perulangan
- Struktur data: list dan dictionary
- Organisasi kode: function dan module
- Ketahanan program dan I/O: file handling dan exception handling
- Pemrograman berorientasi objek: class dan objek, inheritance, encapsulation, polymorphism, dan abstraction
- Perkakas: virtual environment dan manajemen paket dengan `pip`

Prinsip rancangan repositori:

- Satu topik per file, sehingga tiap konsep dapat dibaca dan dijalankan secara terpisah
- Komentar pada kode menjelaskan tujuan setiap potongan program
- Setiap topik disertai screenshot hasil keluaran
- Tidak ada dependensi pihak ketiga; hanya menggunakan pustaka standar Python

## Prasyarat

| Kebutuhan | Versi | Keterangan |
|-----------|-------|------------|
| Python | 3.8 atau lebih baru | Catatan instalasi menggunakan Python 3.9 |
| pip | Sudah termasuk dalam Python | Hanya diperlukan jika membuat virtual environment |
| Sistem operasi | Linux atau macOS | `test_env.py` memakai `os.uname()` yang tidak tersedia di Windows |

Periksa instalasi Python Anda:

```bash
python3 --version
```

## Struktur Proyek

```text
tugas-pak-jihan/
├── README.md
├── .gitignore
├── requirements.txt            # Kosong: tidak ada dependensi eksternal
│
├── pengenalan                  # Catatan: pengenalan Python
├── instalasi                   # Catatan: instalasi Python di Ubuntu
│
├── hello.py                    # Struktur dasar program
├── variable.py                 # Variabel
├── konstanta.py                # Konstanta
├── tipe-data.py                # Tipe data
├── operator.py                 # Operator
├── control-flow.py             # Percabangan
├── perulangan.py               # Perulangan
├── list.py                     # List
├── dictionaries.py             # Dictionary
├── function.py                 # Function
├── file-handling.py            # Penanganan file
├── exception-handling.py       # Penanganan exception
│
├── class-dan-objek.py          # Class dan objek
├── inheritance.py              # Inheritance (pewarisan)
├── encapulation.py             # Encapsulation (enkapsulasi)
├── polymorphism.py             # Polymorphism (polimorfisme)
├── abstraction.py              # Abstraction (abstraksi)
│
├── module/
│   ├── matematika.py           # Contoh module buatan sendiri
│   └── main.py                 # Mengimpor dan memakai matematika
│
├── catatan.txt                 # Contoh file hasil file-handling.py
├── test_env.py                 # Skrip pengujian environment
│
└── screenshot/                 # Hasil eksekusi tiap topik
```

## Memulai

### 1. Dapatkan kode sumber

```bash
git clone <url-repositori>
cd tugas-pak-jihan
```

Atau unduh repositori dalam bentuk arsip ZIP lalu ekstrak.

### 2. Buat virtual environment (disarankan)

```bash
python3 -m venv venv
source venv/bin/activate
```

Di Windows, aktifkan environment dengan `venv\Scripts\activate`.

### 3. Instal dependensi

Proyek ini hanya memakai pustaka standar Python, dan `requirements.txt` sengaja dibiarkan kosong. Jika di kemudian hari ada dependensi yang ditambahkan, instal dengan:

```bash
pip install -r requirements.txt
```

## Penggunaan

Jalankan setiap latihan langsung dengan interpreter Python:

```bash
python3 hello.py
python3 list.py
python3 inheritance.py
```

### Menjalankan contoh module

Latihan `module/` harus dijalankan dari dalam foldernya agar `import matematika` dapat ditemukan:

```bash
cd module
python3 main.py
```

### Menjalankan contoh interaktif

`exception-handling.py` meminta input dari pengguna. Coba masukkan bilangan bulat yang valid, `0`, dan nilai non-angka untuk melihat setiap cabang error:

```bash
python3 exception-handling.py
```

## Daftar Materi

| No | Topik | Sumber | Hasil |
|----|-------|--------|-------|
| 1 | Pengenalan Python | `pengenalan` | [Screenshot](screenshot/bagian%20pengenalan%20dan%20instalasi%20python.png) |
| 2 | Instalasi Python | `instalasi` | [Screenshot](screenshot/bagian%20pengenalan%20dan%20instalasi%20python.png) |
| 3 | Struktur dasar program | `hello.py` | [Screenshot](screenshot/bagian%20struktur%20dasar%20python.png) |
| 4 | Variabel | `variable.py` | [Screenshot](screenshot/bagian%20variable.png) |
| 5 | Konstanta | `konstanta.py` | [Screenshot](screenshot/bagian%20kosntanta.png) |
| 6 | Tipe data | `tipe-data.py` | [Screenshot](screenshot/bagian%20tipe%20data%20.png) |
| 7 | Operator | `operator.py` | [Screenshot](screenshot/bagian%20operator.png) |
| 8 | Control flow | `control-flow.py` | [Screenshot](screenshot/bagian%20control.flow.png) |
| 9 | Perulangan | `perulangan.py` | [Screenshot](screenshot/bagian%20perulangan.png) |
| 10 | List | `list.py` | [Screenshot](screenshot/bagian%20list.png) |
| 11 | Dictionary | `dictionaries.py` | [Screenshot](screenshot/bagian%20dictionaries.png) |
| 12 | Function | `function.py` | [Screenshot](screenshot/bagian%20function.png) |
| 13 | Module | `module/` | [Screenshot](screenshot/bagian%20module.png) |
| 14 | File handling | `file-handling.py` | [Screenshot](screenshot/bagian%20file-handling.png) |
| 15 | Exception handling | `exception-handling.py` | [Screenshot](screenshot/bagian%20exception-handling.png) |
| 16 | Class dan objek | `class-dan-objek.py` | [Screenshot](screenshot/bagian%20class%20dan%20objek.png) |
| 17 | Inheritance | `inheritance.py` | [Screenshot](screenshot/bagian%20inheritance.png) |
| 18 | Encapsulation | `encapulation.py` | [Screenshot](screenshot/bagian%20encapulation.png) |
| 19 | Polymorphism | `polymorphism.py` | [Screenshot](screenshot/bagian%20polymorphism.png) |
| 20 | Abstraction | `abstraction.py` | [Screenshot](screenshot/bagian%20abstraction.png) |
| 21 | Virtual environment dan pip | Tidak ada | [Screenshot](screenshot/bagian%20yang%2019.png) |

## Rincian Topik

### Dasar Bahasa

- **Struktur dasar (`hello.py`)**: Program minimal yang mencetak pesan dengan `print()`.
- **Variabel (`variable.py`)**: Integer, float, string (kutip tunggal, kutip ganda, dan multibaris), penggabungan string, serta boolean.
- **Konstanta (`konstanta.py`)**: Mendefinisikan konstanta melalui konvensi penamaan (`PI`, `GRAVITY`, `MAX_RETRY`). Python tidak memaksa nilai tetap tidak berubah, sehingga konstanta hanya berupa konvensi.
- **Tipe data (`tipe-data.py`)**: Memeriksa tipe nilai `str`, `int`, dan `float` dengan `type()` dan f-string.
- **Operator (`operator.py`)**: Operator aritmatika (`+ - * / % **`), perbandingan (`== != < <= > >=`), dan logika (`and`, `or`, `not`).

### Alur Program

- **Percabangan (`control-flow.py`)**: Struktur `if`, `if / elif`, dan `if / elif / else` dengan contoh penilaian.
- **Perulangan (`perulangan.py`)**: Perulangan `for` pada `range`, list, dan string; perulangan `while`; serta pernyataan `break` dan `continue`.

### Struktur Data

- **List (`list.py`)**: Pembuatan, indexing positif dan negatif, `append`, `insert`, `remove`, `pop`, `clear`, `extend`, dan penggabungan dengan `+`.
- **Dictionary (`dictionaries.py`)**: Pembuatan, akses dengan `[]` dan `get()`, `keys()`, `values()`, menambah dan mengubah item dengan `update()`, serta penghapusan dengan `pop()` dan `clear()`.

### Function dan Module

- **Function (`function.py`)**: Definisi function, argumen posisional, argumen arbitrer (`*args`), argumen keyword, argumen keyword arbitrer (`**kwargs`), dan nilai default.
- **Module (`module/`)**: `matematika.py` mendefinisikan `PI`, `tambah()`, dan `kali()`. `main.py` memperlihatkan tiga cara impor: impor penuh, impor dengan alias (`as`), dan impor selektif (`from ... import ...`).

### File I/O dan Penanganan Error

- **File handling (`file-handling.py`)**: Menulis (`"w"`), menambahkan (`"a"`), dan membaca (`"r"`) file teks dengan context manager (`with open(...)`). Skrip ini menghasilkan `catatan.txt`.
- **Exception handling (`exception-handling.py`)**: `try`, `except ZeroDivisionError`, `except ValueError`, `else`, dan `finally`.

### Pemrograman Berorientasi Objek

- **Class dan objek (`class-dan-objek.py`)**: Atribut class, constructor `__init__`, method instance, dan parameter `self`.
- **Inheritance (`inheritance.py`)**: Class `Mobil` yang mewarisi `Kendaraan`, memakai `super().__init__()`.
- **Encapsulation (`encapulation.py`)**: Class `BankAccount` dengan atribut private (`__saldo`) yang hanya dapat diakses melalui method getter dan setter dengan validasi input.
- **Polymorphism (`polymorphism.py`)**: Class yang tidak berhubungan (`Kucing`, `Anjing`, `Sapi`) memiliki method `bersuara()` yang sama dan dipanggil secara seragam dalam satu perulangan.
- **Abstraction (`abstraction.py`)**: Abstract base class `Kendaraan` yang dibuat dengan `abc.ABC` dan `@abstractmethod`, lalu diimplementasikan oleh `Mobil` dan `Perahu`.

## Pengujian Environment

`test_env.py` mencetak laporan kondisi environment yang sedang dipakai, meliputi:

- Nama dan rilis sistem operasi
- Versi Python
- Lokasi executable Python
- Status virtual environment (aktif atau tidak)
- Direktori kerja saat ini

Jalankan dengan:

```bash
python3 test_env.py
```

Contoh hasilnya tersedia di [screenshot/pengujian environment.png](screenshot/pengujian%20environment.png).

## Catatan dan Keterbatasan

- **Error yang disengaja pada `variable.py`**: Bagian terakhir menetapkan `c = true` (huruf kecil) untuk menunjukkan bahwa boolean Python harus ditulis `True` atau `False`. Menjalankan seluruh skrip akan berakhir dengan `NameError`. Ini adalah perilaku yang diharapkan pada latihan tersebut.
- **Contoh abstraction**: Komentar di akhir `abstraction.py` menyebutkan bahwa membuat objek langsung dari `Kendaraan()` akan memunculkan `TypeError`. Baris tersebut sengaja tidak dieksekusi.
- **Nama file `operator.py`**: Nama ini sama dengan salah satu module pada pustaka standar Python. Jika Anda mengimpor module standar `operator` dari dalam direktori ini, Python bisa saja memuat file lokal tersebut. Ganti nama file jika proyek dikembangkan.
- **Efek samping `file-handling.py`**: Setiap kali dijalankan, skrip menimpa `catatan.txt` dengan isi baru sebelum menambahkan baris.
- **Dukungan platform**: `test_env.py` bergantung pada `os.uname()` dan akan gagal di Windows.
- **Penulisan nama file**: `encapulation.py` dan screenshot `bagian kosntanta.png` mempertahankan ejaan aslinya, dan tautan dalam dokumen ini disesuaikan persis dengan nama tersebut.
- **Catatan teks**: `pengenalan` dan `instalasi` adalah catatan belajar berupa teks biasa tanpa ekstensi. File `instalasi` masih memuat sisa penanda sitasi dan code fence yang tidak lengkap sehingga perlu dirapikan.
- **Keakuratan komentar**: Beberapa komentar di `dictionaries.py` menampilkan contoh keluaran yang tidak sepenuhnya sesuai dengan data pada skrip.

## Kontribusi

Kontribusi yang meningkatkan kejelasan atau ketepatan sangat diterima.

1. Fork repositori ini.
2. Buat branch fitur: `git checkout -b feature/perubahan-anda`
3. Simpan setiap latihan dalam file tersendiri dan tambahkan komentar singkat yang menjelaskan konsepnya.
4. Ikuti gaya penulisan [PEP 8](https://peps.python.org/pep-0008/) bila memungkinkan.
5. Tambahkan screenshot yang sesuai ke folder `screenshot/` dan perbarui tabel [Daftar Materi](#daftar-materi).
6. Lakukan commit dengan pesan yang jelas, lalu buka pull request.

## Lisensi

Saat ini belum ada file lisensi di repositori ini. Sebelum lisensi ditambahkan, seluruh hak dimiliki oleh penulis. Agar kode dapat digunakan ulang oleh pihak lain, tambahkan file `LICENSE`, misalnya MIT License, lalu rujuk di bagian ini.

## Penulis

Ganti bagian ini dengan nama, institusi, dan kontak Anda.

- Nama: _Nama Anda_
- Mata kuliah: _Nama mata kuliah_
- Dosen: Pak Jihan
