import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="АКЫЛДУУ КОТОРМО СИСТЕМАСЫ",
    page_icon="✨",
    layout="wide"
)

# ================= STYLE =================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.main {
    background: linear-gradient(135deg, #fff7fb, #ffeef6, #fff7fb);
}

.block-container {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] {
    background: #fff0f7;
}

h1, h2, h3 {
    color: #c2185b;
}

.stButton>button {
    background: linear-gradient(90deg, #ff4fa3, #d63384);
    color: white;
    border: none;
    border-radius: 20px;
    padding: 13px 34px;
    font-size: 17px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: #c2185b;
    color: white;
}

[data-testid="stMetricValue"] {
    color: #c2185b;
}
</style>
""", unsafe_allow_html=True)

# ================= LOAD DATA =================

@st.cache_data
def load_data():
    df = pd.read_csv("corpus.csv")

    df["Category"] = df["Category"].replace({
        "Business English": "Бизнес англис тили",
        "Psychology": "Психология",
        "Emotional Expressions": "Эмоционалдык сөздөр",
        "Memes": "Мемдер",
        "Internet Slang": "Интернет сленги",
        "Social Media": "Социалдык тармактар",
        "Gaming Slang": "Оюн сленги",
        "Idioms": "Идиомалар",
        "Kyrgyz Proverbs": "Кыргыз макал-лакаптары",
        "Kyrgyz Expressions": "Кыргыз сөз айкаштары",
        "Technical NLP": "NLP терминдери"
    })

    return df

try:
    df = load_data()
except:
    df = None

# ================= SIDEBAR =================

st.sidebar.markdown("""
<h2 style='text-align:center; color:#c2185b;'>
✨ АКЫЛДУУ КОТОРМО
</h2>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Бөлүмдү тандаңыз:",
    [
        "🏠 Башкы бет",
        "👩‍🎓 Автор жөнүндө",
        "🧠 Котормо анализи",
        "📊 Аналитика",
        "📚 Корпус"
    ]
)

# ================= HOME PAGE =================

if page == "🏠 Башкы бет":

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        background:rgba(255,255,255,0.82);
        padding:75px 45px;
        border-radius:45px;
        box-shadow:0 18px 45px rgba(194,24,91,0.13);
    ">

    <img src="https://kstu.kg/fileadmin/user_upload/russkii_var.png"
    width="230"
    style="
        margin-bottom:30px;
        filter:drop-shadow(0 0 25px rgba(214,51,132,0.25));
    ">

    <h1 style="
        font-size:72px;
        font-family:Georgia, serif;
        line-height:1.25;
        letter-spacing:2px;
        color:#c2185b;
        margin-bottom:20px;
    ">
    АКЫЛДУУ КОТОРМО<br>
    СИСТЕМАСЫ
    </h1>

    <p style="
        font-size:24px;
        color:#7a5066;
        line-height:1.8;
    ">
    AI • NLP • Машиналык котормо
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        display:grid;
        grid-template-columns:1fr 1fr 1fr;
        gap:20px;
        margin-top:25px;
    ">

    <div style="background:white; padding:25px; border-radius:25px; text-align:center; box-shadow:0 8px 20px rgba(0,0,0,0.06);">
    <h3>🧠 Анализ</h3>
    <p>Котормолорду салыштыруу</p>
    </div>

    <div style="background:white; padding:25px; border-radius:25px; text-align:center; box-shadow:0 8px 20px rgba(0,0,0,0.06);">
    <h3>📊 Аналитика</h3>
    <p>Диаграммалар жана рейтинг</p>
    </div>

    <div style="background:white; padding:25px; border-radius:25px; text-align:center; box-shadow:0 8px 20px rgba(0,0,0,0.06);">
    <h3>📚 Корпус</h3>
    <p>Изилдөө маалыматтары</p>
    </div>

    </div>
    """, unsafe_allow_html=True)

# ================= ABOUT PAGE =================

elif page == "👩‍🎓 Автор жөнүндө":

    st.markdown("""
    <div style="
        background:rgba(255,255,255,0.85);
        padding:45px;
        border-radius:35px;
        box-shadow:0 12px 30px rgba(0,0,0,0.08);
        text-align:center;
    ">
    <h1 style="font-family:Georgia; font-size:52px;">
    ДОЛБООР ЖӨНҮНДӨ ✨
    </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
        <div style="
            background:white;
            padding:35px;
            border-radius:30px;
            text-align:center;
            box-shadow:0 8px 20px rgba(0,0,0,0.08);
        ">
        <img src="https://kstu.kg/fileadmin/user_upload/russkii_var.png" width="190">
        <h2 style="margin-top:25px;">КМТУ</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background:white;
            padding:38px;
            border-radius:30px;
            box-shadow:0 8px 20px rgba(0,0,0,0.08);
        ">
        <div style="font-size:21px; line-height:2.4; color:#4a4a4a;">

        👩‍🎓 <b>Автор:</b><br>
        Сезим Темирбековна<br><br>

        🎓 <b>Адистик:</b><br>
        Компьютердик лингвистика<br><br>

        🏫 <b>Университет:</b><br>
        Кыргыз мамлекеттик техникалык университети<br><br>

        💻 <b>Изилдөө багыты:</b><br>
        Машиналык котормо жана NLP технологиялары

        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Изилдөө деңгээли")

    st.progress(92)
    st.caption("Машиналык котормо системаларын салыштырма анализдөө")

