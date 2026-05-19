import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Машиналык котормо анализатору",
    page_icon="🌐",
    layout="wide"
)

# BACKGROUND
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f6f1ff;
    }

    h1 {
        color: #7c4dff;
    }

    h2, h3 {
        color: #5e35b1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# LOGO
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/2/2e/KSTU_logo.png",
    width=180
)

# SIDEBAR
st.sidebar.title("👩‍🎓 Автор жөнүндө")

st.sidebar.info(
    """
    ✨ Аты-жөнү:
    Сезим Темирбековна
    
    🎓 Адистиги:
    Компьютердик лингвистика
    
    🏫 Университет:
    Кыргыз мамлекеттик техникалык университети
    
    💻 Институт:
    Маалыматтык технологиялар институту
    
    👩‍🏫 Илимий жетекчи:
    Укуева Клара Акиновна
    
    📚 Долбоор:
    Машиналык котормо системаларын салыштырма талдоо
    
    🌐 NLP жана Machine Translation долбоору
    """
)

# HEADER
st.markdown(
    """
    <h1 style='text-align: center;'>
    🌐 Машиналык котормо анализатору
    </h1>
    """,
    unsafe_allow_html=True
)

# NLP IMAGE
st.image(
    "https://miro.medium.com/max/1400/1*YM2HXc7f4v02pZBEO8h-qw.png",
    use_container_width=True
)

st.subheader("📚 Машиналык котормо системаларын салыштырма талдоо")

st.write(
    """
    Бул NLP долбоору Google Translate, DeepL жана
    Yandex Translate аркылуу:
    
    - 😂 мемдерди
    - 🧠 психологиялык терминдерди
    - 💼 business English сөздөрүн
    - 🌍 социалдык тармактардагы сленгдерди
    - 🎮 gaming slang сөздөрүн
    - 📖 идиомаларды
    - 🇰🇬 кыргыз макал-лакаптарын
    
    талдайт жана салыштырат.
    """
)

# INFO
st.info(
    "💡 Машиналык котормо системалары көбүнчө "
    "сленгдерди жана маданий сөз айкаштарын туура эмес которот."
)

# DATA
df = pd.read_csv("corpus.csv")

# METRICS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Жалпы мисалдар", len(df))

with col2:
    st.metric("🌍 Тилдер", df["Language"].nunique())

with col3:
    st.metric("📚 Категориялар", df["Category"].nunique())

# SEARCH
search = st.text_input("🔍 Сөз издөө")

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
    "📚 Категорияны тандаңыз:",
    ["All"] + sorted(filtered_df["Category"].unique())
)

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

expression = st.selectbox(
    "🧠 Сөз айкашын тандаңыз:",
    filtered_df["Expression"]
)

# BUTTON
if st.button("✨ Анализди көрсөтүү"):

    row = filtered_df[
        filtered_df["Expression"] == expression
    ].iloc[0]

    st.subheader("📝 Сөз айкашы")
    st.success(row["Expression"])

    st.subheader("👩 Адам тарабынан которулган")
    st.info(row["Human Translation"])

    st.subheader("🤖 Google Translate")
    st.write(row["Google Translate"])

    st.subheader("💙 DeepL")
    st.write(row["DeepL"])

    st.subheader("🟡 Yandex Translate")
    st.write(row["Yandex Translate"])

    st.subheader("🌍 Тил")
    st.write(row["Language"])

    st.subheader("📚 Категория")
    st.write(row["Category"])

    st.subheader("💬 Комментарий")
    st.warning(row["Comment"])

# DIVIDER
st.divider()

# PIE CHART
st.subheader("📊 Категориялар боюнча бөлүштүрүү")

category_counts = df["Category"].value_counts()

fig1, ax1 = plt.subplots(figsize=(7,7))

category_counts.plot.pie(
    autopct='%1.1f%%',
    ax=ax1
)

st.pyplot(fig1)

# TRANSLATOR RANKING
st.subheader("🏆 Котормо системаларынын рейтинги")

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
st.subheader("⚡ NLP долбоорунун даярдык деңгээли")

st.progress(92)

st.caption(
    "💜 Корпустун жана NLP долбоорунун даярдык көрсөткүчү"
)

# TABLE
st.subheader("📚 Изилдөө корпусу")

styled_df = filtered_df.style.background_gradient(
    cmap="Purples"
)

st.dataframe(
    styled_df,
    use_container_width=True
)

# FOOTER
st.markdown(
    """
    ---
    💜 Streamlit NLP Project | Machine Translation Analysis System
    """
)
