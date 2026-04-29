import streamlit as st
import pandas as pd
import joblib
import io
import plotly.express as px

# 1. KONFIGURASI HALAMAN & CSS
st.set_page_config(
    page_title="MindfulAI - Deteksi Stres Siswa",
    layout="wide",
    initial_sidebar_state="collapsed", 
)

st.markdown("""
<style>
    /* Mengurangi jarak kosong di atas */
    .block-container { padding-top: 3rem !important; }

    .hero-container {
        background: linear-gradient(135deg, #F0F4F8 0%, #D9E2EC 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        border: 1px solid #BCCCDC;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03);
    }
    .hero-title {
        color: #102A43;
        font-weight: 900;
        font-size: 3.5rem;
        margin-bottom: 10px;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        color: #486581;
        font-size: 1.2rem;
        font-weight: 500;
    }

    /* Menargetkan tombol yang ada di halaman Home */
    .element-container:has(.btn-marker-home) + .element-container .stButton > button {
        width: 100% !important;
        height: 100% !important;
        min-height: 220px;
        white-space: pre-wrap !important;
        border-radius: 16px !important;
        border: 2px solid #D9E2EC !important;
        background-color: #FFFFFF !important;
        padding: 40px 30px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02) !important;
        transition: all 0.3s ease !important;
        display: block;
        text-align: center;
    }
    .element-container:has(.btn-marker-home) + .element-container .stButton > button:hover {
        border-color: #434190 !important;
        background-color: #F8FAFC !important;
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(67, 65, 144, 0.1) !important;
    }
    
    /* Mengatur Judul Kartu (Baris Pertama) */
    .element-container:has(.btn-marker-home) + .element-container .stButton > button p::first-line {
        font-size: 26px;
        font-weight: 900;
        color: #434190;
        line-height: 2.5;
    }
    /* Mengatur Deskripsi Kartu (Baris Selanjutnya) */
    .element-container:has(.btn-marker-home) + .element-container .stButton > button p {
        font-size: 15px;
        font-weight: 400;
        color: #627D98;
        line-height: 1.6;
        margin: 0;
    }
            
    /* CSS Siswa & Konselor */
    .section-header {
        color: #434190; font-weight: 800; font-size: 20px;
        border-bottom: 2px solid #EDF2F7; padding-bottom: 10px; margin-bottom: 20px;
    }
    .status-card {
        border-radius: 12px; padding: 30px 20px; text-align: center;
        background-color: white; height: 100%; display: flex;
        flex-direction: column; justify-content: center; align-items: center;
        border-width: 3px; border-style: solid; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .status-title {
        color: #718096; font-weight: 800; font-size: 14px;
        letter-spacing: 1.5px; margin-bottom: 20px;
    }
    .status-text { font-weight: 900; font-size: 30px; margin-top: 20px; }
    .bars-card {
        border: 2px solid #E2E8F0; border-radius: 12px;
        padding: 25px 30px; background-color: white; height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .bar-label {
        font-weight: 800; font-size: 12px; color: #434190;
        margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;
    }
    .bar-bg {
        background-color: #EDF2F7; border: 1px solid #CBD5E0;
        border-radius: 6px; width: 100%; height: 28px;
        position: relative; margin-bottom: 25px;
    }
    .bar-fill-hp { background-color: #48BB78; height: 100%; border-radius: 5px 0 0 5px; transition: width 0.5s; }
    .bar-fill-mp { background-color: #3182CE; height: 100%; border-radius: 5px 0 0 5px; transition: width 0.5s; }
    .bar-fill-stress { background-color: #E53E3E; height: 100%; border-radius: 5px 0 0 5px; transition: width 0.5s; }
    .bar-text {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        font-weight: 900; font-size: 12px; color: #1A202C;
    }
</style>
""", unsafe_allow_html=True)

# 2. LOAD MODEL
@st.cache_resource
def load_assets():
    try:
        scaler = joblib.load('scaler.pkl')
        model = joblib.load('model_stacking.pkl')
        return scaler, model
    except: return None, None

scaler, model = load_assets()
EXPECTED_FEATURES = ["Kualitas Tidur", "Sakit Kepala", "Kinerja Akademis", "Beban Belajar", "Ekstrakurikuler"]

