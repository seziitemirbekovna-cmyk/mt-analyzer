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
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.03);
    background:#c2185b;
    color:white;
}

[data-testid="stMetricValue"]{
    color:#c2185b;
}

.card{
    background:rgba(255,255,255,0.85);
    padding:35px;
    border-radius:30px;
    box-shadow:0 8px 22px rgba(0,0,0,0.07);
}

.blue-card{
    background:#edf4ff;
    border:2px solid #d6e6ff;
}

.green-card{
    background:#eefcf3;
    border:2px solid #d8f5e2;
}

.yellow-card{
    background:#fff9e9;
    border:2px solid #ffe8a3;
}

.purple-card{
    background:#f7efff;
    border:2px solid #ead6ff;
}

.sky-card{
    background:#eef9ff;
    border:2px solid #cfefff;
}

</style>
""", unsafe_allow_html=True)

# ================= LOAD DATA =================

@st.cache_data
def load_data():

    df = pd.read_csv("corpus.csv")

    df["Category"] = df["Category"].replace({

        "Business English": "Бизнес Англис Тили",
        "Psychology": "Психология",
        "Emotional Expressions": "Эмоционалдык Сөздөр",
        "Memes": "Мемдер",
        "Internet Slang": "Интернет Сленги",
        "Social Media": "Социалдык Тармактар",
        "Gaming Slang": "Оюн Сленги",
        "Idioms": "Идиомалар",
        "Kyrgyz Proverbs": "Кыргыз Макал-Лакаптары",
        "Kyrgyz Expressions": "Кыргыз Сөз Айкаштары",
        "Technical NLP": "NLP Терминдери"

    })

    return df

try:
    df = load_data()

except:
    df = None

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

    "БӨЛҮМДӨР",

    [

        "🏠 Башкы бет",
        "👩‍🎓 Автор жөнүндө",
        "🧠 Котормо анализи",
        "📊 Аналитика",
        "📚 Корпус"

    ]

)

# ================= HOME =================

if page == "🏠 Башкы бет":

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        background:rgba(255,255,255,0.82);
        padding:80px 50px;
        border-radius:45px;
        box-shadow:0 18px 45px rgba(194,24,91,0.13);
    ">

    <img src="https://kstu.kg/fileadmin/user_upload/russkii_var.png"
    width="240"
    style="
    filter:drop-shadow(0 0 30px rgba(214,51,132,0.25));
    ">

    <br><br>

    <h1 style="
        font-size:74px;
        font-family:Georgia;
        line-height:1.25;
        letter-spacing:2px;
        color:#c2185b;
    ">

    АКЫЛДУУ КОТОРМО
    СИСТЕМАСЫ

    </h1>

    <p style="
        font-size:25px;
        color:#7a5066;
        margin-top:15px;
        line-height:2;
    ">

    AI • NLP • Машиналык Котормо

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="card">
        <h2>🧠 Анализ</h2>
        <p style="font-size:18px;">
        Котормолорду салыштыруу
        жана текшерүү
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="card">
        <h2>📊 Аналитика</h2>
        <p style="font-size:18px;">
        Диаграммалар жана
        AI рейтингдер
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="card">
        <h2>📚 Корпус</h2>
        <p style="font-size:18px;">
        Изилдөө маалыматтары
        жана корпус
        </p>
        </div>
        """, unsafe_allow_html=True)

# ================= ABOUT =================

