# # # import streamlit as st
# # # import pandas as pd
# # # import joblib
# # # import io
# # # import plotly.graph_objects as go
# # # import plotly.express as px


# # # # 1. KONFIGURASI HALAMAN & HIDE SIDEBAR
# # # # ==========================================
# # # st.set_page_config(
# # #     page_title="MindfulAI - Deteksi Stres Siswa",
# # #     layout="wide",
# # #     initial_sidebar_state="collapsed", 
# # # )

# # # # ==========================================
# # # # 2. CUSTOM CSS (FULL REFINEMENT & RESPONSIVE)
# # # # ==========================================
# # # st.markdown("""
# # # <style>
# # #     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
# # #     html, body, [class*="css"] {
# # #         font-family: 'Plus Jakarta Sans', sans-serif;
# # #     }
    
# # #     .stApp { background-color: #FDFCF8; }
    
# # #     /* Sembunyikan Sidebar & Header Streamlit secara total */
# # #     [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
# # #     [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
# # #     /* CONTAINER UTAMA */
# # #     .block-container {
# # #         padding-top: 2rem !important;
# # #         padding-left: 5rem !important;
# # #         padding-right: 5rem !important;
# # #     }

# # #     /* =========================================
# # #        FLOATING PILL NAVBAR (DESKTOP)
# # #        ========================================= */
# # #     /* Menargetkan row (baris) yang berisi logo navigasi */
# # #     [data-testid="stHorizontalBlock"]:has(.nav-logo) {
# # #         background-color: #FFFFFF;
# # #         border-radius: 50px;
# # #         padding: 10px 40px;
# # #         box-shadow: 0 10px 30px rgba(0,0,0,0.06);
# # #         max-width: 900px;
# # #         margin: 0 auto 2.5rem auto; /* Posisi di tengah */
# # #         align-items: center;
# # #         border: 1px solid #EDF2F7;
# # #         position: relative;
# # #         z-index: 100;
# # #     }

# # #     /* Style Radio Button menyamar jadi Navbar */
# # #     div[role="radiogroup"] {
# # #         display: flex;
# # #         flex-direction: row;
# # #         justify-content: flex-end;
# # #         gap: 25px;
# # #         border: none !important;
# # #         margin-bottom: 0;
# # #     }
# # #     div[role="radiogroup"] > label {
# # #         background: transparent !important;
# # #         border: none !important;
# # #         padding: 0 !important;
# # #     }
# # #     div[role="radiogroup"] > label > div:first-child { display: none !important; }
# # #     div[role="radiogroup"] > label > div:last-child {
# # #         font-weight: 600;
# # #         font-size: 1rem;
# # #         color: #64748B !important; 
# # #         cursor: pointer;
# # #         transition: all 0.3s ease;
# # #     }
# # #     div[role="radiogroup"] > label:hover > div:last-child { color: #434190 !important; }
# # #     div[role="radiogroup"] > label[data-checked="true"] > div:last-child {
# # #         color: #5A67D8 !important; 
# # #         border-bottom: 2px solid #5A67D8;
# # #     }

# # #     /* =========================================
# # #        ELEMENT UI LAINNYA
# # #        ========================================= */
# # #     .stTabs [data-baseweb="tab-highlight"] { background-color: #5A67D8 !important; }
# # #     .stTabs [data-baseweb="tab"] { color: #64748B !important; }
# # #     .stTabs [aria-selected="true"] { color: #5A67D8 !important; }

# # #     .stSelectbox label, .stSlider label { color: #4A5568 !important; font-weight: 600 !important; }
# # #     .stSlider [data-baseweb="slider"] > div > div > div:nth-child(1) { background: #5A67D8 !important; }
# # #     .stSlider [data-baseweb="slider"] > div { background: transparent !important; }
# # #     .stSlider [data-baseweb="slider"] div[style*="color: rgb(255, 75, 75)"], 
# # #     .stSlider [data-baseweb="slider"] div[style*="color: #ff4b4b"] { color: #5A67D8 !important; }
# # #     .stSlider [data-baseweb="slider"] [role="slider"] { background-color: #5A67D8 !important; border: 2px solid #5A67D8 !important; }
# # #     .stSlider [data-testid="stTickBarItem"] { color: #64748B !important; }

# # #     /* =========================================
# # #        MEDIA QUERIES (RESPONSIVE UNTUK HP & TABLET)
# # #        ========================================= */
# # #     @media screen and (max-width: 768px) {
# # #         /* Pengecilan padding utama di HP */
# # #         .block-container {
# # #             padding-top: 1rem !important;
# # #             padding-left: 1rem !important;
# # #             padding-right: 1rem !important;
# # #         }
        
# # #         /* Navbar menyesuaikan bentuk tumpuk di HP */
# # #         [data-testid="stHorizontalBlock"]:has(.nav-logo) {
# # #             max-width: 95%;
# # #             border-radius: 25px;
# # #             padding: 15px 20px;
# # #             flex-direction: column;
# # #             gap: 15px;
# # #             margin-bottom: 1.5rem;
# # #         }
# # #         .nav-logo { text-align: center; }
        
# # #         div[role="radiogroup"] {
# # #             justify-content: center;
# # #             flex-wrap: wrap;
# # #             gap: 15px;
# # #         }

# # #         /* Penyesuaian teks besar agar tidak terpotong */
# # #         h1 { font-size: 2.2rem !important; }
# # #         .game-card-light div[style*="font-size: 5rem"] { font-size: 3.5rem !important; }
# # #         .game-card-light h2 { font-size: 1.5rem !important; }
# # #     }
# # # </style>
# # # """, unsafe_allow_html=True)

# # # # ==========================================
# # # # 3. LOAD MODEL & LOGIC
# # # # ==========================================
# # # @st.cache_resource
# # # def load_assets():
# # #     try:
# # #         scaler = joblib.load('scaler.pkl')
# # #         model = joblib.load('model_stacking.pkl')
# # #         return scaler, model
# # #     except: return None, None

# # # scaler, model = load_assets()

# # # SCALE_MAP = {
# # #     "Kualitas Tidur": {"Sangat Buruk": 1, "Buruk": 2, "Cukup": 3, "Baik": 4, "Sangat Baik": 5},
# # #     "Sakit Kepala": {"Tidak Pernah": 1, "Jarang": 2, "Kadang-kadang": 3, "Sering": 4, "Sangat Sering": 5},
# # #     "Kinerja Akademis": {"Sangat Rendah": 1, "Rendah": 2, "Rata-rata": 3, "Tinggi": 4, "Sangat Tinggi": 5},
# # #     "Beban Belajar": {"Sangat Ringan": 1, "Ringan": 2, "Sedang": 3, "Berat": 4, "Sangat Berat": 5},
# # #     "Ekstrakurikuler": {"Tidak Aktif": 1, "Kurang Aktif": 2, "Cukup Aktif": 3, "Aktif": 4, "Sangat Aktif": 5}
# # # }

# # # EXPECTED_FEATURES = ["Kualitas Tidur", "Sakit Kepala", "Kinerja Akademis", "Beban Belajar", "Ekstrakurikuler"]

# # # # ==========================================
# # # # 4. RENDER NAVBAR ATAS (FLOATING PILL)
# # # # ==========================================
# # # # Kolom navbar diatur agar bisa terpengaruh CSS pill-shape
# # # nav_col1, nav_col2 = st.columns([1, 2])
# # # with nav_col1:
# # #     # Class 'nav-logo' digunakan oleh CSS untuk menargetkan baris ini
# # #     st.markdown("<h2 class='nav-logo' style='color: #434190; font-weight: 800; margin: 0; padding: 0;'>MindfulAI.</h2>", unsafe_allow_html=True)
# # # with nav_col2:
# # #     menu = st.radio("Navigation", ["Home", "Simulator", "Informasi Sistem"], horizontal=True, label_visibility="collapsed")

# # # def render_hero(title, subtitle):
# # #     st.markdown(f"""
# # #     <div style="background-color: #EDF2F7; padding: 4rem 2rem 1rem 2rem; border-radius: 40px 40px 0 0; text-align: center;">
# # #         <h1 style="color: #2D3748; font-weight: 800; font-size: 3.5rem; margin-bottom: 1.2rem; line-height: 1.1;">{title}</h1>
# # #         <p style="color: #718096; font-size: 1.2rem; max-width: 800px; margin: 0 auto; line-height: 1.6;">{subtitle}</p>
# # #     </div>
# # #     <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 120" style="display: block; width: 100%; margin-bottom: 2rem;">
# # #       <path fill="#EDF2F7" d="M0,64L80,69.3C160,75,320,85,480,80C640,75,800,53,960,48C1120,43,1280,53,1360,58.7L1440,64L1440,0L1360,0C1280,0,1120,0,960,0C800,0,640,0,480,0C320,0,160,0,80,0L0,0Z"></path>
# # #     </svg>
# # #     """, unsafe_allow_html=True)

# # # # ==========================================
# # # # HALAMAN HOME
# # # # ==========================================
# # # if menu == "Home":
# # #     render_hero("Helping Your Student Shine Through Life", "Mendeteksi tingkat stres akademik siswa SMA dengan pendekatan cerdas berbasis Machine Learning multi-model.")
    
# # #     col1, col2, col3 = st.columns(3)
# # #     feats = [
# # #         ("Holistic Approach", "Evaluasi kondisi akademis dan fisik siswa secara individual."),
# # #         ("Science Research", "Menggunakan pendekatan Stacking Ensemble Learning (DT, SVM, KNN)."),
# # #         ("Experienced", "Fasilitas ekstraksi massal untuk tenaga pendidik dalam format Excel.")
# # #     ]
# # #     for i, (t, d) in enumerate(feats):
# # #         with [col1, col2, col3][i]:
# # #             with st.container(border=True):
# # #                 st.markdown(f"<h4 style='color: #2D3748; text-align:center;'>{t}</h4><p style='color: #718096; text-align:center;'>{d}</p>", unsafe_allow_html=True)

# # # # ==========================================
# # # # HALAMAN SIMULATOR
# # # # ==========================================
# # # elif menu == "Simulator":
# # #     render_hero("Simulator Keseimbangan Siswa", "Eksplorasi bagaimana beban belajar dan waktu istirahat menentukan tingkat stres.")
    
