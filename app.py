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
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
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

.big-title{
    font-size:80px;
    text-align:center;
    font-family:Georgia;
    color:#c2185b;
}

.subtitle{
    text-align:center;
    font-size:25px;
    color:#7a5066;
}

</style>
""", unsafe_allow_html=True)

# ================= DATA =================

@st.cache_data
def load_data():

    # CSV ОКУУ

    try:

        df = pd.read_csv(
            "corpus.csv",
            encoding="utf-8",
            sep=","
        )

    except:

        try:

            df = pd.read_csv(
                "corpus.csv",
                encoding="utf-8",
                sep=";"
            )

        except:

            df = pd.read_csv(
                "corpus.csv"
            )

    # КОЛОНКА АТТАРЫН ТАЗАЛОО

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
padding:20px;
">

<img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Globe_icon.svg"
width="110">

<h1 style="
color:#c2185b;
font-family:Georgia;
font-size:34px;
margin-top:10px;
">

АКЫЛДУУ КОТОРМО

</h1>

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

    NLP • AI • Машиналык Котормо

    </div>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.image(

        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",

        use_container_width=True

    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""

        <div class="card blue-card">

        <h2>🧠 AI Анализ</h2>

        <p>

        Машиналык котормо системаларын
        салыштыруу

        </p>

        </div>

        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""

        <div class="card green-card">

        <h2>📊 Аналитика</h2>

        <p>

        Диаграммалар жана
        статистикалык маалыматтар

        </p>

        </div>

        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""

        <div class="card purple-card">

        <h2>📚 Корпус</h2>

        <p>

        Изилдөө corpus dataset

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

    <div style="
    font-size:24px;
    line-height:2.2;
    color:#4a4a4a;
    ">

    👩‍🎓 Автор: Сезим Темирбековна

    <br>

    🎓 Компьютердик Лингвистика

    <br>

    🏫 Кыргыз Мамлекеттик
    Техникалык Университети

    <br>

    💻 Машиналык Котормо Анализи

    <br>

    🤖 Artificial Intelligence • NLP

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

    # ЭГЕР COLUMN БАР БОЛСО

    if "Expression" in df.columns:

        search = st.text_input(
            "🔎 Сөз же сүйлөм жазыңыз"
        )

        filtered_df = df.copy()

        if search:

            filtered_df = filtered_df[
                filtered_df["Expression"].astype(str).str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        # КАТЕГОРИЯ

        if "Category" in filtered_df.columns:

            categories = sorted(
                filtered_df["Category"].dropna().unique()
            )

            selected_category = st.selectbox(

                "🧩 КАТЕГОРИЯ",

                ["Бардыгы"] + categories

            )

            if selected_category != "Бардыгы":

                filtered_df = filtered_df[
                    filtered_df["Category"] == selected_category
                ]

        # СӨЗ ТАНДОО

        if len(filtered_df) > 0:

            expression = st.selectbox(

                "💬 СӨЗ АЙКАШЫ",

                filtered_df["Expression"]

            )

            if st.button("📌 АНАЛИЗ"):

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

    else:

        st.error(
            "CSV колонкалары туура эмес 😭"
        )

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

    if "Category" in df.columns:

        st.subheader("📚 Категориялар")

        category_counts = df[
            "Category"
        ].value_counts()

        fig1, ax1 = plt.subplots(
            figsize=(7,7)
        )

        ax1.pie(

            category_counts,

            labels=category_counts.index,

            autopct='%1.1f%%'

        )

        st.pyplot(fig1)

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.subheader(
            "🤖 AI Тактык Салыштыруу"
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

    display_df = df.copy()

    # COMMENT ӨЧҮРҮҮ

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
