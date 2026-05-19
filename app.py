import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================= PAGE =================

st.set_page_config(
    page_title="Machine Translation Research",
    page_icon="🧠",
    layout="wide"
)

# ================= STYLE =================

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
    background-color: #fff8fc;
}

.main {
    background: linear-gradient(
        to bottom,
        #fff8fc,
        #ffeef7
    );
}

h1, h2, h3 {
    color:#b83280;
}

.stButton>button {
    background-color:#d63384;
    color:white;
    border:none;
    border-radius:15px;
    padding:12px 28px;
    font-size:17px;
    font-weight:600;
}

.stButton>button:hover {
    background-color:#b83280;
    color:white;
}

[data-testid="stSidebar"] {
    background-color:#fff0f7;
}

</style>
""", unsafe_allow_html=True)

# ================= TOP =================

col1, col2, col3 = st.columns([1,4,1])

with col1:

    st.image(
        "https://kstu.kg/fileadmin/user_upload/russkii_var.png",
        width=140
    )

with col2:

    st.markdown("""
    <div style='text-align:center;'>

    <h1 style='
        font-size:55px;
        font-family:Georgia;
        line-height:1.3;
        color:#c2185b;
    '>

    Машиналык Котормо
    Анализ Системасы

    </h1>

    <p style='
        font-size:24px;
        color:#7a4f65;
        margin-top:-10px;
    '>

    Компьютердик Лингвистика боюнча
    Дипломдук Долбоор 🎓

    </p>

    </div>
    """, unsafe_allow_html=True)

# ================= HERO =================

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([1,2.2])

with left:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=260
    )

with right:

    st.markdown("""
    <div style="
        background-color:rgba(255,255,255,0.75);
        padding:35px;
        border-radius:30px;
        box-shadow:0 6px 20px rgba(0,0,0,0.08);
    ">

    <h2 style="
        color:#d63384;
        font-size:38px;
        font-family:Georgia;
    ">

    NLP & Translation Research 🌸

    </h2>

    <p style="
        font-size:19px;
        line-height:2;
        color:#4a4a4a;
    ">

    Бул долбоор Google Translate,
    DeepL жана Yandex Translate
    системаларынын котормо сапатын
    салыштырып анализдейт.

    </p>

    <div style="
        font-size:18px;
        line-height:2.2;
        color:#5a5a5a;
        margin-top:20px;
    ">

    ✨ Интернет Сленги <br>
    ✨ Мемдер <br>
    ✨ Идиомалар <br>
    ✨ NLP Терминдери <br>
    ✨ Кыргыз Макал-Лакаптары <br>
    ✨ Социалдык Тармактар

    </div>

    </div>
    """, unsafe_allow_html=True)

# ================= SIDEBAR =================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=130
)

st.sidebar.title("Автор Жөнүндө 💖")

st.sidebar.info("""
👩‍🎓 Аты-Жөнү:
Сезим Темирбековна

🎓 Адистиги:
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

start = st.button("🚀 Долбоорду Ачуу")

# ================= PROJECT =================

if start:

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

    # ================= METRICS =================

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📚 Жалпы Мисалдар", len(df))

    with col2:
        st.metric("🌍 Тилдер", 3)

    with col3:
        st.metric(
            "🧩 Категориялар",
            df["Category"].nunique()
        )

    # ================= SEARCH =================

    st.markdown("## 🔎 Издөө")

    search = st.text_input(
        "Сөз же фраза жазыңыз"
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
        "🌍 Тилди Тандаңыз",
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
        "🧩 Категория",
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
        "💬 Сөз Айкашы",
        filtered_df["Expression"]
    )

    # ================= TABS =================

    tab1, tab2, tab3, tab4 = st.tabs([
        "📖 Анализ",
        "📚 Корпус",
        "📊 Диаграммалар",
        "💡 Долбоор"
    ])

    # ================= TAB 1 =================

    with tab1:

        st.subheader("Котормо Анализи ✨")

        if st.button("📌 Анализ Көрсөтүү"):

            row = filtered_df[
                filtered_df["Expression"] == expression
            ].iloc[0]

            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"💬 Сөз Айкашы:\n\n{row['Expression']}"
                )

                st.success(
                    f"✅ Адам Котормосу:\n\n{row['Human Translation']}"
                )

                st.write(
                    f"🌐 Google Translate:\n\n{row['Google Translate']}"
                )

            with col2:

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

        st.subheader("Изилдөө Корпусу 📚")

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
            "Категориялар Боюнча Бөлүштүрүү 📊"
        )

        category_counts = df["Category"].value_counts()

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
            "Котормо Системаларынын Рейтинги 🏆"
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

        st.subheader("Долбоор Жөнүндө 💖")

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
<div style="
    text-align:center;
    color:gray;
    font-size:17px;
    padding:10px;
">

✨ Machine Translation Research Project ✨

</div>
""", unsafe_allow_html=True)
