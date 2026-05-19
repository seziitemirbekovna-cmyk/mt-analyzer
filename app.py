import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator

st.set_page_config(page_title="MT Analyzer")

st.title("MT Analyzer")
st.subheader("Сравнительный анализ машинного перевода")

corpus = {
    "Expression": [
        "Touch grass",
        "Ghost someone",
        "Delulu",
        "NPC behavior",
        "It’s giving rich energy"
    ],

    "Human Translation": [
        "выйди в реальный мир",
        "резко игнорировать человека",
        "жить в иллюзиях",
        "поведение как у NPC",
        "создает вайб богатства"
    ],

    "Comment": [
        "Possible literal translation",
        "Context important",
        "Slang adaptation required",
        "Gaming slang",
        "Cultural adaptation"
    ]
}

df = pd.DataFrame(corpus)

selected = st.selectbox(
    "Выберите выражение:",
    df["Expression"]
)

if st.button("Analyze"):

    machine_translation = GoogleTranslator(
        source='en',
        target='ru'
    ).translate(selected)

    human_translation = df[
        df["Expression"] == selected
    ]["Human Translation"].values[0]

    comment = df[
        df["Expression"] == selected
    ]["Comment"].values[0]

    st.subheader("Machine Translation")
    st.success(machine_translation)

    st.subheader("Human Translation")
    st.info(human_translation)

    st.subheader("Comment")
    st.warning(comment)

st.subheader("Research Corpus")
st.table(df)
