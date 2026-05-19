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
    transform:scale(1.05);
}

.card{
    background:white;
    padding:30px;
    border-radius:30px;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
    transition:0.3s;
}

.card:hover{
    transform:translateY(-6px);
    box-shadow:0 12px 25px rgba(0,0,0,0.15);
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

.big-title{
    font-size:85px;
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
    font-size:22px;
    line-height:2.2;
    color:#4a4a4a;
}

</style>
""", unsafe_allow_html=True)

# ================= DATA =================

@st.cache_data
def load_data():

    try:
        df = pd.read_csv(
            "corpus.csv",
            sep=",",
            encoding="utf-8"
        )

    except:
        df = pd.read_csv(
            "corpus.csv",
            sep=";",
            encoding="utf-8"
        )

    df.columns = [
        col.strip()
        for col in df.columns
    ]

    return df

df = load_data()

# ================= SIDEBAR =================

st.sidebar.markdown("""

<div style="
text-align:center;
padding:10px;
">

<img src="
https://kstu.kg/fileadmin/user_upload/kyrg.png
"
width="110">

<h1 style="
color:#c2185b;
font-family:Georgia;
font-size:34px;
margin-top:10px;
">

АКЫЛДУУ КОТОРМО

</h1>

<div style="
font-size:15px;
color:#7a5066;
line-height:1.6;
">

Computer Linguistics
<br>
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

    АКЫЛДУУ КОТОРМО
    СИСТЕМАСЫ ✨

    </div>

    <div class="subtitle">

    Машиналык Котормо • NLP • AI

    </div>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.image(
        "https://kstu.kg/fileadmin/main_menu/enrollee/fasad.jpg",
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.code(
        "NLP • Machine Translation • Corpus Analysis • Artificial Intelligence"
    )

    st.success(
        "🎓 Бул сайт дипломдук изилдөө долбоору катары түзүлгөн."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Мисалдар", len(df))

    with col2:
        st.metric("🌍 Тилдер", df["Language"].nunique())

    with col3:
        st.metric("🤖 Системалар", "3")

    with col4:
        st.metric("🧩 Категориялар", df["Category"].nunique())

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""

    <div class="card">

    <h2 style="
    text-align:center;
    font-size:38px;
    ">

    📖 ДОЛБООР ЖӨНҮНДӨ

    </h2>

    <p style="
    font-size:22px;
    line-height:2;
    text-align:center;
    color:#4a4a4a;
    ">

    Бул долбоор машиналык котормо
    системаларын салыштыруу үчүн түзүлгөн.

    Сайтта Google Translate,
    DeepL жана Yandex Translate
    системаларынын котормолору
    анализденет.

    </p>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""

    <div class="card">

    <h2 style="
    text-align:center;
    font-size:35px;
    ">

    🤖 КЫЗЫКТУУ ФАКТЫЛАР

    </h2>

    <p style="
    font-size:21px;
    line-height:2;
    ">

    • DeepL эмоционалдык сүйлөмдөрдү жакшыраак түшүнөт.

    <br><br>

    • Google Translate техникалык терминдерде так иштейт.

    <br><br>

    • Yandex Translate кыргызча диалекттерде ката кетириши мүмкүн.

    <br><br>

    • Машиналык котормо фразеологизмдерди түз мааниде которгон учурлар көп кездешет.

    </p>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""

        <div class="card blue-card">

        <h2>🧠 AI Анализ</h2>

        <p>
        Машиналык котормо
        системаларын салыштыруу
        </p>

        </div>

        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""

        <div class="card green-card">

        <h2>📊 Аналитика</h2>

        <p>
        Диаграммалар жана
        статистикалык маалыматтар
        </p>

        </div>

        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""

        <div class="card purple-card">

        <h2>📚 Корпус</h2>

        <p>
        Изилдөө маалыматтары
        </p>

        </div>

        """, unsafe_allow_html=True)

# ================= ABOUT =================

elif page == "👩‍🎓 Автор жөнүндө":

    st.markdown("""

    <div class="card">

    <h1 style="
    text-align:center;
    font-size:60px;
    font-family:Georgia;
    ">

    АВТОР ЖӨНҮНДӨ ✨

    </h1>

    <div class="info-text">

    👩‍🎓 Автор:
    Сезим Темирбековна

    <br>

    🎓 Адистик:
    Компьютердик Лингвистика

    <br>

    🏛 Институт:
    Маалыматтык Технологиялар Институту

    <br>

    🏫 Исхак Раззаков атындагы Кыргыз Мамлекеттик
    Техникалык Университети
   

    <br>

    👩‍🏫 Илимий Жетекчи:
    Укуева Клара Акиновна

    <br>

    💻 Долбоор:
    Машиналык Котормо Анализи

    <br>

    🤖 NLP • Artificial Intelligence

    </div>

    </div>

    """, unsafe_allow_html=True)

# ================= ANALYSIS =================

elif page == "🧠 Котормо анализи":

    st.markdown("""

    <div class="card">

    <h1 style="
    text-align:center;
    font-size:60px;
    font-family:Georgia;
    ">

    КОТОРМО АНАЛИЗИ 🧠

    </h1>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "📌 Сөздү же категорияны тандап, котормо системаларын салыштырыңыз."
    )

    language = st.selectbox(

        "🌍 ТИЛ ТАНДОО",

        [

            "Кыргызча",
            " English",
            " Русский"

        ]

    )

    filtered_df = df.copy()

    if language == "🇰🇬 Кыргызча":

        filtered_df = filtered_df[
            filtered_df["Language"].astype(str).str.contains(
                "Kyrgyz",
                case=False,
                na=False
            )
        ]

    elif language == "🇬🇧 English":

        filtered_df = filtered_df[
            filtered_df["Language"].astype(str).str.contains(
                "English",
                case=False,
                na=False
            )
        ]

    elif language == "🇷🇺 Русский":

        filtered_df = filtered_df[
            filtered_df["Language"].astype(str).str.contains(
                "Russian",
                case=False,
                na=False
            )
        ]

    search = st.text_input(
        "🔎 Сөз же сүйлөм жазыңыз"
    )

    if search:

        filtered_df = filtered_df[
            filtered_df["Expression"].astype(str).str.contains(
                search,
                case=False,
                na=False
            )
        ]

    col1, col2 = st.columns(2)

    with col1:

        categories = sorted(
            filtered_df["Category"].dropna().unique()
        )

        selected_category = st.selectbox(

            "🧩 КАТЕГОРИЯ ТАНДОО",

            ["Бардыгы"] + categories

        )

    if selected_category != "Бардыгы":

        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    with col2:

        if len(filtered_df) > 0:

            expression = st.selectbox(

                "💬 СӨЗ ТАНДОО",

                filtered_df["Expression"]

            )

        else:

            expression = None

            st.warning(
                "Маалымат табылган жок."
            )

    if expression and st.button("📌 АНАЛИЗ КӨРСӨТҮҮ"):

        row = filtered_df[
            filtered_df["Expression"] == expression
        ].iloc[0]

        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2 = st.columns(2)

        with c1:

            st.markdown(f"""

            <div class="card blue-card">

            <h2>💬 Сөз Айкашы</h2>

            <p style="font-size:22px;">
            {row['Expression']}
            </p>

            </div>

            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""

            <div class="card green-card">

            <h2>✅ Адам Котормосу</h2>

            <p style="font-size:22px;">
            {row['Human Translation']}
            </p>

            </div>

            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""

            <div class="card blue-card">

            <h2>🌐 Google Translate</h2>

            <p style="font-size:22px;">
            {row['Google Translate']}
            </p>

            </div>

            """, unsafe_allow_html=True)

        with c2:

            st.markdown(f"""

            <div class="card purple-card">

            <h2>🧠 DeepL</h2>

            <p style="font-size:22px;">
            {row['DeepL']}
            </p>

            </div>

            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""

            <div class="card yellow-card">

            <h2>📘 Yandex Translate</h2>

            <p style="font-size:22px;">
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
    font-size:60px;
    font-family:Georgia;
    ">

    АНАЛИТИКА 📊

    </h1>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🧠 DeepL", "92%")

    with col2:
        st.metric("🌐 Google Translate", "84%")

    with col3:
        st.metric("📘 Yandex Translate", "71%")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader(
        "📚 Категориялар боюнча бөлүштүрүү"
    )

    category_counts = df[
        "Category"
    ].value_counts()

    st.bar_chart(category_counts)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader(
        "🤖 Котормо Системаларын Салыштыруу"
    )

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
        translator_scores.set_index(
            "Котормо системасы"
        )
    )

    st.success(
        "📌 DeepL эмоционалдык жана идиомалык сөздөрдү эң так которгон."
    )

    st.warning(
        "⚠️ Yandex Translate айрым кыргызча диалект сөздөрүн туура эмес которгон."
    )

    st.error(
        "❌ Google Translate кээ бир фразеологизмдердин маанисин түз мааниде которгон."
    )

    st.markdown("""

    ### 📌 ЖЫЙЫНТЫК

    DeepL системасы фразеологизмдерди
    жана эмоционалдык сүйлөмдөрдү
    салыштырмалуу так которгон.

    Google Translate техникалык
    сүйлөмдөрдө жакшы натыйжа көрсөткөн.

    Yandex Translate айрым
    маданий сөз айкаштарын
    толук түшүндүрө алган эмес.

    """)

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

    if "Comment" in display_df.columns:

        display_df = display_df.drop(
            columns=["Comment"]
        )

    st.caption(
        f"📚 Жалпы мисалдар саны: {len(display_df)}"
    )

    search_corpus = st.text_input(
        "🔎 Корпустан издөө"
    )

    if search_corpus:

        display_df = display_df[
            display_df.astype(str).apply(
                lambda row:
                row.str.contains(
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

✨ NLP • Machine Translation • KSTU • 2026 ✨

</div>

""", unsafe_allow_html=True)
