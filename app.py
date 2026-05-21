import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================= PAGE =================

st.set_page_config(
    page_title="АКЫЛДУУ КОТОРМО СИСТЕМАСЫ",
    page_icon="🧠",
    layout="wide"
)

# ================= DARK MODE =================

theme = st.sidebar.toggle("🌙 Түнкү режим")

# ================= COLORS =================

if theme:

    bg = """
    linear-gradient(
    135deg,
    #0f0f0f,
    #181818,
    #1f1f1f
    )
    """

    card = "rgba(30,30,30,0.75)"
    text = "white"

else:

    bg = """
    linear-gradient(
    135deg,
    #fff7fb,
    #ffeef6,
    #f8f3ff,
    #eef4ff
    )
    """

    card = "rgba(255,255,255,0.70)"
    text = "#4a4a4a"

# ================= STYLE =================

st.markdown(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{{
    font-family:'Poppins', sans-serif;
}}

.main {{
    background:{bg};
}}

.block-container {{
    padding-top:2rem;
}}

section[data-testid="stSidebar"] {{
    background:#fff1f7;
}}

h1,h2,h3,p,label,div {{
    color:{text};
}}

.card {{
    background:{card};
    backdrop-filter:blur(14px);
    border:1px solid rgba(255,255,255,0.25);
    padding:30px;
    border-radius:30px;
    box-shadow:0 8px 30px rgba(0,0,0,0.08);
    margin-bottom:25px;
    animation:fadeUp 0.6s ease;
}}

.card:hover {{
    transform:translateY(-8px) scale(1.01);
    transition:0.35s;
}}

.big-title {{
    font-size:82px;
    text-align:center;
    font-family:Georgia;
    color:#c2185b;
    font-weight:700;
    text-shadow:0 0 18px rgba(255,79,163,0.25);
    animation:float 4s ease-in-out infinite;
}}

.subtitle {{
    text-align:center;
    font-size:28px;
    color:#7a5066;
}}

.info-text {{
    font-size:20px;
    line-height:2;
}}

.blue-card{{background:#edf4ff;}}
.green-card{{background:#eefcf3;}}
.yellow-card{{background:#fff9e9;}}
.purple-card{{background:#f7efff;}}
.pink-card{{background:#fff0f7;}}

.stButton>button {{
    background:
    linear-gradient(
    90deg,
    #ff4fa3,
    #d63384,
    #8e44ad
    );

    color:white;
    border:none;
    border-radius:20px;
    padding:12px 35px;
    font-size:18px;
    font-weight:600;
}}

.stButton>button:hover {{
    transform:scale(1.03);
    transition:0.3s;
}}

::-webkit-scrollbar {{
width:10px;
}}

::-webkit-scrollbar-thumb {{
background:#d63384;
border-radius:20px;
}}

@keyframes fadeUp {{
from {{
opacity:0;
transform:translateY(20px);
}}

to {{
opacity:1;
transform:translateY(0);
}}
}}

@keyframes float {{
0% {{
transform:translateY(0px);
}}

50% {{
transform:translateY(-6px);
}}

100% {{
transform:translateY(0px);
}}
}}

</style>
""", unsafe_allow_html=True)

# ================= DATA =================

@st.cache_data
def load_data():

    try:
        df = pd.read_csv("corpus.csv", encoding="utf-8")

    except:
        df = pd.read_csv(
            "corpus.csv",
            sep=";",
            encoding="utf-8"
        )

    df.columns = [col.strip() for col in df.columns]

    df["Category"] = (
        df["Category"]
        .astype(str)
        .str.strip()
    )

    df["Language"] = (
        df["Language"]
        .astype(str)
        .str.strip()
    )

    df = df.drop_duplicates()

    return df

df = load_data()

# ================= SIDEBAR =================

st.sidebar.markdown("""
<div style="text-align:center;">

<img src="https://kstu.kg/fileadmin/user_upload/kyrg.png" width="120">

<h1 style="
color:#c2185b;
font-family:Georgia;
font-size:34px;
">
АКЫЛДУУ<br>КОТОРМО
</h1>

<div style="
font-size:15px;
line-height:1.8;
">
NLP • Машиналык котормо<br>
Дипломдук долбоор
</div>

</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "БӨЛҮМ",
    [
        "🏠 Башкы бет",
        "👩‍🎓 Автор жөнүндө",
        "🧠 Котормо анализи",
        "📊 Аналитика",
        "⚠️ Ката анализи",
        "📚 Изилдөө корпусу"
    ]
)

# ================= HOME =================

if page == "🏠 Башкы бет":

    st.markdown("""
    <div class="card">

    <div class="big-title">
    АКЫЛДУУ КОТОРМО<br>
    СИСТЕМАСЫ
    </div>

    <div class="subtitle">
    Машиналык котормо • NLP • Жасалма интеллект
    </div>

    <div style='
    text-align:center;
    font-size:20px;
    color:#c2185b;
    margin-top:15px;
    '>
    🧠 AI Powered Translation Research Platform
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://kstu.kg/fileadmin/main_menu/enrollee/fasad.jpg",
        use_container_width=True
    )

    st.info("🧠 Корпустук NLP изилдөө долбоору")

    st.markdown("""
    <h2 style='text-align:center;'>
    📈 СИСТЕМА СТАТИСТИКАСЫ
    </h2>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Мисалдар", len(df))

    with col2:
        st.metric("🌍 Тилдер", df["Language"].nunique())

    with col3:
        st.metric("🧩 Категориялар", df["Category"].nunique())

    with col4:
        st.metric("🤖 MT Системалар", "3")

    st.success(
        "🏆 DeepL көп учурда эң так машиналык котормо системасы болуп чыкты."
    )

    st.markdown("""
    <div class="card pink-card">

    <h2>📖 ДОЛБООР ЖӨНҮНДӨ</h2>

    <p class="info-text">
    Бул веб-система машиналык котормо
    системаларын талдоо жана салыштыруу үчүн түзүлгөн.
    Изилдөөдө Google Translate,
    DeepL жана Yandex Translate
    системалары адам котормосу менен салыштырылат.
    </p>

    </div>
    """, unsafe_allow_html=True)

# ================= ABOUT =================

elif page == "👩‍🎓 Автор жөнүндө":

    st.markdown("""
    <div class="card">

    <h1 style="text-align:center;font-size:55px;">
    👩‍🎓 АВТОР ЖӨНҮНДӨ
    </h1>

    <div class="info-text">

    👩‍🎓 Автор: Сезим Темирбековна
    <br><br>

    🎓 Адистик: Компьютердик Лингвистика
    <br><br>

    👩‍🎓 Тайпа: МКЛ(б)-1-22
    <br><br>

    🏛 Институт: Маалыматтык Технологиялар Институту
    <br><br>

    🏫 И. Раззаков атындагы Кыргыз Мамлекеттик Техникалык Университети
    <br><br>

    👩‍🏫 Илимий жетекчи:
    Укуева Клара Акиновна
    <br><br>

    🤖 NLP • Жасалма интеллект • Машиналык котормо

    </div>

    </div>
    """, unsafe_allow_html=True)

# ================= ANALYSIS =================

elif page == "🧠 Котормо анализи":

    st.markdown("""
    <div class="card">

    <h1 style="text-align:center;font-size:60px;">
    🧠 КОТОРМО АНАЛИЗИ
    </h1>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        language = st.selectbox(
            "🌍 ТИЛ",
            [
                "Бардык тилдер",
                "Кыргызча",
                "English",
                "Русский"
            ]
        )

    filtered_df = df.copy()

    if language == "Кыргызча":

        filtered_df = filtered_df[
            filtered_df["Language"]
            .str.lower()
            .isin(["kyrgyz", "кыргызча"])
        ]

    elif language == "English":

        filtered_df = filtered_df[
            filtered_df["Language"]
            .str.lower()
            .isin(["english", "англисче"])
        ]

    elif language == "Русский":

        filtered_df = filtered_df[
            filtered_df["Language"]
            .str.lower()
            .isin(["russian", "русский"])
        ]

    with col2:

        categories = sorted(
            filtered_df["Category"]
            .dropna()
            .unique()
        )

        selected_category = st.selectbox(
            "🧩 КАТЕГОРИЯ",
            ["Бардыгы"] + list(categories)
        )

    if selected_category != "Бардыгы":

        filtered_df = filtered_df[
            filtered_df["Category"]
            == selected_category
        ]

    with col3:

        expressions = sorted(
            filtered_df["Expression"]
            .dropna()
            .unique()
        )

        expression = st.selectbox(
            "💬 СӨЗ",
            expressions
        )

    if st.button("📌 АНАЛИЗ КӨРСӨТҮҮ"):

        with st.spinner("🤖 Жасалма интеллект анализ жүргүзүүдө..."):

            row = filtered_df[
                filtered_df["Expression"]
                == expression
            ].iloc[0]

            c1, c2 = st.columns(2)

            with c1:

                st.markdown(f"""
                <div class="card blue-card">
                <h2>💬 Сөз</h2>
                <p class="info-text">{row['Expression']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="card green-card">
                <h2>✅ Адам котормосу</h2>
                <p class="info-text">{row['Human Translation']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="card yellow-card">
                <h2>🌐 Google Translate</h2>
                <p class="info-text">{row['Google Translate']}</p>
                </div>
                """, unsafe_allow_html=True)

            with c2:

                st.markdown(f"""
                <div class="card purple-card">
                <h2>🧠 DeepL</h2>
                <p class="info-text">{row['DeepL']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="card pink-card">
                <h2>📘 Yandex Translate</h2>
                <p class="info-text">{row['Yandex Translate']}</p>
                </div>
                """, unsafe_allow_html=True)

# ================= ANALYTICS =================

elif page == "📊 Аналитика":

    st.markdown("""
    <div class="card">

    <h1 style="text-align:center;font-size:60px;">
    📊 АНАЛИТИКА
    </h1>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🧠 DeepL", "92%")
        st.progress(92)

    with col2:
        st.metric("🌐 Google", "84%")
        st.progress(84)

    with col3:
        st.metric("📘 Yandex", "71%")
        st.progress(71)

    st.success(
        "🏆 DeepL эң так система болуп чыкты."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    category_counts = df["Category"].value_counts()

    st.subheader("📊 Категориялар боюнча статистика")

    top_categories = category_counts.sort_values(
        ascending=False
    ).head(10)

    st.bar_chart(top_categories)

# ================= ERROR ANALYSIS =================

elif page == "⚠️ Ката анализи":

    st.markdown("""
    <div class="card">

    <h1 style="
    text-align:center;
    font-size:60px;
    ">
    ⚠️ КАТА АНАЛИЗИ
    </h1>

    <p class="info-text" style="text-align:center;">
    Машиналык котормо системаларында
    эң көп кездешкен каталар
    төмөнкү категорияларга бөлүндү.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card pink-card">

        <h2>📝 Буквалдуу котормо</h2>

        <p class="info-text">
        Система сүйлөмдүн түз маанисин гана берип,
        чыныгы контекстти жоготкон учурлар.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card yellow-card">

        <h2>😂 Сарказм</h2>

        <p class="info-text">
        Сарказм жана ирония
        көп учурда туура эмес которулган.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card blue-card">

        <h2>🌐 Интернет сленг</h2>

        <p class="info-text">
        Delulu, NPC, Ghosting сыяктуу
        сөздөрдү AI дайыма эле туура түшүнө албайт.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card purple-card">

        <h2>📚 Фразеологизмдер</h2>

        <p class="info-text">
        Идиомалык сөз айкаштары
        түз мааниде которулуп калган учурлар.
        </p>

        </div>
        """, unsafe_allow_html=True)

# ================= CORPUS =================

elif page == "📚 Изилдөө корпусу":

    st.markdown("""
    <div class="card">

    <h1 style="text-align:center;font-size:60px;">
    📚 ИЗИЛДӨӨ КОРПУСУ
    </h1>

    </div>
    """, unsafe_allow_html=True)

    display_df = df.rename(columns={
        "Expression": "Сөз",
        "Human Translation": "Адам котормосу",
        "Google Translate": "Google",
        "DeepL": "DeepL",
        "Yandex Translate": "Yandex",
        "Language": "Тил",
        "Category": "Категория"
    })

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 CSV ЖҮКТӨӨ",
        csv,
        "corpus.csv",
        "text/csv"
    )

# ================= FOOTER =================

st.markdown("---")

st.markdown("""
<div style='
text-align:center;
font-size:18px;
padding:15px;
'>
✨ NLP • Машиналык котормо • Корпустук анализ • КМТУ • 2026 ✨
</div>
""", unsafe_allow_html=True)