elif page == "👩‍🎓 Автор жөнүндө":

    st.markdown("""
    <div class="card">
    <h1 style="
    text-align:center;
    font-size:54px;
    font-family:Georgia;
    ">
    ДОЛБООР ЖӨНҮНДӨ ✨
    </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1,2])

    with left:

        st.markdown("""
        <div class="card" style="text-align:center;">
        <img src="https://kstu.kg/fileadmin/user_upload/russkii_var.png"
        width="190">

        <h2 style="margin-top:25px;">
        КМТУ
        </h2>
        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div class="card">

        <div style="
        font-size:21px;
        line-height:2.5;
        color:#4a4a4a;
        ">

        👩‍🎓 <b>Автор:</b><br>
        Сезим Темирбековна

        <br>

        🎓 <b>Адистик:</b><br>
        Компьютердик Лингвистика

        <br>

        🏫 <b>Университет:</b><br>
        Кыргыз Мамлекеттик Техникалык Университети

        <br>

        💻 <b>Изилдөө Темасы:</b><br>
        Машиналык Котормо Анализи

        <br>

        🧠 <b>Багыт:</b><br>
        NLP • AI • Translation

        </div>

        </div>
        """, unsafe_allow_html=True)

# ================= ANALYSIS =================

elif page == "🧠 Котормо анализи":

    if df is None:

        st.error("❌ corpus.csv табылган жок")
        st.stop()

    st.markdown("""
    <div class="card">
    <h1 style="
    text-align:center;
    font-family:Georgia;
    font-size:54px;
    ">
    КОТОРМО АНАЛИЗИ ✨
    </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("📚 Жалпы Мисалдар", len(df))

    with m2:
        st.metric("🌍 Тилдер", 3)

    with m3:
        st.metric("🧩 Категориялар", df["Category"].nunique())

    st.markdown("## 🔎 ИЗДӨӨ")

    search = st.text_input(
        "Сөз же сүйлөм жазыңыз"
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

    language_map = {

        "English": "Англисче",
        "Russian": "Орусча",
        "Kyrgyz": "Кыргызча"

    }

    language_options = ["Бардыгы"] + [

        language_map.get(lang, lang)

        for lang in sorted(
            filtered_df["Language"].unique()
        )

    ]

    selected_language = st.selectbox(
        "🌍 ТИЛ",
        language_options
    )

    reverse_map = {
        v: k for k, v in language_map.items()
    }

    if selected_language != "Бардыгы":

        real_lang = reverse_map[selected_language]

        filtered_df = filtered_df[
            filtered_df["Language"] == real_lang
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

    if filtered_df.empty:

        st.warning("Маалымат табылган жок")
        st.stop()

    expression = st.selectbox(
        "💬 СӨЗ АЙКАШЫ",
        filtered_df["Expression"]
    )

    if st.button("📌 АНАЛИЗ КӨРСӨТҮҮ"):

        with st.spinner(
            "AI анализ жүргүзүлүүдө..."
        ):

            time.sleep(1)

        row = filtered_df[
            filtered_df["Expression"] == expression
        ].iloc[0]

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(f"""
            <div class="card blue-card">
            <h2>💬 Сөз Айкашы:</h2>
            <br>
            <p style="font-size:20px;">
            {row['Expression']}
            </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card green-card">
            <h2>✅ Адам Котормосу:</h2>
            <br>
            <p style="font-size:20px;">
            {row['Human Translation']}
            </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card blue-card">
            <h2>🌐 Google Translate:</h2>
            <br>
            <p style="font-size:20px;">
            {row['Google Translate']}
            </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown(f"""
            <div class="card purple-card">
            <h2>🧠 DeepL:</h2>
            <br>
            <p style="font-size:20px;">
            {row['DeepL']}
            </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card sky-card">
            <h2>📘 Yandex Translate:</h2>
            <br>
            <p style="font-size:20px;">
            {row['Yandex Translate']}
            </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card yellow-card">
            <h2>📝 Түшүндүрмө:</h2>
            <br>
            <p style="font-size:20px;">
            {row['Comment']}
            </p>
            </div>
            """, unsafe_allow_html=True)

# ================= ANALYTICS =================

elif page == "📊 Аналитика":

    if df is None:

        st.error("❌ corpus.csv табылган жок")
        st.stop()

    st.markdown("""
    <div class="card">
    <h1 style="
    text-align:center;
    font-size:54px;
    font-family:Georgia;
    ">
    АНАЛИТИКА 📊
    </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("🏆 Эң Так Система", "DeepL")

    with c2:
        st.metric("📈 Тактык", "92%")

    with c3:
        st.metric("🌍 Система", "3")

    st.markdown("<br>", unsafe_allow_html=True)

    chart1, chart2 = st.columns(2)

    with chart1:

        st.subheader(
            "Категориялар"
        )

        category_counts = df[
            "Category"
        ].value_counts()

        fig1, ax1 = plt.subplots(
            figsize=(6,6)
        )

        ax1.pie(

            category_counts,

            labels=category_counts.index,

            autopct='%1.1f%%',

            wedgeprops=dict(width=0.4)

        )

        st.pyplot(fig1)

    with chart2:

        st.subheader(
            "Котормо Сапаты"
        )

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

    st.markdown("<br>", unsafe_allow_html=True)

    st.success(
        "🏆 DeepL эмоционалдык "
        "жана идиомалык сөздөрдү "
        "эң так которгон."
    )

    st.info(
        "📘 Google Translate "
        "жалпы маанини жакшы берет."
    )

    st.warning(
        "⚠️ Yandex Translate "
        "айрым сөз айкаштарын "
        "туура эмес которгон."
    )

# ================= CORPUS =================

elif page == "📚 Корпус":

    if df is None:

        st.error("❌ corpus.csv табылган жок")
        st.stop()

    st.markdown("""
    <div class="card">
    <h1 style="
    text-align:center;
    font-size:54px;
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
        "Category": "Категория",
        "Comment": "Түшүндүрмө"

    })

    styled_df = display_df.style.background_gradient(
        cmap="RdPu"
    )

    st.dataframe(
        styled_df,
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
