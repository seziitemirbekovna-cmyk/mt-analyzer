import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

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
    background:
    linear-gradient(
        135deg,
        #fff7fb,
        #ffeef6,
        #fff7fb
    );
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

    background:
    linear-gradient(
        90deg,
        #ff4fa3,
        #d63384
    );

    color:white;
    border:none;
    border-radius:20px;
    padding:14px 40px;
    font-size:18px;
    font-weight:600;
}

.card{
    background:white;
    padding:30px;
    border-radius:30px;
    box-shadow:0 8px 20px rgba(0,0,0,0.07);
}

.blue-card{
    background:#edf4ff;
}

.green-card{
    background:#eefcf3;
}

.yellow-card{
    background:#fff9e9;
}

.purple-card{
    background:#f7efff;
}

.sky-card{
    background:#eef9ff;
}

</style>
""", unsafe_allow_html=True)

# ================= LOAD DATA =================

@st.cache_data
def load_data():

    df = pd.read_csv("corpus.csv")

    df["Category"] = df["Category"].replace({

        "Business English": "💼 Бизнес Англис Тили",
        "Psychology": "🧠 Психология",
        "Emotional Expressions": "💔 Эмоционалдык Сөздөр",
        "Memes": "😂 Мемдер",
        "Internet Slang": "🌍 Интернет Сленги",
        "Social Media": "📱 Социалдык Тармактар",
        "Gaming Slang": "🎮 Оюн Сленги",
        "Idioms": "📖 Идиомалар",
        "Kyrgyz Proverbs": "🇰🇬 Кыргыз Макал-Лакаптары",
        "Kyrgyz Expressions": "🗣 Кыргыз Сөз Айкаштары",
        "Technical NLP": "🤖 NLP Терминдери",

        # ЖАҢЫ КАТЕГОРИЯЛАР

        "Sarcasm": "😂 Сарказм Жана Юмор",
        "Movie Quotes": "🎬 Кино Жана Сериал Репликалары",
        "AI Terms": "🤖 AI Жана Технология",
        "Cultural Expressions": "🌏 Маданий Сөз Айкаштары",
        "Spoken Language": "💬 Сүйлөө Тили",
        "Regionalisms": "🌍 Диалект Жана Регионализмдер"

    })

    return df

df = load_data()

# ================= SIDEBAR =================

st.sidebar.markdown("""
<h1 style='
text-align:center;
color:#c2185b;
font-family:Georgia;
'>

✨ АКЫЛДУУ КОТОРМО

