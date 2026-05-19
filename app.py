import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Машиналык котормо анализатору",
    page_icon="🌐",
    layout="wide"
)

# STYLE
st.markdown(
    """
    <style>

    html, body, [class*="css"]  {
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

# SIDEBAR
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

# TITLE
st.markdown(
    """
    <h1>🌐 Машиналык котормо анализатору</h1>
    """,
    unsafe_allow_html=True
)

# IMAGE
st.image(
    "https://miro.medium.com/max/1400/1*YM2HXc7f4v02pZBEO8h-qw.png",
    width=500
)

# DESCRIPTION
st.subheader("📚 NLP жана Machine Translation Analysis")

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

# LOAD CSV
df = pd.read_csv("corpus.csv")

# CATEGORY TRANSLATION
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

# METRICS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Жалпы мисалдар", len(df))

with col2:
    st.metric("🌍 Тилдер", df["Language"].nunique())

with col3:
    st.metric("📚 Категориялар", df["Category"].nunique())

# SEARCH
search = st.text_input("🔍 Издөө")

if search:
    df = df[df["Expression"].str.contains(search, case=False, na=False)]

# FILTERS
language = st.selectbox(
    "🌍 Тилди тандаңыз:",
    ["All"] + sorted(df["Language"].unique())
)

if language != "All":
    filtered_df = df[df["Language"] == language]
else:
    filtered_df = df

category = st.selectbox(
    "📚 Категория:",
    ["All"] + sorted(filtered_df["Category"].unique())
)

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

expression = st.selectbox(
    "🧠 Сөз айкашы:",
    filtered_df["Expression"]
)

# BUTTON
if st.button("✨ Анализ көрсөтүү"):

    row = filtered_df[
        filtered_df["Expression"] == expression
    ].iloc[0]

    st.subheader("📝 Expression")
    st.success(row["Expression"])

    st.subheader("👩 Human Translation")
    st.info(row["Human Translation"])

    st.subheader("🤖 Google Translate")
    st.write(row["Google Translate"])

    st.subheader("💙 DeepL")
    st.write(row["DeepL"])

    st.subheader("🟡 Yandex Translate")
    st.write(row["Yandex Translate"])

    st.subheader("🌍 Language")
    st.write(row["Language"])

    st.subheader("📚 Category")
    st.write(row["Category"])

    st.subheader("💬 Comment")
    st.warning(row["Comment"])

# PIE CHART
st.subheader("📊 Категориялар боюнча бөлүштүрүү")

category_counts = df["Category"].value_counts()

fig1, ax1 = plt.subplots(figsize=(4,4))

category_counts.plot.pie(
    autopct='%1.1f%%',
    ax=ax1
)

st.pyplot(fig1)

# BAR CHART
st.subheader("🏆 Translation System Ranking")

translator_scores = pd.DataFrame({
    "Translator": [
        "DeepL",
        "Google Translate",
        "Yandex Translate"
    ],
    "Accuracy": [
        92,
        84,
        71
    ]
})

st.bar_chart(
    translator_scores.set_index("Translator")
)

# PROGRESS
st.subheader("⚡ Project Progress")

st.progress(92)

st.caption(
    "💜 NLP corpus and machine translation analysis project"
)

# TABLE
st.subheader("📚 Research Corpus")

styled_df = filtered_df.style.background_gradient(
    cmap="Purples"
)

st.dataframe(
    styled_df,
    use_container_width=True
)

# FOOTER
st.markdown("---")

st.markdown(
    """
    💜 Streamlit NLP Project  
    🌐 Machine Translation Analysis System
    """
)
