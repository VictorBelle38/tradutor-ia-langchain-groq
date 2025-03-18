import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["GROQ_API_KEY"] = "API GROQ AQUI"

llm = ChatGroq(model = "mixtral-8x7b-32768")

prompt = ChatPromptTemplate.from_template("Traduza para {language}: {text}")
chain = prompt | llm | StrOutputParser()

st.title(" Tradutor com IA (Groq + LangChain)")
st.write("Digite um texto e escolha o idioma para traduzir.")

text_input = st.text_area("Texto original", "")
language = st.selectbox("Idioma para tradução", ["Inglês", "Espanhol", "Francês", "Alemão", "Italiano"])

if st.button("Traduzir") and text_input:
    with st.spinner("Traduzindo..."):
        result = chain.invoke({"language": language, "text": text_input})
        st.success("Tradução:")
        st.write(result)