# ================= IMPORT =================

import streamlit as st
import pandas as pd

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
    background:linear-gradient(
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
    background:linear-gradient(
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

.big-title{
    font-size:82px;
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
    line-height:2.1;
    color:#4a4a4a;
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

</style>
""", unsafe_allow_html=True)

# ================= DATA =================

@st.cache_data
def load_data():

    try:
        df = pd.read_csv(
            "corpus.csv",
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

    # FIX SPACES
    df["Category"] = df["Category"].astype(str).str.strip()
    df["Language"] = df["Language"].astype(str).str.strip()

    return df

df = load_data()

# ================= SIDEBAR =================

st.sidebar.markdown("""

<div style="
text-align:center;
padding-top:10px;
">

<img src="
https://kstu.kg/fileadmin/user_upload/kyrg.png
"
width="110">

<h1 style="
color:#c2185b;
font-family:Georgia;
font-size:34px;
">

АКЫЛДУУ
КОТОРМО

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

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""

        <div class="card blue-card">

        <h2>🧠 AI Анализ</h2>

        <p class="info-text">

        Машиналык котормо системаларын
        салыштыруу

        </p>

        </div>

        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""

        <div class="card green-card">

        <h2>📊 Аналитика</h2>

        <p class="info-text">

        Диаграммалар жана статистика

        </p>

        </div>

        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""

        <div class="card purple-card">

        <h2>📚 Корпус</h2>

        <p class="info-text">

        Изилдөө маалыматтары

        </p>

        </div>

        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.success(
        "🎓 Бул дипломдук изилдөө долбоору."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""

    <div class="card">

    <h2 style="text-align:center;">

    🤖 КЫЗЫКТУУ ФАКТЫЛАР

    </h2>

    <p class="info-text">

    • DeepL эмоционалдык сүйлөмдөрдү жакшыраак түшүнөт.

    <br><br>

    • Google Translate техникалык терминдерде жакшы иштейт.

    <br><br>

    • Yandex Translate сленг сөздөрдө көбүрөөк ката кетирет.

    <br><br>

    • Машиналык котормо фразеологизмдерди түз мааниде которгон учурлар көп кездешет.

    </p>

    </div>

    """, unsafe_allow_html=True)

# ================= ABOUT =================

elif page == "👩‍🎓 Автор жөнүндө":

    st.markdown("""

    <div class="card">

    <h1 style="
    text-align:center;
    font-size:55px;
    ">

    👩‍🎓 АВТОР ЖӨНҮНДӨ

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

    🏫 КМТУ им. И. Раззакова

    <br>

    👩‍🏫 Илимий Жетекчи:
    Укуева Клара Акиновна

    <br>

    🤖 NLP • AI • Machine Translation

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

    language = st.selectbox(

        "🌍 ТИЛ ТАНДОО",

        [
            "Кыргызча",
            "English",
            "Русский"
        ]

    )

    filtered_df = df.copy()

    # ================= LANGUAGE FILTER =================

    if language == "Кыргызча":

        filtered_df = filtered_df[
            filtered_df["Language"].str.lower() == "kyrgyz"
        ]

    elif language == "English":

        filtered_df = filtered_df[
            filtered_df["Language"].str.lower() == "english"
        ]

    elif language == "Русский":

        filtered_df = filtered_df[
            filtered_df["Language"].str.lower() == "russian"
        ]

    # ================= SEARCH =================

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

    # ================= CATEGORY =================

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

    # ================= WORD =================

    with col2:

        if len(filtered_df) > 0:

            words = sorted(
                filtered_df["Expression"].dropna().unique()
            )

            expression = st.selectbox(

                "💬 СӨЗ ТАНДОО",

                words

            )

        else:

            expression = None

            st.warning(
                "Маалымат табылган жок."
            )

    # ================= BUTTON =================

    if expression and st.button("📌 АНАЛИЗ КӨРСӨТҮҮ"):

        row = filtered_df[
            filtered_df["Expression"] == expression
        ].iloc[0]

        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2 = st.columns(2)

        with c1:

            st.markdown(f"""

            <div class="card blue-card">

            <h2>💬 Сөз</h2>

            <p class="info-text">
            {row['Expression']}
            </p>

            </div>

            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""

            <div class="card green-card">

            <h2>✅ Human Translation</h2>

            <p class="info-text">
            {row['Human Translation']}
            </p>

            </div>

            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""

            <div class="card blue-card">

            <h2>🌐 Google Translate</h2>

            <p class="info-text">
            {row['Google Translate']}
            </p>

            </div>

            """, unsafe_allow_html=True)

        with c2:

            st.markdown(f"""

            <div class="card purple-card">

            <h2>🧠 DeepL</h2>

            <p class="info-text">
            {row['DeepL']}
            </p>

            </div>

            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""

            <div class="card yellow-card">

            <h2>📘 Yandex Translate</h2>

            <p class="info-text">
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
    ">

    📊 АНАЛИТИКА

    </h1>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🧠 DeepL", "92%")

    with col2:
        st.metric("🌐 Google", "84%")

    with col3:
        st.metric("📘 Yandex", "71%")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📚 Категориялар")

    category_counts = df["Category"].value_counts()

    st.bar_chart(category_counts)

# ================= CORPUS =================

elif page == "📚 Изилдөө корпусу":

    st.markdown("""

    <div class="card">

    <h1 style="
    text-align:center;
    font-size:60px;
    ">

    📚 ИЗИЛДӨӨ КОРПУСУ

    </h1>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    display_df = df.rename(columns={

        "Expression": "Сөз",
        "Human Translation": "Адам Котормосу",
        "Google Translate": "Google",
        "DeepL": "DeepL",
        "Yandex Translate": "Yandex",
        "Language": "Тил",
        "Category": "Категория"

    })

    if "Comment" in display_df.columns:

        display_df = display_df.drop(
            columns=["Comment"]
        )

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
