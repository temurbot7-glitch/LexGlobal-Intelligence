import streamlit as st
from google import genai
import datetime
import folium
from streamlit_folium import st_folium

# === SAHIFA SOZLAMALARI ===
st.set_page_config(
    page_title="LexGlobal | Enterprise Legal Intelligence",
    page_icon="⚖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === GEMINI AI API CLIENT ===
API_KEY = "AQ.Ab8RN6JSKi1Ju-4JGCAZMrL07yggOMTPhEmgfXcDsoLRiqOjxA"

try:
    client = genai.Client(api_key=API_KEY)
except Exception:
    client = None

# === SESSION STATE XOTIRASI ===
if "const_text" not in st.session_state:
    st.session_state.const_text = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

# === HIGH-PERFORMANCE ANIMATED AURORA MESH CSS ===
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    /* Плавно переливающийся анимированный фон Aurora Mesh Flow */
    .stApp {
        background: linear-gradient(-45deg, #020617, #0f172a, #1e1b4b, #090d16);
        background-size: 400% 400%;
        animation: auroraFlow 15s ease infinite;
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    @keyframes auroraFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: rgba(10, 15, 30, 0.75) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* Заголовки */
    h1 {
        font-weight: 800 !important;
        letter-spacing: -0.04em !important;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 40%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.6rem !important;
        margin-bottom: 0.1rem !important;
    }

    /* Стеклянные панели Glassmorphism с анимацией при наведении */
    .glass-panel {
        background: rgba(15, 23, 42, 0.55);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 18px;
        padding: 26px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(16px);
        margin-bottom: 22px;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .glass-panel:hover {
        border-color: rgba(56, 189, 248, 0.4);
        box-shadow: 0 25px 50px -12px rgba(56, 189, 248, 0.25);
        transform: translateY(-3px);
    }

    /* Карточки метрик */
    .stat-card {
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 18px 22px;
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
    }
    .stat-card:hover {
        border-color: rgba(56, 189, 248, 0.3);
        background: rgba(30, 41, 59, 0.65);
        transform: translateY(-2px);
    }
    .stat-label {
        font-size: 0.75rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 700;
    }
    .stat-value {
        font-size: 1.25rem;
        color: #f8fafc;
        font-weight: 800;
        margin-top: 4px;
    }

    /* Пульсирующий индикатор */
    .badge-active {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #34d399;
        padding: 5px 14px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 700;
    }
    .badge-dot {
        width: 7px;
        height: 7px;
        background-color: #34d399;
        border-radius: 50%;
        box-shadow: 0 0 10px #34d399;
        animation: pulseGlow 2s infinite ease-in-out;
    }

    @keyframes pulseGlow {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(1.3); }
    }

    /* Поля ввода */
    .stTextInput input, .stTextArea textarea {
        background: rgba(15, 23, 42, 0.75) !important;
        color: #f8fafc !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 14px !important;
        padding: 16px 20px !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.18) !important;
    }

    /* Стильные кнопки с градиентом */
    .stButton button {
        background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 14px !important;
        padding: 12px 28px !important;
        font-weight: 700 !important;
        box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #38bdf8 0%, #3b82f6 100%) !important;
        box-shadow: 0 15px 30px -5px rgba(56, 189, 248, 0.6) !important;
        transform: translateY(-2px);
    }

    /* Вкладки Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(15, 23, 42, 0.5);
        padding: 6px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
    }
    .stTabs [data-baseweb="tab"] {
        height: 46px;
        border-radius: 12px;
        color: #94a3b8;
        font-weight: 700;
        transition: all 0.25s ease;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.2) 0%, rgba(37, 99, 235, 0.3) 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(56, 189, 248, 0.4);
    }

    .disclaimer-box {
        background: rgba(245, 158, 11, 0.05);
        border: 1px solid rgba(245, 158, 11, 0.2);
        border-radius: 14px;
        padding: 14px 18px;
        font-size: 0.82rem;
        color: #fbbf24;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# === YURISDIKSIYALAR VA METADATA ===
jurisdictions = {
    "🇺🇿 O'zbekiston": {
        "name": "O'zbekiston Respublikasi",
        "system": "Kontinental (Fuqarolik) huquqi",
        "adopted": "1992-yil 8-dekabr (Yangilangan: 2023)",
        "court": "Oliy Sud / Konstitutsiyaviy Sud",
        "coords": [41.2995, 69.2401]
    },
    "🇺🇸 AQSh": {
        "name": "Amerika Qo'shma Shtatlari",
        "system": "Umumiy huquq (Common Law)",
        "adopted": "1787-yil 17-sentyabr",
        "court": "US Supreme Court",
        "coords": [38.9072, -77.0369]
    },
    "🇩🇪 Germaniya": {
        "name": "Germaniya Federativ Respublikasi",
        "system": "Kontinental (Romano-German)",
        "adopted": "1949-yil 23-may (Grundgesetz)",
        "court": "Bundesverfassungsgericht",
        "coords": [52.5200, 13.4050]
    },
    "🇬🇧 Buyuk Britaniya": {
        "name": "Buyuk Britaniya Qirolligi",
        "system": "Kodifikatsiya qilinmagan Umumiy huquq",
        "adopted": "Konstitutsiyaviy precedentlar va aktlar",
        "court": "UK Supreme Court",
        "coords": [51.5074, -0.1278]
    },
    "🇰🇿 Qozog'iston": {
        "name": "Qozog'iston Respublikasi",
        "system": "Kontinental (Fuqarolik) huquqi",
        "adopted": "1995-yil 30-avgust",
        "court": "Konstitutsiyaviy Sud",
        "coords": [51.1693, 71.4491]
    },
    "🇷🇺 Rossiya": {
        "name": "Rossiya Federatsiyasi",
        "system": "Kontinental huquq",
        "adopted": "1993-yil 12-dekabr",
        "court": "Konstitutsiyaviy Sud",
        "coords": [55.7558, 37.6173]
    }
}

# === SIDEBAR CONTROL PANEL ===
with st.sidebar:
    st.markdown("<h2 style='font-size: 1.2rem; margin-bottom: 1rem;'>🌐 Yurisdiksiya Sozlamalari</h2>", unsafe_allow_html=True)
    
    selected_flag = st.selectbox(
        "Maqsadli davlatni tanlang:",
        list(jurisdictions.keys())
    )
    
    country_info = jurisdictions[selected_flag]
    
    st.markdown("<div style='margin: 1.5rem 0; border-top: 1px solid rgba(255,255,255,0.08);'></div>", unsafe_allow_html=True)
    
    st.markdown("### 📊 Davlat Huquqiy Profili")
    st.markdown(f"""
        <div style='font-size: 0.85rem; color: #94a3b8; line-height: 1.8;'>
        • <b>Rasmiy nom:</b> <span style='color: #f8fafc;'>{country_info['name']}</span><br>
        • <b>Huquq tizimi:</b> <span style='color: #38bdf8;'>{country_info['system']}</span><br>
        • <b>Konstitutsiya:</b> <span style='color: #f8fafc;'>{country_info['adopted']}</span><br>
        • <b>Yuqori instansiya:</b> <span style='color: #cbd5e1;'>{country_info['court']}</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 1.5rem 0; border-top: 1px solid rgba(255,255,255,0.08);'></div>", unsafe_allow_html=True)
    
    st.markdown("### ⚡ AI System Core")
    st.markdown("""
        <div class="badge-active">
            <div class="badge-dot"></div> Enterprise Core Active
        </div>
        <div style='font-size: 0.8rem; color: #64748b; margin-top: 10px;'>
        • Engine: Gemini Legal Core<br>
        • Model: gemini-3.8-flash<br>
        • Motion: Aurora Flow 60FPS
        </div>
    """, unsafe_allow_html=True)

# === MAIN HEADER ===
col_header, col_status = st.columns([3, 1])

with col_header:
    st.title("LexGlobal Intelligence")
    st.markdown("<p style='color: #94a3b8; font-size: 1.05rem;'>Autonomous Multi-Jurisdictional Constitutional Database & AI Legal Advisory Suite</p>", unsafe_allow_html=True)

with col_status:
    st.markdown(f"""
        <div style='text-align: right; padding-top: 10px;'>
            <div style='font-size: 0.75rem; color: #64748b;'>Sana & Vaqt</div>
            <div style='font-size: 0.9rem; font-weight: 700; color: #38bdf8; font-family: "JetBrains Mono";'>
                {datetime.datetime.now().strftime("%Y-%m-%d | %H:%M")}
            </div>
        </div>
    """, unsafe_allow_html=True)

# === METRIC DASHBOARD PANEL ===
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Tanlangan Hudud</div>
            <div class="stat-value">{country_info['name']}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Tizim Turi</div>
            <div class="stat-value" style="color: #38bdf8;">Civil / Common</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Animatsiya</div>
            <div class="stat-value" style="color: #34d399;">Aurora Flow 🌊</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Audit Holati</div>
            <div class="stat-value" style="color: #a855f7;">Verified AI</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

# === MAIN WORKSPACE TABS ===
tab_map, tab_corpus, tab_chat, tab_compare = st.tabs([
    "🗺️ Interaktiv Dunyo Xaritasi",
    "📖 Konstitutsiyaviy Korpus", 
    "💬 AI Advokat (Interaktiv Chat)",
    "⚖️ Qonunchilikni Taqqoslash"
])

# TAB 0: INTERACTIVE WORLD MAP
with tab_map:
    st.subheader("🌐 Global Yurisdiksiyalar Xaritasi")
    st.markdown("<p style='color: #94a3b8;'>Xaritadagi davlatlar ustiga bosing va ularning huquqiy markazlarini ko'ring.</p>", unsafe_allow_html=True)
    
    m = folium.Map(
        location=[30.0, 10.0], 
        zoom_start=2, 
        tiles="OpenStreetMap"
    )
    
    for key, info in jurisdictions.items():
        folium.Marker(
            location=info["coords"],
            popup=f"<b>{info['name']}</b><br>{info['system']}",
            tooltip=f"{key}: {info['name']}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)
        
    st_folium(m, width="100%", height=450, returned_objects=[])

# TAB 1: CONSTITUTIONAL CORPUS
with tab_corpus:
    st.subheader(f"{country_info['name']} Konstitutsiyaviy Normalari")
    st.markdown("<p style='color: #94a3b8;'>Rasmiy davlat reestriga asoslangan moddalar va prinsiplar tahlili.</p>", unsafe_allow_html=True)
    
    if st.button(f"🏛 {country_info['name']} Konstitutsiyasini Generatsiya Qilish"):
        if not API_KEY:
            st.error("API Kalit topilmadi.")
        else:
            with st.spinner("Neyron tarmoq orqali konstitutsiyaviy korpus sintez qilinmoqda..."):
                try:
                    prompt_const = f"""
                    Siz konstitutsiyaviy huquq bo'yicha dunyo darajasidagi ekspert-huquqshunosdirsiz.
                    Davlat: {country_info['name']}
                    
                    Quyidagi tuzilmada ushbu davlat Konstitutsiyasining rasmiy va mukammal sharhini taqdim eting:
                    1. 📜 Preambula va Davlat Suvereniteti Tamoyillari.
                    2. ⚖️ Konstitutsiyaviy Tuzum Asoslari.
                    3. 🛡 Inson va Fuqaroning Asosiy Huquqlari, Erkinliklari hamda Burchlari.
                    4. 🏛 Hokimiyat Bo'linishi va Davlat Organlari Tizimi.
                    
                    JAVOBNI TO'LIQ VA BENUQSON O'ZBEK TILIDA (LOTIN YOZUVIDA), RASMIY HUQUQIY TERMINOLOGIYA BILAN TAQDIM ETING.
                    """
                    
                    res = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt_const
                    )
                    
                    st.session_state.const_text = res.text
                    
                except Exception as e:
                    st.error(f"Xatolik yuz berdi: {e}")

    if st.session_state.const_text:
        st.markdown(f"""
            <div class="glass-panel">
                <div style='color: #38bdf8; font-weight: 700; margin-bottom: 12px; font-size: 1.1rem;'>
                    📜 {country_info['name']} Konstitutsiyaviy Sharhi
                </div>
                {st.session_state.const_text}
            </div>
        """, unsafe_allow_html=True)

# TAB 2: MULTI-TURN LEGAL CHAT
with tab_chat:
    st.subheader(f"Advokat Konsultatsiyasi — {country_info['name']}")
    st.markdown("<p style='color: #94a3b8;'>Sun'iy intellekt advokat bilan matnli suhbatlashing va savollaringizga javob oling.</p>", unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input(f"{country_info['name']} qonunchiligi bo'yicha savolingizni kiriting...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Yuridik tahlil qilinmoqda..."):
                try:
                    prompt_chat = f"""
                    Siz {country_info['name']} davlatining professional advokat va yuridik konsultantisiz.
                    Foydalanuvchining ushbu savoliga ushbu davlat qonunlariga tayanib, aniq moddalar bilan javob bering.
                    
                    Savol: {user_input}
                    
                    Javob to'liq O'zbek tilida (Lotin yozuvida), rasmiy va tushunarli bo'lsin.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt_chat
                    )
                    
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                    
                except Exception as e:
                    st.error(f"Xatolik yuz berdi: {e}")

# TAB 3: CROSS-BORDER COMPARISON
with tab_compare:
    st.subheader("⚖️ Ikki Davlat Qonunchiligini Taqqoslash")
    st.markdown("<p style='color: #94a3b8;'>Ikkita turli mamlakat huquqiy normalarini bir vaqtning o'zida solishtiring.</p>", unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        country1 = st.selectbox("Birinchi davlat:", list(jurisdictions.keys()), index=0, key="c1")
    with col_c2:
        country2 = st.selectbox("Ikkinchi davlat:", list(jurisdictions.keys()), index=1, key="c2")
        
    compare_topic = st.text_input("Taqqoslanadigan huquqiy soha yoki situatsiya:", placeholder="Masalan: IT kompaniya ochish, mehnat huquqlari yoki intellektual mulkni himoya qilish...")
    
    if st.button("🔄 Qonunchilikni Solishtirish va Taqqoslash"):
        if not compare_topic:
            st.warning("Iltimos, taqqoslanadigan sohani kiriting.")
        else:
            with st.spinner(f"{country1} va {country2} qonunchiligi tahlil qilinmoqda..."):
                try:
                    prompt_compare = f"""
                    Siz xalqaro huquq bo'yicha ekspert-huquqshunosdirsiz.
                    Birinchi davlat: {country1}
                    Ikkinchi davlat: {country2}
                    Taqqoslash mavzusi: {compare_topic}
                    
                    Quyidagi tuzilmada batafsil xalqaro taqqoslash hisobotini berishingiz kerak:
                    1. ⚖️ Birinchi davlat ({country1}) tartibi va talablari.
                    2. ⚖️ Ikkinchi davlat ({country2}) tartibi va talablari.
                    3. 📊 Asosiy Farqlar va Afzalliklar.
                    4. 💡 Biznes / Fuqaro uchun Yakuniy Xalqaro Advokat Tavsiyasi.
                    
                    Javobni TO'LIQ O'ZBEK TILIDA (LOTIN YOZUVIDA) taqdim eting.
                    """
                    
                    res_comp = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt_compare
                    )
                    
                    st.markdown(f"""
                        <div class="glass-panel">
                            {res_comp.text}
                        </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Xatolik: {e}")

# === FOOTER DISCLAIMER ===
st.markdown("""
    <div class="disclaimer-box">
        ⚠️ <b>Rasmiy Ogohlantirish:</b> LexGlobal Intelligence tizimi AI algoritmlariga asoslangan avtonom ma'lumot beruvchi dasturdir. Berilgan javoblar rasmiy sud hujjati o'rnini bosmaydi. Muhim sud ishlarida litsenziyalangan advokatga murojaat qilish tavsiya etiladi.
    </div>
""", unsafe_allow_html=True)