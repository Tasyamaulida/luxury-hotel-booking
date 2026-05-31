# 🏨 Luxury Hotel Booking System

## 📖 Deskripsi Project

Luxury Hotel Booking System adalah aplikasi web berbasis Django yang digunakan untuk melakukan pemesanan kamar hotel secara online. Sistem menyediakan halaman publik untuk pengguna umum dan dashboard admin untuk mengelola data hotel.

Aplikasi ini dikembangkan sebagai tugas Final Stage Mata Kuliah Proyek Perangkat Lunak (PPL).

---

# 🎯 Tujuan Aplikasi

Menyediakan sistem pemesanan hotel yang memungkinkan:

* Pengguna melihat informasi hotel
* Pengguna melakukan booking kamar
* Pengguna melihat riwayat booking
* Admin mengelola data kamar
* Admin mengelola data booking
* Admin mengelola data pelanggan
* Admin memantau ketersediaan kamar

---

# 🚀 Fitur Utama

## 👤 User Features

### Landing Page

Menampilkan informasi utama hotel dan promosi.

### Daftar Kamar

Menampilkan seluruh kamar yang tersedia lengkap dengan:

* Gambar kamar
* Harga
* Deskripsi kamar
* Tombol booking

### Fasilitas Hotel

Menampilkan fasilitas yang tersedia seperti:

* Kolam Renang
* Gym
* Spa
* Restoran
* Meeting Room

### Tentang Kami

Menampilkan profil dan informasi hotel.

### Booking Kamar

Pengguna dapat:

* Memilih kamar
* Mengisi tanggal check-in
* Mengisi tanggal check-out
* Menentukan jumlah tamu

### My Booking

Menampilkan:

* Riwayat booking
* Status booking
* Total pembayaran
* Detail kamar yang dipesan

---

## 🔐 Admin Features

### Dashboard Admin

Menampilkan statistik:

* Total Booking
* Total Customer
* Kamar Tersedia
* Check-In Hari Ini

### Manajemen Kamar (CRUD)

Admin dapat:

* Menambah kamar
* Melihat kamar
* Mengubah data kamar
* Menghapus kamar

### Manajemen Booking

Admin dapat:

* Melihat seluruh booking
* Mengubah status booking

Status booking:

* Pending
* Confirmed
* Cancelled
* Selesai

### Manajemen Customer

Admin dapat:

* Melihat data pelanggan
* Memantau aktivitas pelanggan

---

# 🏗️ Arsitektur Sistem

Project menggunakan arsitektur MVT (Model View Template) milik Django.

### Model

Mengelola database:

* Room
* Booking
* User

### View

Mengelola logika aplikasi.

### Template

Mengelola tampilan antarmuka pengguna.

---

# 🛠️ Teknologi yang Digunakan

## Backend

* Python 3
* Django

## Frontend

* HTML5
* CSS3
* Bootstrap 5

## Database

* SQLite3

## Tools

* Visual Studio Code
* Git
* GitHub

---

# 📂 Struktur Project

```text
hotel_booking/
│
├── booking/
│   ├── migrations/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── core/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   │
│   ├── admin/
│   │   ├── base_site.html
│   │   ├── dashboard.html
│   │   ├── booking_list.html
│   │   ├── customers.html
│   │   ├── room_form.html
│   │   ├── room_list.html
│   │   ├── index.html
│   │   └── login.html
│   │
│   ├── home.html
│   ├── kamar.html
│   ├── fasilitas.html
│   ├── tentang_kami.html
│   ├── booking_form.html
│   ├── booking_user.html
│   ├── my_bookings.html
│   └── register.html
│
├── static/
│   └── images/
│       ├── hotel-luxury.png
│       ├── admin.png
│       ├── card_pool.png
│       ├── gym.jpg
│       ├── spa.jpg
│       ├── dit.jpg
│       └── ...
│
├── media/
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# 🗄️ Database

Database yang digunakan:

SQLite3

Tabel utama:

### Room

* name
* category
* price
* description
* image
* total_rooms

### Booking

* user
* room
* check_in
* check_out
* guests
* total_price
* status

### User

Menggunakan Django Authentication System.

---

# ⚙️ Cara Menjalankan Project

## 1. Clone Repository

```bash
git clone https://github.com/Tasyamaulida/luxury-hotel-booking.git
```

## 2. Masuk ke Folder Project

```bash
cd hotel_booking
```

## 3. Membuat Virtual Environment

```bash
python -m venv venv
```

## 4. Aktifkan Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

## 5. Install Dependency

```bash
pip install django
```

## 6. Jalankan Migration

```bash
python manage.py migrate
```

## 7. Buat Akun Admin

```bash
python manage.py createsuperuser
```

## 8. Menjalankan Server

```bash
python manage.py runserver
```

Buka browser:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```
usernma: admin
password: admin123
---

# 📸 Hasil Aplikasi

## Halaman User

* Landing Page
* Katalog Kamar
* Booking Kamar
* My Booking
* Fasilitas
* Tentang Kami

## Dashboard Admin

* Dashboard Statistik
* CRUD Kamar
* Kelola Booking
* Kelola Customer

---

# 📚 Mata Kuliah

Proyek Perangkat Lunak (PPL)

Week 11 – Final Stage

---

# 👩‍💻 Developer

Nama : Tasya Maulida

Program Studi : Informatika

Universitas Syiah Kuala
