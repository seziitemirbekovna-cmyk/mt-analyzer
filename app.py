import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="NLP Translation Project",
    page_icon="🌸",
    layout="wide"
)

# ================= STYLE =================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(
            135deg,
            #fff0f6,
            #fce4ec,
            #f8bbd0
        );
    }

    h1 {
        color: #d63384;
        font-size: 58px;
        font-weight: 700;
        text-align: center;
    }

    h2, h3 {
        color: #c2185b;
        font-weight: 600;
    }

    section[data-testid="stSidebar"] {
        background-color: #ffe3ec;
    }

    .stButton>button {
        background: linear-gradient(
            90deg,
            #ff6fa5,
            #ff8fab
        );

        color: white;
        border-radius: 15px;
        height: 3.2em;
        width: 250px;
        font-size: 18px;
        font-weight: 600;
        border: none;
    }

    .stButton>button:hover {
        background: linear-gradient(
            90deg,
            #ff4f8b,
            #ff6fa5
        );

        color: white;
    }

    .stMetric {
        background-color: rgba(255,255,255,0.5);
        padding: 15px;
        border-radius: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ================= SIDEBAR =================

st.sidebar.image(
    "https://kstu.kg/fileadmin/user_upload/russkii_var.png",
    width=220
)

st.sidebar.title("Автор Жөнүндө")

st.sidebar.info(
    """
    ✨ Аты-Жөнү:
    Сезим Темирбековна

    🎓 Адистиги:
    Компьютердик Лингвистика

    🏫 Университет:
    Кыргыз Мамлекеттик Техникалык Университети

    💻 Институт:
    Маалыматтык Технологиялар Институту

    👩‍🏫 Илимий Жетекчи:
    Укуева Клара Акиновна
    """
)

# ================= TITLE =================

st.markdown(
    """
    <div style='text-align:center; margin-top:20px;'>

    <h1 style='
        color:#d63384;
        font-size:58px;
        font-weight:700;
        line-height:1.2;
    '>

    Машиналык Котормо
    Системаларын
    Салыштырма Талдоо

    </h1>

    <p style='
        font-size:24px;
        color:#7a4b6a;
        margin-top:-10px;
        font-weight:500;
    '>

    Компьютердик Лингвистика Боюнча
    NLP Изилдөө Долбоору

    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# ================= HERO SECTION =================

col1, col2 = st.columns([1,2])

with col1:

    st.image(
        "https://miro.medium.com/max/1400/1*YM2HXc7f4v02pZBEO8h-qw.png",
        width=180
    )

with col2:

    st.markdown(
        """
        <div style="
            background-color: rgba(255,255,255,0.5);
            padding: 25px;
            border-radius: 20px;
            margin-top: 20px;
        ">

        <h3 style="color:#d63384;">
        NLP Жана Machine Translation Analysis
        </h3>

        <p style="font-size:18px;">

        Бул долбоор Google Translate,
        DeepL жана Yandex Translate
        системаларын салыштырат.

        </p>

        <p style="font-size:17px;">

        Мемдер <br>
        Интернет Сленги <br>
        Оюн Терминдери <br>
        Эмоционалдык Сөздөр <br>
        Идиомалар <br>
        Кыргыз Макал-Лакаптары

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# ================= LOAD DATA =================

df = pd.read_csv("corpus.csv")

# ================= CATEGORY TRANSLATION =================

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

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Жалпы Мисалдар", len(df))

with col2:
    st.metric("Тилдер", 3)

with col3:
    st.metric("Категориялар", df["Category"].nunique())

# ================= SEARCH =================

search = st.text_input("Издөө")

if search:
    df = df[df["Expression"].str.contains(search, case=False, na=False)]

# ================= LANGUAGE =================

language_mapping = {
    "English": "Англисче",
    "Kyrgyz": "Кыргызча",
    "Russian": "Орусча"
}

language_options = ["Бардыгы"] + [
    language_mapping.get(lang, lang)
    for lang in sorted(df["Language"].unique())
]

selected_language = st.selectbox(
    "Тилди Тандаңыз:",
    language_options
)

reverse_mapping = {
    v: k for k, v in language_mapping.items()
}

if selected_language != "Бардыгы":
    real_language = reverse_mapping[selected_language]
    filtered_df = df[df["Language"] == real_language]
else:
    filtered_df = df

# ================= CATEGORY =================

category = st.selectbox(
    "Категория:",
    ["Бардыгы"] + sorted(filtered_df["Category"].unique())
)

if category != "Бардыгы":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

# ================= EXPRESSION =================

expression = st.selectbox(
    "Сөз Айкашы:",
    filtered_df["Expression"]
)

# ================= TABS =================

tab1, tab2, tab3, tab4 = st.tabs([
    "Анализ",
    "Корпус",
    "Диаграммалар",
    "Долбоор Жөнүндө"
])

# ================= TAB 1 =================

with tab1:

    st.subheader("Котормо Анализи")

    if st.button("Анализ Көрсөтүү"):

        row = filtered_df[
            filtered_df["Expression"] == expression
        ].iloc[0]

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                f"Сөз Айкашы:\n\n{row['Expression']}"
            )

            st.success(
                f"Адам Котормосу:\n\n{row['Human Translation']}"
            )

            st.write(
                f"Google Translate:\n\n{row['Google Translate']}"
            )

        with col2:

            st.write(
                f"DeepL:\n\n{row['DeepL']}"
            )

            st.write(
                f"Yandex Translate:\n\n{row['Yandex Translate']}"
            )

            st.warning(
                f"Комментарий:\n\n{row['Comment']}"
            )

# ================= TAB 2 =================

with tab2:

    st.subheader("Изилдөө Корпусу")

    filtered_df_display = filtered_df.rename(columns={
        "Expression": "Сөз Айкашы",
        "Human Translation": "Адам Котормосу",
        "Google Translate": "Google Translate",
        "DeepL": "DeepL",
        "Yandex Translate": "Yandex Translate",
        "Language": "Тил",
        "Category": "Категория",
        "Comment": "Комментарий"
    })

    styled_df = filtered_df_display.style.background_gradient(
        cmap="RdPu"
    )

    st.dataframe(
        styled_df,
        use_container_width=True
    )

# ================= TAB 3 =================

with tab3:

    st.subheader("Категориялар Боюнча Бөлүштүрүү")

    category_counts = df["Category"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(5,5))

    ax1.pie(
        category_counts,
        labels=category_counts.index,
        autopct='%1.1f%%'
    )

    st.pyplot(fig1)

    st.subheader("Котормо Системаларынын Рейтинги")

    translator_scores = pd.DataFrame({
        "Котормочу": [
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
        translator_scores.set_index("Котормочу")
    )

# ================= TAB 4 =================

with tab4:

    st.subheader("Долбоор Жөнүндө")

    st.write(
        """
        Бул NLP долбоору машиналык
        котормо системаларын салыштырат.

        Изилдөөдө:
        - Google Translate
        - DeepL
        - Yandex Translate

        системалары колдонулган.
        """
    )

    st.progress(92)

    st.success(
        "Компьютердик Лингвистика Боюнча Дипломдук Долбоор"
    )

# ================= FOOTER =================

st.markdown("---")

st.markdown(
    """
    NLP Translation Research Project
    """
)

