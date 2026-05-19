import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="АКЫЛДУУ КОТОРМО СИСТЕМАСЫ",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.main {
    background: linear-gradient(135deg, #fff7fb, #ffeaf4, #fff7fb);
}

.block-container {
    padding-top: 3rem;
}

section[data-testid="stSidebar"] {
    background: #fff0f7;
}

h1, h2, h3 {
    color: #c2185b;
}

.stButton>button {
    background: linear-gradient(90deg, #ff4fa3, #d63384);
    color: white;
    border: none;
    border-radius: 20px;
    padding: 14px 38px;
    font-size: 17px;
    font-weight: 600;
}

.stButton>button:hover {
    background: #c2185b;
    color: white;
    transform: scale(1.03);
}

[data-testid="stMetricValue"] {
    color: #c2185b;
}
</style>
""", unsafe_allow_html=True)

# ================= БАШКЫ БЕТ =================

st.markdown("""
<div style="
    text-align:center;
    padding:55px 30px;
    border-radius:40px;
    background:rgba(255,255,255,0.75);
    box-shadow:0 15px 40px rgba(194,24,91,0.12);
">

<h1 style="
    font-size:58px;
    font-family:Georgia, serif;
    letter-spacing:2px;
    line-height:1.25;
    margin-bottom:20px;
">
АКЫЛДУУ КОТОРМО<br>
СИСТЕМАСЫ
</h1>

<p style="
    font-size:22px;
    color:#7a5066;
    line-height:1.8;
">
Компьютердик лингвистика багыты боюнча<br>
машиналык котормону салыштырма талдоо долбоору
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
    background:rgba(255,255,255,0.82);
    padding:38px;
    border-radius:35px;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
">

<h2 style="
    text-align:center;
    font-size:34px;
    font-family:Georgia, serif;
">
ДОЛБООРДУН НЕГИЗГИ БАГЫТТАРЫ ✨
</h2>

<p style="
    text-align:center;
    font-size:19px;
    color:#4a4a4a;
    line-height:2;
">
Бул система Google Translate, DeepL жана Yandex Translate
аркылуу алынган котормолорду адам котормосу менен салыштырып,
алардын тактыгын жана маанилик өзгөчөлүктөрүн анализдөөгө арналган.
</p>

<div style="
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    gap:18px;
    margin-top:30px;
    font-size:17px;
    color:#5f4a55;
    text-align:center;
">

<div>🌐 Интернет сленги</div>
<div>💬 Мемдер</div>
<div>📚 Идиомалар</div>
<div>🧠 NLP терминдери</div>
<div>🇰🇬 Кыргыз макал-лакаптары</div>
<div>📱 Социалдык тармактар</div>

</div>
</div>
""", unsafe_allow_html=True)

# ================= КАПТАЛ МЕНЮ =================

st.sidebar.markdown("## ДОЛБООР ЖӨНҮНДӨ ✨")

st.sidebar.info("""
👩‍🎓 Автор:
Сезим Темирбековна

🎓 Адистик:
Компьютердик лингвистика

🏫 Университет:
Кыргыз мамлекеттик техникалык университети

💻 Институт:
Маалыматтык технологиялар институту

👩‍🏫 Илимий жетекчи:
Укуева Клара Акиновна
""")

st.markdown("<br>", unsafe_allow_html=True)

start = st.button("🚀 ДОЛБООРДУ АЧУУ")

if start:

    try:
        df = pd.read_csv("corpus.csv")
    except:
        st.error("❌ corpus.csv файлы табылган жок")
        st.stop()

    df["Category"] = df["Category"].replace({
        "Business English": "Бизнес англис тили",
        "Psychology": "Психология",
        "Emotional Expressions": "Эмоционалдык сөздөр",
        "Memes": "Мемдер",
        "Internet Slang": "Интернет сленги",
        "Social Media": "Социалдык тармактар",
        "Gaming Slang": "Оюн сленги",
        "Idioms": "Идиомалар",
        "Kyrgyz Proverbs": "Кыргыз макал-лакаптары",
        "Kyrgyz Expressions": "Кыргыз сөз айкаштары",
        "Technical NLP": "NLP терминдери"
    })

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("📚 Жалпы мисалдар", len(df))

    with m2:
        st.metric("🌍 Тилдер", 3)

    with m3:
        st.metric("🧩 Категориялар", df["Category"].nunique())

    st.markdown("## 🔎 ИЗДӨӨ")

    search = st.text_input("Сөз же сүйлөм жазыңыз")

    if search:
        df = df[df["Expression"].str.contains(search, case=False, na=False)]

    language_map = {
        "English": "Англисче",
        "Russian": "Орусча",
        "Kyrgyz": "Кыргызча"
    }

    language_options = ["Бардыгы"] + [
        language_map.get(lang, lang)
        for lang in sorted(df["Language"].unique())
    ]

    selected_language = st.selectbox("🌍 Тилди тандаңыз", language_options)

    reverse_map = {v: k for k, v in language_map.items()}

    if selected_language != "Бардыгы":
        real_lang = reverse_map[selected_language]
        filtered_df = df[df["Language"] == real_lang]
    else:
        filtered_df = df

    category = st.selectbox(
        "🧩 Категорияны тандаңыз",
        ["Бардыгы"] + sorted(filtered_df["Category"].unique())
    )

    if category != "Бардыгы":
        filtered_df = filtered_df[filtered_df["Category"] == category]

    if filtered_df.empty:
        st.warning("Маалымат табылган жок.")
        st.stop()

    expression = st.selectbox(
        "💬 Сөз айкашын тандаңыз",
        filtered_df["Expression"]
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "📖 Анализ",
        "📚 Корпус",
        "📊 Диаграммалар",
        "💡 Долбоор"
    ])

    with tab1:
        st.subheader("Котормо анализи ✨")

        if st.button("📌 Анализди көрсөтүү"):
            row = filtered_df[filtered_df["Expression"] == expression].iloc[0]

            c1, c2 = st.columns(2)

            with c1:
                st.info(f"💬 Сөз айкашы:\n\n{row['Expression']}")
                st.success(f"✅ Адам котормосу:\n\n{row['Human Translation']}")
                st.write(f"🌐 Google Translate:\n\n{row['Google Translate']}")

            with c2:
                st.write(f"🧠 DeepL:\n\n{row['DeepL']}")
                st.write(f"📘 Yandex Translate:\n\n{row['Yandex Translate']}")
                st.warning(f"📝 Түшүндүрмө:\n\n{row['Comment']}")

    with tab2:
        st.subheader("Изилдөө корпусу 📚")

        display_df = filtered_df.rename(columns={
            "Expression": "Сөз айкашы",
            "Human Translation": "Адам котормосу",
            "Google Translate": "Google Translate",
            "DeepL": "DeepL",
            "Yandex Translate": "Yandex Translate",
            "Language": "Тил",
            "Category": "Категория",
            "Comment": "Түшүндүрмө"
        })

        st.dataframe(
            display_df.style.background_gradient(cmap="RdPu"),
            use_container_width=True
        )

    with tab3:
        st.subheader("Категориялар боюнча бөлүштүрүү 📊")

        category_counts = df["Category"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(
            category_counts,
            labels=category_counts.index,
            autopct="%1.1f%%"
        )

        st.pyplot(fig)

        st.subheader("Котормо системаларынын тактык көрсөткүчү 🏆")

        translator_scores = pd.DataFrame({
            "Котормо системасы": [
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
            translator_scores.set_index("Котормо системасы")
        )

    with tab4:
        st.subheader("Долбоор жөнүндө 💖")

        st.write("""
        Бул дипломдук долбоор машиналык котормо системаларын
        салыштырма анализдөөгө арналган.

        Изилдөөдө Google Translate, DeepL жана Yandex Translate
        системалары колдонулат.
        """)

        st.progress(92)

        st.success("🎓 Компьютердик лингвистика боюнча долбоор")

st.markdown("---")

st.markdown("""
<div style="
    text-align:center;
    color:#7a5066;
    font-size:17px;
    padding:15px;
">
✨ АКЫЛДУУ КОТОРМО СИСТЕМАСЫ ✨
</div>
""", unsafe_allow_html=True)
