# ================= IMPORT =================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================= PAGE =================

st.set_page_config(
    page_title="АКЫЛДУУ КОТОРМО СИСТЕМАСЫ",
    page_icon="✨",
    layout="wide"
)

# ================= STYLE =================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins', sans-serif;
}

.main{
    background:linear-gradient(135deg,#fff7fb,#ffeef6,#fff7fb);
}

.block-container{
    padding-top:2rem;
}

section[data-testid="stSidebar"]{
    background:#fff1f7;
}

h1,h2,h3{
    color:#c2185b;
}

.stButton>button{
    background:linear-gradient(90deg,#ff4fa3,#d63384);
    color:white;
    border:none;
    border-radius:20px;
    padding:14px 40px;
    font-size:18px;
    font-weight:600;
}

.stButton>button:hover{
    transform:scale(1.04);
    transition:0.3s;
}

.card{
    background:white;
    padding:30px;
    border-radius:30px;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
    margin-bottom:20px;
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
    box-shadow:0 12px 25px rgba(0,0,0,0.13);
}

.big-title{
    font-size:78px;
    text-align:center;
    font-family:Georgia;
    color:#c2185b;
    font-weight:700;
}

.subtitle{
    text-align:center;
    font-size:28px;
    color:#7a5066;
    margin-top:10px;
}

.info-text{
    font-size:21px;
    line-height:2;
    color:#4a4a4a;
}

.blue-card{background:#edf4ff;}
.green-card{background:#eefcf3;}
.yellow-card{background:#fff9e9;}
.purple-card{background:#f7efff;}
.pink-card{background:#fff0f7;}

</style>
""", unsafe_allow_html=True)

# ================= DATA =================

@st.cache_data
def load_data():

    try:
        df = pd.read_csv("corpus.csv", encoding="utf-8")
    except:
        df = pd.read_csv("corpus.csv", sep=";", encoding="utf-8")

    df.columns = [col.strip() for col in df.columns]

    df["Category"] = df["Category"].astype(str).str.strip()
    df["Language"] = df["Language"].astype(str).str.strip()

    df = df.drop_duplicates()

    return df

df = load_data()

# ================= SIDEBAR =================

st.sidebar.markdown("""
<div style="text-align:center;padding-top:10px;">

<img src="https://kstu.kg/fileadmin/user_upload/kyrg.png" width="120">

<h1 style="
color:#c2185b;
font-family:Georgia;
font-size:36px;
">
АКЫЛДУУ<br>КОТОРМО
</h1>

<div style="
font-size:15px;
color:#7a5066;
line-height:1.6;
">
NLP • Machine Translation<br>
Graduation Project
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
    Machine Translation • NLP • AI
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://kstu.kg/fileadmin/main_menu/enrollee/fasad.jpg",
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

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
        "🏆 Изилдөөнүн негизинде DeepL көп учурда эң так машиналык котормо системасы катары көрүнөт."
    )

    st.markdown("""
    <div class="card pink-card">

    <h2 style="text-align:center;">📖 ДОЛБООР ЖӨНҮНДӨ</h2>

    <p class="info-text">
    Бул сайт машиналык котормо системаларын салыштыруу жана талдоо үчүн түзүлгөн.
    Изилдөөдө Google Translate, DeepL жана Yandex Translate системаларынын
    котормолору адам котормосу менен салыштырылат.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card blue-card">

    <h2 style="text-align:center;">🤖 КЫЗЫКТУУ ФАКТЫЛАР</h2>

    <p class="info-text">
    • DeepL эмоционалдык жана идиомалык сүйлөмдөрдү көбүрөөк туура берет.
    <br><br>
    • Google Translate техникалык жана жалпы тексттерде туруктуу натыйжа көрсөтөт.
    <br><br>
    • Yandex Translate айрым сленг, мем жана диалект сөздөрүндө маанини толук бере албайт.
    <br><br>
    • Фразеологизмдер, сарказм жана интернет сленг машиналык котормо үчүн эң татаал бөлүктөрдүн бири.
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
    <br>
    🎓 Адистик: Компьютердик Лингвистика
    <br>
    👩‍🎓 Тайпа: МКЛ(б)-1-22
    <br>
    🏛 Институт: Маалыматтык Технологиялар Институту
    <br>
    🏫 И. Раззаков атындагы Кыргыз Мамлекеттик Техникалык Университети
    <br>
    👩‍🏫 Илимий Жетекчи: Укуева Клара Акиновна
    <br>
    🤖 NLP • Artificial Intelligence • Machine Translation
    </div>

    </div>
    """, unsafe_allow_html=True)

# ================= ANALYSIS =================

elif page == "🧠 Котормо анализи":

    st.markdown("""
    <div class="card">
    <h1 style="text-align:center;font-size:60px;">
    КОТОРМО АНАЛИЗИ 🧠
    </h1>
    </div>
    """, unsafe_allow_html=True)

    language = st.selectbox(
        "🌍 ТИЛ ТАНДОО",
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
            filtered_df["Language"].str.lower().isin(["kyrgyz", "кыргызча"])
        ]

    elif language == "English":
        filtered_df = filtered_df[
            filtered_df["Language"].str.lower().isin(["english", "англисче"])
        ]

    elif language == "Русский":
        filtered_df = filtered_df[
            filtered_df["Language"].str.lower().isin(["russian", "русский"])
        ]

    search = st.text_input("🔎 Сөз же сүйлөм жазыңыз")

    if search:
        filtered_df = filtered_df[
            filtered_df["Expression"]
            .astype(str)
            .str.contains(search, case=False, na=False)
        ]

    col1, col2 = st.columns(2)

    with col1:
        categories = sorted(
            filtered_df["Category"]
            .astype(str)
            .str.strip()
            .unique()
        )

        selected_category = st.selectbox(
            "🧩 КАТЕГОРИЯ ТАНДОО",
            ["Бардыгы"] + list(categories)
        )

    if selected_category != "Бардыгы":
        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    with col2:
        if len(filtered_df) > 0:
            words = sorted(filtered_df["Expression"].dropna().unique())

            expression = st.selectbox(
                "💬 СӨЗ ТАНДОО",
                words
            )
        else:
            expression = None
            st.warning("Маалымат табылган жок.")

    if expression and st.button("📌 АНАЛИЗ КӨРСӨТҮҮ"):

        row = filtered_df[
            filtered_df["Expression"] == expression
        ].iloc[0]

        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2 = st.columns(2)

        with c1:
            st.markdown(f"""
            <div class="card blue-card">
            <h2>💬 Сөз / Сүйлөм</h2>
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

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🧠 DeepL", "92%")
        st.progress(92)

    with col2:
        st.metric("🌐 Google Translate", "84%")
        st.progress(84)

    with col3:
        st.metric("📘 Yandex Translate", "71%")
        st.progress(71)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📚 Категориялар боюнча бөлүштүрүү")

    category_counts = df["Category"].value_counts()

    st.bar_chart(category_counts)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("🥇 Категориялар боюнча мыкты система")

    best_systems = pd.DataFrame({
        "Категория": [
            "AI Жана Технология",
            "Сарказм",
            "Юмор",
            "Интернет Сленг",
            "Диалекттер",
            "Идиомалар"
        ],
        "Мыкты система": [
            "Google Translate",
            "DeepL",
            "DeepL",
            "DeepL",
            "Адам котормосу",
            "DeepL"
        ],
        "Себеби": [
            "Техникалык терминдерди жакшы берет",
            "Контекстти жакшыраак түшүнөт",
            "Маанини табигый берет",
            "Сленгди жакын мааниде берет",
            "Диалект сөздөрдү AI толук түшүнбөйт",
            "Түз эмес маанини жакшыраак берет"
        ]
    })

    st.dataframe(
        best_systems,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("""
    <div class="card blue-card">

    <h2>🤖 КОТОРМО СИСТЕМАЛАРЫНЫН АНАЛИЗИ</h2>

    <p class="info-text">
    ✅ DeepL эмоционалдык, идиомалык жана сарказм сүйлөмдөрүн салыштырмалуу так которгон.
    <br><br>
    ✅ Google Translate техникалык терминдерде жана жалпы сүйлөмдөрдө жакшы натыйжа көрсөткөн.
    <br><br>
    ⚠️ Yandex Translate интернет сленг, мем жана диалект сөздөрүндө көп учурда түз мааниге жакын которгон.
    <br><br>
    ⚠️ Фразеологизмдер жана маданий сөз айкаштары машиналык котормо үчүн эң татаал бөлүк болуп саналат.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card green-card">

    <h2>📌 МИСАЛДАР</h2>

    <p class="info-text">
    💬 <b>Ghosting</b>
    <br>
    Yandex Translate: "Арбак болуу" ❌
    <br>
    Адам котормосу: "Сүйлөшпөй жоголуп кетүү" ✅
    <br><br>

    💬 <b>Break the ice</b>
    <br>
    Google Translate: "Музду сындыруу" ❌
    <br>
    Адам котормосу: "Абалды жеңилдетүү" ✅
    <br><br>

    💬 <b>Delulu</b>
    <br>
    DeepL: "Кыялкеч адам" ✅
    <br>
    Адам котормосу: "Реалдуулуктан алыстаган адам" ✅
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card yellow-card">

    <h2>🔥 ЭҢ ТАТААЛ КАТЕГОРИЯЛАР</h2>

    <p class="info-text">
    • Сарказм
    <br>
    • Интернет Сленг
    <br>
    • Диалекттер
    <br>
    • Идиомалар
    <br>
    • Мемдер
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card purple-card">

    <h2>📖 ЖАЛПЫ ЖЫЙЫНТЫК</h2>

    <p class="info-text">
    Изилдөөнүн негизинде DeepL системасы контекстке жакын котормолорду көбүрөөк берген.
    Google Translate техникалык жана нейтралдуу тексттерде жакшы иштеген.
    Yandex Translate айрым сленг, диалект жана маданий сөз айкаштарын түз мааниде которгон.
    Ошондуктан машиналык котормону колдонууда адамдык редакциялоо дагы деле маанилүү.
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

    st.caption(f"📚 Жалпы мисалдар саны: {len(df)}")

    search_corpus = st.text_input("🔎 Корпустан издөө")

    display_df = df.rename(columns={
        "Expression": "Сөз",
        "Human Translation": "Адам котормосу",
        "Google Translate": "Google",
        "DeepL": "DeepL",
        "Yandex Translate": "Yandex",
        "Language": "Тил",
        "Category": "Категория"
    })

    if "Comment" in display_df.columns:
        display_df = display_df.drop(columns=["Comment"])

    if search_corpus:
        display_df = display_df[
            display_df.astype(str).apply(
                lambda row: row.str.contains(
                    search_corpus,
                    case=False,
                    na=False
                ).any(),
                axis=1
            )
        ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

# ================= FOOTER =================

st.markdown("---")

st.markdown("""
<div style='
text-align:center;
color:#7a5066;
font-size:18px;
padding:15px;
'>
✨ NLP • Machine Translation • Corpus Analysis • KSTU • 2026 ✨
</div>
""", unsafe_allow_html=True)