# # #     tab_ind, tab_mass = st.tabs(["Evaluasi Mandiri (Interaktif)", "Impor Data Kelas (Massal)"])

# # #     with tab_ind:
# # #         st.markdown("""
# # #         <style>
# # #         .game-card-light { background: #FFFFFF; padding: 20px; border-radius: 15px; border: 3px solid #E2E8F0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; text-align: center;}
# # #         .stat-label-light { font-weight: 800; font-size: 13px; text-transform: uppercase; color: #4A5568; margin-bottom: 5px; letter-spacing: 1px;}
# # #         .bar-bg-light { background-color: #EDF2F7; border-radius: 8px; height: 28px; width: 100%; border: 2px solid #CBD5E0; overflow: hidden; position: relative; }
# # #         .hp-bar { background: linear-gradient(90deg, #48BB78, #38A169); height: 100%; transition: width 0.6s ease; }
# # #         .mp-bar { background: linear-gradient(90deg, #4299E1, #3182CE); height: 100%; transition: width 0.6s ease; }
# # #         .stress-bar { background: linear-gradient(90deg, #F56565, #E53E3E); height: 100%; transition: width 0.6s ease; }
# # #         .bar-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #1A202C; font-weight: 900; font-size: 13px; }
# # #         </style>
# # #         """, unsafe_allow_html=True)

# # #         st.markdown("<div class='game-card-light' style='border-color: #5A67D8;'><h2 style='color: #434190; margin:0; font-weight:900;'>KARAKTER STATUS BUILDER</h2><p style='color: #718096; margin:0;'>Atur atribut aktivitasmu dan lihat dampaknya secara real-time!</p></div>", unsafe_allow_html=True)

# # #         col_in1, col_in2 = st.columns(2)
# # #         with col_in1:
# # #             with st.container(border=True):
# # #                 st.markdown("<h4 style='color: #38A169; margin-top:0;'>Atribut Buff (Pemulihan)</h4>", unsafe_allow_html=True)
# # #                 v_tidur = st.select_slider("Kualitas Tidur (Regen HP)", options=list(SCALE_MAP["Kualitas Tidur"].keys()), value="Baik")
# # #                 v_ekskul = st.select_slider("Aktivitas Ekskul (Stamina)", options=list(SCALE_MAP["Ekstrakurikuler"].keys()), value="Cukup Aktif")
# # #                 v_akademis = st.select_slider("Kinerja Akademis (Mana/MP)", options=list(SCALE_MAP["Kinerja Akademis"].keys()), value="Rata-rata")

# # #         with col_in2:
# # #             with st.container(border=True):
# # #                 st.markdown("<h4 style='color: #E53E3E; margin-top:0;'>Atribut Debuff (Beban)</h4>", unsafe_allow_html=True)
# # #                 v_beban = st.select_slider("Beban Belajar (Weight)", options=list(SCALE_MAP["Beban Belajar"].keys()), value="Sedang")
# # #                 v_kepala = st.select_slider("Keluhan Sakit Kepala (Damage)", options=list(SCALE_MAP["Sakit Kepala"].keys()), value="Jarang")

# # #         val_tidur = SCALE_MAP["Kualitas Tidur"][v_tidur]
# # #         val_ekskul = SCALE_MAP["Ekstrakurikuler"][v_ekskul]
# # #         val_akademis = SCALE_MAP["Kinerja Akademis"][v_akademis]
# # #         val_beban = SCALE_MAP["Beban Belajar"][v_beban]
# # #         val_kepala = SCALE_MAP["Sakit Kepala"][v_kepala]

# # #         hp_pct = int(((val_tidur + val_ekskul) / 10) * 100)
# # #         mp_pct = int((val_akademis / 5) * 100)
# # #         stress_pct = int(((val_beban + val_kepala) / 10) * 100)

# # #         if scaler and model:
# # #             input_data = pd.DataFrame([{
# # #                 "Kualitas Tidur": val_tidur,
# # #                 "Sakit Kepala": val_kepala,
# # #                 "Kinerja Akademis": val_akademis,
# # #                 "Beban Belajar": val_beban,
# # #                 "Ekstrakurikuler": val_ekskul
# # #             }])
# # #             scaled = scaler.transform(input_data)
# # #             pred = model.predict(scaled)[0]
            
# # #             hasil_label = {0: "Rendah (Aman)", 1: "Sedang (Waspada)", 2: "Tinggi (Bahaya!)"}[pred]
# # #             warna = {"Rendah (Aman)": "#48BB78",  "Sedang (Waspada)": "#D69E2E",  "Tinggi (Bahaya!)": "#E53E3E"}[hasil_label]
# # #             emoji_status = {"Rendah (Aman)": "🛡️",  "Sedang (Waspada)": "⚠️",  "Tinggi (Bahaya!)": "☠️"}[hasil_label]

# # #             rekomendasi = {
# # #                 0: "Kondisi akademis dan psikologismu sangat seimbang! Pertahankan pola tidur yang baik dan terus nikmati kegiatan ekstrakurikulermu.",
# # #                 1: "Kamu mulai merasakan tekanan. Coba kurangi sedikit beban belajarmu di akhir pekan dan perbanyak jam tidur untuk *recovery* HP.",
# # #                 2: "Peringatan! Tingkat stresmu terlalu tinggi. Segera bicarakan dengan guru BK atau istirahat total dari tugas selama 1-2 hari. Kesehatanmu adalah prioritas utama."
# # #             }[pred]

# # #             st.markdown("<hr style='border: 2px dashed #E2E8F0; margin: 2rem 0;'>", unsafe_allow_html=True)
            
# # #             res_col1, res_col2 = st.columns([1, 1.5], gap="large")
# # #             with res_col1:
# # #                 st.markdown(f"""
# # #                 <div class='game-card-light' style='border-color: {warna}; height: 100%; display: flex; flex-direction: column; justify-content: center;'>
# # #                     <p style='color: #718096; font-weight: 800; letter-spacing: 1px; margin-bottom: 5px;'>FINAL STATUS</p>
# # #                     <div style='font-size: 5rem; margin: 10px 0;'>{emoji_status}</div>
# # #                     <h2 style='color: {warna}; font-weight: 900; margin: 0;'>{hasil_label.upper()}</h2>
# # #                 </div>
# # #                 """, unsafe_allow_html=True)
                
# # #             with res_col2:
# # #                 st.markdown(f"""
# # #                 <div class='game-card-light' style='height: 100%; text-align:left;'>
# # #                     <div class='stat-label-light'>HP (Health - Tidur & Ekskul)</div>
# # #                     <div class='bar-bg-light'><div class='hp-bar' style='width: {hp_pct}%;'></div><div class='bar-text'>{hp_pct}/100</div></div>
# # #                     <br>
# # #                     <div class='stat-label-light'>MP (Mana - Akademis)</div>
# # #                     <div class='bar-bg-light'><div class='mp-bar' style='width: {mp_pct}%;'></div><div class='bar-text'>{mp_pct}/100</div></div>
# # #                     <br>
# # #                     <div class='stat-label-light'>STRESS (Debuff - Beban & Sakit)</div>
# # #                     <div class='bar-bg-light'><div class='stress-bar' style='width: {stress_pct}%;'></div><div class='bar-text'>{stress_pct}/100</div></div>
# # #                 </div>
# # #                 """, unsafe_allow_html=True)
            
# # #             st.info(f"**Rekomendasi Sistem:** {rekomendasi}")

# # #     with tab_mass:
# # #         st.markdown("<h4 style='color: #2D3748; margin-bottom: 1rem;'>Import Data Kelas Massal</h4>", unsafe_allow_html=True)
# # #         st.write("Gunakan template di bawah ini. Pastikan data diisi dengan **angka 1 sampai 5** sesuai skala instrumen penelitian.")
        
# # #         with st.expander("Buka Panduan Pengisian Skala Angka (1 - 5)"):
# # #             st.markdown("""
# # #             **Tabel Referensi Pengisian Dataset Excel:**
            
# # #             | Kriteria | Angka 1 | Angka 2 | Angka 3 | Angka 4 | Angka 5 |
# # #             | :--- | :--- | :--- | :--- | :--- | :--- |
# # #             | **Kualitas Tidur** | Sangat Buruk | Buruk | Cukup | Baik | Sangat Baik |
# # #             | **Sakit Kepala** | Tidak Pernah | Jarang | Kadang-kadang | Sering | Sangat Sering |
# # #             | **Kinerja Akademis** | Sangat Rendah | Rendah | Rata-rata | Tinggi | Sangat Tinggi |
# # #             | **Beban Belajar** | Sangat Ringan | Ringan | Sedang | Berat | Sangat Berat |
# # #             | **Ekstrakurikuler**| Tidak Aktif | Kurang Aktif | Cukup Aktif | Aktif | Sangat Aktif |
            
# # #             *Catatan: Kolom Nama Siswa bebas diisi teks (nama, inisial, atau NIS).*
# # #             """)
        
# # #         template_data = {
# # #             "Nama Siswa": ["Siswa A", "Siswa B", "Siswa C"],
# # #             "Kualitas Tidur": [5, 2, 3],
# # #             "Sakit Kepala": [2, 4, 3],
# # #             "Kinerja Akademis": [4, 1, 3],
# # #             "Beban Belajar": [3, 5, 4],
# # #             "Ekstrakurikuler": [4, 1, 3]
# # #         }
# # #         towrite = io.BytesIO()
# # #         pd.DataFrame(template_data).to_excel(towrite, index=False, header=True)
# # #         towrite.seek(0)
        
# # #         st.download_button(
# # #             label="Unduh Format Template Excel (Skala 1-5)",
# # #             data=towrite,
# # #             file_name="Template_Dataset_Numerik.xlsx",
# # #             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
# # #         )
        
# # #         st.write("<br>", unsafe_allow_html=True)
# # #         uploaded_file = st.file_uploader("Upload file dataset (Excel/CSV)", type=['csv', 'xlsx'])
        
# # #         @st.cache_data(show_spinner=False)
# # #         def fast_load_file(file):
# # #             if file.name.endswith('.csv'): return pd.read_csv(file)
# # #             return pd.read_excel(file)

# # #         if uploaded_file is not None:
# # #             df = fast_load_file(uploaded_file)
            
