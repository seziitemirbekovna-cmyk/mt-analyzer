import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MT Analyzer",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 MT Analyzer")
st.subheader("Сравнительный анализ машинного перевода")

st.write(
    "Веб-приложение для анализа перевода интернет-сленга, "
    "идиоматических выражений и кыргызских культурных конструкций."
)

df = pd.read_csv("corpus.csv")

language = st.selectbox(
    "Выберите язык:",
    ["All"] + list(df["Language"].unique())
)

if language != "All":
    filtered_df = df[df["Language"] == language]
else:
    filtered_df = df

expression = st.selectbox(
    "Выберите выражение:",
    filtered_df["Expression"]
)

if st.button("Показать анализ"):
    row = filtered_df[filtered_df["Expression"] == expression].iloc[0]

    st.subheader("Expression")
    st.success(row["Expression"])

    st.subheader("Human Translation")
    st.info(row["Human Translation"])

    st.subheader("Language")
    st.write(row["Language"])

    st.subheader("Comment")
    st.warning(row["Comment"])

st.divider()

st.subheader("Research Corpus")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.subheader("Corpus Statistics")

stats = df["Language"].value_counts()

st.bar_chart(stats)
