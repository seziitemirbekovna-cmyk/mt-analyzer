import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MT Analyzer",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 MT Analyzer")
st.subheader("Comparative Analysis of Machine Translation Systems")

st.write(
    "This NLP project analyzes the translation of slang, idioms, "
    "memes, emotional expressions, and Kyrgyz cultural expressions "
    "using Google Translate, DeepL, and Yandex Translate."
)

df = pd.read_csv("corpus.csv")

language = st.selectbox(
    "Select language:",
    ["All"] + list(df["Language"].unique())
)

if language != "All":
    filtered_df = df[df["Language"] == language]
else:
    filtered_df = df

category = st.selectbox(
    "Select category:",
    ["All"] + list(filtered_df["Category"].unique())
)

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

expression = st.selectbox(
    "Choose expression:",
    filtered_df["Expression"]
)

if st.button("Show Analysis"):
    row = filtered_df[
        filtered_df["Expression"] == expression
    ].iloc[0]

    st.subheader("Expression")
    st.success(row["Expression"])

    st.subheader("Human Translation")
    st.info(row["Human Translation"])

    st.subheader("Google Translate")
    st.write(row["Google Translate"])

    st.subheader("DeepL")
    st.write(row["DeepL"])

    st.subheader("Yandex Translate")
    st.write(row["Yandex Translate"])

    st.subheader("Language")
    st.write(row["Language"])

    st.subheader("Category")
    st.write(row["Category"])

    st.subheader("Comment")
    st.warning(row["Comment"])

st.divider()

st.subheader("Research Corpus")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.subheader("Corpus Statistics")

stats = df["Category"].value_counts()

st.bar_chart(stats)