# # #             st.markdown("#####Preview Data Mentah (Belum Diproses)")
# # #             st.dataframe(df.head(5), use_container_width=True)
            
# # #             with st.container(border=True):
# # #                 st.markdown("<p style='font-weight:700; color:#2C5282;'>Pemetaan Kolom (Pastikan kolom sesuai)</p>", unsafe_allow_html=True)
# # #                 col_mapping = {}
# # #                 actual_cols = list(df.columns)
                
# # #                 c_map1, c_map2 = st.columns(2)
# # #                 with c_map1:
# # #                     col_mapping["Kualitas Tidur"] = st.selectbox("Kolom Data Tidur:", actual_cols, index=actual_cols.index("Kualitas Tidur") if "Kualitas Tidur" in actual_cols else 0)
# # #                     col_mapping["Sakit Kepala"] = st.selectbox("Kolom Sakit Kepala:", actual_cols, index=actual_cols.index("Sakit Kepala") if "Sakit Kepala" in actual_cols else 0)
# # #                     col_mapping["Ekstrakurikuler"] = st.selectbox("Kolom Ekstrakurikuler:", actual_cols, index=actual_cols.index("Ekstrakurikuler") if "Ekstrakurikuler" in actual_cols else 0)
# # #                 with c_map2:
# # #                     col_mapping["Kinerja Akademis"] = st.selectbox("Kolom Kinerja Akademis:", actual_cols, index=actual_cols.index("Kinerja Akademis") if "Kinerja Akademis" in actual_cols else 0)
# # #                     col_mapping["Beban Belajar"] = st.selectbox("Kolom Beban Belajar:", actual_cols, index=actual_cols.index("Beban Belajar") if "Beban Belajar" in actual_cols else 0)
                
# # #                 st.write("<br>", unsafe_allow_html=True)
                
# # #                 if st.button("Mulai Analisis Deteksi Stres", type="primary", use_container_width=True):
# # #                     if scaler is None or model is None:
# # #                         st.error("Model tidak tersedia.")
# # #                     else:
# # #                         with st.spinner('Menganalisis data menggunakan Ensemble Learning...'):
# # #                             df_numeric_mass = pd.DataFrame()
                            
# # #                             for target_col, excel_col in col_mapping.items():
# # #                                 df_numeric_mass[target_col] = pd.to_numeric(df[excel_col], errors='coerce')
                            
# # #                             df_numeric_mass = df_numeric_mass[EXPECTED_FEATURES]
                            
# # #                             if df_numeric_mass.isnull().values.any():
# # #                                 st.error("Terdapat sel yang kosong atau berisi huruf pada kolom kriteria yang dipilih. Pastikan semua data nilai diisi angka 1-5.")
# # #                             else:
# # #                                 scaled_mass = scaler.transform(df_numeric_mass)
# # #                                 pred_mass = model.predict(scaled_mass)
                                
# # #                                 label_map = {0: "Rendah", 1: "Sedang", 2: "Tinggi"}
# # #                                 df_result = df.copy()
# # #                                 df_result["Prediksi Tingkat Stres"] = pd.Series(pred_mass).map(label_map)
                                
# # #                                 st.success("Proses deteksi selesai!")
                                
# # #                                 st.markdown("##### Preview Hasil Deteksi")
# # #                                 st.dataframe(df_result.head(10), use_container_width=True)
                            
# # #                                 st.markdown("<hr style='border: 1px solid #E2E8F0; margin: 2rem 0;'>", unsafe_allow_html=True)
# # #                                 st.markdown("<h4 style='color: #2D3748;'>Ringkasan Distribusi Kelas</h4>", unsafe_allow_html=True)
                                
# # #                                 counts = df_result["Prediksi Tingkat Stres"].value_counts().reset_index()
# # #                                 counts.columns = ['Status', 'Total']
# # #                                 chart_colors = {"Tinggi": "#E53E3E", "Sedang": "#D69E2E", "Rendah": "#48BB78"}
                                
# # #                                 viz_col1, viz_col2 = st.columns(2)
# # #                                 with viz_col1:
# # #                                     fig_bar = px.bar(counts, x='Status', y='Total', color='Status', color_discrete_map=chart_colors, text_auto=True)
# # #                                     fig_bar.update_layout(showlegend=False, margin=dict(t=20, b=20, l=10, r=10))
# # #                                     st.plotly_chart(fig_bar, use_container_width=True)
                                    
# # #                                 with viz_col2:
# # #                                     fig_pie = px.pie(counts, values='Total', names='Status', color='Status', color_discrete_map=chart_colors, hole=0.5)
# # #                                     fig_pie.update_layout(margin=dict(t=20, b=20, l=10, r=10))
# # #                                     st.plotly_chart(fig_pie, use_container_width=True)
                                
# # #                                 csv = df_result.to_csv(index=False).encode('utf-8')
# # #                                 st.download_button(
# # #                                     label="Simpan Laporan Keseluruhan (.CSV)",
# # #                                     data=csv,
# # #                                     file_name='Hasil_Deteksi_Stres_Siswa.csv',
# # #                                     mime='text/csv',
# # #                                     use_container_width=True
# # #                                 )

# # # # ==========================================
# # # # HALAMAN INFORMASI
# # # # ==========================================
# # # elif menu == "Informasi Sistem":
# # #     render_hero("Mekanisme Machine Learning", "Menjamin tingkat akurasi deteksi melalui evaluasi silang.")
# # #     c1, c2 = st.columns(2)
# # #     with c1:
# # #         with st.container(border=True):
# # #             st.markdown("<h4 style='color: #5A67D8;'>Tahap 1: Base Learner</h4><p style='color: #718096;'>Decision Tree, SVM, dan KNN.</p>", unsafe_allow_html=True)
# # #     with c2:
# # #         with st.container(border=True):
# # #             st.markdown("<h4 style='color: #5A67D8;'>Tahap 2: Meta Learner</h4><p style='color: #718096;'>Logistic Regression menyimpulkan hasil.</p>", unsafe_allow_html=True)





















# # import streamlit as st
# # import pandas as pd
# # import joblib
# # import io
# # import plotly.graph_objects as go
# # import plotly.express as px

# # # 1. KONFIGURASI HALAMAN & HIDE SIDEBAR
# # st.set_page_config(
# #     page_title="MindfulAI - Deteksi Stres Siswa",
# #     layout="wide",
# #     initial_sidebar_state="collapsed", 
# # )

# # # 2. CSS
# # st.markdown("""
# # <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
# #     html, body, [class*="css"] {
# #         font-family: 'Plus Jakarta Sans', sans-serif;
# #     }
    
# #     .stApp { background-color: #FDFCF8; }
    
# #     /* Sembunyikan Sidebar & Header Streamlit secara total */
# #     [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
# #     [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
# #     /* CONTAINER UTAMA */
# #     .block-container {
# #         padding-top: 2rem !important;
# #         padding-left: 5rem !important;
# #         padding-right: 5rem !important;
# #     }

# #     /*  FLOATING PILL NAVBAR (DESKTOP) - ALIGNMENT FIXED */
            
# #     /* Menargetkan row (baris) yang berisi logo navigasi */
# #     [data-testid="stHorizontalBlock"]:has(.nav-logo) {
# #         background-color: #FFFFFF;
# #         border-radius: 50px;
# #         padding: 5px 40px; /* Disesuaikan agar pill tidak terlalu gemuk */
# #         box-shadow: 0 10px 30px rgba(0,0,0,0.06);
# #         max-width: 700px;
# #         margin: 0 auto 2.5rem auto; /* Posisi di tengah */
# #         border: 1px solid #EDF2F7;
# #         position: relative;
# #         z-index: 100;
# #         align-items: center !important; /* MEMAKSA RATA TENGAH VERTIKAL */
# #     }

# #     /* Menghapus margin bawaan H2 agar sejajar sempurna */
# #     .nav-logo {
# #         margin: 0 !important;
# #         padding: 0 !important;
# #         line-height: 1 !important;
# #         display: flex;
# #         align-items: center;
# #         height: 100%;
# #     }

# #     /* Membersihkan wrapper radio button Streamlit */
# #     div.stRadio {
# #         margin: 0 !important;
# #         padding: 0 !important;
# #     }

# #     /* Style Radio Button menyamar jadi Navbar */
# #     div[role="radiogroup"] {
# #         display: flex;
# #         flex-direction: row;
# #         justify-content: flex-end !important; /* MEMAKSA MENU MENTOK KANAN */
# #         align-items: center !important; /* MEMAKSA MENU RATA TENGAH VERTIKAL */
# #         gap: 30px;
# #         border: none !important;
# #         margin: 0 !important;
# #         height: 100%;
# #     }
# #     div[role="radiogroup"] > label {
# #         background: transparent !important;
# #         border: none !important;
# #         padding: 0 !important;
# #     }
# #     div[role="radiogroup"] > label > div:first-child { display: none !important; }
# #     div[role="radiogroup"] > label > div:last-child {
# #         font-weight: 600;
# #         font-size: 1rem;
# #         color: #64748B !important; 
# #         cursor: pointer;
# #         transition: all 0.3s ease;
# #     }
# #     div[role="radiogroup"] > label:hover > div:last-child { color: #434190 !important; }
# #     div[role="radiogroup"] > label[data-checked="true"] > div:last-child {
# #         color: #5A67D8 !important; 
# #         border-bottom: 2px solid #5A67D8;
# #     }

# #     /* =========================================
# #        ELEMENT UI LAINNYA
# #        ========================================= */
# #     .stTabs [data-baseweb="tab-highlight"] { background-color: #5A67D8 !important; }
# #     .stTabs [data-baseweb="tab"] { color: #64748B !important; }
# #     .stTabs [aria-selected="true"] { color: #5A67D8 !important; }

# #     .stSelectbox label, .stSlider label { color: #4A5568 !important; font-weight: 600 !important; }
# #     .stSlider [data-baseweb="slider"] > div > div > div:nth-child(1) { background: #5A67D8 !important; }
# #     .stSlider [data-baseweb="slider"] > div { background: transparent !important; }
# #     .stSlider [data-baseweb="slider"] div[style*="color: rgb(255, 75, 75)"], 
# #     .stSlider [data-baseweb="slider"] div[style*="color: #ff4b4b"] { color: #5A67D8 !important; }
# #     .stSlider [data-baseweb="slider"] [role="slider"] { background-color: #5A67D8 !important; border: 2px solid #5A67D8 !important; }
# #     .stSlider [data-testid="stTickBarItem"] { color: #64748B !important; }