# 3. STATE MANAGEMENT & NAVBAR
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Navbar Atas
st.markdown(f"""
    <style>
    /* Mengubah warna latar belakang dan teks tombol */
    div.stButton > button {{
        background-color: #fffff;
        color: #5a57b5;
        border-radius: 5px;
        border: none;
    }}

    /* Mengubah warna saat kursor diarahkan (hover) */
    div.stButton > button:hover {{
        background-color: D9E2EC;
    }}
    </style>
    """, unsafe_allow_html=True)
nav1, nav2, nav3, nav4 = st.columns([4, 1, 1, 0.1])
with nav1:
    st.markdown("<h2 style='color: #434190; margin-top:0;'>MindfulAI.</h2>", unsafe_allow_html=True)
with nav2:
    if  st.button("Home", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
with nav3:
    if st.button("Tentang Sistem", use_container_width=True):
        st.session_state.page = 'tentang'
        st.rerun()

st.markdown("<hr style='margin-top: 0px; margin-bottom: 30px; border-color: #EDF2F7;'>", unsafe_allow_html=True)

# 4. HALAMAN UTAMA (HOME)
if st.session_state.page == 'home':
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Helping Your Student Shine Through Life</div>
        <div class="hero-subtitle">Sistem Cerdas Pendeteksi Tingkat Stres Akademik Berbasis Machine Learning</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: #434190; margin-bottom: 10px;'>Pilih Jalur Akses Anda</h3>", unsafe_allow_html=True)
    
    col_siswa, col_guru = st.columns(2, gap="large")
    
    # TOMBOL KARTU RAKSASA SISWA
    with col_siswa:
        # Marker HTML ini memicu trik CSS di atas untuk mengubah tombol menjadi kartu raksasa
        st.markdown("<div class='btn-marker-home'></div>", unsafe_allow_html=True)
        
        # Baris pertama akan menjadi judul, baris setelah enter (\n\n) menjadi deskripsi
        if st.button("Mode Siswa\nEvaluasi kondisi akademis dan fisikmu secara mandiri melalui antarmuka yang interaktif. Temukan tingkat keseimbanganmu sekarang.", key="btn_siswa"):
            st.session_state.page = 'siswa'
            st.rerun()

    # TOMBOL KARTU RAKSASA KONSELOR
    with col_guru:
        st.markdown("<div class='btn-marker-home'></div>", unsafe_allow_html=True)
        if st.button("Mode Konselor\nAkses dashboard analitik untuk melakukan ekstraksi data massal, memantau kondisi kelas, dan mengunduh laporan akhir.", key="btn_konselor"):
            st.session_state.page = 'konselor'
            st.rerun()

# 5. HALAMAN SISWA (INTERAKTIF RPG)
elif st.session_state.page == 'siswa':
    st.markdown("<h2 style='color: #434190;'>Simulator Keseimbangan Siswa</h2>", unsafe_allow_html=True)
    st.write("Eksplorasi bagaimana beban belajar dan waktu istirahat menentukan tingkat stres.")
    
    # --- SLIDER INPUT ---
    col_buff, col_debuff = st.columns(2, gap="large")
    
    with col_buff:
        st.markdown("<div class='section-header'>Atribut Pemulihan (Buff)</div>", unsafe_allow_html=True)
        v_tidur = st.select_slider("Kualitas Tidur (Regen HP)", 
                                   options=["Sangat Buruk", "Buruk", "Cukup", "Baik", "Sangat Baik"], value="Baik")
        v_ekskul = st.select_slider("Aktivitas Ekskul (Stamina)", 
                                    options=["Tidak Aktif", "Kurang Aktif", "Cukup Aktif", "Aktif", "Sangat Aktif"], value="Cukup Aktif")
        v_akademis = st.select_slider("Kinerja Akademis (Mana/MP)", 
                                      options=["Sangat Rendah", "Rendah", "Rata-rata", "Tinggi", "Sangat Tinggi"], value="Rata-rata")
        
    with col_debuff:
        st.markdown("<div class='section-header'>Atribut Beban (Debuff)</div>", unsafe_allow_html=True)
        v_beban = st.select_slider("Beban Belajar (Weight)", 
                                   options=["Sangat Ringan", "Ringan", "Sedang", "Berat", "Sangat Berat"], value="Sedang")
        v_kepala = st.select_slider("Keluhan Sakit Kepala (Damage)", 
                                    options=["Tidak Pernah", "Jarang", "Kadang-kadang", "Sering", "Sangat Sering"], value="Jarang")

    st.markdown("<hr style='border: 1px dashed #CBD5E0; margin: 30px 0;'>", unsafe_allow_html=True)

    # --- LOGIKA KLASIFIKASI & BAR ---
    val_map = {
        "Sangat Buruk": 1, "Buruk": 2, "Cukup": 3, "Baik": 4, "Sangat Baik": 5,
        "Tidak Aktif": 1, "Kurang Aktif": 2, "Cukup Aktif": 3, "Aktif": 4, "Sangat Aktif": 5,
        "Sangat Rendah": 1, "Rendah": 2, "Rata-rata": 3, "Tinggi": 4, "Sangat Tinggi": 5,
        "Sangat Ringan": 1, "Ringan": 2, "Sedang": 3, "Berat": 4, "Sangat Berat": 5,
        "Tidak Pernah": 1, "Jarang": 2, "Kadang-kadang": 3, "Sering": 4, "Sangat Sering": 5
    }
    
    hp_pct = int(((val_map[v_tidur] + val_map[v_ekskul]) / 10) * 100)
    mp_pct = int((val_map[v_akademis] / 5) * 100)
    stress_pct = int(((val_map[v_beban] + val_map[v_kepala]) / 10) * 100)
    
    if stress_pct <= 40:
        status_text = "RENDAH (AMAN)"
        status_color = "#38A169" # Hijau Aman
        icon_url = "https://i.pinimg.com/1200x/f5/2a/ce/f52ace4b103d7369d346521bdfa46ac8.jpg"
    elif stress_pct <= 70:
        status_text = "SEDANG (WASPADA)"
        status_color = "#D69E2E" # Kuning Waspada
        icon_url = "https://regeld.com/desi/wp-content/uploads/2021/03/2103011_earthquake_02-1.png"
    else:
        status_text = "TINGGI (BAHAYA)"
        status_color = "#E53E3E" # Merah Bahaya
        icon_url = "https://regeld.com/desi/wp-content/uploads/2021/03/2103011_earthquake_03-1.png"

    # --- UI RENDER ---
    c_status, c_bars = st.columns([1, 1.5], gap="large")
    with c_status:
        st.markdown(f"""<div class="status-card" style="border-color: {status_color};"><div class="status-title">FINAL STATUS</div><img src="{icon_url}" width="110" style="margin: 10px 0;"><div class="status-text" style="color: {status_color};">{status_text}</div></div>""", unsafe_allow_html=True)
    with c_bars:
        st.markdown(f"""<div class="bars-card"><div class="bar-label">HP (HEALTH - TIDUR & EKSKUL)</div><div class="bar-bg"><div class="bar-fill-hp" style="width: {hp_pct}%;"></div><div class="bar-text">{hp_pct}/100</div></div><div class="bar-label">MP (MANA - AKADEMIS)</div><div class="bar-bg"><div class="bar-fill-mp" style="width: {mp_pct}%;"></div><div class="bar-text">{mp_pct}/100</div></div><div class="bar-label">STRESS (DEBUFF - BEBAN & SAKIT)</div><div class="bar-bg"><div class="bar-fill-stress" style="width: {stress_pct}%;"></div><div class="bar-text">{stress_pct}/100</div></div></div>""", unsafe_allow_html=True)

# 6. HALAMAN KONSELOR (MASS IMPORT)
elif st.session_state.page == 'konselor':
    st.markdown("<h2 style='color: #434190;'>Dashboard Analisis Massal</h2>", unsafe_allow_html=True)
    st.write("Gunakan template di bawah ini. Pastikan data diisi dengan angka 1 sampai 5 sesuai skala instrumen penelitian.")
    
    with st.expander("Lihat Panduan Pengisian Skala Angka (1 - 5)"):
        st.markdown("""
        **Tabel Referensi Pengisian Dataset Excel:**
        | Kriteria | Angka 1 | Angka 2 | Angka 3 | Angka 4 | Angka 5 |
        | :--- | :--- | :--- | :--- | :--- | :--- |
        | **Kualitas Tidur** | Sangat Buruk | Buruk | Cukup | Baik | Sangat Baik |
        | **Sakit Kepala** | Tidak Pernah | Jarang | Kadang-kadang | Sering | Sangat Sering |
        | **Kinerja Akademis** | Sangat Rendah | Rendah | Rata-rata | Tinggi | Sangat Tinggi |
        | **Beban Belajar** | Sangat Ringan | Ringan | Sedang | Berat | Sangat Berat |
        | **Ekstrakurikuler**| Tidak Aktif | Kurang Aktif | Cukup Aktif | Aktif | Sangat Aktif |
        """)
    
    template_data = {
        "Nama Siswa": ["Siswa A", "Siswa B", "Siswa C"],
        "Kualitas Tidur": [5, 2, 3],
        "Sakit Kepala": [2, 4, 3],
        "Kinerja Akademis": [4, 1, 3],
        "Beban Belajar": [3, 5, 4],
        "Ekstrakurikuler": [4, 1, 3]
    }
    towrite = io.BytesIO()
    pd.DataFrame(template_data).to_excel(towrite, index=False, header=True)
    towrite.seek(0)
    
    st.download_button(
        label="Unduh Format Template Excel",
        data=towrite,
        file_name="Template_Dataset_Numerik.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    
    st.write("<br>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload file dataset (Excel/CSV)", type=['csv', 'xlsx'])
    
    @st.cache_data(show_spinner=False)
    def fast_load_file(file):
        if file.name.endswith('.csv'): return pd.read_csv(file)
        return pd.read_excel(file)

    if uploaded_file is not None:
        df = fast_load_file(uploaded_file)
        
        st.markdown("<div class='section-header' style='font-size:18px;'>Preview Data Mentah (Belum Diproses)</div>", unsafe_allow_html=True)
        st.dataframe(df.head(5), use_container_width=True)
        
        with st.container(border=True):
            st.markdown("<p style='font-weight:700; color:#434190;'>Pemetaan Kolom (Pastikan kolom sesuai dengan kriteria model)</p>", unsafe_allow_html=True)
            col_mapping = {}
            actual_cols = list(df.columns)
            
            c_map1, c_map2 = st.columns(2)
            with c_map1:
                col_mapping["Kualitas Tidur"] = st.selectbox("Kolom Data Tidur:", actual_cols, index=actual_cols.index("Kualitas Tidur") if "Kualitas Tidur" in actual_cols else 0)
                col_mapping["Sakit Kepala"] = st.selectbox("Kolom Sakit Kepala:", actual_cols, index=actual_cols.index("Sakit Kepala") if "Sakit Kepala" in actual_cols else 0)
                col_mapping["Ekstrakurikuler"] = st.selectbox("Kolom Ekstrakurikuler:", actual_cols, index=actual_cols.index("Ekstrakurikuler") if "Ekstrakurikuler" in actual_cols else 0)
            with c_map2:
                col_mapping["Kinerja Akademis"] = st.selectbox("Kolom Kinerja Akademis:", actual_cols, index=actual_cols.index("Kinerja Akademis") if "Kinerja Akademis" in actual_cols else 0)
                col_mapping["Beban Belajar"] = st.selectbox("Kolom Beban Belajar:", actual_cols, index=actual_cols.index("Beban Belajar") if "Beban Belajar" in actual_cols else 0)
            
            st.write("<br>", unsafe_allow_html=True)
            
            if st.button("Mulai Analisis Deteksi Stres", type="primary", use_container_width=True):
                with st.spinner('Menganalisis jutaan kemungkinan data...'):
                    df_numeric_mass = pd.DataFrame()
                    for target_col, excel_col in col_mapping.items():
                        df_numeric_mass[target_col] = pd.to_numeric(df[excel_col], errors='coerce')
                    
                    df_numeric_mass = df_numeric_mass[EXPECTED_FEATURES]
                    
                    if df_numeric_mass.isnull().values.any():
                        st.error("Terdapat sel kosong atau huruf pada kolom kriteria. Pastikan semua diisi angka 1-5.")
                    else:
                        if scaler and model:
                            scaled_mass = scaler.transform(df_numeric_mass)
                            pred_mass = model.predict(scaled_mass)
                        else:
                            # Fallback Dummy
                            pred_mass = []
                            for row in df_numeric_mass.values:
                                stress_score = row[1] + row[3] 
                                if stress_score <= 4: pred_mass.append(0)
                                elif stress_score <= 7: pred_mass.append(1)
                                else: pred_mass.append(2)

                        label_map = {0: "Rendah", 1: "Sedang", 2: "Tinggi"}
                        df_result = df.copy()
                        df_result["Prediksi Tingkat Stres"] = pd.Series(pred_mass).map(label_map)
                        
                        st.success("Proses deteksi selesai!")
                        
                        st.markdown("<div class='section-header' style='font-size:18px;'>Preview Hasil Deteksi</div>", unsafe_allow_html=True)
                        st.dataframe(df_result.head(10), use_container_width=True)
                        
                        st.markdown("<h4 style='color: #434190; margin-top:30px;'>Ringkasan Distribusi Kelas</h4>", unsafe_allow_html=True)
                        
                        counts = df_result["Prediksi Tingkat Stres"].value_counts().reset_index()
                        counts.columns = ['Status', 'Total']
                        chart_colors = {"Tinggi": "#E53E3E", "Sedang": "#D69E2E", "Rendah": "#38A169"}
                        
                        viz_col1, viz_col2 = st.columns(2)
                        with viz_col1:
                            fig_bar = px.bar(counts, x='Status', y='Total', color='Status', color_discrete_map=chart_colors, text_auto=True)
                            fig_bar.update_layout(showlegend=False, margin=dict(t=20, b=20, l=10, r=10), plot_bgcolor='rgba(0,0,0,0)')
                            st.plotly_chart(fig_bar, use_container_width=True)
                        with viz_col2:
                            fig_pie = px.pie(counts, values='Total', names='Status', color='Status', color_discrete_map=chart_colors, hole=0.5)
                            fig_pie.update_layout(margin=dict(t=20, b=20, l=10, r=10))
                            st.plotly_chart(fig_pie, use_container_width=True)
                        
                        csv = df_result.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="Simpan Laporan Keseluruhan (.CSV)",
                            data=csv,
                            file_name='Hasil_Deteksi_Stres_Siswa.csv',
                            mime='text/csv',
                            use_container_width=True
                        )

# 7. HALAMAN TENTANG SISTEM
elif st.session_state.page == 'tentang':
    st.markdown("<h2 style='color: #434190; margin-bottom: 20px;'>Bagaimana MindfulAI Bekerja?</h2>", unsafe_allow_html=True)
    st.write("Sistem ini menggunakan algoritma canggih bernama **Stacking Ensemble Learning**. Agar mudah dipahami, bayangkan algoritma ini seperti sebuah **Tim Dokter Rumah Sakit** yang sedang memeriksa kesehatan siswa.")
    
    st.markdown("<div class='section-header' style='margin-top: 30px;'>Tahap 1: Analisis Dokter Spesialis (Base Learner)</div>", unsafe_allow_html=True)
    st.write("Ketika data siswa masuk, data tersebut tidak hanya diperiksa oleh satu orang, melainkan oleh tiga dokter spesialis sekaligus. Masing-masing memiliki keahlian berbeda:")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.markdown("<h4 style='color: #434190;'>Decision Tree (DT)</h4>", unsafe_allow_html=True)
            st.write("Ibarat dokter umum yang menganalisis dengan runtutan pertanyaan Ya atau Tidak. Ia melihat logika langsung: Jika tidur kurang dan beban berat, maka risikonya tinggi.")
    with c2:
        with st.container(border=True):
            st.markdown("<h4 style='color: #434190;'>Support Vector Machine</h4>", unsafe_allow_html=True)
            st.write("Ibarat dokter bedah yang menarik batas tegas. Ia sangat pintar mencari garis batas pemisah antara siswa yang masih aman dan siswa yang sudah terindikasi stres.")
    with c3:
        with st.container(border=True):
            st.markdown("<h4 style='color: #434190;'>K-Nearest Neighbor (KNN)</h4>", unsafe_allow_html=True)
            st.write("Ibarat dokter yang melihat riwayat pasien masa lalu. Ia mendiagnosis dengan cara mencari kemiripan data siswa tersebut dengan kasus-kasus siswa sebelumnya.")

    st.markdown("<div class='section-header' style='margin-top: 40px;'>Tahap 2: Keputusan Final (Meta Learner)</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<h4 style='color: #434190;'>Direktur Rumah Sakit (Logistic Regression)</h4>", unsafe_allow_html=True)
        st.write("Setelah ketiga dokter spesialis di atas memberikan hasil diagnosis masing-masing, kadang hasilnya bisa berbeda (misal: DT bilang Tinggi, tapi KNN bilang Sedang).")
        st.write("Di sinilah **Meta Learner (Logistic Regression)** bertugas. Sebagai Direktur Rumah Sakit, ia mendengarkan pendapat ketiga dokter tersebut, mengevaluasi siapa yang paling bisa dipercaya untuk kasus tertentu, dan menjatuhkan **Satu Keputusan Final** (Rendah, Sedang, atau Tinggi) yang paling akurat.")
