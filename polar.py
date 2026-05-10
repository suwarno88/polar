"""
Website Interaktif: Pola dan Pemikiran Aljabar dalam Matematika
Untuk Mahasiswa Calon Guru Sekolah Dasar
Dibuat dengan Streamlit
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, FancyBboxPatch, Polygon
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import pandas as pd

# ---------- KONFIGURASI HALAMAN ----------
st.set_page_config(
    page_title="Pola & Pemikiran Aljabar | Calon Guru SD",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)

plt.rcParams["font.family"] = "DejaVu Sans"

# ---------- CSS KUSTOM ----------
CUSTOM_CSS = """
<style>
/* ===== PALET WARNA UTAMA (LIGHT MODE PAKSA) ===== */
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%) !important;
    color: #1e293b !important;
}

/* ===== PASTIKAN SEMUA TEKS GELAP DI AREA UTAMA ===== */
.main .block-container,
.main .block-container p,
.main .block-container li,
.main .block-container span:not([class*="hero"]):not([class*="info-box"]):not([class*="concept-box"]):not([class*="example-box"]):not([class*="activity-box"]):not([class*="quiz-box"]),
.main .block-container div,
.main .block-container label,
.main .block-container td,
.main .block-container th,
.stMarkdown,
.stMarkdown p,
.stMarkdown li,
.stMarkdown span,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span {
    color: #1e293b !important;
}

/* ===== HEADINGS DI AREA UTAMA ===== */
.main h1, [data-testid="stMarkdownContainer"] h1 {
    color: #1e3a8a !important;
    font-weight: 700 !important;
    border-bottom: 4px solid #fbbf24 !important;
    padding-bottom: 12px !important;
    margin-bottom: 24px !important;
}
.main h2, [data-testid="stMarkdownContainer"] h2 {
    color: #2563eb !important;
    font-weight: 600 !important;
    margin-top: 28px !important;
    border-left: 5px solid #2563eb !important;
    padding-left: 12px !important;
}
.main h3, [data-testid="stMarkdownContainer"] h3 {
    color: #4f46e5 !important;
    font-weight: 600 !important;
}
.main h4, .main h5, .main h6,
[data-testid="stMarkdownContainer"] h4,
[data-testid="stMarkdownContainer"] h5,
[data-testid="stMarkdownContainer"] h6 {
    color: #1e3a8a !important;
}