# #     /* =========================================
# #        MEDIA QUERIES (RESPONSIVE UNTUK HP & TABLET)
# #        ========================================= */
# #     @media screen and (max-width: 768px) {
# #         .block-container {
# #             padding-top: 1rem !important;
# #             padding-left: 1rem !important;
# #             padding-right: 1rem !important;
# #         }
        
# #         [data-testid="stHorizontalBlock"]:has(.nav-logo) {
# #             max-width: 95%;
# #             border-radius: 25px;
# #             padding: 15px 20px;
# #             flex-direction: column;
# #             gap: 15px;
# #             margin-bottom: 1.5rem;
# #         }
# #         .nav-logo { text-align: center; justify-content: center; }
        
# #         div[role="radiogroup"] {
# #             justify-content: center !important;
# #             flex-wrap: wrap;
# #             gap: 15px;
# #         }

# #         h1 { font-size: 2.2rem !important; }
# #         .game-card-light div[style*="font-size: 5rem"] { font-size: 3.5rem !important; }
# #         .game-card-light h2 { font-size: 1.5rem !important; }
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # 3. LOAD MODEL & LOGI
# # @st.cache_resource
# # def load_assets():
# #     try:
# #         scaler = joblib.load('scaler.pkl')
# #         model = joblib.load('model_stacking.pkl')
# #         return scaler, model
# #     except: return None, None

# # scaler, model = load_assets()

# # SCALE_MAP = {
# #     "Kualitas Tidur": {"Sangat Buruk": 1, "Buruk": 2, "Cukup": 3, "Baik": 4, "Sangat Baik": 5},
# #     "Sakit Kepala": {"Tidak Pernah": 1, "Jarang": 2, "Kadang-kadang": 3, "Sering": 4, "Sangat Sering": 5},
# #     "Kinerja Akademis": {"Sangat Rendah": 1, "Rendah": 2, "Rata-rata": 3, "Tinggi": 4, "Sangat Tinggi": 5},
# #     "Beban Belajar": {"Sangat Ringan": 1, "Ringan": 2, "Sedang": 3, "Berat": 4, "Sangat Berat": 5},
# #     "Ekstrakurikuler": {"Tidak Aktif": 1, "Kurang Aktif": 2, "Cukup Aktif": 3, "Aktif": 4, "Sangat Aktif": 5}
# # }

# # EXPECTED_FEATURES = ["Kualitas Tidur", "Sakit Kepala", "Kinerja Akademis", "Beban Belajar", "Ekstrakurikuler"]

# # # 4. RENDER NAVBAR ATAS (FLOATING PILL)
# # nav_col1, nav_col2 = st.columns([1, 2])
# # with nav_col1:
# #     st.markdown("<h2 class='nav-logo' style='color: #434190; font-weight: 800;'>MindfulAI.</h2>", unsafe_allow_html=True)
# # with nav_col2:
# #     menu = st.radio("Navigation", ["Home", "Simulator", "Informasi Sistem"], horizontal=True, label_visibility="collapsed")

# # def render_hero(title, subtitle):
# #     st.markdown(f"""
# #     <div style="background-color: #EDF2F7; padding: 4rem 2rem 1rem 2rem; border-radius: 40px 40px 0 0; text-align: center;">
# #         <h1 style="color: #2D3748; font-weight: 800; font-size: 3.5rem; margin-bottom: 1.2rem; line-height: 1.1;">{title}</h1>
# #         <p style="color: #718096; font-size: 1.2rem; max-width: 800px; margin: 0 auto; line-height: 1.6;">{subtitle}</p>
# #     </div>
# #     <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 120" style="display: block; width: 100%; margin-bottom: 2rem;">
# #       <path fill="#EDF2F7" d="M0,64L80,69.3C160,75,320,85,480,80C640,75,800,53,960,48C1120,43,1280,53,1360,58.7L1440,64L1440,0L1360,0C1280,0,1120,0,960,0C800,0,640,0,480,0C320,0,160,0,80,0L0,0Z"></path>
# #     </svg>
# #     """, unsafe_allow_html=True)

# # # HALAMAN HOME
# # if menu == "Home":
# #     render_hero("Helping Your Student Shine Through Life", "Mendeteksi tingkat stres akademik siswa SMA dengan pendekatan cerdas berbasis Machine Learning multi-model.")
    
# #     col1, col2, col3 = st.columns(3)
# #     feats = [
# #         ("Holistic Approach", "Evaluasi kondisi akademis dan fisik siswa secara individual."),
# #         ("Science Research", "Menggunakan pendekatan Stacking Ensemble Learning (DT, SVM, KNN)."),
# #         ("Experienced", "Fasilitas ekstraksi massal untuk tenaga pendidik dalam format Excel.")
# #     ]
# #     for i, (t, d) in enumerate(feats):
# #         with [col1, col2, col3][i]:
# #             with st.container(border=True):
# #                 st.markdown(f"<h4 style='color: #2D3748; text-align:center;'>{t}</h4><p style='color: #718096; text-align:center;'>{d}</p>", unsafe_allow_html=True)

# # # HALAMAN SIMULATOR
# # elif menu == "Simulator":
# #     render_hero("Simulator Keseimbangan Siswa", "Eksplorasi bagaimana beban belajar dan waktu istirahat menentukan tingkat stres.")
    
# #     tab_ind, tab_mass = st.tabs(["Evaluasi Mandiri (Interaktif)", "Impor Data Kelas (Massal)"])

# #     with tab_ind:
# #         st.markdown("""
# #         <style>
# #         .game-card-light { background: #FFFFFF; padding: 20px; border-radius: 15px; border: 3px solid #E2E8F0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; text-align: center;}
# #         .stat-label-light { font-weight: 800; font-size: 13px; text-transform: uppercase; color: #4A5568; margin-bottom: 5px; letter-spacing: 1px;}
# #         .bar-bg-light { background-color: #EDF2F7; border-radius: 8px; height: 28px; width: 100%; border: 2px solid #CBD5E0; overflow: hidden; position: relative; }
# #         .hp-bar { background: linear-gradient(90deg, #48BB78, #38A169); height: 100%; transition: width 0.6s ease; }
# #         .mp-bar { background: linear-gradient(90deg, #4299E1, #3182CE); height: 100%; transition: width 0.6s ease; }
# #         .stress-bar { background: linear-gradient(90deg, #F56565, #E53E3E); height: 100%; transition: width 0.6s ease; }
# #         .bar-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #1A202C; font-weight: 900; font-size: 13px; }
# #         </style>
# #         """, unsafe_allow_html=True)

# #         st.markdown("<div class='game-card-light' style='border-color: #5A67D8;'><h2 style='color: #434190; margin:0; font-weight:900;'>KARAKTER STATUS BUILDER</h2><p style='color: #718096; margin:0;'>Atur atribut aktivitasmu dan lihat dampaknya secara real-time!</p></div>", unsafe_allow_html=True)

# #         col_in1, col_in2 = st.columns(2)
# #         with col_in1:
# #             with st.container(border=True):
# #                 st.markdown("<h4 style='color: #38A169; margin-top:0;'>Atribut Buff (Pemulihan)</h4>", unsafe_allow_html=True)
# #                 v_tidur = st.select_slider("Kualitas Tidur (Regen HP)", options=list(SCALE_MAP["Kualitas Tidur"].keys()), value="Baik")
# #                 v_ekskul = st.select_slider("Aktivitas Ekskul (Stamina)", options=list(SCALE_MAP["Ekstrakurikuler"].keys()), value="Cukup Aktif")
# #                 v_akademis = st.select_slider("Kinerja Akademis (Mana/MP)", options=list(SCALE_MAP["Kinerja Akademis"].keys()), value="Rata-rata")

# #         with col_in2:
# #             with st.container(border=True):
# #                 st.markdown("<h4 style='color: #E53E3E; margin-top:0;'>Atribut Debuff (Beban)</h4>", unsafe_allow_html=True)
# #                 v_beban = st.select_slider("Beban Belajar (Weight)", options=list(SCALE_MAP["Beban Belajar"].keys()), value="Sedang")
# #                 v_kepala = st.select_slider("Keluhan Sakit Kepala (Damage)", options=list(SCALE_MAP["Sakit Kepala"].keys()), value="Jarang")

# #         val_tidur = SCALE_MAP["Kualitas Tidur"][v_tidur]
# #         val_ekskul = SCALE_MAP["Ekstrakurikuler"][v_ekskul]
# #         val_akademis = SCALE_MAP["Kinerja Akademis"][v_akademis]
# #         val_beban = SCALE_MAP["Beban Belajar"][v_beban]
# #         val_kepala = SCALE_MAP["Sakit Kepala"][v_kepala]

# #         hp_pct = int(((val_tidur + val_ekskul) / 10) * 100)
# #         mp_pct = int((val_akademis / 5) * 100)
# #         stress_pct = int(((val_beban + val_kepala) / 10) * 100)

# #         if scaler and model:
# #             input_data = pd.DataFrame([{
# #                 "Kualitas Tidur": val_tidur,
# #                 "Sakit Kepala": val_kepala,
# #                 "Kinerja Akademis": val_akademis,
# #                 "Beban Belajar": val_beban,
# #                 "Ekstrakurikuler": val_ekskul
# #             }])
# #             scaled = scaler.transform(input_data)
# #             pred = model.predict(scaled)[0]
            
# #             hasil_label = {0: "Rendah (Aman)", 1: "Sedang (Waspada)", 2: "Tinggi (Bahaya!)"}[pred]
# #             warna = {"Rendah (Aman)": "#48BB78",  "Sedang (Waspada)": "#D69E2E",  "Tinggi (Bahaya!)": "#E53E3E"}[hasil_label]
# #             emoji_status = {"Rendah (Aman)": "🛡️",  "Sedang (Waspada)": "⚠️",  "Tinggi (Bahaya!)": "☠️"}[hasil_label]

