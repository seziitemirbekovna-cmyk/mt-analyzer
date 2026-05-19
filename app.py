import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="NLP Translation Project",
    page_icon="🌸",
    layout="wide"
)

# ================= STYLE =================

# ================= TITLE =================

st.markdown(
    """
    <div style='text-align:center; margin-top:20px;'>

    <h1 style='
        font-size:52px;
        color:#b83280;
        font-weight:700;
        line-height:1.3;
        font-family: Georgia, serif;
    '>

    Машиналык Котормо
    Жана NLP Изилдөө Системасы

    </h1>

    <p style='
        font-size:22px;
        color:#7b506f;
        margin-top:-10px;
        font-family: Poppins, sans-serif;
    '>

    Компьютердик Лингвистика Боюнча
    Дипломдук Долбоор

    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# ================= HERO SECTION =================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2.5])

with col1:

    st.image(
        "https://miro.medium.com/max/1400/1*YM2HXc7f4v02pZBEO8h-qw.png",
        width=170
    )

with col2:

    st.markdown(
        """
        <div style="
            background-color: rgba(255,255,255,0.55);
            padding: 35px;
            border-radius: 30px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        ">

        <h2 style="
            color:#d63384;
            font-size:38px;
            margin-bottom:20px;
            font-family: Georgia, serif;
        ">

        Smart Translation Research

        </h2>

        <p style="
            font-size:19px;
            color:#4a4a4a;
            line-height:1.9;
        ">

        Бул долбоор Google Translate,
        DeepL жана Yandex Translate
        системаларынын котормо сапатын
        салыштырып анализдейт.

        </p>

        <div style="
            font-size:18px;
            color:#5c4b51;
            line-height:2.1;
            margin-top:20px;
        ">

        • Мемдер жана Интернет Сленги <br>
        • Оюн Терминдери <br>
        • Эмоционалдык Сөздөр <br>
        • Идиомалар <br>
        • Кыргыз Макал-Лакаптары <br>
        • Социалдык Тармактардагы Сөздөр

        </div>

        </div>
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

    <h1>

    Машиналык Котормо Системаларын
    Салыштырма Талдоо

    </h1>

    </div>
    """,
    unsafe_allow_html=True
)

# ================= HERO SECTION =================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:

    st.image(
        "https://miro.medium.com/max/1400/1*YM2HXc7f4v02pZBEO8h-qw.png",
        width=180
    )

with col2:

    st.markdown(
        """
        <div style="
            background-color: rgba(255,255,255,0.45);
            padding: 30px;
            border-radius: 25px;
            margin-top: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        ">

        <h2 style="
            color:#d63384;
            margin-bottom:20px;
        ">

        NLP Жана Machine Translation Analysis

        </h2>

        <p style="
            font-size:19px;
            color:#4a4a4a;
            line-height:1.8;
        ">

        Бул долбоор Google Translate,
        DeepL жана Yandex Translate
        системаларын салыштырат.

        </p>

        <div style="
            font-size:18px;
            line-height:2;
            color:#5c4b51;
        ">

        • Мемдер <br>
        • Интернет Сленги <br>
        • Оюн Терминдери <br>
        • Эмоционалдык Сөздөр <br>
        • Идиомалар <br>
        • Кыргыз Макал-Лакаптары

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ================= OPEN BUTTON =================

st.markdown("<br><br>", unsafe_allow_html=True)

start = st.button("Долбоорду Ачуу")

# ================= MAIN PROJECT =================

if start:

    # LOAD DATA

    df = pd.read_csv("corpus.csv")

    # CATEGORY TRANSLATION

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

    # METRICS

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Жалпы Мисалдар", len(df))

    with col2:
        st.metric("Тилдер", 3)

    with col3:
        st.metric("Категориялар", df["Category"].nunique())

    # SEARCH

    search = st.text_input("Издөө")

    if search:
        df = df[df["Expression"].str.contains(search, case=False, na=False)]

    # LANGUAGE

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

    # CATEGORY

    category = st.selectbox(
        "Категория:",
        ["Бардыгы"] + sorted(filtered_df["Category"].unique())
    )

    if category != "Бардыгы":
        filtered_df = filtered_df[
            filtered_df["Category"] == category
        ]

    # EXPRESSION

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