/* ===== BOX KONTEN — SEMUA TEKS DI DALAMNYA HARUS GELAP ===== */
.info-box, .info-box * {
    color: #1e293b !important;
}
.info-box {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%) !important;
    border-left: 5px solid #2563eb !important;
    padding: 16px 22px !important;
    border-radius: 10px !important;
    margin: 16px 0 !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
}
.info-box strong { color: #1e3a8a !important; }

.concept-box, .concept-box * {
    color: #78350f !important;
}
.concept-box {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%) !important;
    border-left: 5px solid #f59e0b !important;
    padding: 16px 22px !important;
    border-radius: 10px !important;
    margin: 16px 0 !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
}
.concept-box strong { color: #92400e !important; }

.example-box, .example-box * {
    color: #064e3b !important;
}
.example-box {
    background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%) !important;
    border-left: 5px solid #059669 !important;
    padding: 16px 22px !important;
    border-radius: 10px !important;
    margin: 16px 0 !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
}
.example-box strong { color: #064e3b !important; }

.activity-box, .activity-box * {
    color: #831843 !important;
}
.activity-box {
    background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%) !important;
    border-left: 5px solid #db2777 !important;
    padding: 16px 22px !important;
    border-radius: 10px !important;
    margin: 16px 0 !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
}
.activity-box strong { color: #9d174d !important; }

.quiz-box, .quiz-box * {
    color: #3730a3 !important;
}
.quiz-box {
    background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%) !important;
    border: 2px solid #7c3aed !important;
    padding: 22px !important;
    border-radius: 12px !important;
    margin: 22px 0 !important;
    box-shadow: 0 4px 12px rgba(124,58,237,0.15) !important;
}
.quiz-box h3 { color: #4c1d95 !important; }
.quiz-box strong { color: #4c1d95 !important; }

/* ===== HERO CARD (TEKS PUTIH PADA GRADIEN GELAP) ===== */
/* Specificity tinggi agar menang vs [data-testid] h1 dan .main h1 */
div.hero,
div.hero h1,
div.hero h2,
div.hero h3,
div.hero p,
div.hero em,
div.hero span,
div.hero strong,
[data-testid="stMarkdownContainer"] div.hero,
[data-testid="stMarkdownContainer"] div.hero h1,
[data-testid="stMarkdownContainer"] div.hero h2,
[data-testid="stMarkdownContainer"] div.hero h3,
[data-testid="stMarkdownContainer"] div.hero p,
[data-testid="stMarkdownContainer"] div.hero em {
    color: #ffffff !important;
}
div.hero {
    background: linear-gradient(135deg, #1e3a8a 0%, #4f46e5 50%, #7c3aed 100%) !important;
    padding: 48px 32px !important;
    border-radius: 18px !important;
    margin: 12px 0 28px 0 !important;
    text-align: center !important;
    box-shadow: 0 12px 32px rgba(30,58,138,0.25) !important;
}
[data-testid="stMarkdownContainer"] div.hero h1,
div.hero h1 {
    border: none !important;
    font-size: 2.6em !important;
    margin-bottom: 12px !important;
    padding: 0 !important;
}
[data-testid="stMarkdownContainer"] div.hero h2,
div.hero h2 {
    border: none !important;
    padding: 0 !important;
    margin: 0 !important;
}
div.hero p {
    font-size: 1.15em !important;
    opacity: 0.95 !important;
    margin: 6px 0 !important;
}

/* ===== FEATURE CARDS ===== */
.feature-card, .feature-card * {
    color: #1e293b !important;
}
.feature-card {
    background: white !important;
    padding: 22px !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    border-top: 4px solid #2563eb !important;
    margin: 8px 0 !important;
    height: 100% !important;
}
.feature-card h4 {
    color: #1e3a8a !important;
    margin-top: 0 !important;
}

/* ===== SIDEBAR (TEKS PUTIH PADA GRADIEN GELAP) ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e3a8a 0%, #312e81 50%, #4f46e5 100%) !important;
}
section[data-testid="stSidebar"] *,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] li {
    color: white !important;
}
section[data-testid="stSidebar"] .stAlert,
section[data-testid="stSidebar"] .stAlert * {
    color: #1e293b !important;
    background: rgba(255,255,255,0.95) !important;
}

/* ===== KOMPONEN STREAMLIT ===== */
/* Slider label */
.stSlider label, .stSlider [data-testid="stWidgetLabel"] {
    color: #1e293b !important;
    font-weight: 600 !important;
}
/* Selectbox label */
.stSelectbox label, .stSelectbox [data-testid="stWidgetLabel"] {
    color: #1e293b !important;
    font-weight: 600 !important;
}
/* Text input label */
.stTextInput label, .stTextInput [data-testid="stWidgetLabel"] {
    color: #1e293b !important;
    font-weight: 600 !important;
}
/* Radio label */
.stRadio label, .stRadio [data-testid="stWidgetLabel"] {
    color: #1e293b !important;
    font-weight: 600 !important;
}
/* Expander */
.streamlit-expanderHeader, [data-testid="stExpander"] summary {
    color: #1e3a8a !important;
    font-weight: 600 !important;
}
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] * {
    color: #1e293b !important;
}
/* DataFrame */
.stDataFrame, .stDataFrame * {
    color: #1e293b !important;
}
/* Caption */
.stCaption, [data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] * {
    color: #475569 !important;
}
/* Code blocks (inline) */
code {
    color: #be185d !important;
    background: #fce7f3 !important;
    padding: 2px 6px !important;
    border-radius: 4px !important;
}
/* Tables in markdown */
table, table th, table td {
    color: #1e293b !important;
    border-color: #cbd5e1 !important;
}
table th {
    background: #e0e7ff !important;
    color: #1e3a8a !important;
    font-weight: 700 !important;
}
table tr:nth-child(even) {
    background: #f8fafc !important;
}
table tr:nth-child(odd) {
    background: #ffffff !important;
}

/* ===== FOOTER NOTE ===== */
.footer-note, .footer-note * {
    color: #cbd5e1 !important;
}
.footer-note {
    background: #1e293b !important;
    padding: 18px !important;
    border-radius: 10px !important;
    margin-top: 30px !important;
    text-align: center !important;
    font-size: 0.9em !important;
}

/* ===== LINK ===== */
a, a:visited {
    color: #2563eb !important;
}
a:hover {
    color: #1e40af !important;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------- HELPER VISUALISASI ----------
def fig_setup(figsize=(9, 4.5)):
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax

def style_axes(ax, equal=False, grid=True):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if grid:
        ax.grid(alpha=0.25, linestyle="--")
    if equal:
        ax.set_aspect("equal")

# ---------- SIDEBAR NAVIGASI ----------
st.sidebar.markdown("## 📚 Navigasi Materi")
st.sidebar.markdown("---")

PAGES = {
    "🏠 Beranda": "home",
    "📖 Bab 1 — Pengenalan Pola": "ch1",
    "🔄 Bab 2 — Jenis-Jenis Pola": "ch2",
    "🔢 Bab 3 — Pola Bilangan": "ch3",
    "📊 Bab 4 — Dari Pola ke Generalisasi": "ch4",
    "🧮 Bab 5 — Pemikiran Aljabar": "ch5",
    "✨ Bab 6 — Eksplorasi Pola Persamaan": "ch6",
    "🎯 Bab 7 — Soal Penalaran Pola": "ch7",
    "📚 Tentang & Referensi": "about",
}

selection = st.sidebar.radio("Pilih Bab:", list(PAGES.keys()), label_visibility="collapsed")
page = PAGES[selection]

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Tips Belajar**\n\n"
    "- Geser **slider** untuk mengubah parameter\n"
    "- Klik **tombol** untuk simulasi interaktif\n"
    "- Buka **expander** untuk penjelasan lebih lanjut\n"
    "- Coba semua bab secara berurutan"
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='text-align:center;font-size:0.85em;opacity:0.85'>"
    "Dirancang untuk Mahasiswa<br>Calon Guru SD 🎓"
    "</div>",
    unsafe_allow_html=True,
)

# ============================================================
# HALAMAN: BERANDA
# ============================================================
def page_home():
    st.markdown(
        """
        <div class='hero'>
            <h1>🧮 Pola & Pemikiran Aljabar</h1>
            <p><em>Sebuah Petualangan Matematika untuk Calon Guru Sekolah Dasar</em></p>
            <p>Belajar mengenali pola, berpikir aljabar, dan menemukan keindahan matematika</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## 🎯 Selamat Datang!")
    st.markdown(
        """
        Website ini dirancang khusus untuk **mahasiswa calon guru Sekolah Dasar** yang ingin
        mendalami konsep _pola_ dan _pemikiran aljabar_. Kemampuan berpikir aljabar bukan hanya
        urusan SMP atau SMA — ia harus mulai ditanamkan sejak SD melalui pengenalan pola yang
        konkret dan menyenangkan.

        Materi disusun secara berjenjang, dimulai dari konsep dasar pola hingga eksplorasi
        persamaan matematika yang membentuk pola unik. Setiap bab dilengkapi dengan
        **simulasi interaktif** yang dapat Anda otak-atik untuk membangun intuisi.
        """
    )

    st.markdown("## ✨ Fitur Unggulan")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class='feature-card'>
            <h4>🎚️ Simulasi Interaktif</h4>
            <p>Setiap bab memiliki slider dan kontrol yang dapat Anda eksplorasi. Ubah parameter dan amati bagaimana pola berubah secara langsung.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class='feature-card'>
            <h4>🖼️ Visualisasi Konkret</h4>
            <p>Setiap subbab dilengkapi minimal satu visualisasi gambar untuk memperkuat pemahaman dan menjembatani konsep abstrak.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class='feature-card'>
            <h4>🎯 Soal Penalaran</h4>
            <p>Tiga soal penalaran berbasis pengenalan pola untuk mengasah berpikir kritis dan kemampuan generalisasi calon guru.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("## 🗺️ Peta Materi")
    st.markdown(
        """
        | Bab | Topik | Fokus |
        |-----|-------|-------|
        | 1 | Pengenalan Pola | _Apa itu pola? Mengapa penting?_ |
        | 2 | Jenis-Jenis Pola | _Pola berulang, tumbuh, berkurang_ |
        | 3 | Pola Bilangan | _Aritmetika, geometri, Fibonacci, figuratif_ |
        | 4 | Dari Pola ke Generalisasi | _Tabel, kata-kata, simbol_ |
        | 5 | Pemikiran Aljabar | _Variabel, persamaan, kesetaraan_ |
        | 6 | Eksplorasi Pola Persamaan | _Lab eksperimen pola unik_ |
        | 7 | Soal Penalaran Pola | _Tiga tantangan penalaran_ |
        """
    )

    st.markdown("## 🚀 Mulai Belajar")
    st.markdown(
        """
        <div class='info-box'>
        Gunakan menu di sebelah kiri untuk berpindah antar bab. Disarankan mengikuti urutan dari
        Bab 1 hingga Bab 7 untuk pengalaman belajar yang optimal. Selamat belajar dan selamat
        bereksplorasi! 🎉
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# BAB 1: PENGENALAN POLA
# ============================================================
def page_ch1():
    st.title("📖 Bab 1 — Pengenalan Pola")

    st.markdown(
        """
        <div class='concept-box'>
        <strong>Tujuan Pembelajaran</strong><br>
        Setelah mempelajari bab ini, mahasiswa calon guru SD diharapkan mampu:
        <ol>
        <li>Menjelaskan pengertian <em>pola</em> dalam konteks matematika SD</li>
        <li>Mengenali pola dalam kehidupan sehari-hari</li>
        <li>Menyadari pentingnya pengenalan pola sebagai fondasi pemikiran aljabar</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 1.1 Apa itu Pola? ----
    st.header("1.1 Apa Itu Pola?")
    st.markdown(
        """
        Dalam matematika, **pola** adalah _susunan objek, bilangan, bentuk, atau peristiwa yang
        mengikuti aturan tertentu sehingga dapat diprediksi kelanjutannya_. Pola adalah jantung
        dari matematika: matematikawan sering disebut sebagai "pencari pola" (_pattern seekers_).

        Ketika seorang anak SD melihat susunan **🔴🔵🔴🔵🔴🔵...**, ia secara tidak sadar sedang
        melakukan kegiatan matematis yang penting: mencari aturan, memprediksi, dan
        menggeneralisasi. Inilah benih dari _pemikiran aljabar_ yang akan tumbuh seiring
        bertambahnya usia.
        """
    )

    # Visualisasi: Pola di sekitar kita
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))

    # Pola warna
    ax = axes[0]
    colors = ["#ef4444", "#3b82f6"] * 5
    for i, c in enumerate(colors):
        ax.add_patch(Circle((i + 0.5, 0.5), 0.35, color=c))
    ax.set_xlim(0, 10); ax.set_ylim(0, 1)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Pola Warna Berulang", fontsize=11, fontweight="bold")

    # Pola bentuk
    ax = axes[1]
    shapes = ["circle", "square", "triangle"] * 4
    for i, s in enumerate(shapes[:9]):
        if s == "circle":
            ax.add_patch(Circle((i + 0.5, 0.5), 0.3, color="#10b981"))
        elif s == "square":
            ax.add_patch(Rectangle((i + 0.2, 0.2), 0.6, 0.6, color="#f59e0b"))
        else:
            ax.add_patch(RegularPolygon((i + 0.5, 0.5), 3, radius=0.35, color="#8b5cf6"))
    ax.set_xlim(0, 9); ax.set_ylim(0, 1)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Pola Bentuk Berulang", fontsize=11, fontweight="bold")

    # Pola tumbuh
    ax = axes[2]
    for n, x in enumerate([0.5, 2, 4.2, 7]):
        size = n + 1
        for i in range(size):
            for j in range(size):
                ax.add_patch(Rectangle((x + i*0.3, 0.1 + j*0.3), 0.28, 0.28, color="#ec4899"))
    ax.set_xlim(0, 10); ax.set_ylim(0, 1.4)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Pola Tumbuh (1, 4, 9, 16)", fontsize=11, fontweight="bold")

    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.caption("📷 _Gambar 1.1 — Tiga contoh pola dasar: berulang, berulang dengan variasi, dan tumbuh._")

    # ---- 1.2 Pola di Sekitar Kita ----
    st.header("1.2 Pola di Sekitar Kita")
    st.markdown(
        """
        Pola tidak hanya ada di buku matematika. Pola ada di mana-mana: di alam, di rumah, di
        sekolah, bahkan di tubuh kita sendiri. Berikut beberapa contoh konkret yang dapat Anda
        gunakan saat mengajar di SD nanti:
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class='example-box'>
            <strong>🌿 Pola di Alam</strong>
            <ul>
            <li>Susunan kelopak bunga matahari (<em>spiral Fibonacci</em>)</li>
            <li>Belang pada zebra dan harimau</li>
            <li>Sarang lebah berbentuk segi enam</li>
            <li>Pola percabangan pohon</li>
            <li>Pasang surut air laut (pola periodik)</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='example-box'>
            <strong>🏠 Pola di Kehidupan Sehari-hari</strong>
            <ul>
            <li>Susunan ubin lantai kamar mandi</li>
            <li>Motif batik dan kain tradisional Indonesia</li>
            <li>Jadwal hari dalam seminggu (Senin–Minggu)</li>
            <li>Lampu lalu lintas (merah → kuning → hijau)</li>
            <li>Notasi musik dan ketukan lagu</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ---- 1.3 Simulasi Interaktif ----
    st.header("1.3 🎮 Simulasi Interaktif: Pola Warna Berulang")
    st.markdown(
        """
        Mari bereksperimen! Geser slider di bawah untuk membuat pola warna berulang dengan
        panjang siklus yang berbeda. Amati bagaimana pola yang sama muncul kembali setelah
        sejumlah langkah tertentu.
        """
    )

    c1, c2 = st.columns([1, 2])
    with c1:
        n_warna = st.slider("Jumlah warna dalam siklus", 2, 5, 3, key="ch1_n")
        n_total = st.slider("Total objek yang ditampilkan", 6, 24, 15, key="ch1_total")
        warna_palet = ["#ef4444", "#3b82f6", "#10b981", "#f59e0b", "#8b5cf6"]
        warna_aktif = warna_palet[:n_warna]
        st.markdown("**Warna siklus:**")
        for i, w in enumerate(warna_aktif):
            st.markdown(
                f"<div style='display:inline-block;width:30px;height:30px;background:{w};"
                f"border-radius:50%;margin:3px;border:2px solid white;"
                f"box-shadow:0 2px 4px rgba(0,0,0,0.2)'></div> Warna {i+1}",
                unsafe_allow_html=True,
            )
    with c2:
        fig, ax = plt.subplots(figsize=(10, 1.8))
        for i in range(n_total):
            warna = warna_aktif[i % n_warna]
            ax.add_patch(Circle((i + 0.5, 0.5), 0.42, color=warna,
                                ec="white", linewidth=2))
            ax.text(i + 0.5, -0.4, str(i+1), ha="center", fontsize=9, color="#475569")
        ax.set_xlim(0, n_total); ax.set_ylim(-0.7, 1)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(f"Pola Berulang dengan Siklus {n_warna} Warna", fontweight="bold")
        st.pyplot(fig)
        plt.close()

        st.markdown(
            f"<div class='info-box'>"
            f"💡 <strong>Pertanyaan reflektif:</strong> Pada posisi ke-{n_total}, "
            f"warna apa yang muncul? Coba prediksi tanpa menghitung satu per satu. "
            f"<br>Petunjuk: hitung sisa pembagian {n_total} oleh {n_warna}.<br>"
            f"<strong>Jawaban:</strong> Posisi ke-{n_total} mod {n_warna} = "
            f"{(n_total-1) % n_warna + 1} → Warna {(n_total-1) % n_warna + 1}."
            f"</div>",
            unsafe_allow_html=True,
        )

    # ---- 1.4 Mengapa Pola Penting di SD ----
    st.header("1.4 Mengapa Pola Penting di Pembelajaran SD?")
    st.markdown(
        """
        Pengenalan pola di SD bukan sekadar permainan menyenangkan. Ia memiliki peran
        pedagogis yang sangat penting:

        1. **Fondasi pemikiran aljabar** — Pola adalah _jembatan_ dari aritmetika konkret ke
           aljabar abstrak. Anak yang terbiasa dengan pola akan lebih mudah memahami variabel
           dan persamaan di SMP.
        2. **Mengembangkan _generalisasi_** — Ketika anak menemukan aturan dari sebuah pola, ia
           sedang belajar _membuat kesimpulan umum_ dari kasus-kasus khusus.
        3. **Melatih penalaran logis** — Mencari pola membutuhkan observasi, dugaan
           (_konjektur_), dan pengujian — proses yang sama dengan berpikir ilmiah.
        4. **Membangun pemahaman bilangan** — Banyak sifat bilangan (genap-ganjil, kelipatan,
           pembagian) lebih mudah dipahami melalui pola.
        5. **Sesuai _Kurikulum Merdeka_** — Capaian Pembelajaran (CP) Bilangan dan Aljabar di SD
           secara eksplisit menyebutkan pengenalan pola.
        """
    )

    st.markdown(
        """
        <div class='activity-box'>
        <strong>🎓 Refleksi Calon Guru</strong><br>
        Bayangkan Anda mengajar kelas 2 SD. Bagaimana cara Anda memperkenalkan konsep "pola"
        kepada siswa <em>tanpa</em> langsung menyebut kata "pola"? Coba pikirkan satu kegiatan
        yang melibatkan benda konkret di sekitar kelas.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# BAB 2: JENIS-JENIS POLA
# ============================================================
def page_ch2():
    st.title("🔄 Bab 2 — Jenis-Jenis Pola")

    st.markdown(
        """
        <div class='concept-box'>
        <strong>Tujuan Pembelajaran</strong><br>
        Mahasiswa mampu mengidentifikasi dan membedakan tiga jenis pola utama yang umum
        dijumpai di SD: <em>pola berulang</em>, <em>pola tumbuh</em>, dan <em>pola berkurang</em>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 2.1 Pola Berulang ----
    st.header("2.1 Pola Berulang (Repeating Patterns)")
    st.markdown(
        """
        **Pola berulang** adalah pola yang memiliki _unit inti_ (sering disebut **inti pola**
        atau _core_) yang diulang terus-menerus. Inti pola ini bisa terdiri dari 2, 3, 4, atau
        lebih elemen.

        - Pola **AB**: 🔴🔵🔴🔵🔴🔵...
        - Pola **ABC**: 🔺⬛🟢🔺⬛🟢...
        - Pola **AABB**: 🔴🔴🔵🔵🔴🔴🔵🔵...

        Di SD kelas rendah, anak-anak biasanya mulai dari pola AB yang sederhana, kemudian
        secara bertahap diperkenalkan pada inti pola yang lebih panjang dan bervariasi.
        """
    )

    # Visualisasi pola berulang
    fig, axes = plt.subplots(3, 1, figsize=(10, 4))
    pola_data = [
        ("Pola AB", ["#ef4444", "#3b82f6"], 10),
        ("Pola ABC", ["#10b981", "#f59e0b", "#8b5cf6"], 9),
        ("Pola AABB", ["#ef4444", "#ef4444", "#3b82f6", "#3b82f6"], 12),
    ]
    for ax, (judul, warna, n) in zip(axes, pola_data):
        for i in range(n):
            ax.add_patch(Circle((i + 0.5, 0.5), 0.4,
                                color=warna[i % len(warna)],
                                ec="white", linewidth=2))
        ax.set_xlim(0, n); ax.set_ylim(0, 1)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(judul, fontsize=11, fontweight="bold", loc="left")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    st.caption("📷 _Gambar 2.1 — Tiga jenis pola berulang dengan inti pola yang berbeda._")

    # Simulasi interaktif Pola Berulang
    st.markdown("### 🎮 Simulasi: Bangun Pola Berulang Anda Sendiri")
    c1, c2 = st.columns([1, 2])
    with c1:
        inti = st.text_input(
            "Tulis inti pola (huruf saja, mis. ABC)",
            value="AB", max_chars=6, key="ch2_inti"
        ).upper()
        n_ulang = st.slider("Banyak pengulangan", 2, 8, 4, key="ch2_ulang")
    with c2:
        if inti and inti.isalpha():
            warna_map = {
                "A": "#ef4444", "B": "#3b82f6", "C": "#10b981",
                "D": "#f59e0b", "E": "#8b5cf6", "F": "#ec4899",
            }
            urutan = (inti * n_ulang)[: len(inti) * n_ulang]
            fig, ax = plt.subplots(figsize=(10, 1.5))
            for i, h in enumerate(urutan):
                c = warna_map.get(h, "#94a3b8")
                ax.add_patch(Circle((i + 0.5, 0.5), 0.42, color=c, ec="white", linewidth=2))
                ax.text(i + 0.5, 0.5, h, ha="center", va="center",
                        color="white", fontweight="bold", fontsize=11)
            ax.set_xlim(0, len(urutan)); ax.set_ylim(0, 1)
            ax.set_aspect("equal"); ax.axis("off")
            st.pyplot(fig)
            plt.close()
            st.markdown(
                f"<div class='info-box'>Inti pola <strong>{inti}</strong> "
                f"(panjang {len(inti)}) diulang <strong>{n_ulang}</strong> kali, "
                f"menghasilkan total <strong>{len(urutan)}</strong> objek.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.warning("Masukkan huruf saja, ya 😊")

    # ---- 2.2 Pola Tumbuh ----
    st.header("2.2 Pola Tumbuh (Growing Patterns)")
    st.markdown(
        """
        **Pola tumbuh** adalah pola yang setiap suku berikutnya _bertambah_ menurut aturan
        tertentu. Berbeda dengan pola berulang, pola tumbuh tidak memiliki inti yang sama;
        sebaliknya, ia memiliki _aturan pertumbuhan_.

        Contoh klasik: tumpukan ubin yang membentuk persegi: 1, 4, 9, 16, 25, ...

        Pola tumbuh sangat penting karena merupakan _benih barisan bilangan_ yang akan
        dikembangkan lebih lanjut di Bab 3.
        """
    )

    # Visualisasi pola tumbuh
    fig, ax = plt.subplots(figsize=(11, 3))
    x_offset = 0
    for n in range(1, 6):
        for i in range(n):
            for j in range(n):
                ax.add_patch(Rectangle(
                    (x_offset + i*0.4, j*0.4), 0.38, 0.38,
                    color="#3b82f6", ec="white", linewidth=1.5
                ))
        ax.text(x_offset + n*0.2, -0.5, f"{n}² = {n*n}",
                ha="center", fontsize=10, fontweight="bold", color="#1e3a8a")
        x_offset += n*0.4 + 0.8
    ax.set_xlim(-0.5, x_offset)
    ax.set_ylim(-1, 2.5)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Pola Tumbuh: Bilangan Persegi (1, 4, 9, 16, 25)",
                 fontweight="bold", fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    st.caption("📷 _Gambar 2.2 — Bilangan persegi sebagai pola tumbuh visual._")

    # Simulasi pola tumbuh
    st.markdown("### 🎮 Simulasi: Pola Tumbuh dengan Aturan")
    c1, c2 = st.columns([1, 2])
    with c1:
        suku_awal = st.slider("Suku pertama", 1, 10, 2, key="ch2_a")
        tambah = st.slider("Tambahan tiap langkah", 1, 8, 3, key="ch2_d")
        n_suku = st.slider("Banyak suku", 4, 10, 6, key="ch2_n")
    with c2:
        suku = [suku_awal + i*tambah for i in range(n_suku)]
        fig, ax = plt.subplots(figsize=(10, 3))
        for i, s in enumerate(suku):
            ax.bar(i, s, color=plt.cm.viridis(i/n_suku), edgecolor="white", linewidth=2)
            ax.text(i, s + 0.5, str(s), ha="center", fontweight="bold", fontsize=11)
        ax.set_xticks(range(n_suku))
        ax.set_xticklabels([f"Suku {i+1}" for i in range(n_suku)], fontsize=9)
        ax.set_title(f"Pola Tumbuh: mulai {suku_awal}, tambah {tambah} setiap kali",
                     fontweight="bold")
        style_axes(ax)
        st.pyplot(fig)
        plt.close()
        st.markdown(
            f"<div class='example-box'>Barisan: <strong>{', '.join(map(str, suku))}, ...</strong><br>"
            f"Aturan: <em>setiap suku = suku sebelumnya + {tambah}</em></div>",
            unsafe_allow_html=True,
        )

    # ---- 2.3 Pola Berkurang ----
    st.header("2.3 Pola Berkurang (Shrinking Patterns)")
    st.markdown(
        """
        **Pola berkurang** adalah kebalikan dari pola tumbuh — setiap suku berikutnya _berkurang_
        menurut aturan tertentu.

        Contoh: 20, 17, 14, 11, 8, ... (berkurang 3 setiap langkah).

        Di SD, pola berkurang sering muncul dalam soal cerita: _"Ibu memiliki 30 kue. Setiap
        hari habis 4 kue. Berapa kue yang tersisa setelah 5 hari?"_
        """
    )

    fig, ax = plt.subplots(figsize=(10, 3))
    suku_b = [20, 17, 14, 11, 8, 5]
    for i, s in enumerate(suku_b):
        ax.bar(i, s, color=plt.cm.Reds(0.4 + 0.1*i), edgecolor="white", linewidth=2)
        ax.text(i, s + 0.5, str(s), ha="center", fontweight="bold")
    ax.set_xticks(range(len(suku_b)))
    ax.set_xticklabels([f"Hari {i+1}" for i in range(len(suku_b))])
    ax.set_title("Pola Berkurang: Sisa kue setiap hari (mulai 20, berkurang 3)",
                 fontweight="bold")
    style_axes(ax)
    st.pyplot(fig)
    plt.close()
    st.caption("📷 _Gambar 2.3 — Visualisasi pola berkurang sebagai konteks cerita._")

    st.markdown(
        """
        <div class='activity-box'>
        <strong>🎓 Untuk Calon Guru</strong><br>
        Buatlah <em>satu</em> contoh pola berulang, satu pola tumbuh, dan satu pola berkurang
        menggunakan benda yang ada di sekitar Anda (mis. pensil, kelereng, kancing). Foto dan
        diskusikan dengan teman sejawat: bagaimana cara Anda akan memandu siswa SD untuk
        membedakan ketiganya?
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# BAB 3: POLA BILANGAN
# ============================================================
def page_ch3():
    st.title("🔢 Bab 3 — Pola Bilangan")

    st.markdown(
        """
        <div class='concept-box'>
        <strong>Tujuan Pembelajaran</strong><br>
        Mahasiswa mampu mengenali, mendeskripsikan, dan memvisualisasikan pola-pola bilangan
        yang umum: <em>barisan aritmetika</em>, <em>barisan geometri</em>, <em>bilangan
        figuratif</em>, dan <em>barisan Fibonacci</em>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 3.1 Barisan Aritmetika ----
    st.header("3.1 Barisan Aritmetika")
    st.markdown(
        """
        **Barisan aritmetika** adalah barisan bilangan yang _selisih antar dua suku
        berurutan selalu sama_. Selisih ini disebut **beda** (notasi: $b$).

        Bentuk umum: $a, a+b, a+2b, a+3b, \\ldots$

        Rumus suku ke-$n$: $$U_n = a + (n-1) \\cdot b$$

        di mana $a$ adalah _suku pertama_ dan $b$ adalah _beda_.
        """
    )

    st.markdown("### 🎮 Simulasi Interaktif: Barisan Aritmetika")
    c1, c2 = st.columns([1, 2])
    with c1:
        a_arit = st.slider("Suku pertama (a)", -10, 20, 3, key="ch3_a_arit")
        b_arit = st.slider("Beda (b)", -5, 10, 2, key="ch3_b_arit")
        n_arit = st.slider("Banyak suku", 5, 15, 8, key="ch3_n_arit")
    with c2:
        suku_arit = [a_arit + i*b_arit for i in range(n_arit)]
        fig, ax = plt.subplots(figsize=(10, 3.5))
        ax.plot(range(1, n_arit+1), suku_arit, "o-",
                color="#2563eb", markersize=10, linewidth=2.5)
        for i, s in enumerate(suku_arit):
            ax.annotate(str(s), (i+1, s), textcoords="offset points",
                        xytext=(0, 10), ha="center", fontweight="bold", fontsize=10)
        ax.set_xlabel("Suku ke-n", fontweight="bold")
        ax.set_ylabel("Nilai", fontweight="bold")
        ax.set_title(f"Barisan: {a_arit}, {a_arit+b_arit}, {a_arit+2*b_arit}, ...  "
                     f"(a={a_arit}, b={b_arit})", fontweight="bold")
        style_axes(ax)
        st.pyplot(fig)
        plt.close()
        st.markdown(
            f"<div class='example-box'>"
            f"<strong>Suku ke-{n_arit}</strong> = {a_arit} + ({n_arit}-1) × {b_arit} = "
            f"<strong>{suku_arit[-1]}</strong><br>"
            f"<em>Catatan:</em> jika beda positif → barisan naik; jika negatif → turun."
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class='example-box'>
        <strong>💡 Contoh untuk SD</strong><br>
        "Andi menabung Rp2.000 di hari pertama, dan setiap hari berikutnya menambah Rp500.
        Berapa tabungan Andi di hari ke-10?"<br>
        Jawab: $a = 2000$, $b = 500$, $n = 10$ → $U_{10} = 2000 + 9 \\times 500 = 6500$. Jadi
        tabungannya Rp6.500.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 3.2 Barisan Geometri ----
    st.header("3.2 Barisan Geometri")
    st.markdown(
        """
        **Barisan geometri** adalah barisan yang _rasio (perbandingan) antar dua suku berurutan
        selalu sama_. Rasio ini dinotasikan $r$.

        Bentuk umum: $a, a \\cdot r, a \\cdot r^2, a \\cdot r^3, \\ldots$

        Rumus suku ke-$n$: $$U_n = a \\cdot r^{n-1}$$
        """
    )

    st.markdown("### 🎮 Simulasi Interaktif: Barisan Geometri")
    c1, c2 = st.columns([1, 2])
    with c1:
        a_geo = st.slider("Suku pertama (a)", 1, 10, 2, key="ch3_a_geo")
        r_geo = st.slider("Rasio (r)", 0.5, 3.0, 2.0, 0.1, key="ch3_r_geo")
        n_geo = st.slider("Banyak suku", 4, 10, 6, key="ch3_n_geo")
    with c2:
        suku_geo = [a_geo * (r_geo ** i) for i in range(n_geo)]
        fig, ax = plt.subplots(figsize=(10, 3.5))
        ax.bar(range(1, n_geo+1), suku_geo,
               color=plt.cm.plasma(np.linspace(0.2, 0.8, n_geo)),
               edgecolor="white", linewidth=2)
        for i, s in enumerate(suku_geo):
            ax.text(i+1, s + max(suku_geo)*0.02, f"{s:.1f}",
                    ha="center", fontweight="bold", fontsize=9)
        ax.set_xlabel("Suku ke-n", fontweight="bold")
        ax.set_ylabel("Nilai", fontweight="bold")
        ax.set_title(f"Barisan Geometri: a={a_geo}, r={r_geo:.1f}", fontweight="bold")
        style_axes(ax)
        st.pyplot(fig)
        plt.close()
        st.markdown(
            f"<div class='example-box'>"
            f"Barisan: <strong>{', '.join(f'{s:.2f}' for s in suku_geo[:6])}, ...</strong><br>"
            f"Jika $r > 1$: tumbuh sangat cepat (eksponensial). "
            f"Jika $0 < r < 1$: mengecil mendekati nol."
            f"</div>",
            unsafe_allow_html=True,
        )

    # ---- 3.3 Bilangan Figuratif ----
    st.header("3.3 Bilangan Figuratif (Segitiga & Persegi)")
    st.markdown(
        """
        **Bilangan figuratif** adalah bilangan yang dapat _disusun membentuk gambar tertentu_.
        Dua yang paling populer di SD: bilangan segitiga dan bilangan persegi.

        - **Bilangan segitiga**: $T_n = \\dfrac{n(n+1)}{2}$ → 1, 3, 6, 10, 15, 21, ...
        - **Bilangan persegi**: $S_n = n^2$ → 1, 4, 9, 16, 25, 36, ...
        """
    )

    n_fig = st.slider("Pilih n untuk melihat bilangan figuratif ke-n",
                      1, 8, 5, key="ch3_fig")

    col1, col2 = st.columns(2)
    with col1:
        # Bilangan segitiga
        fig, ax = plt.subplots(figsize=(5, 5))
        for row in range(n_fig):
            for col in range(row + 1):
                ax.add_patch(Circle(
                    (col - row*0.5, n_fig - row),
                    0.4, color="#10b981", ec="white", linewidth=2
                ))
        ax.set_xlim(-n_fig*0.6, n_fig*0.6)
        ax.set_ylim(0, n_fig + 1)
        ax.set_aspect("equal"); ax.axis("off")
        T_n = n_fig * (n_fig + 1) // 2
        ax.set_title(f"Bilangan Segitiga T_{n_fig} = {T_n}",
                     fontweight="bold", fontsize=12)
        st.pyplot(fig)
        plt.close()

    with col2:
        # Bilangan persegi
        fig, ax = plt.subplots(figsize=(5, 5))
        for i in range(n_fig):
            for j in range(n_fig):
                ax.add_patch(Rectangle(
                    (i, j), 0.9, 0.9,
                    color="#f59e0b", ec="white", linewidth=2
                ))
        ax.set_xlim(-0.5, n_fig + 0.5)
        ax.set_ylim(-0.5, n_fig + 0.5)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(f"Bilangan Persegi S_{n_fig} = {n_fig**2}",
                     fontweight="bold", fontsize=12)
        st.pyplot(fig)
        plt.close()

    st.caption("📷 _Gambar 3.3 — Bilangan figuratif dapat 'dilihat' bentuknya, sangat cocok untuk SD._")

    st.markdown(
        """
        <div class='info-box'>
        <strong>🎓 Tahukah Anda?</strong><br>
        Penjumlahan dua bilangan segitiga berurutan selalu menghasilkan bilangan persegi!
        Contoh: $T_3 + T_4 = 6 + 10 = 16 = 4^2$. Coba buktikan dengan menyusun gambar!
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 3.4 Fibonacci ----
    st.header("3.4 Barisan Fibonacci")
    st.markdown(
        """
        **Barisan Fibonacci** adalah barisan yang _setiap suku merupakan jumlah dua suku
        sebelumnya_:

        $$F_1 = 1, \\quad F_2 = 1, \\quad F_n = F_{n-1} + F_{n-2}$$

        Hasilnya: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

        Barisan ini muncul di banyak fenomena alam: susunan kelopak bunga, spiral cangkang
        nautilus, dan susunan biji bunga matahari!
        """
    )

    n_fib = st.slider("Berapa suku Fibonacci ditampilkan?", 5, 15, 10, key="ch3_fib")
    fib = [1, 1]
    for _ in range(n_fib - 2):
        fib.append(fib[-1] + fib[-2])
    fib = fib[:n_fib]

    c1, c2 = st.columns([2, 1])
    with c1:
        fig, ax = plt.subplots(figsize=(10, 3.5))
        ax.plot(range(1, n_fib+1), fib, "o-",
                color="#dc2626", markersize=10, linewidth=2.5)
        for i, f in enumerate(fib):
            ax.annotate(str(f), (i+1, f), textcoords="offset points",
                        xytext=(0, 10), ha="center", fontweight="bold")
        ax.set_xlabel("n", fontweight="bold")
        ax.set_ylabel("Nilai Fibonacci", fontweight="bold")
        ax.set_title("Pertumbuhan Eksponensial Barisan Fibonacci", fontweight="bold")
        style_axes(ax)
        st.pyplot(fig)
        plt.close()
    with c2:
        df_fib = pd.DataFrame({
            "n": range(1, n_fib+1),
            "F(n)": fib,
            "Rasio F(n)/F(n-1)": ["—"] + [f"{fib[i]/fib[i-1]:.4f}" for i in range(1, n_fib)]
        })
        st.dataframe(df_fib, hide_index=True, height=370)

    st.markdown(
        """
        <div class='example-box'>
        <strong>✨ Keajaiban Rasio Emas</strong><br>
        Perhatikan kolom rasio di tabel: ia mendekati <em>1.618...</em> yang dikenal sebagai
        <strong>rasio emas</strong> ($\\varphi$). Banyak seniman dan arsitek menggunakan rasio ini
        karena dianggap memberi proporsi paling indah secara visual.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# BAB 4: DARI POLA KE GENERALISASI
# ============================================================
def page_ch4():
    st.title("📊 Bab 4 — Dari Pola ke Generalisasi")

    st.markdown(
        """
        <div class='concept-box'>
        <strong>Tujuan Pembelajaran</strong><br>
        Mahasiswa mampu menggeneralisasi sebuah pola dari kasus-kasus khusus, menyatakannya
        dengan kata-kata, tabel, dan akhirnya simbol matematika (variabel).
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 4.1 Tiga Tahap Generalisasi ----
    st.header("4.1 Tiga Tahap Generalisasi")
    st.markdown(
        """
        Menurut _van de Walle_ (2018), proses generalisasi pola di SD melalui tiga tahap:

        1. **Tahap konkret** — siswa mengamati objek nyata (lidi, kelereng, gambar).
        2. **Tahap representasi** — siswa membuat tabel atau grafik.
        3. **Tahap simbolik** — siswa menyatakan aturan dengan kata, lalu dengan simbol/variabel.

        Sebagai calon guru SD, Anda harus mahir _bergerak bolak-balik_ di antara ketiga tahap
        ini agar siswa tidak terburu-buru ke tahap simbolik tanpa pemahaman.
        """
    )

    # Visualisasi 3 tahap
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.5))

    # Konkret
    ax = axes[0]
    for n in range(3):
        for i in range(n+1):
            ax.add_patch(Circle((n*2 + i*0.5, 0.5), 0.22,
                                color="#3b82f6", ec="white"))
    ax.text(0.5, -0.3, "n=1", ha="center", fontsize=10)
    ax.text(2.25, -0.3, "n=2", ha="center", fontsize=10)
    ax.text(4.5, -0.3, "n=3", ha="center", fontsize=10)
    ax.set_xlim(-0.5, 6); ax.set_ylim(-0.6, 1)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("① Konkret\n(objek nyata)", fontweight="bold")

    # Tabel
    ax = axes[1]
    ax.axis("off")
    tabel_data = [["n", "Banyak"], ["1", "1"], ["2", "2"], ["3", "3"], ["4", "?"]]
    table = ax.table(cellText=tabel_data, loc="center", cellLoc="center",
                     colWidths=[0.3, 0.4])
    table.auto_set_font_size(False); table.set_fontsize(11); table.scale(1, 1.8)
    for i in range(2):
        table[(0, i)].set_facecolor("#3b82f6")
        table[(0, i)].set_text_props(color="white", fontweight="bold")
    ax.set_title("② Representasi\n(tabel)", fontweight="bold")

    # Simbolik
    ax = axes[2]
    ax.text(0.5, 0.6, "Aturan:", fontsize=14, ha="center", fontweight="bold")
    ax.text(0.5, 0.35, "Banyak titik = $n$", fontsize=18, ha="center", color="#dc2626")
    ax.text(0.5, 0.1, "atau $f(n) = n$", fontsize=14, ha="center", color="#475569")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.set_title("③ Simbolik\n(variabel/rumus)", fontweight="bold")

    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    st.caption("📷 _Gambar 4.1 — Tiga tahap menggeneralisasi pola: konkret → representasi → simbolik._")

    # ---- 4.2 Tabel Pola: Mencari Aturan ----
    st.header("4.2 Mencari Aturan dari Tabel")
    st.markdown(
        """
        Salah satu strategi paling kuat untuk menemukan aturan pola adalah **membuat tabel**.
        Mari kita lihat sebuah contoh: _"Berapa banyak korek api yang dibutuhkan untuk membuat n
        segitiga berjejer?"_
        """
    )

    # Visualisasi segitiga korek api
    n_segi = st.slider("Banyak segitiga (n)", 1, 6, 3, key="ch4_segi")

    fig, ax = plt.subplots(figsize=(10, 2.5))
    h = np.sqrt(3) / 2
    for i in range(n_segi):
        if i % 2 == 0:
            tri = plt.Polygon([(i*0.5, 0), ((i+2)*0.5, 0), ((i+1)*0.5, h)],
                              fill=False, edgecolor="#dc2626", linewidth=3)
        else:
            tri = plt.Polygon([(i*0.5, h), ((i+2)*0.5, h), ((i+1)*0.5, 0)],
                              fill=False, edgecolor="#dc2626", linewidth=3)
        ax.add_patch(tri)
    ax.set_xlim(-0.2, (n_segi+1)*0.5 + 0.2)
    ax.set_ylim(-0.2, h + 0.2)
    ax.set_aspect("equal"); ax.axis("off")
    n_korek = 2*n_segi + 1
    ax.set_title(f"{n_segi} segitiga membutuhkan {n_korek} korek api",
                 fontweight="bold", fontsize=12)
    st.pyplot(fig)
    plt.close()

    # Tabel
    df_korek = pd.DataFrame({
        "Banyak segitiga (n)": list(range(1, 8)),
        "Banyak korek api": [2*i + 1 for i in range(1, 8)],
        "Selisih dgn sebelumnya": ["—"] + ["+2"]*6,
    })
    st.dataframe(df_korek, hide_index=True)

    st.markdown(
        """
        <div class='example-box'>
        <strong>🔍 Pengamatan:</strong> Selisih antar suku <em>selalu 2</em>. Ini berarti
        polanya bertambah dua setiap kali. Aturan dapat ditulis:<br><br>
        <em>"Banyak korek api = 2 × banyak segitiga + 1"</em><br>
        Atau dalam simbol: $$K = 2n + 1$$
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 4.3 Pola "Kata" ke "Simbol" ----
    st.header("4.3 Dari Kata-kata ke Simbol")
    st.markdown(
        """
        Bagi siswa SD, melompat langsung ke simbol matematika sering membingungkan. Mulailah
        dengan **deskripsi kata-kata** (verbal), lalu pelan-pelan kenalkan _variabel_.
        """
    )

    pola_pilih = st.selectbox(
        "Pilih pola untuk dianalisis:",
        [
            "Bilangan genap: 2, 4, 6, 8, ...",
            "Kelipatan 5: 5, 10, 15, 20, ...",
            "Bilangan kuadrat: 1, 4, 9, 16, ...",
            "Pola pagar: 4, 7, 10, 13, ... (1 pilar + tambah 3)",
        ],
        key="ch4_pilih",
    )

    aturan_kata = {
        "Bilangan genap: 2, 4, 6, 8, ...": (
            "Setiap bilangan adalah dua kali nomor urutnya",
            "U_n = 2n",
            [2*i for i in range(1, 8)],
        ),
        "Kelipatan 5: 5, 10, 15, 20, ...": (
            "Setiap bilangan adalah lima kali nomor urutnya",
            "U_n = 5n",
            [5*i for i in range(1, 8)],
        ),
        "Bilangan kuadrat: 1, 4, 9, 16, ...": (
            "Setiap bilangan adalah nomor urutnya dikalikan dengan dirinya sendiri",
            "U_n = n^2",
            [i**2 for i in range(1, 8)],
        ),
        "Pola pagar: 4, 7, 10, 13, ... (1 pilar + tambah 3)": (
            "Mulai dari 4, lalu setiap suku bertambah 3",
            "U_n = 3n + 1",
            [3*i + 1 for i in range(1, 8)],
        ),
    }
    deskripsi, rumus, suku = aturan_kata[pola_pilih]

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"<div class='info-box'>"
            f"<strong>Deskripsi kata:</strong><br><em>{deskripsi}</em>"
            f"</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='example-box'>"
            f"<strong>Bentuk simbolik:</strong><br>$${rumus}$$"
            f"</div>",
            unsafe_allow_html=True,
        )
    with c2:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.plot(range(1, 8), suku, "s-", color="#7c3aed", markersize=10, linewidth=2.5)
        for i, s in enumerate(suku):
            ax.annotate(str(s), (i+1, s), textcoords="offset points",
                        xytext=(0, 10), ha="center", fontweight="bold")
        ax.set_xlabel("n"); ax.set_ylabel("U_n")
        ax.set_title("7 suku pertama", fontweight="bold")
        style_axes(ax)
        st.pyplot(fig)
        plt.close()

    st.markdown(
        """
        <div class='activity-box'>
        <strong>🎓 Refleksi Pedagogis</strong><br>
        Mengapa penting bagi siswa SD untuk <em>mendeskripsikan pola dengan kata-kata
        terlebih dahulu</em> sebelum menggunakan simbol $n$? Diskusikan dengan teman dan
        kaitkan dengan konsep <em>scaffolding</em> dalam pembelajaran.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# BAB 5: PEMIKIRAN ALJABAR
# ============================================================
def page_ch5():
    st.title("🧮 Bab 5 — Pemikiran Aljabar")

    st.markdown(
        """
        <div class='concept-box'>
        <strong>Tujuan Pembelajaran</strong><br>
        Mahasiswa memahami konsep <em>variabel</em> dengan berbagai maknanya, prinsip
        <em>kesetaraan</em> dalam persamaan, dan cara mengembangkan pemikiran aljabar
        di kelas SD.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 5.1 Apa itu Pemikiran Aljabar? ----
    st.header("5.1 Apa Itu Pemikiran Aljabar?")
    st.markdown(
        """
        **Pemikiran aljabar** (_algebraic thinking_) bukan sekadar manipulasi simbol seperti
        $2x + 3 = 11$. Pemikiran aljabar adalah _cara berpikir_ yang melibatkan:

        - _Generalisasi_ dari kasus khusus ke aturan umum
        - Penggunaan **simbol** atau **variabel** untuk mewakili bilangan
        - Memahami **hubungan** antar besaran (relasional)
        - **Pemodelan** situasi nyata dengan ekspresi matematika

        Di SD, pemikiran aljabar ditanamkan _tanpa_ harus selalu menggunakan huruf $x$ atau $y$.
        Ia bisa muncul lewat kotak kosong (☐), gambar, atau cerita.
        """
    )

    # ---- 5.2 Variabel ----
    st.header("5.2 Variabel: Lebih dari Sekadar Huruf")
    st.markdown(
        """
        Banyak orang dewasa pun memiliki miskonsepsi: mereka pikir _variabel adalah huruf
        yang mewakili satu angka tertentu_. Padahal, **variabel memiliki banyak makna**
        tergantung konteksnya:
        """
    )

    df_var = pd.DataFrame({
        "Makna Variabel": [
            "1. Bilangan tertentu yang belum diketahui",
            "2. Bilangan yang berubah-ubah",
            "3. Generalisasi pola",
            "4. Parameter (tetap dalam konteks tertentu)",
        ],
        "Contoh": [
            "$x + 5 = 12$ → cari $x$",
            "Keliling = $4s$ → $s$ bisa berapa saja",
            "$U_n = 2n + 1$ → $n$ adalah nomor suku",
            "$y = mx$ → $m$ adalah kemiringan tetap",
        ],
        "Konteks SD": [
            "Soal cerita: 'umur Andi 5 tahun lebih...'",
            "Rumus keliling/luas",
            "Pola bilangan",
            "Resep: 'tepung 2× berat gula'",
        ],
    })
    st.dataframe(df_var, hide_index=True, width="stretch")

    # Visualisasi: variabel sebagai kotak misterius
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.text(0.5, 1.5, "5", fontsize=40, ha="center", fontweight="bold", color="#1e3a8a")
    ax.text(1.2, 1.5, "+", fontsize=35, ha="center", color="#475569")
    ax.add_patch(FancyBboxPatch((1.6, 0.8), 1.2, 1.4,
                                boxstyle="round,pad=0.1",
                                fill=False, edgecolor="#dc2626", linewidth=4))
    ax.text(2.2, 1.5, "?", fontsize=40, ha="center", fontweight="bold", color="#dc2626")
    ax.text(3.2, 1.5, "=", fontsize=35, ha="center", color="#475569")
    ax.text(4.0, 1.5, "12", fontsize=40, ha="center", fontweight="bold", color="#1e3a8a")
    ax.text(2.5, 0.2, "Kotak misterius adalah benih variabel di SD",
            fontsize=11, ha="center", style="italic", color="#475569")
    ax.set_xlim(0, 5); ax.set_ylim(0, 2.5)
    ax.set_aspect("equal"); ax.axis("off")
    st.pyplot(fig)
    plt.close()
    st.caption("📷 _Gambar 5.1 — Kotak misterius (☐) sebagai jembatan menuju variabel formal._")

    # ---- 5.3 Persamaan dan Kesetaraan ----
    st.header("5.3 Persamaan dan Prinsip Kesetaraan")
    st.markdown(
        """
        **Persamaan** ($=$) bukan berarti "menghasilkan jawaban". Banyak siswa SD menganggap
        tanda sama dengan sebagai _operator_ ("hitung dan tulis hasilnya"). Ini adalah
        **miskonsepsi serius** yang harus diluruskan oleh guru.

        Tanda $=$ sebenarnya berarti **kesetaraan** — kedua sisi memiliki nilai yang sama. Cara
        terbaik memvisualisasikannya adalah dengan **timbangan**.
        """
    )

    st.markdown("### 🎮 Simulasi: Timbangan Persamaan")
    c1, c2 = st.columns([1, 2])
    with c1:
        kiri = st.slider("Kiri: berapa apel?", 0, 10, 3, key="ch5_kiri")
        tambah_kiri = st.slider("Kiri: tambah berapa kotak misterius?", 0, 5, 1, key="ch5_kotak")
        kanan = st.slider("Kanan: berapa apel?", 0, 15, 8, key="ch5_kanan")
        st.markdown(f"**Persamaan:** ${kiri} + {tambah_kiri}x = {kanan}$")
        if tambah_kiri == 0:
            if kiri == kanan:
                hasil = "Setara! (Identitas)"
            else:
                hasil = "Tidak ada solusi"
        else:
            x = (kanan - kiri) / tambah_kiri
            if x == int(x):
                hasil = f"$x = {int(x)}$"
            else:
                hasil = f"$x = {x:.2f}$"
        st.markdown(
            f"<div class='example-box'><strong>Solusi:</strong> {hasil}</div>",
            unsafe_allow_html=True,
        )
    with c2:
        # Gambar timbangan
        fig, ax = plt.subplots(figsize=(9, 4.5))
        # Tiang
        ax.plot([5, 5], [0, 3], "k-", linewidth=4)
        # Lengan timbangan
        ax.plot([1.5, 8.5], [3, 3], "k-", linewidth=4)
        # Piring kiri & kanan
        ax.plot([1, 2], [2.7, 2.7], "k-", linewidth=3)
        ax.plot([8, 9], [2.7, 2.7], "k-", linewidth=3)
        ax.plot([1.5, 1.5], [2.7, 3], "k-", linewidth=2)
        ax.plot([8.5, 8.5], [2.7, 3], "k-", linewidth=2)
        # Apel kiri
        for i in range(min(kiri, 6)):
            ax.add_patch(Circle((1 + (i % 3) * 0.35, 3.0 + (i // 3) * 0.4),
                                0.15, color="#dc2626", ec="white"))
        if kiri > 6:
            ax.text(1.5, 3.8, f"+{kiri-6}", fontsize=10, color="#dc2626")
        # Kotak misterius kiri
        for i in range(tambah_kiri):
            ax.add_patch(Rectangle((1.7 + i*0.4, 3.0), 0.3, 0.3,
                                   color="#fbbf24", ec="black", linewidth=2))
            ax.text(1.85 + i*0.4, 3.15, "x", fontsize=10,
                    ha="center", va="center", fontweight="bold")
        # Apel kanan
        for i in range(min(kanan, 9)):
            ax.add_patch(Circle((8 + (i % 3) * 0.35, 3.0 + (i // 3) * 0.4),
                                0.15, color="#dc2626", ec="white"))
        if kanan > 9:
            ax.text(8.5, 4.0, f"+{kanan-9}", fontsize=10, color="#dc2626")
        # Alas
        ax.add_patch(Rectangle((4, -0.3), 2, 0.3, color="#475569"))
        ax.text(2, 1.5, f"{kiri} apel + {tambah_kiri}x",
                ha="center", fontsize=12, fontweight="bold", color="#1e3a8a")
        ax.text(8.5, 1.5, f"{kanan} apel",
                ha="center", fontsize=12, fontweight="bold", color="#1e3a8a")
        ax.text(5, 1.5, "=", fontsize=30, ha="center",
                fontweight="bold", color="#dc2626")
        ax.set_xlim(0, 10); ax.set_ylim(-0.5, 4.5)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title("Persamaan sebagai Timbangan yang Setara",
                     fontsize=12, fontweight="bold")
        st.pyplot(fig)
        plt.close()

    st.markdown(
        """
        <div class='activity-box'>
        <strong>💡 Tips Mengajar</strong><br>
        Saat memperkenalkan persamaan di SD, gunakan istilah <em>"sama dengan"</em> dengan
        sungguh-sungguh: tunjukkan bahwa kedua sisi tanda <strong>=</strong> harus
        <em>seimbang</em>. Hindari kebiasaan menulis $3 + 5 = 8 + 2 = 10$ karena ini melatih
        miskonsepsi: $3 + 5 \\neq 8 + 2$!
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- 5.4 Mesin Fungsi ----
    st.header("5.4 Mesin Fungsi (Function Machines)")
    st.markdown(
        """
        Salah satu cara paling _ramah anak_ untuk memperkenalkan fungsi/aturan adalah dengan
        gambar **mesin fungsi**: ada bilangan yang masuk (_input_), mesin mengubahnya
        berdasarkan aturan, lalu keluar bilangan baru (_output_).
        """
    )

    c1, c2 = st.columns([1, 2])
    with c1:
        operasi = st.selectbox(
            "Aturan mesin:",
            ["Tambah 5", "Kalikan 3", "Kurangi 2", "Kuadratkan",
             "Kalikan 2 lalu tambah 1"],
            key="ch5_mesin",
        )
        input_val = st.slider("Input", 0, 10, 4, key="ch5_input")

        if operasi == "Tambah 5":
            output = input_val + 5; rumus = "f(x) = x + 5"
        elif operasi == "Kalikan 3":
            output = input_val * 3; rumus = "f(x) = 3x"
        elif operasi == "Kurangi 2":
            output = input_val - 2; rumus = "f(x) = x − 2"
        elif operasi == "Kuadratkan":
            output = input_val ** 2; rumus = "f(x) = x²"
        else:
            output = 2 * input_val + 1; rumus = "f(x) = 2x + 1"

        st.markdown(
            f"<div class='example-box'>"
            f"<strong>Aturan:</strong> ${rumus}$<br>"
            f"<strong>Input:</strong> {input_val}<br>"
            f"<strong>Output:</strong> {output}"
            f"</div>",
            unsafe_allow_html=True,
        )
    with c2:
        fig, ax = plt.subplots(figsize=(9, 4))
        # Input
        ax.add_patch(Circle((1, 2), 0.6, color="#3b82f6", ec="white", linewidth=3))
        ax.text(1, 2, str(input_val), ha="center", va="center",
                fontsize=24, fontweight="bold", color="white")
        ax.text(1, 0.9, "INPUT", ha="center", fontsize=10, fontweight="bold")
        # Panah
        ax.annotate("", xy=(2.8, 2), xytext=(1.7, 2),
                    arrowprops=dict(arrowstyle="->", lw=3, color="#475569"))
        # Mesin
        ax.add_patch(FancyBboxPatch((3, 1.3), 3, 1.4,
                                    boxstyle="round,pad=0.05",
                                    facecolor="#fbbf24", ec="#92400e", linewidth=3))
        ax.text(4.5, 2.2, "MESIN", ha="center", fontsize=12, fontweight="bold")
        ax.text(4.5, 1.7, operasi, ha="center", fontsize=11, style="italic")
        # Panah keluar
        ax.annotate("", xy=(7.3, 2), xytext=(6.2, 2),
                    arrowprops=dict(arrowstyle="->", lw=3, color="#475569"))
        # Output
        ax.add_patch(Circle((8.2, 2), 0.6, color="#10b981", ec="white", linewidth=3))
        ax.text(8.2, 2, str(output), ha="center", va="center",
                fontsize=24, fontweight="bold", color="white")
        ax.text(8.2, 0.9, "OUTPUT", ha="center", fontsize=10, fontweight="bold")

        ax.set_xlim(0, 9.5); ax.set_ylim(0, 3.5)
        ax.set_aspect("equal"); ax.axis("off")
        st.pyplot(fig)
        plt.close()


# ============================================================
# BAB 6: EKSPLORASI POLA PERSAMAAN (KHUSUS)
# ============================================================
def page_ch6():
    st.title("✨ Bab 6 — Eksplorasi Pola Persamaan")

    st.markdown(
        """
        <div class='hero' style='padding:24px'>
            <h2 style='color:white;border:none;margin:0'>🧪 Lab Eksperimen Pola</h2>
            <p style='margin-top:8px'>Saksikan bagaimana persamaan matematika yang berbeda menghasilkan pola visual yang unik!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        Bab ini adalah _laboratorium interaktif_. Pilih jenis persamaan, geser parameternya,
        dan amati bagaimana setiap perubahan kecil dapat menciptakan pola yang sangat berbeda.
        Ini akan memperkuat intuisi Anda tentang hubungan antara _persamaan_ dan _pola visual_.
        """
    )

    jenis = st.selectbox(
        "🎨 Pilih jenis pola persamaan:",
        [
            "📈 Persamaan Linear: y = ax + b",
            "🌙 Persamaan Kuadrat: y = ax² + bx + c",
            "🌊 Gelombang Sinus: y = A sin(Bx + C)",
            "⚡ Fungsi Pangkat: y = a · xⁿ",
            "🎭 Kurva Lissajous (parametrik)",
            "🌹 Kurva Mawar (polar): r = a cos(kθ)",
            "🌀 Spiral: r = a · θ",
        ],
    )

    st.markdown("---")

    if jenis.startswith("📈"):
        st.header("📈 Persamaan Linear: y = ax + b")
        st.markdown(
            """
            Persamaan linear menghasilkan **garis lurus**. Parameter $a$ menentukan
            _kemiringan_ (gradien), sedangkan $b$ menentukan _titik potong sumbu y_.
            """
        )
        c1, c2 = st.columns([1, 2])
        with c1:
            a = st.slider("a (kemiringan)", -5.0, 5.0, 1.0, 0.1)
            b = st.slider("b (perpotongan y)", -5.0, 5.0, 0.0, 0.1)
        with c2:
            x = np.linspace(-10, 10, 200)
            y = a*x + b
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(x, y, color="#2563eb", linewidth=3)
            ax.axhline(0, color="black", linewidth=0.8)
            ax.axvline(0, color="black", linewidth=0.8)
            ax.scatter([0], [b], color="#dc2626", s=100, zorder=5,
                       label=f"Titik potong y: (0, {b:.1f})")
            ax.set_title(f"y = {a:.1f}x + {b:.1f}", fontweight="bold")
            ax.legend(); ax.set_xlim(-10, 10); ax.set_ylim(-15, 15)
            style_axes(ax)
            st.pyplot(fig)
            plt.close()
        st.markdown(
            """
            <div class='info-box'>
            🔍 <strong>Eksplorasi:</strong> Apa yang terjadi jika $a = 0$? Apa yang terjadi jika
            $a$ negatif? Mengapa garis selalu lurus, tidak peduli berapa pun nilai $a$ dan $b$?
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif jenis.startswith("🌙"):
        st.header("🌙 Persamaan Kuadrat: y = ax² + bx + c")
        st.markdown(
            "Persamaan kuadrat menghasilkan **parabola**. Tanda $a$ menentukan apakah parabola "
            "terbuka ke atas (positif) atau ke bawah (negatif)."
        )
        c1, c2 = st.columns([1, 2])
        with c1:
            a = st.slider("a", -3.0, 3.0, 1.0, 0.1, key="q_a")
            b = st.slider("b", -5.0, 5.0, 0.0, 0.1, key="q_b")
            c = st.slider("c", -5.0, 5.0, 0.0, 0.1, key="q_c")
            if a != 0:
                x_vert = -b / (2*a)
                y_vert = a*x_vert**2 + b*x_vert + c
                st.markdown(f"**Titik puncak:** ({x_vert:.2f}, {y_vert:.2f})")
        with c2:
            x = np.linspace(-10, 10, 300)
            y = a*x**2 + b*x + c
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(x, y, color="#7c3aed", linewidth=3)
            ax.axhline(0, color="black", linewidth=0.8)
            ax.axvline(0, color="black", linewidth=0.8)
            if a != 0:
                ax.scatter([x_vert], [y_vert], color="#dc2626", s=100, zorder=5,
                           label="Puncak")
                ax.legend()
            ax.set_title(f"y = {a:.1f}x² + {b:.1f}x + {c:.1f}", fontweight="bold")
            ax.set_xlim(-10, 10); ax.set_ylim(-30, 30)
            style_axes(ax)
            st.pyplot(fig)
            plt.close()
        st.markdown(
            """
            <div class='info-box'>
            🔍 <strong>Tantangan:</strong> Cari kombinasi $a$, $b$, $c$ yang membuat parabola
            <em>menyentuh</em> sumbu x tepat di satu titik (akar kembar). Petunjuk: diskriminan
            $b^2 - 4ac = 0$.
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif jenis.startswith("🌊"):
        st.header("🌊 Gelombang Sinus: y = A sin(Bx + C)")
        st.markdown(
            "Gelombang sinus mendasari banyak fenomena periodik: suara, cahaya, gelombang air. "
            "$A$ = amplitudo (tinggi), $B$ = frekuensi (rapatnya), $C$ = pergeseran fase."
        )
        c1, c2 = st.columns([1, 2])
        with c1:
            A = st.slider("A (amplitudo)", 0.1, 5.0, 1.0, 0.1)
            B = st.slider("B (frekuensi)", 0.1, 5.0, 1.0, 0.1)
            C = st.slider("C (fase)", -np.pi, np.pi, 0.0, 0.1)
        with c2:
            x = np.linspace(-2*np.pi, 2*np.pi, 500)
            y = A * np.sin(B*x + C)
            fig, ax = plt.subplots(figsize=(8, 4.5))
            ax.plot(x, y, color="#0891b2", linewidth=3)
            ax.axhline(0, color="black", linewidth=0.8)
            ax.axhline(A, color="#dc2626", linestyle="--", alpha=0.5, label=f"Amplitudo = {A:.1f}")
            ax.axhline(-A, color="#dc2626", linestyle="--", alpha=0.5)
            ax.set_title(f"y = {A:.1f} sin({B:.1f}x + {C:.2f})", fontweight="bold")
            ax.set_ylim(-5.5, 5.5); ax.legend()
            style_axes(ax)
            st.pyplot(fig)
            plt.close()

    elif jenis.startswith("⚡"):
        st.header("⚡ Fungsi Pangkat: y = a · xⁿ")
        st.markdown("Pangkat menghasilkan _pertumbuhan/penurunan_ yang dramatis.")
        c1, c2 = st.columns([1, 2])
        with c1:
            a = st.slider("a", -3.0, 3.0, 1.0, 0.1, key="p_a")
            n = st.slider("n (pangkat)", 0.5, 5.0, 2.0, 0.1, key="p_n")
        with c2:
            x = np.linspace(0.1, 5, 200)
            y = a * x**n
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(x, y, color="#dc2626", linewidth=3)
            ax.axhline(0, color="black", linewidth=0.8)
            ax.axvline(0, color="black", linewidth=0.8)
            ax.set_title(f"y = {a:.1f} · x^{n:.1f}", fontweight="bold")
            ax.set_xlim(0, 5)
            style_axes(ax)
            st.pyplot(fig)
            plt.close()

    elif jenis.startswith("🎭"):
        st.header("🎭 Kurva Lissajous")
        st.markdown(
            """
            Kurva Lissajous adalah pola luar biasa yang muncul ketika dua gerakan harmonik
            digabungkan: $x = \\sin(at)$ dan $y = \\sin(bt + \\delta)$. Ubah $a$, $b$, dan
            $\\delta$ untuk melihat pola yang sangat bervariasi!
            """
        )
        c1, c2 = st.columns([1, 2])
        with c1:
            a = st.slider("a", 1, 8, 3, key="l_a")
            b = st.slider("b", 1, 8, 4, key="l_b")
            delta = st.slider("δ (fase)", 0.0, np.pi, np.pi/2, 0.1, key="l_d")
        with c2:
            t = np.linspace(0, 2*np.pi, 1000)
            x = np.sin(a*t)
            y = np.sin(b*t + delta)
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.plot(x, y, color="#7c3aed", linewidth=2)
            ax.set_title(f"Lissajous: a={a}, b={b}, δ={delta:.2f}",
                         fontweight="bold")
            ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2)
            ax.set_aspect("equal")
            ax.grid(alpha=0.3)
            st.pyplot(fig)
            plt.close()
        st.markdown(
            """
            <div class='example-box'>
            🌟 Coba kombinasi (a, b) = (3, 2), (5, 4), (5, 6). Perhatikan bahwa kurva tertutup
            terjadi ketika $a/b$ adalah <em>bilangan rasional</em>!
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif jenis.startswith("🌹"):
        st.header("🌹 Kurva Mawar (Polar)")
        st.markdown(
            """
            Kurva mawar dirumuskan sebagai $r = a \\cos(k\\theta)$ dalam koordinat polar. Jumlah
            'kelopak' bunga ditentukan oleh $k$:

            - Jika $k$ ganjil: jumlah kelopak = $k$
            - Jika $k$ genap: jumlah kelopak = $2k$
            """
        )
        c1, c2 = st.columns([1, 2])
        with c1:
            a = st.slider("a (ukuran)", 0.5, 3.0, 1.0, 0.1, key="r_a")
            k = st.slider("k (jumlah kelopak)", 1, 10, 5, key="r_k")
        with c2:
            theta = np.linspace(0, 2*np.pi, 1000)
            r = a * np.cos(k * theta)
            x = r * np.cos(theta); y = r * np.sin(theta)
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.plot(x, y, color="#db2777", linewidth=2)
            ax.fill(x, y, color="#db2777", alpha=0.2)
            kelopak = k if k % 2 == 1 else 2*k
            ax.set_title(f"Mawar: a={a:.1f}, k={k} → {kelopak} kelopak",
                         fontweight="bold")
            ax.set_aspect("equal")
            ax.grid(alpha=0.3)
            st.pyplot(fig)
            plt.close()

    elif jenis.startswith("🌀"):
        st.header("🌀 Spiral Archimedes")
        st.markdown(
            """
            Spiral Archimedes: $r = a \\cdot \\theta$. Setiap _putaran_ menambah jarak dari pusat
            sebesar $2\\pi a$. Jenis pola ini muncul di alam (cangkang siput) dan teknologi
            (rekaman piringan hitam, pegas).
            """
        )
        c1, c2 = st.columns([1, 2])
        with c1:
            a = st.slider("a (kerapatan)", 0.05, 1.0, 0.2, 0.05, key="s_a")
            putaran = st.slider("Banyak putaran", 1, 10, 4, key="s_put")
        with c2:
            theta = np.linspace(0, putaran * 2*np.pi, 1000)
            r = a * theta
            x = r * np.cos(theta); y = r * np.sin(theta)
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.plot(x, y, color="#059669", linewidth=2)
            ax.set_title(f"Spiral: r = {a:.2f}θ ({putaran} putaran)", fontweight="bold")
            ax.set_aspect("equal")
            ax.grid(alpha=0.3)
            st.pyplot(fig)
            plt.close()

    st.markdown(
        """
        ---
        <div class='activity-box'>
        <strong>🎓 Refleksi Calon Guru SD</strong><br>
        Memang siswa SD belum belajar persamaan-persamaan kompleks ini. Tapi sebagai
        <em>guru</em>, Anda perlu paham bahwa <strong>semua pola visual yang indah ini berasal
        dari persamaan matematika</strong> yang relatif sederhana. Inilah yang membuat
        matematika begitu menakjubkan: dari aturan sederhana, lahir keindahan yang kompleks.
        Bawalah rasa kagum ini ke dalam kelas Anda nanti!
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# BAB 7: SOAL PENALARAN POLA
# ============================================================
def page_ch7():
    st.title("🎯 Bab 7 — Soal Penalaran Pola")

    st.markdown(
        """
        <div class='concept-box'>
        Tiga soal berikut dirancang untuk <em>mengasah penalaran</em> Anda sebagai calon guru SD.
        Cobalah memecahkannya tanpa terburu-buru. Tuliskan strategi Anda di kertas, baru
        kemudian buka <strong>petunjuk</strong> dan <strong>pembahasan</strong>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========== SOAL 1 ==========
    st.markdown(
        """
        <div class='quiz-box'>
        <h3 style='margin-top:0'>🧩 Soal 1 — Pola Susunan Korek Api</h3>
        Perhatikan susunan persegi yang dibuat dari korek api di bawah ini:<br>
        - 1 persegi membutuhkan <strong>4</strong> korek api<br>
        - 2 persegi berjejer membutuhkan <strong>7</strong> korek api<br>
        - 3 persegi berjejer membutuhkan <strong>10</strong> korek api<br><br>
        <strong>Pertanyaan:</strong> Berapa banyak korek api yang dibutuhkan untuk membuat
        <strong>50 persegi</strong> berjejer? Tuliskan rumus umumnya, lalu jelaskan
        bagaimana Anda akan memandu siswa kelas 5 SD untuk menemukan rumus tersebut.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Visual untuk soal 1
    fig, axes = plt.subplots(1, 3, figsize=(11, 2.5))
    for n_p, ax in zip([1, 2, 3], axes):
        for i in range(n_p):
            ax.add_patch(Rectangle((i, 0), 1, 1, fill=False,
                                   edgecolor="#dc2626", linewidth=4))
        ax.set_xlim(-0.3, n_p + 0.3); ax.set_ylim(-0.3, 1.3)
        ax.set_aspect("equal"); ax.axis("off")
        korek = 3*n_p + 1
        ax.set_title(f"{n_p} persegi → {korek} korek", fontweight="bold")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    with st.expander("💡 Petunjuk Soal 1"):
        st.markdown(
            """
            - Buat **tabel**: kolom $n$ (banyak persegi) dan kolom $K$ (banyak korek).
            - Hitung **selisih** antara $K$ untuk $n=1, 2, 3, 4$. Apakah selalu sama?
            - Jika selisih konstan, polanya **linear**: $K = an + b$.
            - Cara visual: bayangkan persegi pertama butuh 4, lalu setiap persegi tambahan butuh 3.
            """
        )

    with st.expander("✅ Pembahasan Soal 1"):
        st.markdown(
            """
            **Tabel:**

            | n | 1 | 2 | 3 | 4 | 5 |
            |---|---|---|---|---|---|
            | K | 4 | 7 | 10 | 13 | 16 |

            **Selisih:** selalu 3. Jadi pola linear dengan beda 3.

            **Penemuan rumus secara visual:**
            - Persegi pertama: butuh 4 korek (semua sisi penuh)
            - Setiap persegi tambahan: hanya butuh 3 korek baru (1 sisi sudah dipakai bersama)
            - Maka $K = 4 + 3(n-1) = 3n + 1$

            **Untuk n = 50:** $K = 3(50) + 1 = \\mathbf{151}$ korek api.

            **Strategi mengajar di SD kelas 5:**
            1. Mulai dari **manipulatif konkret** — gunakan korek api/lidi sungguhan, bangun bersama.
            2. Buat **tabel di papan tulis**, isi bersama-sama.
            3. Tanya: _"Apa yang berubah setiap kali ditambah 1 persegi?"_ → Anak akan melihat "+3".
            4. Dorong anak menemukan rumus dengan **kata-kata** dulu: "kalikan 3, tambah 1".
            5. Baru kenalkan simbol $n$ sebagai pengganti "banyaknya persegi".
            """
        )

    # ========== SOAL 2 ==========
    st.markdown(
        """
        <div class='quiz-box'>
        <h3 style='margin-top:0'>🧩 Soal 2 — Pola Bilangan Tersembunyi</h3>
        Perhatikan barisan bilangan berikut:<br><br>
        <strong>2, 6, 12, 20, 30, 42, ...</strong><br><br>
        <strong>Pertanyaan:</strong>
        <ol>
        <li>Apa suku ke-10 dari barisan ini?</li>
        <li>Tulislah rumus umum suku ke-n.</li>
        <li>Identifikasi <em>dua pendekatan visual</em> yang berbeda untuk menjelaskan pola ini
            kepada siswa SD.</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    fig, ax = plt.subplots(figsize=(10, 2.5))
    angka = [2, 6, 12, 20, 30, 42]
    for i, a in enumerate(angka):
        ax.add_patch(Circle((i*1.5 + 0.5, 0.5), 0.5,
                            color=plt.cm.viridis(i/6), ec="white", linewidth=2))
        ax.text(i*1.5 + 0.5, 0.5, str(a), ha="center", va="center",
                fontweight="bold", fontsize=14, color="white")
    ax.set_xlim(0, 9); ax.set_ylim(0, 1)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Barisan: 2, 6, 12, 20, 30, 42, ...", fontweight="bold")
    st.pyplot(fig)
    plt.close()

    with st.expander("💡 Petunjuk Soal 2"):
        st.markdown(
            """
            - Hitung selisih: $6-2=4$, $12-6=6$, $20-12=8$, ... Selisihnya **bertambah 2** setiap kali.
            - Selisih yang naik teratur biasanya menandakan pola **kuadrat**.
            - Coba faktorkan tiap suku: $2 = 1 \\times 2$, $6 = 2 \\times 3$, $12 = 3 \\times 4$, ...
            - Apakah Anda melihat polanya?
            """
        )

    with st.expander("✅ Pembahasan Soal 2"):
        st.markdown(
            r"""
            **1) Suku ke-10**

            $$U_n = n(n+1)$$

            $$U_{10} = 10 \times 11 = \mathbf{110}$$

            **2) Rumus umum:** $U_n = n(n+1) = n^2 + n$

            **3) Dua pendekatan visual untuk SD:**

            **Pendekatan A — Persegi panjang:** Setiap suku adalah luas persegi panjang
            berukuran $n \times (n+1)$. Misal $U_3 = 3 \times 4 = 12$ → susunan 3 baris × 4 kolom.

            **Pendekatan B — Dua kali bilangan segitiga:** Perhatikan bahwa $U_n = 2 T_n$
            (dua kali bilangan segitiga). Tunjukkan dua segitiga bilangan yang digabungkan
            membentuk persegi panjang!
            """
        )

        # Visualisasi pembahasan
        fig, axes = plt.subplots(1, 2, figsize=(11, 3))

        ax = axes[0]
        n = 4
        for i in range(n):
            for j in range(n+1):
                ax.add_patch(Rectangle((j*0.5, i*0.5), 0.45, 0.45,
                                       color="#3b82f6", ec="white"))
        ax.set_xlim(-0.3, (n+1)*0.5 + 0.3)
        ax.set_ylim(-0.3, n*0.5 + 0.3)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(f"U₄ = 4 × 5 = 20\n(persegi panjang)", fontweight="bold")

        ax = axes[1]
        n = 4
        # segitiga 1 (biru)
        for i in range(n):
            for j in range(i+1):
                ax.add_patch(Rectangle((j*0.5, i*0.5), 0.45, 0.45,
                                       color="#3b82f6", ec="white"))
        # segitiga 2 (merah, dibalik)
        for i in range(n):
            for j in range(n-i):
                ax.add_patch(Rectangle(((j+i+1)*0.5, i*0.5), 0.45, 0.45,
                                       color="#dc2626", ec="white"))
        ax.set_xlim(-0.3, (n+1)*0.5 + 0.3)
        ax.set_ylim(-0.3, n*0.5 + 0.3)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(f"U₄ = 2 × T₄ = 2 × 10 = 20\n(dua segitiga)", fontweight="bold")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # ========== SOAL 3 ==========
    st.markdown(
        """
        <div class='quiz-box'>
        <h3 style='margin-top:0'>🧩 Soal 3 — Pola Lantai Sekolah</h3>
        Sebuah sekolah memasang ubin di selasar dengan pola seperti gambar di bawah. Setiap
        gambar menunjukkan langkah ke-$n$ dari penyusunan ubin:<br><br>
        - Langkah 1: <strong>1</strong> ubin gelap (di tengah), <strong>0</strong> ubin terang<br>
        - Langkah 2: <strong>1</strong> ubin gelap, <strong>4</strong> ubin terang (mengelilingi)<br>
        - Langkah 3: <strong>1</strong> ubin gelap, <strong>12</strong> ubin terang (dua lapis)<br>
        - Langkah 4: <strong>1</strong> ubin gelap, <strong>24</strong> ubin terang (tiga lapis)<br><br>
        <strong>Pertanyaan:</strong>
        <ol>
        <li>Berapa banyak ubin terang pada langkah ke-10?</li>
        <li>Tulislah rumus umum jumlah <em>seluruh</em> ubin (gelap + terang) pada langkah ke-$n$.</li>
        <li>Pola apa yang Anda kenali, dan bagaimana Anda akan menggunakan pola ini sebagai
            <em>kegiatan eksplorasi</em> di kelas?</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Visual soal 3 — empat langkah
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    for langkah, ax in zip([1, 2, 3, 4], axes):
        size = 2*langkah - 1  # 1, 3, 5, 7
        for i in range(size):
            for j in range(size):
                # ubin gelap di tengah saja
                if i == size//2 and j == size//2:
                    color = "#1e293b"
                else:
                    color = "#fbbf24"
                ax.add_patch(Rectangle((i, j), 0.95, 0.95,
                                       color=color, ec="white", linewidth=1.5))
        ax.set_xlim(-0.3, size + 0.3); ax.set_ylim(-0.3, size + 0.3)
        ax.set_aspect("equal"); ax.axis("off")
        terang = size**2 - 1
        ax.set_title(f"Langkah {langkah}\n(1 gelap + {terang} terang)",
                     fontweight="bold", fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    with st.expander("💡 Petunjuk Soal 3"):
        st.markdown(
            """
            - Perhatikan **ukuran sisi** persegi pada setiap langkah: 1, 3, 5, 7, ... (bilangan ganjil).
            - Rumus sisi langkah ke-$n$: $2n - 1$.
            - Total ubin = sisi × sisi.
            - Ubin gelap selalu 1, jadi ubin terang = total − 1.
            """
        )

    with st.expander("✅ Pembahasan Soal 3"):
        st.markdown(
            r"""
            **Sisi persegi pada langkah ke-$n$:** $s_n = 2n - 1$

            **Total ubin:** $T_n = (2n-1)^2 = 4n^2 - 4n + 1$

            **Ubin terang:** $L_n = T_n - 1 = 4n^2 - 4n$

            **1) Langkah ke-10:**
            $L_{10} = 4(100) - 4(10) = 400 - 40 = \mathbf{360}$ ubin terang.

            **2) Rumus total:** $T_n = (2n-1)^2$ atau $T_n = 4n^2 - 4n + 1$.

            **3) Pola yang dikenali:**
            - $T_n$ adalah **bilangan kuadrat ganjil**: $1, 9, 25, 49, 81, \ldots$
            - Selisih antar $T_n$ dan $T_{n+1}$: 8, 16, 24, ... → kelipatan 8.
            - Ini adalah _bilangan persegi dari bilangan ganjil_!

            **Kegiatan eksplorasi di kelas:**
            1. Bagikan ubin/blok kayu warna gelap-terang ke kelompok kecil.
            2. Minta tiap kelompok menyusun langkah 1, 2, 3 sambil mengisi tabel.
            3. Diskusi kelas: _"Berapa banyak ubin yang ditambahkan setiap langkah?"_
            4. Buat anak menemukan pola **+8, +16, +24...** dan mengaitkannya dengan
               _bilangan ganjil yang berurutan_.
            5. Tantangan terbuka: _"Bisakah kamu memprediksi langkah ke-7 tanpa menyusun?"_
            """
        )

    st.markdown(
        """
        <div class='activity-box'>
        <strong>🎉 Selamat!</strong> Anda telah menyelesaikan tiga soal penalaran pola.
        Yang lebih penting daripada jawaban benar adalah <em>cara berpikir</em> yang Anda lalui:
        observasi → konjektur → uji → generalisasi. Inilah inti dari <strong>pemikiran
        aljabar</strong>, dan inilah yang harus Anda tularkan ke siswa-siswa SD Anda kelak. 🌟
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HALAMAN: TENTANG & REFERENSI
# ============================================================
def page_about():
    st.title("📚 Tentang & Referensi")

    st.markdown(
        """
        ## 🎯 Tentang Website Ini

        Website ini adalah **media pembelajaran interaktif** yang dirancang untuk mahasiswa
        calon guru Sekolah Dasar (SD) sebagai pendamping mata kuliah _Matematika SD_,
        khususnya pada topik **Pola dan Pemikiran Aljabar**.

        Materi disusun secara komprehensif mulai dari:
        - Pengenalan konsep pola yang konkret dan kontekstual
        - Klasifikasi pola dan pola bilangan klasik
        - Generalisasi dan pengenalan variabel
        - Pemikiran aljabar (timbangan, mesin fungsi)
        - Lab eksperimen pola persamaan
        - Soal penalaran untuk mengasah berpikir kritis

        ## 🛠️ Teknologi yang Digunakan

        - **Streamlit** — framework Python untuk aplikasi web interaktif
        - **Matplotlib** — visualisasi grafik dan diagram
        - **NumPy** — perhitungan numerik
        - **Pandas** — pengelolaan data tabular
        - **GitHub + Streamlit Community Cloud** — hosting & deployment

        ## 📖 Referensi Utama

        1. Van de Walle, J. A., Karp, K. S., & Bay-Williams, J. M. (2018). _Elementary and
           Middle School Mathematics: Teaching Developmentally_ (10th ed.). Pearson.
        2. NCTM. (2000). _Principles and Standards for School Mathematics_. National Council
           of Teachers of Mathematics.
        3. Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi. (2022).
           _Capaian Pembelajaran Matematika Fase A–C (SD)_. Jakarta: Kemendikbudristek.
        4. Mason, J., Graham, A., & Johnston-Wilder, S. (2005). _Developing Thinking in
           Algebra_. SAGE Publications.
        5. Tanton, J. (2019). _Exploding Dots: A Global Math Adventure_. Mathematical
           Association of America.
        6. Carpenter, T. P., Franke, M. L., & Levi, L. (2003). _Thinking Mathematically:
           Integrating Arithmetic and Algebra in Elementary School_. Heinemann.

        ## 📝 Lisensi

        Konten edukasi ini disediakan untuk keperluan pembelajaran. Kode sumber tersedia
        secara terbuka di GitHub.

        ## 🙏 Apresiasi

        Terima kasih kepada para dosen, guru SD, dan mahasiswa yang telah memberikan masukan
        untuk pengembangan materi ini.
        """
    )

    st.markdown(
        """
        <div class='footer-note'>
        💙 Dibuat dengan Streamlit untuk pendidikan matematika SD di Indonesia<br>
        <em>Karena setiap anak berhak menemukan keindahan matematika</em>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# ROUTING
# ============================================================
ROUTES = {
    "home": page_home,
    "ch1": page_ch1,
    "ch2": page_ch2,
    "ch3": page_ch3,
    "ch4": page_ch4,
    "ch5": page_ch5,
    "ch6": page_ch6,
    "ch7": page_ch7,
    "about": page_about,
}

ROUTES[page]()