# #             rekomendasi = {
# #                 0: "Kondisi akademis dan psikologismu sangat seimbang! Pertahankan pola tidur yang baik dan terus nikmati kegiatan ekstrakurikulermu.",
# #                 1: "Kamu mulai merasakan tekanan. Coba kurangi sedikit beban belajarmu di akhir pekan dan perbanyak jam tidur untuk *recovery* HP.",
# #                 2: "Peringatan! Tingkat stresmu terlalu tinggi. Segera bicarakan dengan guru BK atau istirahat total dari tugas selama 1-2 hari. Kesehatanmu adalah prioritas utama."
# #             }[pred]

# #             st.markdown("<hr style='border: 2px dashed #E2E8F0; margin: 2rem 0;'>", unsafe_allow_html=True)
            
# #             res_col1, res_col2 = st.columns([1, 1.5], gap="large")
# #             with res_col1:
# #                 st.markdown(f"""
# #                 <div class='game-card-light' style='border-color: {warna}; height: 100%; display: flex; flex-direction: column; justify-content: center;'>
# #                     <p style='color: #718096; font-weight: 800; letter-spacing: 1px; margin-bottom: 5px;'>FINAL STATUS</p>
# #                     <div style='font-size: 5rem; margin: 10px 0;'>{emoji_status}</div>
# #                     <h2 style='color: {warna}; font-weight: 900; margin: 0;'>{hasil_label.upper()}</h2>
# #                 </div>
# #                 """, unsafe_allow_html=True)
                
# #             with res_col2:
# #                 st.markdown(f"""
# #                 <div class='game-card-light' style='height: 100%; text-align:left;'>
# #                     <div class='stat-label-light'>HP (Health - Tidur & Ekskul)</div>
# #                     <div class='bar-bg-light'><div class='hp-bar' style='width: {hp_pct}%;'></div><div class='bar-text'>{hp_pct}/100</div></div>
# #                     <br>
# #                     <div class='stat-label-light'>MP (Mana - Akademis)</div>
# #                     <div class='bar-bg-light'><div class='mp-bar' style='width: {mp_pct}%;'></div><div class='bar-text'>{mp_pct}/100</div></div>
# #                     <br>
# #                     <div class='stat-label-light'>STRESS (Debuff - Beban & Sakit)</div>
# #                     <div class='bar-bg-light'><div class='stress-bar' style='width: {stress_pct}%;'></div><div class='bar-text'>{stress_pct}/100</div></div>
# #                 </div>
# #                 """, unsafe_allow_html=True)
            
# #             st.info(f"**Rekomendasi Sistem:** {rekomendasi}")

# #     with tab_mass:
# #         st.markdown("<h4 style='color: #2D3748; margin-bottom: 1rem;'>Import Data Kelas Massal</h4>", unsafe_allow_html=True)
# #         st.write("Gunakan template di bawah ini. Pastikan data diisi dengan **angka 1 sampai 5** sesuai skala instrumen penelitian.")
        
# #         with st.expander("Buka Panduan Pengisian Skala Angka (1 - 5)"):
# #             st.markdown("""
# #             **Tabel Referensi Pengisian Dataset Excel:**
            
# #             | Kriteria | Angka 1 | Angka 2 | Angka 3 | Angka 4 | Angka 5 |
# #             | :--- | :--- | :--- | :--- | :--- | :--- |
# #             | **Kualitas Tidur** | Sangat Buruk | Buruk | Cukup | Baik | Sangat Baik |
# #             | **Sakit Kepala** | Tidak Pernah | Jarang | Kadang-kadang | Sering | Sangat Sering |
# #             | **Kinerja Akademis** | Sangat Rendah | Rendah | Rata-rata | Tinggi | Sangat Tinggi |
# #             | **Beban Belajar** | Sangat Ringan | Ringan | Sedang | Berat | Sangat Berat |
# #             | **Ekstrakurikuler**| Tidak Aktif | Kurang Aktif | Cukup Aktif | Aktif | Sangat Aktif |
            
# #             *Catatan: Kolom Nama Siswa bebas diisi teks (nama, inisial, atau NIS).*
# #             """)
        
# #         template_data = {
# #             "Nama Siswa": ["Siswa A", "Siswa B", "Siswa C"],
# #             "Kualitas Tidur": [5, 2, 3],
# #             "Sakit Kepala": [2, 4, 3],
# #             "Kinerja Akademis": [4, 1, 3],
# #             "Beban Belajar": [3, 5, 4],
# #             "Ekstrakurikuler": [4, 1, 3]
# #         }
# #         towrite = io.BytesIO()
# #         pd.DataFrame(template_data).to_excel(towrite, index=False, header=True)
# #         towrite.seek(0)
        
# #         st.download_button(
# #             label="Unduh Format Template Excel (Skala 1-5)",
# #             data=towrite,
# #             file_name="Template_Dataset_Numerik.xlsx",
# #             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
# #         )
        
# #         st.write("<br>", unsafe_allow_html=True)
# #         uploaded_file = st.file_uploader("Upload file dataset (Excel/CSV)", type=['csv', 'xlsx'])
        
# #         @st.cache_data(show_spinner=False)
# #         def fast_load_file(file):
# #             if file.name.endswith('.csv'): return pd.read_csv(file)
# #             return pd.read_excel(file)

# #         if uploaded_file is not None:
# #             df = fast_load_file(uploaded_file)
            
# #             st.markdown("##### Preview Data Mentah (Belum Diproses)")
# #             st.dataframe(df.head(5), use_container_width=True)
            
# #             with st.container(border=True):
# #                 st.markdown("<p style='font-weight:700; color:#2C5282;'>Pemetaan Kolom (Pastikan kolom sesuai)</p>", unsafe_allow_html=True)
# #                 col_mapping = {}
# #                 actual_cols = list(df.columns)
                
# #                 c_map1, c_map2 = st.columns(2)
# #                 with c_map1:
# #                     col_mapping["Kualitas Tidur"] = st.selectbox("Kolom Data Tidur:", actual_cols, index=actual_cols.index("Kualitas Tidur") if "Kualitas Tidur" in actual_cols else 0)
# #                     col_mapping["Sakit Kepala"] = st.selectbox("Kolom Sakit Kepala:", actual_cols, index=actual_cols.index("Sakit Kepala") if "Sakit Kepala" in actual_cols else 0)
# #                     col_mapping["Ekstrakurikuler"] = st.selectbox("Kolom Ekstrakurikuler:", actual_cols, index=actual_cols.index("Ekstrakurikuler") if "Ekstrakurikuler" in actual_cols else 0)
# #                 with c_map2:
# #                     col_mapping["Kinerja Akademis"] = st.selectbox("Kolom Kinerja Akademis:", actual_cols, index=actual_cols.index("Kinerja Akademis") if "Kinerja Akademis" in actual_cols else 0)
# #                     col_mapping["Beban Belajar"] = st.selectbox("Kolom Beban Belajar:", actual_cols, index=actual_cols.index("Beban Belajar") if "Beban Belajar" in actual_cols else 0)
                
# #                 st.write("<br>", unsafe_allow_html=True)
                
# #                 if st.button("Mulai Analisis Deteksi Stres", type="primary", use_container_width=True):
# #                     if scaler is None or model is None:
# #                         st.error("Model tidak tersedia.")
# #                     else:
# #                         with st.spinner('Menganalisis data menggunakan Ensemble Learning...'):
# #                             df_numeric_mass = pd.DataFrame()
                            
# #                             for target_col, excel_col in col_mapping.items():
# #                                 df_numeric_mass[target_col] = pd.to_numeric(df[excel_col], errors='coerce')
                            
# #                             df_numeric_mass = df_numeric_mass[EXPECTED_FEATURES]
                            
# #                             if df_numeric_mass.isnull().values.any():
# #                                 st.error("Terdapat sel yang kosong atau berisi huruf pada kolom kriteria yang dipilih. Pastikan semua data nilai diisi angka 1-5.")
# #                             else:
# #                                 scaled_mass = scaler.transform(df_numeric_mass)
# #                                 pred_mass = model.predict(scaled_mass)
                                
# #                                 label_map = {0: "Rendah", 1: "Sedang", 2: "Tinggi"}
# #                                 df_result = df.copy()
# #                                 df_result["Prediksi Tingkat Stres"] = pd.Series(pred_mass).map(label_map)
                                
# #                                 st.success("Proses deteksi selesai!")
                                
# #                                 st.markdown("##### Preview Hasil Deteksi")
# #                                 st.dataframe(df_result.head(10), use_container_width=True)
                            
# #                                 st.markdown("<hr style='border: 1px solid #E2E8F0; margin: 2rem 0;'>", unsafe_allow_html=True)
# #                                 st.markdown("<h4 style='color: #2D3748;'>Ringkasan Distribusi Kelas</h4>", unsafe_allow_html=True)
                                
# #                                 counts = df_result["Prediksi Tingkat Stres"].value_counts().reset_index()
# #                                 counts.columns = ['Status', 'Total']
# #                                 chart_colors = {"Tinggi": "#E53E3E", "Sedang": "#D69E2E", "Rendah": "#48BB78"}
                                
# #                                 viz_col1, viz_col2 = st.columns(2)
# #                                 with viz_col1:
# #                                     fig_bar = px.bar(counts, x='Status', y='Total', color='Status', color_discrete_map=chart_colors, text_auto=True)
# #                                     fig_bar.update_layout(showlegend=False, margin=dict(t=20, b=20, l=10, r=10))
# #                                     st.plotly_chart(fig_bar, use_container_width=True)
                                    
# #                                 with viz_col2:
# #                                     fig_pie = px.pie(counts, values='Total', names='Status', color='Status', color_discrete_map=chart_colors, hole=0.5)
# #                                     fig_pie.update_layout(margin=dict(t=20, b=20, l=10, r=10))
# #                                     st.plotly_chart(fig_pie, use_container_width=True)
                                
# #                                 csv = df_result.to_csv(index=False).encode('utf-8')
# #                                 st.download_button(
# #                                     label="Simpan Laporan Keseluruhan (.CSV)",
# #                                     data=csv,
# #                                     file_name='Hasil_Deteksi_Stres_Siswa.csv',
# #                                     mime='text/csv',
# #                                     use_container_width=True
# #                                 )

