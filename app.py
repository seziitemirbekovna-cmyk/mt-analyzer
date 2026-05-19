```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Машиналык котормо анализатору",
    page_icon="🌐",
    layout="wide"
)

# ================= STYLE =================

st.markdown(
    """
    <style>

    html, body, [class*="css"] {
        font-family: 'Trebuchet MS', sans-serif;
    }

    .stApp {
        background-color: #f6f1ff;
    }

    h1 {
        color: #7c4dff;
        font-size: 52px;
        font-weight: bold;
        text-align: center;
    }

    h2, h3 {
        color: #5e35b1;
    }

    .stButton>button {
        background-color: #b39ddb;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 240px;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #9575cd;
        color: white;
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

st.sidebar.title("👩‍🎓 Автор жөнүндө")

st.sidebar.info(
    """
    ✨ Аты-жөнү:
    Сезим Тумобаева

    🎓 Адистиги:
    Компьютердик лингвистика

    🏫 Университет:
    Кыргыз мамлекеттик техникалык университети

    💻 Институт:
    Маалыматтык технологиялар институту

    👩‍🏫 Илимий жетекчи:
    Куоева Клара Акеновна

    📚 Долбоор:
    Машиналык котормо системаларын салыштырма талдоо
    """
)

# ================= TITLE =================

st.markdown(
    """
    <h1>🌐 Машиналык котормо анализатору</h1>
    """,
    unsafe_allow_html=True
)

# ================= IMAGE =================

st.image(
    "https://miro.medium.com/max/1400/1*YM2HXc7f4v02pZBEO8h-qw.png",
    width=250
)

# ================= DESCRIPTION =================

st.write(
    """
    Бул долбоор Google Translate, DeepL жана
    Yandex Translate системаларын салыштырат.

    Система:
    - 😂 мемдерди
    - 📱 интернет сленгди
    - 🎮 оюн терминдерин
    - 💔 эмоционалдык сөздөрдү
    - 📖 идиомаларды
    - 🇰🇬 кыргыз макал-лакаптарын

    анализдейт.
    """
)

# ================= LOAD DATA =================

df = pd.read_csv("corpus.csv")

# ================= CATEGORY TRANSLATION =================

df["Category"] = df["Category"].replace({
    "Business English": "💼 Бизнес англис тили",
    "Psychology": "🧠 Психология",
    "Emotional Expressions": "💔 Эмоционалдык сөздөр",
    "Memes": "😂 Мемдер",
    "Internet Slang": "🌍 Интернет сленги",
    "Social Media": "📱 Социалдык тармактар",
    "Gaming Slang": "🎮 Оюн сленги",
    "Idioms": "📖 Идиомалар",
    "Kyrgyz Proverbs": "🇰🇬 Кыргыз макал-лакаптары",
    "Kyrgyz Expressions": "🗣 Кыргыз сөз айкаштары",
    "Technical NLP": "🤖 NLP терминдери"
})

# ================= METRICS =================

language_count = 3

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Жалпы мисалдар", len(df))

with col2:
    st.metric("🌍 Тилдер", language_count)

with col3:
    st.metric("📚 Категориялар", df["Category"].nunique())

# ================= SEARCH =================

search = st.text_input("🔍 Издөө")

if search:
    df = df[df["Expression"].str.contains(search, case=False, na=False)]

# ================= FILTERS =================

language = st.selectbox(
    "🌍 Тилди тандаңыз:",
    ["Бардыгы"] + sorted(df["Language"].unique())
)

if language != "Бардыгы":
    filtered_df = df[df["Language"] == language]
else:
    filtered_df = df

category = st.selectbox(
    "📚 Категория:",
    ["Бардыгы"] + sorted(filtered_df["Category"].unique())
)

if category != "Бардыгы":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

expression = st.selectbox(
    "🧠 Сөз айкашы:",
    filtered_df["Expression"]
)

# ================= TABS =================

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Анализ",
    "📚 Корпус",
    "📈 Диаграммалар",
    "ℹ️ Долбоор жөнүндө"
])

# ================= TAB 1 =================

with tab1:

    st.subheader("🧠 Котормо анализи")

    if st.button("✨ Анализ көрсөтүү"):

        row = filtered_df[
            filtered_df["Expression"] == expression
        ].iloc[0]

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                f"📝 Сөз айкашы:\n\n{row['Expression']}"
            )

            st.success(
                f"👩 Адам котормосу:\n\n{row['Human Translation']}"
            )

            st.write(
                f"🤖 Google Translate:\n\n{row['Google Translate']}"
            )

        with col2:

            st.write(
                f"💙 DeepL:\n\n{row['DeepL']}"
            )

            st.write(
                f"🟡 Yandex Translate:\n\n{row['Yandex Translate']}"
            )

            st.warning(
                f"💬 Комментарий:\n\n{row['Comment']}"
            )

# ================= TAB 2 =================

with tab2:

    st.subheader("📚 Изилдөө корпусу")

    filtered_df_display = filtered_df.rename(columns={
        "Expression": "Сөз айкашы",
        "Human Translation": "Адам котормосу",
        "Google Translate": "Google Translate",
        "DeepL": "DeepL",
        "Yandex Translate": "Yandex Translate",
        "Language": "Тил",
        "Category": "Категория",
        "Comment": "Комментарий"
    })

    styled_df = filtered_df_display.style.background_gradient(
        cmap="Purples"
    )

    st.dataframe(
        styled_df,
        use_container_width=True
    )

# ================= TAB 3 =================

with tab3:

    st.subheader("📊 Категориялар боюнча бөлүштүрүү")

    category_counts = df["Category"].value_counts()

    clean_labels = [
        label.replace("💼", "")
             .replace("🧠", "")
             .replace("💔", "")
             .replace("😂", "")
             .replace("🌍", "")
             .replace("📱", "")
             .replace("🎮", "")
             .replace("📖", "")
             .replace("🇰🇬", "")
             .replace("🗣", "")
             .replace("🤖", "")
        for label in category_counts.index
    ]

    fig1, ax1 = plt.subplots(figsize=(5,5))

    ax1.pie(
        category_counts,
        labels=clean_labels,
        autopct='%1.1f%%'
    )

    st.pyplot(fig1)

    st.subheader("🏆 Котормо системаларынын рейтинги")

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

    st.subheader("ℹ️ Долбоор жөнүндө")

    st.write(
        """
        Бул NLP долбоору машиналык котормо
        системаларын салыштырат.

        Изилдөөдө:
        - Google Translate
        - DeepL
        - Yandex Translate

        системалары колдонулган.

        Долбоор интернет сленг,
        мемдер, эмоционалдык сөздөр,
        кыргыз макал-лакаптары жана
        идиомаларды анализдейт.
        """
    )

    st.progress(92)

    st.success(
        "💜 Компьютердик лингвистика боюнча дипломдук долбоор"
    )

# ================= FOOTER =================

st.markdown("---")

st.markdown(
    """
    💜 Streamlit NLP Project  
    🌐 Machine Translation Analysis System
    """
)
```
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
        color: #ff4f8b;
        font-size: 58px;
        font-weight: 700;
        text-align: center;
    }

    h2, h3 {
        color: #d63384;
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
        box-shadow: 0 4px 15px rgba(255,105,135,0.3);
    }

    .stButton>button:hover {
        background: linear-gradient(
            90deg,
            #ff4f8b,
            #ff6fa5
        );

        color: white;
        transform: scale(1.03);
        transition: 0.3s;
    }

    div[data-baseweb="select"] {
        background-color: white;
        border-radius: 12px;
    }

    .stTextInput input {
        border-radius: 12px;
        border: 2px solid #ffb3c6;
    }

    .stMetric {
        background-color: rgba(255,255,255,0.6);
        padding: 15px;
        border-radius: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
