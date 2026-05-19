# ================= IMPORT =================

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

# ================= SESSION =================

if "page" not in st.session_state:
    st.session_state.page = "welcome"

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

</style>
""", unsafe_allow_html=True)

# ================= WELCOME PAGE =================

if st.session_state.page == "welcome":

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        background:rgba(255,255,255,0.78);
        padding:70px 50px;
        border-radius:40px;
        box-shadow:0 15px 40px rgba(0,0,0,0.08);
    ">

    <img src="https://kstu.kg/fileadmin/user_upload/russkii_var.png"
    width="140">

    <br><br>

    <h1 style="
        font-size:68px;
        font-family:Georgia;
        line-height:1.3;
        color:#c2185b;
        letter-spacing:2px;
    ">

    АКЫЛДУУ КОТОРМО
    СИСТЕМАСЫ

    </h1>

    <p style="
        font-size:24px;
        color:#7a5066;
        margin-top:15px;
        line-height:2;
    ">

    AI • NLP • MACHINE TRANSLATION

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2,1,2])

    with c2:

        if st.button("🚀 БАШТОО"):

            with st.spinner("Система жүктөлүүдө..."):

                time.sleep(2)

            st.session_state.page = "about"
            st.rerun()

# ================= ABOUT PAGE =================

elif st.session_state.page == "about":

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:rgba(255,255,255,0.82);
        padding:45px;
        border-radius:35px;
        box-shadow:0 12px 30px rgba(0,0,0,0.08);
    ">

    <h1 style="
        text-align:center;
        font-family:Georgia;
        font-size:50px;
        color:#c2185b;
    ">

    ДОЛБООР ЖӨНҮНДӨ ✨

    </h1>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1,2])

    with left:

        st.markdown("""
        <div style="
            background:white;
            padding:30px;
            border-radius:30px;
            text-align:center;
            box-shadow:0 8px 20px rgba(0,0,0,0.08);
        ">

        <img src="https://kstu.kg/fileadmin/user_upload/russkii_var.png"
        width="160">

        <h2 style="
            margin-top:25px;
            color:#c2185b;
        ">

        КМТУ

        </h2>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div style="
            background:white;
            padding:35px;
            border-radius:30px;
            box-shadow:0 8px 20px rgba(0,0,0,0.08);
        ">

        <div style="
            font-size:20px;
            line-height:2.4;
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

    st.markdown("<br><br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2,1,2])

    with c2:

        if st.button("✨ СИСТЕМАГА ӨТҮҮ"):

            st.session_state.page = "system"
            st.rerun()

# ================= MAIN SYSTEM =================

elif st.session_state.page == "system":

    st.sidebar.markdown("""
    # АКЫЛДУУ КОТОРМО ✨
    """)

    # ================= LOAD DATA =================

    try:

        df = pd.read_csv("corpus.csv")

    except:

        st.error("❌ corpus.csv файлы табылган жок")
        st.stop()

    # ================= CATEGORY =================

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

    # ================= TITLE =================

    st.markdown("""
    <div style="
        text-align:center;
        background:rgba(255,255,255,0.78);
        padding:40px;
        border-radius:35px;
        box-shadow:0 10px 25px rgba(0,0,0,0.08);
    ">

    <h1 style="
        font-size:52px;
        font-family:Georgia;
        color:#c2185b;
    ">

    NLP ЖАНА
    МАШИНАЛЫК КОТОРМО ✨

    </h1>

    </div>
    """, unsafe_allow_html=True)

    # ================= METRICS =================

    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "📚 Жалпы Мисалдар",
            len(df)
        )

    with m2:
        st.metric(
            "🌍 Тилдер",
            3
        )

    with m3:
        st.metric(
            "🧩 Категориялар",
            df["Category"].nunique()
        )

    # ================= SEARCH =================

    st.markdown("## 🔎 ИЗДӨӨ")

    search = st.text_input(
        "Сөз же сүйлөм жазыңыз"
    )

    if search:

        df = df[
            df["Expression"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    # ================= LANGUAGE =================

    language_map = {

        "English": "Англисче",
        "Russian": "Орусча",
        "Kyrgyz": "Кыргызча"

    }

    language_options = ["Бардыгы"] + [

        language_map.get(lang, lang)
        for lang in sorted(df["Language"].unique())

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

        filtered_df = df[
            df["Language"] == real_lang
        ]

    else:

        filtered_df = df

    # ================= CATEGORY FILTER =================

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

    # ================= EMPTY =================

    if filtered_df.empty:

        st.warning("Маалымат табылган жок")
        st.stop()

    # ================= EXPRESSION =================

    expression = st.selectbox(
        "💬 МИСАЛ",
        filtered_df["Expression"]
    )

    # ================= TABS =================

    tab1, tab2, tab3, tab4 = st.tabs([

        "📖 АНАЛИЗ",
        "📚 КОРПУС",
        "📊 ДИАГРАММАЛАР",
        "💡 ДОЛБООР"

    ])

    # ================= TAB 1 =================

    with tab1:

        st.subheader(
            "КОТОРМО АНАЛИЗИ ✨"
        )

        if st.button(
            "📌 АНАЛИЗ КӨРСӨТҮҮ"
        ):

            row = filtered_df[
                filtered_df["Expression"] == expression
            ].iloc[0]

            c1, c2 = st.columns(2)

            with c1:

                st.info(
                    f"💬 Мисал:\n\n{row['Expression']}"
                )

                st.success(
                    f"✅ Адам Котормосу:\n\n{row['Human Translation']}"
                )

                st.write(
                    f"🌐 Google Translate:\n\n{row['Google Translate']}"
                )

            with c2:

                st.write(
                    f"🧠 DeepL:\n\n{row['DeepL']}"
                )

                st.write(
                    f"📘 Yandex Translate:\n\n{row['Yandex Translate']}"
                )

                st.warning(
                    f"📝 Түшүндүрмө:\n\n{row['Comment']}"
                )

    # ================= TAB 2 =================

    with tab2:

        st.subheader(
            "ИЗИЛДӨӨ КОРПУСУ 📚"
        )

        display_df = filtered_df.rename(columns={

            "Expression": "Мисалдар",
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

    # ================= TAB 3 =================

    with tab3:

        st.subheader(
            "КАТЕГОРИЯЛАР БОЮНЧА БӨЛҮШТҮРҮҮ 📊"
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
            autopct='%1.1f%%'
        )

        st.pyplot(fig1)

        st.subheader(
            "КОТОРМО СИСТЕМАЛАРЫНЫН РЕЙТИНГИ 🏆"
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

    # ================= TAB 4 =================

    with tab4:

        st.subheader(
            "ДОЛБООР ЖӨНҮНДӨ 💖"
        )

        st.write("""

        Бул долбоор машиналык котормо
        системаларын анализдөөгө арналган.

        Изилдөөдө Google Translate,
        DeepL жана Yandex Translate
        системалары колдонулган.

        """)

        st.progress(92)

        st.success(
            "🎓 Компьютердик Лингвистика Долбоору"
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

✨ АКЫЛДУУ КОТОРМО СИСТЕМАСЫ ✨

</div>
""", unsafe_allow_html=True)