# # # HALAMAN INFORMASI
# # elif menu == "Informasi Sistem":
# #     render_hero("Mekanisme Machine Learning", "Menjamin tingkat akurasi deteksi melalui evaluasi silang.")
# #     c1, c2 = st.columns(2)
# #     with c1:
# #         with st.container(border=True):
# #             st.markdown("<h4 style='color: #5A67D8;'>Tahap 1: Base Learner</h4><p style='color: #718096;'>Decision Tree, SVM, dan KNN.</p>", unsafe_allow_html=True)
# #     with c2:
# #         with st.container(border=True):
# #             st.markdown("<h4 style='color: #5A67D8;'>Tahap 2: Meta Learner</h4><p style='color: #718096;'>Logistic Regression menyimpulkan hasil.</p>", unsafe_allow_html=True)



# import streamlit as st
# import pandas as pd
# import joblib
# import io
# import plotly.express as px

# # ==========================================
# # 1. KONFIGURASI HALAMAN & CSS
# # ==========================================
# st.set_page_config(
#     page_title="MindfulAI - Deteksi Stres Siswa",
#     layout="wide",
#     initial_sidebar_state="collapsed", 
# )

# st.markdown("""
# <style>
#     /* Mengurangi jarak kosong di atas */
#     .block-container { padding-top: 1.5rem !important; }

#     /* --- HERO BANNER HOME --- */
#     .hero-banner {
#         background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);
#         padding: 4rem 2rem;
#         border-radius: 24px;
#         text-align: center;
#         margin-bottom: 3rem;
#         box-shadow: 0 10px 30px rgba(67, 65, 144, 0.05);
#         border: 1px solid #C7D2FE;
#     }
#     .hero-title { color: #312E81; font-size: 3rem; font-weight: 900; margin-bottom: 1rem; line-height: 1.2; }
#     .hero-subtitle { color: #4F46E5; font-size: 1.2rem; font-weight: 500; max-width: 800px; margin: 0 auto; }

#     /* --- FEATURE CARDS HOME --- */
#     .feature-box {
#         background: white; padding: 25px 20px; border-radius: 16px;
#         text-align: center; border: 1px solid #E2E8F0;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.02); height: 100%;
#         transition: transform 0.3s ease;
#     }
#     .feature-box:hover { transform: translateY(-5px); border-color: #A5B4FC; }
#     .feature-title { color: #434190; margin-top: 15px; font-weight: 800; font-size: 18px; }
#     .feature-desc { color: #718096; font-size: 14px; margin-top: 10px; line-height: 1.5; }

#     /* --- ROLE CARD (GATEWAY) --- */
#     .role-header { color: #434190; font-weight: 800; font-size: 22px; margin-top: 20px; margin-bottom: 10px;}
#     .role-desc { color: #718096; font-size: 15px; margin-bottom: 25px;}

#     /* Typography & Umum */
#     .section-header { color: #434190; font-weight: 800; font-size: 20px; border-bottom: 2px solid #EDF2F7; padding-bottom: 10px; margin-bottom: 20px; }

#     /* Override Button Streamlit agar senada */
#     .stButton>button[kind="primary"] { background-color: #434190; border-color: #434190; padding: 20px; border-radius: 12px; font-weight: bold;}
#     .stButton>button[kind="primary"]:hover { background-color: #312E81; border-color: #312E81; }
#     .stButton>button[kind="secondary"] { padding: 20px; border-radius: 12px; font-weight: bold; border: 2px solid #E2E8F0; color: #434190; }
#     .stButton>button[kind="secondary"]:hover { border-color: #434190; color: #434190; background-color: #F8FAFC;}

#     /* CSS Custom untuk Student Mode (RPG Bar) */
#     .status-card {
#         border-radius: 12px; padding: 30px 20px; text-align: center;
#         background-color: white; height: 100%; display: flex;
#         flex-direction: column; justify-content: center; align-items: center;
#         border-width: 3px; border-style: solid; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
#     }
#     .status-title { color: #718096; font-weight: 800; font-size: 14px; letter-spacing: 1.5px; margin-bottom: 20px; }
#     .status-text { font-weight: 900; font-size: 30px; margin-top: 20px; }
    
#     .bars-card {
#         border: 2px solid #E2E8F0; border-radius: 12px; padding: 25px 30px;
#         background-color: white; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
#     }
#     .bar-label { font-weight: 800; font-size: 12px; color: #434190; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
#     .bar-bg { background-color: #EDF2F7; border: 1px solid #CBD5E0; border-radius: 6px; width: 100%; height: 28px; position: relative; margin-bottom: 25px; }
#     .bar-fill-hp { background-color: #48BB78; height: 100%; border-radius: 5px 0 0 5px; transition: width 0.5s; }
#     .bar-fill-mp { background-color: #3182CE; height: 100%; border-radius: 5px 0 0 5px; transition: width 0.5s; }
#     .bar-fill-stress { background-color: #E53E3E; height: 100%; border-radius: 5px 0 0 5px; transition: width 0.5s; }
#     .bar-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-weight: 900; font-size: 12px; color: #1A202C; }
# </style>
# """, unsafe_allow_html=True)

# # ==========================================
# # 2. LOAD MODEL
# # ==========================================
# @st.cache_resource
# def load_assets():
#     try:
#         scaler = joblib.load('scaler.pkl')
#         model = joblib.load('model_stacking.pkl')
#         return scaler, model
#     except: return None, None

# scaler, model = load_assets()
# EXPECTED_FEATURES = ["Kualitas Tidur", "Sakit Kepala", "Kinerja Akademis", "Beban Belajar", "Ekstrakurikuler"]

# # ==========================================
# # 3. STATE MANAGEMENT & NAVBAR
# # ==========================================
# if 'page' not in st.session_state:
#     st.session_state.page = 'home'

# # Navbar Atas
# nav1, nav2, nav3, nav4 = st.columns([4, 1, 1, 0.1])
# with nav1:
#     st.markdown("<h2 style='color: #434190; margin-top:0; font-weight: 900;'>MindfulAI.</h2>", unsafe_allow_html=True)
# with nav2:
#     if st.button("Home", use_container_width=True):
#         st.session_state.page = 'home'
#         st.rerun()
# with nav3:
#     if st.button("Tentang Sistem", use_container_width=True):
#         st.session_state.page = 'tentang'
#         st.rerun()

# st.markdown("<hr style='margin-top: 0px; margin-bottom: 30px; border-color: #EDF2F7;'>", unsafe_allow_html=True)

# # ==========================================
# # 4. HALAMAN UTAMA (HOME)
# # ==========================================
# if st.session_state.page == 'home':
#     # HERO BANNER
#     st.markdown("""
#     <div class="hero-banner">
#         <div class="hero-title">Helping Your Student Shine Through Life</div>
#         <div class="hero-subtitle">Mendeteksi tingkat stres akademik siswa SMA dengan pendekatan cerdas berbasis Machine Learning multi-model.</div>
#     </div>
#     """, unsafe_allow_html=True)

#     # PILIHAN AKSES (GATEWAY)
#     st.markdown("<h3 style='text-align: center; color: #434190; margin-bottom: 30px; font-weight:800;'>Pilih Jalur Akses Anda</h3>", unsafe_allow_html=True)
    
#     col_siswa, col_guru = st.columns(2, gap="large")
    
#     with col_siswa:
#         with st.container(border=True):
#             st.markdown("""
#             <div style="text-align: center; padding: 10px;">
#                 <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
#                 <div class="role-header">Mode Siswa</div>
#                 <div class="role-desc">Evaluasi kondisi akademis dan fisikmu secara mandiri dengan antarmuka simulasi interaktif.</div>
#             </div>
#             """, unsafe_allow_html=True)
#             if st.button("Masuk Sebagai Siswa", use_container_width=True, type="primary"):
#                 st.session_state.page = 'siswa'
#                 st.rerun()

#     with col_guru:
#         with st.container(border=True):
#             st.markdown("""
#             <div style="text-align: center; padding: 10px;">
#                 <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
#                 <div class="role-header">Mode Konselor</div>
#                 <div class="role-desc">Fasilitas ekstraksi massal untuk tenaga pendidik dalam format dataset dan visualisasi grafik.</div>
#             </div>
#             """, unsafe_allow_html=True)
#             if st.button("Masuk Sebagai Konselor", use_container_width=True):
#                 st.session_state.page = 'konselor'
#                 st.rerun()

#     st.markdown("<br><br>", unsafe_allow_html=True)

#     # KARTU FITUR BAWAH
#     f1, f2, f3 = st.columns(3)
#     with f1:
#         st.markdown("""
#         <div class="feature-box">
#             <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#434190" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
#             <div class="feature-title">Holistic Approach</div>
#             <div class="feature-desc">Mengevaluasi secara seimbang antara keluhan fisik dan tekanan akademis siswa secara individual.</div>
#         </div>
#         """, unsafe_allow_html=True)
#     with f2:
#         st.markdown("""
#         <div class="feature-box">
#             <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#434190" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
#             <div class="feature-title">Science Research</div>
#             <div class="feature-desc">Menggunakan model Machine Learning teruji yaitu Stacking Ensemble (DT, SVM, KNN).</div>
#         </div>
#         """, unsafe_allow_html=True)
#     with f3:
#         st.markdown("""
#         <div class="feature-box">
#             <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#434190" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
#             <div class="feature-title">Experienced Tools</div>
#             <div class="feature-desc">Memiliki alat impor massal berbasis spreadsheet yang didesain khusus untuk tenaga pendidik.</div>
#         </div>
#         """, unsafe_allow_html=True)

# # ==========================================
# # 5. HALAMAN SISWA (INTERAKTIF RPG)
# # ==========================================
# elif st.session_state.page == 'siswa':
#     st.markdown("<h2 style='color: #434190; font-weight:800;'>Simulator Keseimbangan Siswa</h2>", unsafe_allow_html=True)
#     st.markdown("<p style='color: #718096;'>Eksplorasi bagaimana beban belajar dan waktu istirahat menentukan tingkat stresmu.</p>", unsafe_allow_html=True)
#     st.write("<br>", unsafe_allow_html=True)
    
#     # --- SLIDER INPUT ---
#     col_buff, col_debuff = st.columns(2, gap="large")
    
