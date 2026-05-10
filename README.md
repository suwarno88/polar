# 🧮 Pola & Pemikiran Aljabar dalam Matematika

> **Website Pembelajaran Interaktif untuk Mahasiswa Calon Guru Sekolah Dasar**

Aplikasi web interaktif berbasis **Streamlit** yang menyajikan materi komprehensif tentang
*Patterns and Algebraic Thinking* (Pola dan Pemikiran Aljabar) khusus untuk konteks
pembelajaran matematika di Sekolah Dasar Indonesia.

---

## 📚 Daftar Isi Materi

| Bab | Topik |
|-----|-------|
| 1 | Pengenalan Pola |
| 2 | Jenis-Jenis Pola (Berulang, Tumbuh, Berkurang) |
| 3 | Pola Bilangan (Aritmetika, Geometri, Figuratif, Fibonacci) |
| 4 | Dari Pola ke Generalisasi |
| 5 | Pemikiran Aljabar (Variabel, Timbangan, Mesin Fungsi) |
| 6 | **Eksplorasi Pola Persamaan** (Lab Interaktif Khusus) |
| 7 | Soal Penalaran Pola (3 Soal Penalaran) |

---

## ✨ Fitur Utama

- 🎚️ **Simulasi interaktif** dengan slider di setiap bab
- 🖼️ **Visualisasi gambar** minimal satu per subbab (matplotlib)
- 🌹 **Lab eksperimen** persamaan yang menghasilkan pola unik:
  linear, kuadrat, sinus, fungsi pangkat, kurva Lissajous, kurva mawar polar, spiral
- 🎯 **Tiga soal penalaran** dengan petunjuk dan pembahasan terbuka/tertutup
- 🇮🇩 Seluruh konten dalam **Bahasa Indonesia** dengan terminologi sesuai Kurikulum Merdeka
- 🎨 Desain visual modern dengan _gradient_, _box_ konsep, dan tipografi yang ramah anak

---

## 🚀 Cara Menjalankan Secara Lokal

### Prasyarat
- Python 3.9 atau lebih baru
- pip (Python package manager)

### Langkah-langkah

```bash
# 1. Clone repository
git clone https://github.com/USERNAME/pola-aljabar-sd.git
cd pola-aljabar-sd

# 2. (Opsional tapi direkomendasikan) Buat virtual environment
python -m venv venv
# Aktivasi venv:
#   - Windows:    venv\Scripts\activate
#   - Mac/Linux:  source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan aplikasi
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`.

---

## ☁️ Deploy ke Streamlit Community Cloud (Gratis)

### Langkah 1 — Push ke GitHub

```bash
# Inisialisasi git (jika belum)
git init
git add .
git commit -m "Initial commit: Pola & Pemikiran Aljabar"

# Buat repository baru di GitHub, lalu:
git remote add origin https://github.com/USERNAME/pola-aljabar-sd.git
git branch -M main
git push -u origin main
```

### Langkah 2 — Deploy

1. Buka **https://share.streamlit.io/** dan login dengan akun GitHub.
2. Klik **"New app"**.
3. Pilih:
   - **Repository:** `USERNAME/pola-aljabar-sd`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Klik **"Deploy!"**.

Dalam beberapa menit, aplikasi Anda akan tersedia secara publik di URL seperti:
`https://USERNAME-pola-aljabar-sd-app-xxxxx.streamlit.app/`

### Langkah 3 — Update otomatis

Setiap kali Anda melakukan `git push`, Streamlit Cloud akan **otomatis melakukan re-deploy**
aplikasi dengan versi terbaru.

---

## 📁 Struktur Proyek

```
pola-aljabar-sd/
│
├── app.py              # Aplikasi Streamlit utama (semua halaman)
├── requirements.txt    # Daftar dependensi Python
├── README.md           # File ini
└── .gitignore          # (opsional) File untuk mengabaikan venv, __pycache__, dst.
```

---

## 🎓 Saran Penggunaan untuk Dosen

- **Pembelajaran Mandiri:** Mahasiswa dapat menjelajahi bab demi bab di luar jam kuliah.
- **Diskusi Kelas:** Tampilkan layar simulasi di proyektor, lalu undang mahasiswa
  memperdebatkan _"apa yang terjadi jika..."_.
- **Tugas Refleksi:** Minta mahasiswa menjawab pertanyaan pada kotak _Refleksi Calon Guru_.
- **Penilaian:** Soal Bab 7 dapat dijadikan ujian terbuka atau bahan diskusi kelompok.

---

## 🔧 Kustomisasi & Pengembangan

Aplikasi ini ditulis dalam **satu file** (`app.py`) untuk kemudahan _deployment_.
Setiap bab adalah fungsi independen (`page_ch1`, `page_ch2`, dst.) sehingga mudah:
- Menambah/mengubah konten
- Menambah bab baru (cukup tambahkan fungsi & daftarkan di `ROUTES`)
- Mengubah palet warna (lihat bagian `CUSTOM_CSS`)

---

## 📖 Referensi

- Van de Walle, J. A., et al. (2018). *Elementary and Middle School Mathematics*.
- NCTM. (2000). *Principles and Standards for School Mathematics*.
- Kemendikbudristek. (2022). *Capaian Pembelajaran Matematika SD*.
- Carpenter, T. P., et al. (2003). *Thinking Mathematically*.

---

## 📝 Lisensi

Konten edukasi disediakan untuk keperluan pembelajaran (CC BY-NC-SA).
Silakan adaptasi dan kembangkan untuk kebutuhan kelas Anda.

---

<p align="center">
💙 Dibuat dengan ❤️ untuk pendidikan matematika SD di Indonesia<br>
<em>"Karena setiap anak berhak menemukan keindahan matematika"</em>
</p>
