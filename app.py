```python
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
        to bottom,
        #fff7fb,
        #ffeef6,
        #fff7fb
    );
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
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
    border-radius:18px;
    padding:14px 36px;
    font-size:17px;
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

# ================= HEADER =================

top1, top2 = st.columns([1,4])

with top1:

    st.image(
        "https://kstu.kg/fileadmin/user_upload/russkii_var.png",
        width=140
    )

with top2:

    st.markdown("""
    <div style='
        text-align:center;
        margin-top:10px;
    '>

    <h1 style='
        font-size:56px;
        font-family:Georgia;
        font-weight:700;
        color:#c2185b;
        line-height:1.3;
        letter-spacing:2px;
    '>

    АКЫЛДУУ КОТОРМО
    СИСТЕМАСЫ

    </h1>

    <p style='
        font-size:21px;
        color:#7a5066;
        margin-top:-10px;
        line-height:1.9;
    '>

    Компьютердик Лингвистика боюнча
    Дипломдук Долбоор ✨

    </p>

    </div>
    """, unsafe_allow_html=True)

# ================= HERO =================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
    background:rgba(255,255,255,0.78);
    padding:45px;
    border-radius:35px;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
    backdrop-filter:blur(10px);
">

<h2 style="
    font-size:38px;
    color:#d63384;
    text-align:center;
    font-family:Georgia;
    margin-bottom:25px;
">

NLP ЖАНА МАШИНАЛЫК КОТОРМО ✨

</h2>

<p style="
    font-size:19px;
    line-height:2.1;
    color:#4a4a4a;
    text-align:center;
">

Бул долбоор Google Translate,
DeepL жана Yandex Translate
системаларынын котормо сапатын
салыштырып анализдөөгө арналган.

</p>

<br>

<div style="
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:15px;
    font-size:18px;
    color:#5f4a55;
    line-height:2;
">

<div>💖 Интернет Сленги</div>
<div>💖 Мемдер</div>

<div>💖 Идиомалар</div>
<div>💖 NLP Терминдери</div>

<div>💖 Кыргыз Макал-Лакаптары</div>
<div>💖 Социалдык Тармактар</div>

</div>

</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================

st.sidebar.image(
    "https://kstu.kg/fileadmin/user_upload/russkii_var.png",
    width=180
)

st.sidebar.markdown("""
<h2 style='
    color:#c2185b;
    text-align:center;
'>

ДОЛБООР ЖӨНҮНДӨ ✨

</h2>
""", unsafe_allow_html=True)

st.sidebar.info("""
👩‍🎓 Автор:
Сезим Темирбековна

🎓 Адистик:
Компьютердик Лингвистика

🏫 Университет:
Кыргыз Мамлекеттик
Техникалык Университети

💻 Институт:
Маалыматтык Технологиялар Институту

👩‍🏫 Илимий Жетекчи:
Укуева Клара Акиновна
""")

# ================= BUTTON =================

st.markdown("<br><br>", unsafe_allow_html=True)

start = st.button("🚀 ДОЛБООРДУ АЧУУ")

# ================= PROJECT =================

if start:

    # ================= DATA =================

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

    # ================= EXPRESSION =================

    expression = st.selectbox(
        "💬 СӨЗ АЙКАШЫ",
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
                    f"💬 Сөз Айкашы:\n\n{row['Expression']}"
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
                    f"📝 Комментарий:\n\n{row['Comment']}"
                )

    # ================= TAB 2 =================

    with tab2:

        st.subheader(
            "ИЗИЛДӨӨ КОРПУСУ 📚"
        )

        display_df = filtered_df.rename(columns={

            "Expression": "Сөз Айкашы",
            "Human Translation": "Адам Котормосу",
            "Google Translate": "Google Translate",
            "DeepL": "DeepL",
            "Yandex Translate": "Yandex Translate",
            "Language": "Тил",
            "Category": "Категория",
            "Comment": "Комментарий"

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

        Бул дипломдук долбоор
        машиналык котормо
        системаларын анализдөөгө арналган.

        Изилдөөдө:

        • Google Translate  
        • DeepL  
        • Yandex Translate  

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