#     with col_buff:
#         st.markdown("<div class='section-header'>Atribut Pemulihan (Buff)</div>", unsafe_allow_html=True)
#         v_tidur = st.select_slider("Kualitas Tidur (Regenerasi HP)", 
#                                    options=["Sangat Buruk", "Buruk", "Cukup", "Baik", "Sangat Baik"], value="Baik")
#         v_ekskul = st.select_slider("Aktivitas Ekskul (Stamina)", 
#                                     options=["Tidak Aktif", "Kurang Aktif", "Cukup Aktif", "Aktif", "Sangat Aktif"], value="Cukup Aktif")
#         v_akademis = st.select_slider("Kinerja Akademis (Mana/MP)", 
#                                       options=["Sangat Rendah", "Rendah", "Rata-rata", "Tinggi", "Sangat Tinggi"], value="Rata-rata")
        
#     with col_debuff:
#         st.markdown("<div class='section-header'>Atribut Beban (Debuff)</div>", unsafe_allow_html=True)
#         v_beban = st.select_slider("Beban Belajar (Weight)", 
#                                    options=["Sangat Ringan", "Ringan", "Sedang", "Berat", "Sangat Berat"], value="Sedang")
#         v_kepala = st.select_slider("Keluhan Sakit Kepala (Damage)", 
#                                     options=["Tidak Pernah", "Jarang", "Kadang-kadang", "Sering", "Sangat Sering"], value="Jarang")

#     st.markdown("<hr style='border: 1px dashed #CBD5E0; margin: 30px 0;'>", unsafe_allow_html=True)

#     # --- LOGIKA KLASIFIKASI & BAR ---
#     val_map = {
#         "Sangat Buruk": 1, "Buruk": 2, "Cukup": 3, "Baik": 4, "Sangat Baik": 5,
#         "Tidak Aktif": 1, "Kurang Aktif": 2, "Cukup Aktif": 3, "Aktif": 4, "Sangat Aktif": 5,
#         "Sangat Rendah": 1, "Rendah": 2, "Rata-rata": 3, "Tinggi": 4, "Sangat Tinggi": 5,
#         "Sangat Ringan": 1, "Ringan": 2, "Sedang": 3, "Berat": 4, "Sangat Berat": 5,
#         "Tidak Pernah": 1, "Jarang": 2, "Kadang-kadang": 3, "Sering": 4, "Sangat Sering": 5
#     }
    
#     hp_pct = int(((val_map[v_tidur] + val_map[v_ekskul]) / 10) * 100)
#     mp_pct = int((val_map[v_akademis] / 5) * 100)
#     stress_pct = int(((val_map[v_beban] + val_map[v_kepala]) / 10) * 100)
    
#     if stress_pct <= 40:
#         status_text = "RENDAH (AMAN)"
#         status_color = "#38A169" # Hijau Aman
#         icon_url = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Check_green_icon.svg"
#     elif stress_pct <= 70:
#         status_text = "SEDANG (WASPADA)"
#         status_color = "#D69E2E" # Kuning Waspada
#         icon_url = "https://upload.wikimedia.org/wikipedia/commons/4/41/Symbol_warning_yellow.svg"
#     else:
#         status_text = "TINGGI (BAHAYA)"
#         status_color = "#E53E3E" # Merah Bahaya
#         icon_url = "https://upload.wikimedia.org/wikipedia/commons/c/c3/Cross_red_circle.svg"

#     # --- UI RENDER ---
#     c_status, c_bars = st.columns([1, 1.5], gap="large")
#     with c_status:
#         st.markdown(f"""<div class="status-card" style="border-color: {status_color};"><div class="status-title">FINAL STATUS</div><img src="{icon_url}" width="110" style="margin: 10px 0;"><div class="status-text" style="color: {status_color};">{status_text}</div></div>""", unsafe_allow_html=True)
#     with c_bars:
#         st.markdown(f"""<div class="bars-card"><div class="bar-label">HP (HEALTH - TIDUR & EKSKUL)</div><div class="bar-bg"><div class="bar-fill-hp" style="width: {hp_pct}%;"></div><div class="bar-text">{hp_pct}/100</div></div><div class="bar-label">MP (MANA - AKADEMIS)</div><div class="bar-bg"><div class="bar-fill-mp" style="width: {mp_pct}%;"></div><div class="bar-text">{mp_pct}/100</div></div><div class="bar-label">STRESS (DEBUFF - BEBAN & SAKIT)</div><div class="bar-bg"><div class="bar-fill-stress" style="width: {stress_pct}%;"></div><div class="bar-text">{stress_pct}/100</div></div></div>""", unsafe_allow_html=True)

# # ==========================================
# # 6. HALAMAN KONSELOR (MASS IMPORT)
# # ==========================================
# elif st.session_state.page == 'konselor':
#     st.markdown("<h2 style='color: #434190; font-weight:800;'>Dashboard Analisis Massal</h2>", unsafe_allow_html=True)
#     st.markdown("<p style='color: #718096;'>Gunakan fitur ini untuk memproses dataset kelas dalam format Excel atau CSV.</p>", unsafe_allow_html=True)
#     st.write("<br>", unsafe_allow_html=True)
    
#     with st.expander("Lihat Panduan Pengisian Skala Angka (1 - 5)"):
#         st.markdown("""
#         **Tabel Referensi Pengisian Dataset Excel:**
#         | Kriteria | Angka 1 | Angka 2 | Angka 3 | Angka 4 | Angka 5 |
#         | :--- | :--- | :--- | :--- | :--- | :--- |
#         | **Kualitas Tidur** | Sangat Buruk | Buruk | Cukup | Baik | Sangat Baik |
#         | **Sakit Kepala** | Tidak Pernah | Jarang | Kadang-kadang | Sering | Sangat Sering |
#         | **Kinerja Akademis** | Sangat Rendah | Rendah | Rata-rata | Tinggi | Sangat Tinggi |
#         | **Beban Belajar** | Sangat Ringan | Ringan | Sedang | Berat | Sangat Berat |
#         | **Ekstrakurikuler**| Tidak Aktif | Kurang Aktif | Cukup Aktif | Aktif | Sangat Aktif |
#         """)
    
#     template_data = {
#         "Nama Siswa": ["Siswa A", "Siswa B", "Siswa C"],
#         "Kualitas Tidur": [5, 2, 3],
#         "Sakit Kepala": [2, 4, 3],
#         "Kinerja Akademis": [4, 1, 3],
#         "Beban Belajar": [3, 5, 4],
#         "Ekstrakurikuler": [4, 1, 3]
#     }
#     towrite = io.BytesIO()
#     pd.DataFrame(template_data).to_excel(towrite, index=False, header=True)
#     towrite.seek(0)
    
#     st.download_button(
#         label="Unduh Format Template Excel",
#         data=towrite,
#         file_name="Template_Dataset_Numerik.xlsx",
#         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     )
    
#     st.write("<br>", unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("Upload file dataset (Excel/CSV)", type=['csv', 'xlsx'])
    
#     @st.cache_data(show_spinner=False)
#     def fast_load_file(file):
#         if file.name.endswith('.csv'): return pd.read_csv(file)
#         return pd.read_excel(file)

#     if uploaded_file is not None:
#         df = fast_load_file(uploaded_file)
        
#         st.markdown("<div class='section-header' style='font-size:18px;'>Preview Data Mentah (Belum Diproses)</div>", unsafe_allow_html=True)
#         st.dataframe(df.head(5), use_container_width=True)
        
#         with st.container(border=True):
#             st.markdown("<p style='font-weight:700; color:#434190;'>Pemetaan Kolom Kriteria</p>", unsafe_allow_html=True)
#             col_mapping = {}
#             actual_cols = list(df.columns)
            
#             c_map1, c_map2 = st.columns(2)
#             with c_map1:
#                 col_mapping["Kualitas Tidur"] = st.selectbox("Kolom Data Tidur:", actual_cols, index=actual_cols.index("Kualitas Tidur") if "Kualitas Tidur" in actual_cols else 0)
#                 col_mapping["Sakit Kepala"] = st.selectbox("Kolom Sakit Kepala:", actual_cols, index=actual_cols.index("Sakit Kepala") if "Sakit Kepala" in actual_cols else 0)
#                 col_mapping["Ekstrakurikuler"] = st.selectbox("Kolom Ekstrakurikuler:", actual_cols, index=actual_cols.index("Ekstrakurikuler") if "Ekstrakurikuler" in actual_cols else 0)
#             with c_map2:
#                 col_mapping["Kinerja Akademis"] = st.selectbox("Kolom Kinerja Akademis:", actual_cols, index=actual_cols.index("Kinerja Akademis") if "Kinerja Akademis" in actual_cols else 0)
#                 col_mapping["Beban Belajar"] = st.selectbox("Kolom Beban Belajar:", actual_cols, index=actual_cols.index("Beban Belajar") if "Beban Belajar" in actual_cols else 0)
            
#             st.write("<br>", unsafe_allow_html=True)
            
#             if st.button("Mulai Analisis Deteksi Stres", type="primary", use_container_width=True):
#                 with st.spinner('Menganalisis jutaan kemungkinan data...'):
#                     df_numeric_mass = pd.DataFrame()
#                     for target_col, excel_col in col_mapping.items():
#                         df_numeric_mass[target_col] = pd.to_numeric(df[excel_col], errors='coerce')
                    
#                     df_numeric_mass = df_numeric_mass[EXPECTED_FEATURES]
                    
#                     if df_numeric_mass.isnull().values.any():
#                         st.error("Terdapat sel kosong atau huruf pada kolom kriteria. Pastikan semua diisi angka 1-5.")
#                     else:
#                         if scaler and model:
#                             scaled_mass = scaler.transform(df_numeric_mass)
#                             pred_mass = model.predict(scaled_mass)
#                         else:
#                             # Fallback Dummy (Logika sederhana pengganti ML jika file .pkl tidak ada)
#                             pred_mass = []
#                             for row in df_numeric_mass.values:
#                                 stress_score = row[1] + row[3] # Beban + Sakit Kepala
#                                 if stress_score <= 4: pred_mass.append(0)
#                                 elif stress_score <= 7: pred_mass.append(1)
#                                 else: pred_mass.append(2)

