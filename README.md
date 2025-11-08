<div align="center">

# 🏠 Prediksi Harga Rumah Menggunakan Linear Regression  

📊 _Proyek Machine Learning untuk memprediksi harga rumah berbasis data properti_

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)](https://scikit-learn.org/)
[![GitHub repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/felixluwint/prediksi-harga-rumah-linear-regression)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)

</div>

---

## 👨‍🎓 Anggota Kelompok
| Nama Lengkap | NIM |
|---------------|------|
| **Felix Luwinta** | 221111259 |
| **Constantin Anggriano** | 221112405 |

---

## 🎯 Deskripsi Proyek
Proyek ini bertujuan untuk membangun **model Machine Learning Linear Regression** yang mampu memprediksi harga rumah berdasarkan beberapa parameter properti seperti:

- Luas Tanah (m²)
- Luas Bangunan (m²)
- Jumlah Kamar Tidur
- Jumlah Kamar Mandi
- Skor Lokasi

Model ini diintegrasikan dengan **Flask** sebagai backend API dan **HTML + JavaScript** untuk tampilan antarmuka pengguna (frontend).

---

## ⚙️ Fitur Utama
✅ Prediksi harga rumah berbasis input pengguna  
✅ Model dilatih dengan dataset simulasi (fitur relevan properti)  
✅ Aplikasi berbasis web, dapat dijalankan lokal  
✅ Tampilan user-friendly dan responsif  
✅ Kode terstruktur dan mudah dikembangkan  

---

## 🧠 Teknologi yang Digunakan
| Komponen | Teknologi |
|-----------|------------|
| Bahasa Pemrograman | Python 3.x |
| Framework Backend | Flask |
| Machine Learning | scikit-learn (Linear Regression) |
| Library Tambahan | NumPy, Joblib |
| Frontend | HTML, CSS, JavaScript |
| Kontrol Versi | Git & GitHub |

---

## 🛠️ Cara Instalasi dan Menjalankan Proyek

### 1️⃣ Clone Repository
```bash
git clone https://github.com/felixluwint/prediksi-harga-rumah-linear-regression.git
cd prediksi-harga-rumah-linear-regression
````

### 2️⃣ Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3️⃣ Jalankan Backend Flask

```bash
python app.py
```

Jika berhasil, akan muncul pesan:

```
 * Running on http://127.0.0.1:5000
```

### 4️⃣ Buka Aplikasi di Browser

```
http://127.0.0.1:5000
```

Masukkan data seperti **luas tanah, luas bangunan, kamar tidur, kamar mandi, dan skor lokasi** → klik tombol **Prediksi Harga**.

---

## 📦 Struktur Folder

```
house_price_lr_full/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── model/
│       ├── model.pkl
│       └── scaler.pkl
│
├── frontend/
│   └── index.html
│
├── train_model.py
├── README.md
└── video/link_video.txt
```

---

## 📊 Contoh Hasil Prediksi

```
Prediksi Harga Rumah: Rp 620.000.000
```

---

## 🎥 Demo Video

📽️ Link video demo dapat dilihat pada:

```
[video/link_video.txt](https://youtu.be/JEWf_2L6n5k)
```

Atau unggah ke YouTube dan tambahkan tautan di sini:
➡️ [Tonton Demo di YouTube](https://youtube.com)

---

## 💡 Catatan

* Pastikan Python sudah terinstall.
* Jalankan `pip install flask flask-cors numpy scikit-learn joblib` jika ada error missing library.
* Proyek ini dibuat untuk keperluan **akademik dan pembelajaran Machine Learning**.

---

## 👨‍💻 Kontributor

Made with ❤️ by **Felix Luwinta** & **Constantin Anggriano**
Universitas ✨ — 2025

📎 [GitHub Repository](https://github.com/felixluwint/prediksi-harga-rumah-linear-regression)
