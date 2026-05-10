# 🧮 Pola & Pemikiran Aljabar dalam Matematika

> **Website Pembelajaran Interaktif untuk Mahasiswa Calon Guru Sekolah Dasar**

Aplikasi web interaktif berbasis **Streamlit** yang menyajikan materi komprehensif tentang
*Patterns and Algebraic Thinking* (Pola dan Pemikiran Aljabar) untuk pembelajaran
matematika SD Indonesia.

---

## ✨ Fitur Utama

- 🎨 **Toggle Light/Dark Mode** di sidebar — pengguna bebas pilih tampilan terang atau gelap
- 🎚️ **Simulasi interaktif** dengan slider di setiap bab
- 🖼️ **Visualisasi gambar** minimal satu per subbab
- 🌹 **Lab eksperimen persamaan**: linear, kuadrat, sinus, Lissajous, mawar polar, spiral
- 🎯 **Tiga soal penalaran** dengan petunjuk dan pembahasan
- 🇮🇩 Seluruh konten **Bahasa Indonesia** sesuai Kurikulum Merdeka

## 📚 Daftar Bab

| Bab | Topik |
|-----|-------|
| 1 | Pengenalan Pola |
| 2 | Jenis-Jenis Pola (Berulang, Tumbuh, Berkurang) |
| 3 | Pola Bilangan (Aritmetika, Geometri, Figuratif, Fibonacci) |
| 4 | Dari Pola ke Generalisasi |
| 5 | Pemikiran Aljabar (Variabel, Timbangan, Mesin Fungsi) |
| 6 | Eksplorasi Pola Persamaan (Lab Interaktif) |
| 7 | Soal Penalaran Pola |

---

## 🚀 Menjalankan Lokal

```bash
git clone https://github.com/USERNAME/pola-aljabar-sd.git
cd pola-aljabar-sd
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Deploy ke Streamlit Cloud

```bash
git add .
git commit -m "Update aplikasi dengan toggle Light/Dark"
git push origin main
```

Streamlit Cloud akan otomatis _re-deploy_ aplikasi dalam 1–2 menit.

---

## 📁 Struktur Proyek

```
pola-aljabar-sd/
├── .streamlit/
│   └── config.toml         # Konfigurasi tema (HANYA [theme] — TIDAK BOLEH ada [server])
├── app.py                  # Aplikasi utama
├── requirements.txt
├── README.md
└── .gitignore
```

⚠️ **PENTING:** File `.streamlit/config.toml` **HANYA boleh berisi section `[theme]`**.
Jangan tambahkan section `[server]` atau `[browser]` karena dapat menyebabkan aplikasi
gagal _start_ di Streamlit Cloud.

---

## 🎨 Cara Kerja Toggle Light/Dark Mode

Pengguna dapat memilih mode tampilan via radio button di paling atas sidebar:

- ☀️ **Terang** — latar terang dengan teks gelap (default), cocok untuk presentasi & siang hari
- 🌙 **Gelap** — latar gelap dengan teks terang, nyaman untuk malam atau ruang redup

Pilihan akan **persisten selama sesi browser**.

---

## 📖 Referensi

- Van de Walle, J. A., et al. (2018). *Elementary and Middle School Mathematics*
- NCTM. (2000). *Principles and Standards for School Mathematics*
- Kemendikbudristek. (2022). *Capaian Pembelajaran Matematika SD*

---

<p align="center">
💙 Dibuat dengan ❤️ untuk pendidikan matematika SD di Indonesia
</p>