#                         label_map = {0: "Rendah", 1: "Sedang", 2: "Tinggi"}
#                         df_result = df.copy()
#                         df_result["Prediksi Tingkat Stres"] = pd.Series(pred_mass).map(label_map)
                        
#                         st.success("Proses deteksi selesai!")
                        
#                         st.markdown("<div class='section-header' style='font-size:18px;'>Preview Hasil Deteksi</div>", unsafe_allow_html=True)
#                         st.dataframe(df_result.head(10), use_container_width=True)
                        
#                         st.markdown("<h4 style='color: #434190; margin-top:30px; font-weight: 800;'>Ringkasan Distribusi Kelas</h4>", unsafe_allow_html=True)
                        
#                         counts = df_result["Prediksi Tingkat Stres"].value_counts().reset_index()
#                         counts.columns = ['Status', 'Total']
#                         chart_colors = {"Tinggi": "#E53E3E", "Sedang": "#D69E2E", "Rendah": "#38A169"}
                        
#                         viz_col1, viz_col2 = st.columns(2)
#                         with viz_col1:
#                             fig_bar = px.bar(counts, x='Status', y='Total', color='Status', color_discrete_map=chart_colors, text_auto=True)
#                             fig_bar.update_layout(showlegend=False, margin=dict(t=20, b=20, l=10, r=10), plot_bgcolor='rgba(0,0,0,0)')
#                             st.plotly_chart(fig_bar, use_container_width=True)
#                         with viz_col2:
#                             fig_pie = px.pie(counts, values='Total', names='Status', color='Status', color_discrete_map=chart_colors, hole=0.5)
#                             fig_pie.update_layout(margin=dict(t=20, b=20, l=10, r=10))
#                             st.plotly_chart(fig_pie, use_container_width=True)
                        
#                         csv = df_result.to_csv(index=False).encode('utf-8')
#                         st.download_button(
#                             label="Simpan Laporan (.CSV)",
#                             data=csv,
#                             file_name='Hasil_Deteksi_Stres_Siswa.csv',
#                             mime='text/csv',
#                             use_container_width=True
#                         )

# # ==========================================
# # 7. HALAMAN TENTANG SISTEM
# # ==========================================
# elif st.session_state.page == 'tentang':
#     st.markdown("<h2 style='color: #434190; margin-bottom: 20px; font-weight:800;'>Bagaimana MindfulAI Bekerja?</h2>", unsafe_allow_html=True)
#     st.write("Sistem ini menggunakan algoritma canggih bernama **Stacking Ensemble Learning**. Agar mudah dipahami, bayangkan algoritma ini seperti sebuah **Tim Dokter Rumah Sakit** yang sedang memeriksa kesehatan siswa.")
    
#     st.markdown("<div class='section-header' style='margin-top: 30px;'>Tahap 1: Analisis Dokter Spesialis (Base Learner)</div>", unsafe_allow_html=True)
#     st.write("Ketika data siswa masuk, data tersebut tidak hanya diperiksa oleh satu orang, melainkan oleh tiga dokter spesialis sekaligus. Masing-masing memiliki keahlian berbeda:")
    
#     c1, c2, c3 = st.columns(3)
#     with c1:
#         with st.container(border=True):
#             st.markdown("""
#             <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#434190" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
#             <h4 style='color: #434190; margin-top: 10px;'>Decision Tree</h4>
#             """, unsafe_allow_html=True)
#             st.write("Ibarat dokter umum yang menganalisis dengan runtutan pertanyaan logis. Ia melihat pola: 'Jika tidur kurang dan beban berat, maka risikonya tinggi'.")
#     with c2:
#         with st.container(border=True):
#             st.markdown("""
#             <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#434190" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"></path><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
#             <h4 style='color: #434190; margin-top: 10px;'>Support Vector Machine</h4>
#             """, unsafe_allow_html=True)
#             st.write("Ibarat dokter bedah yang menarik batas tegas. Ia sangat pintar mencari garis batas pemisah antara siswa yang masih aman dan yang sudah terindikasi stres.")
#     with c3:
#         with st.container(border=True):
#             st.markdown("""
#             <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#434190" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>
#             <h4 style='color: #434190; margin-top: 10px;'>K-Nearest Neighbor</h4>
#             """, unsafe_allow_html=True)
#             st.write("Ibarat dokter yang melihat riwayat pasien masa lalu. Ia mendiagnosis dengan cara mencari kemiripan data siswa tersebut dengan kasus-kasus siswa sebelumnya.")

#     st.markdown("<div class='section-header' style='margin-top: 40px;'>Tahap 2: Keputusan Final (Meta Learner)</div>", unsafe_allow_html=True)
#     with st.container(border=True):
#         st.markdown("<h4 style='color: #38A169;'>Direktur Rumah Sakit (Logistic Regression)</h4>", unsafe_allow_html=True)
#         st.write("Setelah ketiga dokter spesialis di atas memberikan hasil diagnosis masing-masing, kadang hasilnya bisa berbeda (misal: Decision Tree bilang Tinggi, tapi KNN bilang Sedang).")
#         st.write("Di sinilah **Meta Learner (Logistic Regression)** bertugas. Sebagai Direktur Rumah Sakit, ia mendengarkan pendapat ketiga dokter tersebut, mengevaluasi model mana yang paling bisa dipercaya untuk kasus tertentu, dan menjatuhkan **Satu Keputusan Final** (Rendah, Sedang, atau Tinggi) yang paling akurat.")



import streamlit as st
import pandas as pd
import joblib
import io
import plotly.express as px

# ==========================================
# 1. KONFIGURASI HALAMAN & CSS
# ==========================================
st.set_page_config(
    page_title="MindfulAI - Deteksi Stres Siswa",
    layout="wide",
    initial_sidebar_state="collapsed", 
)

st.markdown("""
<style>
    /* Mengurangi jarak kosong di atas */
    .block-container { padding-top: 1rem !important; }

    /* =========================================
       HERO SECTION (BERANDA BAWAH NAVBAR)
       ========================================= */
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

    /* =========================================
       TRIK CSS: MENGUBAH TOMBOL JADI KARTU RAKSASA
       ========================================= */
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

    /* =========================================
       CSS LAINNYA (Siswa & Konselor)
       ========================================= */
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

# ==========================================
# 2. LOAD MODEL
# ==========================================
@st.cache_resource
def load_assets():
    try:
        scaler = joblib.load('scaler.pkl')
        model = joblib.load('model_stacking.pkl')
        return scaler, model
    except: return None, None

scaler, model = load_assets()
EXPECTED_FEATURES = ["Kualitas Tidur", "Sakit Kepala", "Kinerja Akademis", "Beban Belajar", "Ekstrakurikuler"]

# ==========================================
# 3. STATE MANAGEMENT & NAVBAR
# ==========================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Navbar Atas
nav1, nav2, nav3, nav4 = st.columns([4, 1, 1, 0.1])
with nav1:
    st.markdown("<h2 style='color: #434190; margin-top:0;'>MindfulAI.</h2>", unsafe_allow_html=True)
with nav2:
    if st.button("Home", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
with nav3:
    if st.button("Tentang Sistem", use_container_width=True):
        st.session_state.page = 'tentang'
        st.rerun()

st.markdown("<hr style='margin-top: 0px; margin-bottom: 30px; border-color: #EDF2F7;'>", unsafe_allow_html=True)

# ==========================================
# 4. HALAMAN UTAMA (HOME)
# ==========================================
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

# ==========================================
# 5. HALAMAN SISWA (INTERAKTIF RPG)
# ==========================================
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
        icon_url = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Check_green_icon.svg"
    elif stress_pct <= 70:
        status_text = "SEDANG (WASPADA)"
        status_color = "#D69E2E" # Kuning Waspada
        icon_url = "https://upload.wikimedia.org/wikipedia/commons/4/41/Symbol_warning_yellow.svg"
    else:
        status_text = "TINGGI (BAHAYA)"
        status_color = "#E53E3E" # Merah Bahaya
        icon_url = "https://upload.wikimedia.org/wikipedia/commons/c/c3/Cross_red_circle.svg"

    # --- UI RENDER ---
    c_status, c_bars = st.columns([1, 1.5], gap="large")
    with c_status:
        st.markdown(f"""<div class="status-card" style="border-color: {status_color};"><div class="status-title">FINAL STATUS</div><img src="{icon_url}" width="110" style="margin: 10px 0;"><div class="status-text" style="color: {status_color};">{status_text}</div></div>""", unsafe_allow_html=True)
    with c_bars:
        st.markdown(f"""<div class="bars-card"><div class="bar-label">HP (HEALTH - TIDUR & EKSKUL)</div><div class="bar-bg"><div class="bar-fill-hp" style="width: {hp_pct}%;"></div><div class="bar-text">{hp_pct}/100</div></div><div class="bar-label">MP (MANA - AKADEMIS)</div><div class="bar-bg"><div class="bar-fill-mp" style="width: {mp_pct}%;"></div><div class="bar-text">{mp_pct}/100</div></div><div class="bar-label">STRESS (DEBUFF - BEBAN & SAKIT)</div><div class="bar-bg"><div class="bar-fill-stress" style="width: {stress_pct}%;"></div><div class="bar-text">{stress_pct}/100</div></div></div>""", unsafe_allow_html=True)

# ==========================================
# 6. HALAMAN KONSELOR (MASS IMPORT)
# ==========================================
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

# ==========================================
# 7. HALAMAN TENTANG SISTEM
# ==========================================
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
        st.markdown("<h4 style='color: #38A169;'>Direktur Rumah Sakit (Logistic Regression)</h4>", unsafe_allow_html=True)
        st.write("Setelah ketiga dokter spesialis di atas memberikan hasil diagnosis masing-masing, kadang hasilnya bisa berbeda (misal: DT bilang Tinggi, tapi KNN bilang Sedang).")
        st.write("Di sinilah **Meta Learner (Logistic Regression)** bertugas. Sebagai Direktur Rumah Sakit, ia mendengarkan pendapat ketiga dokter tersebut, mengevaluasi siapa yang paling bisa dipercaya untuk kasus tertentu, dan menjatuhkan **Satu Keputusan Final** (Rendah, Sedang, atau Tinggi) yang paling akurat.")