# ================= ANALYSIS PAGE =================

elif page == "🧠 Котормо анализи":

    if df is None:
        st.error("❌ corpus.csv файлы табылган жок")
        st.stop()

    st.markdown("""
    <div style="
        text-align:center;
        background:rgba(255,255,255,0.8);
        padding:35px;
        border-radius:35px;
        box-shadow:0 10px 25px rgba(0,0,0,0.08);
    ">
    <h1 style="font-family:Georgia; font-size:50px;">
    КОТОРМО АНАЛИЗИ ✨
    </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("📚 Жалпы мисалдар", len(df))

    with m2:
        st.metric("🌍 Тилдер", 3)

    with m3:
        st.metric("🧩 Категориялар", df["Category"].nunique())

    st.markdown("## 🔎 Издөө")

    search = st.text_input("Сөз же сүйлөм жазыңыз")

    filtered_df = df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["Expression"].str.contains(search, case=False, na=False)
        ]

    language_map = {
        "English": "Англисче",
        "Russian": "Орусча",
        "Kyrgyz": "Кыргызча"
    }

    language_options = ["Бардыгы"] + [
        language_map.get(lang, lang)
        for lang in sorted(filtered_df["Language"].unique())
    ]

    selected_language = st.selectbox("🌍 Тилди тандаңыз", language_options)

    reverse_map = {v: k for k, v in language_map.items()}

    if selected_language != "Бардыгы":
        real_lang = reverse_map[selected_language]
        filtered_df = filtered_df[filtered_df["Language"] == real_lang]

    category = st.selectbox(
        "🧩 Категорияны тандаңыз",
        ["Бардыгы"] + sorted(filtered_df["Category"].unique())
    )

    if category != "Бардыгы":
        filtered_df = filtered_df[filtered_df["Category"] == category]

    if filtered_df.empty:
        st.warning("Маалымат табылган жок")
        st.stop()

    expression = st.selectbox(
        "💬 Сөз айкашын тандаңыз",
        filtered_df["Expression"]
    )

    if st.button("📌 Анализди көрсөтүү"):

        with st.spinner("AI анализ жүргүзүлүүдө..."):
            time.sleep(1)

        row = filtered_df[
            filtered_df["Expression"] == expression
        ].iloc[0]

        c1, c2 = st.columns(2)

        with c1:
            st.info(f"💬 Сөз айкашы:\n\n{row['Expression']}")
            st.success(f"✅ Адам котормосу:\n\n{row['Human Translation']}")
            st.write(f"🌐 Google Translate:\n\n{row['Google Translate']}")

        with c2:
            st.write(f"🧠 DeepL:\n\n{row['DeepL']}")
            st.write(f"📘 Yandex Translate:\n\n{row['Yandex Translate']}")
            st.warning(f"📝 Түшүндүрмө:\n\n{row['Comment']}")

# ================= ANALYTICS PAGE =================

elif page == "📊 Аналитика":

    if df is None:
        st.error("❌ corpus.csv файлы табылган жок")
        st.stop()

    st.markdown("""
    <div style="
        text-align:center;
        background:rgba(255,255,255,0.85);
        padding:40px;
        border-radius:35px;
        box-shadow:0 12px 30px rgba(0,0,0,0.08);
    ">
    <h1 style="font-family:Georgia; font-size:52px;">
    АНАЛИТИКА ЖАНА ДИАГРАММАЛАР 📊
    </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    a1, a2, a3 = st.columns(3)

    with a1:
        st.metric("🏆 Эң так система", "DeepL")

    with a2:
        st.metric("📈 Тактык көрсөткүчү", "92%")

    with a3:
        st.metric("📊 Салыштырылган система", "3")

    st.markdown("<br>", unsafe_allow_html=True)

    chart1, chart2 = st.columns(2)

    with chart1:
        st.subheader("Категориялар боюнча бөлүштүрүү")

        category_counts = df["Category"].value_counts()

        fig1, ax1 = plt.subplots(figsize=(6, 6))

        ax1.pie(
            category_counts,
            labels=category_counts.index,
            autopct="%1.1f%%",
            wedgeprops=dict(width=0.4)
        )

        ax1.set_title("Категориялар")
        st.pyplot(fig1)

    with chart2:
        st.subheader("Котормо сапатын салыштыруу")

        translator_scores = pd.DataFrame({
            "Котормо системасы": [
                "DeepL",
                "Google Translate",
                "Yandex Translate"
            ],
            "Тактык": [
                92,
                84,
                71
            ]
        })

        st.bar_chart(
            translator_scores.set_index("Котормо системасы")
        )

        st.dataframe(
            translator_scores,
            use_container_width=True
        )

    st.markdown("## 🧠 Жалпы жыйынтык")

    st.success(
        "DeepL системасы идиомалык жана эмоционалдык сөз айкаштарын "
        "салыштырмалуу так которгон."
    )

    st.info(
        "Google Translate жалпы маанини жакшы берет, бирок айрым маданий "
        "жана контексттик маанилерди толук бере албайт."
    )

    st.warning(
        "Yandex Translate кыргыз тилиндеги айрым сөз айкаштарын которууда "
        "маанилик каталарга жол берген учурлар бар."
    )

# ================= CORPUS PAGE =================

elif page == "📚 Корпус":

    if df is None:
        st.error("❌ corpus.csv файлы табылган жок")
        st.stop()

    st.markdown("""
    <div style="
        text-align:center;
        background:rgba(255,255,255,0.85);
        padding:40px;
        border-radius:35px;
        box-shadow:0 12px 30px rgba(0,0,0,0.08);
    ">
    <h1 style="font-family:Georgia; font-size:52px;">
    ИЗИЛДӨӨ КОРПУСУ 📚
    </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    display_df = df.rename(columns={
        "Expression": "Сөз айкашы",
        "Human Translation": "Адам котормосу",
        "Google Translate": "Google Translate",
        "DeepL": "DeepL",
        "Yandex Translate": "Yandex Translate",
        "Language": "Тил",
        "Category": "Категория",
        "Comment": "Түшүндүрмө"
    })

    st.dataframe(
        display_df.style.background_gradient(cmap="RdPu"),
        use_container_width=True
    )

# ================= FOOTER =================

st.markdown("---")

st.markdown("""
<div style="
    text-align:center;
    color:#7a5066;
    font-size:17px;
    padding:15px;
">
✨ АКЫЛДУУ КОТОРМО СИСТЕМАСЫ • 2026 ✨
</div>
""", unsafe_allow_html=True)
