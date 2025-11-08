# Prediksi Harga Rumah Menggunakan Linear Regression

**Anggota Kelompok**

- Felix Luwinta (221111259)
- Constantin Anggriano (221112405)

---

## Deskripsi Singkat
Proyek ini membuat model Linear Regression untuk memprediksi harga rumah berdasarkan fitur: `sqft` (luas), `bedrooms`, `bathrooms`, `lot_size`, dan `year_built`.

Model dilatih pada dataset sintetis (dihasilkan oleh script) dan disajikan melalui aplikasi web sederhana (frontend + backend Flask). Frontend menampilkan form input, hasil prediksi, dan grafik perbandingan.

---

## Struktur Repository (sesuai format tugas)

```
frontend/            # kode frontend (HTML, CSS, JS)
backend/             # kode backend (Flask), data, model
video/               # simpan file video demo (MP4) atau link
README.md            # dokumentasi utama
train_model.py       # script training (root)
backend/data/        # script generate dataset & csv
backend/model/       # model.pkl & scaler.pkl (setelah training)
```

---

## Cara Instal & Menjalankan (Lingkungan Lokal)

1. Pastikan Python 3.10+ terinstall.
2. Extract repo dan buka terminal di folder proyek.
3. (Opsional tapi direkomendasikan) Buat virtual environment:

```bash
python -m venv venv
# Windows:
venv\\Scripts\\activate
# mac/linux:
source venv/bin/activate
```

4. Install dependency untuk backend:
```bash
pip install -r backend/requirements.txt
```

5. Generate dataset (jika belum ada):
```bash
python backend/data/generate_and_save_data.py
```

6. Train model:
```bash
python train_model.py
```

7. Jalankan aplikasi Flask (server + frontend static):
```bash
python backend/app.py
```

8. Buka browser: `http://localhost:5000` — gunakan form untuk prediksi.

---

## Petunjuk Penggunaan Aplikasi
- Masukkan nilai fitur pada form (sqft, bedrooms, bathrooms, lot_size, year_built).
- Klik **Prediksi** untuk melihat estimasi harga.
- Klik **Preview Data** untuk melihat sample dataset.
- Klik **Retrain** untuk melatih ulang model dari `backend/data/housing.csv`.

---

## Kriteria Penilaian (yang dipenuhi)
- Folder FE & BE lengkap.
- Dokumentasi `README.md` berisi instruksi instalasi & penggunaan.
- Model AI dan proses training & evaluasi tersedia.
- Aplikasi berjalan secara lokal dan terintegrasi.

---

## Catatan Teknis & Pembatasan
- Data dibuat sintetis untuk keperluan demo; tidak representatif untuk aplikasi produksi.
- Untuk produksi, diperlukan validasi data, fitur engineering, dan model kompleks.
- Jangan upload `backend/model/model.pkl` ke repo publik jika menggunakan data sensitif.

---

## Link Video & Submission
Letakkan file video (MP4) di folder `video/` atau ganti isi `video/link_video.txt` dengan link YouTube/Drive.