</h1>
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
    <div style="
        text-align:center;
        background:white;
        padding:80px 40px;
        border-radius:40px;
        box-shadow:0 10px 30px rgba(0,0,0,0.08);
    ">

    <h1 style="
        font-size:75px;
        font-family:Georgia;
        color:#c2185b;
    ">

    АКЫЛДУУ КОТОРМО
    СИСТЕМАСЫ

    </h1>

    <p style="
        font-size:24px;
        color:#7a5066;
        margin-top:20px;
    ">

    NLP • AI • Машиналык Котормо

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="card">
        <h2>🧠 Анализ</h2>
        <p>AI котормолорун салыштыруу</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="card">
        <h2>📊 Аналитика</h2>
        <p>Диаграммалар жана статистика</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="card">
        <h2>📚 Корпус</h2>
        <p>Изилдөө маалыматтары</p>
        </div>
        """, unsafe_allow_html=True)

# ================= ABOUT =================

elif page == "👩‍🎓 Автор жөнүндө":

    st.markdown("""
    <div class="card">

    <h1 style="
    text-align:center;
    font-size:55px;
    font-family:Georgia;
    ">

    ДОЛБООР ЖӨНҮНДӨ ✨

    </h1>

    <div style="
    font-size:22px;
    line-height:2.3;
    color:#4a4a4a;
    ">

    👩‍🎓 Автор: Сезим Темирбековна

    <br>

    🎓 Адистик: Компьютердик Лингвистика

    <br>

    🏫 Кыргыз Мамлекеттик Техникалык Университети

    <br>

    💻 Машиналык Котормо Анализи

    <br>

    🤖 NLP • AI • Translation

    </div>

    </div>
    """, unsafe_allow_html=True)

# ================= ANALYSIS =================

elif page == "🧠 Котормо анализи":

    st.markdown("""
    <div class="card">

    <h1 style="
    text-align:center;
    font-size:55px;
    font-family:Georgia;
    ">

    КОТОРМО АНАЛИЗИ ✨

    </h1>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    search = st.text_input(
        "🔎 Сөз же сүйлөм жазыңыз"
    )

    filtered_df = df.copy()

    if search:

        filtered_df = filtered_df[
            filtered_df["Expression"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    category = st.selectbox(

        "🧩 КАТЕГОРИЯ",

        ["Бардыгы"] + sorted(
            filtered_df["Category"].unique()
        )

    )

    if category != "Бардыгы":

        filtered_df = filtered_df[
            filtered_df["Category"] == category
        ]

    expression = st.selectbox(
        "💬 СӨЗ АЙКАШЫ",
        filtered_df["Expression"]
    )

    if st.button("📌 АНАЛИЗ"):

        row = filtered_df[
            filtered_df["Expression"] == expression
        ].iloc[0]

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(f"""
            <div class="card blue-card">
            <h2>💬 Сөз Айкашы</h2>
            <p style="font-size:20px;">
            {row['Expression']}
            </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card green-card">
            <h2>✅ Адам Котормосу</h2>
            <p style="font-size:20px;">
            {row['Human Translation']}
            </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card blue-card">
            <h2>🌐 Google Translate</h2>
            <p style="font-size:20px;">
            {row['Google Translate']}
            </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown(f"""
            <div class="card purple-card">
            <h2>🧠 DeepL</h2>
            <p style="font-size:20px;">
            {row['DeepL']}
            </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card sky-card">
            <h2>📘 Yandex Translate</h2>
            <p style="font-size:20px;">
            {row['Yandex Translate']}
            </p>
            </div>
            """, unsafe_allow_html=True)

# ================= ANALYTICS =================

elif page == "📊 Аналитика":

    st.markdown("""
    <div class="card">

    <h1 style="
    text-align:center;
    font-size:55px;
    font-family:Georgia;
    ">

    АНАЛИТИКА 📊

    </h1>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    chart1, chart2 = st.columns(2)

    with chart1:

        st.subheader("Категориялар")

        category_counts = df[
            "Category"
        ].value_counts()

        fig1, ax1 = plt.subplots(
            figsize=(6,6)
        )

        ax1.pie(

            category_counts,

            labels=category_counts.index,

            autopct='%1.1f%%'

        )

        st.pyplot(fig1)

    with chart2:

        st.subheader("AI Тактык")

        translator_scores = pd.DataFrame({

            "Система": [

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
            translator_scores.set_index(
                "Система"
            )
        )

# ================= CORPUS =================

elif page == "📚 Изилдөө корпусу":

    st.markdown("""
    <div class="card">

    <h1 style="
    text-align:center;
    font-size:60px;
    font-family:Georgia;
    ">

    ИЗИЛДӨӨ КОРПУСУ 📚

    </h1>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    display_df = df.rename(columns={

        "Expression": "Сөз Айкашы",
        "Human Translation": "Адам Котормосу",
        "Google Translate": "Google Translate",
        "DeepL": "DeepL",
        "Yandex Translate": "Yandex Translate",
        "Language": "Тил",
        "Category": "Категория"

    })

    # ЭГЕР COMMENT БОЛСО ӨЧҮРӨТ

    if "Comment" in display_df.columns:

        display_df = display_df.drop(
            columns=["Comment"]
        )

    st.dataframe(
        display_df,
        use_container_width=True
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

✨ АКЫЛДУУ КОТОРМО СИСТЕМАСЫ • 2026 ✨

</div>
""", unsafe_allow_html=True)
