import streamlit as st
import query as po
from openai import OpenAI
st.title("Gilderoy's Fan Service")

client = OpenAI(api_key="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")
subject = st.text_input("Enter a subject")
if subject.rstrip()!="":
    query = po.prompt(client,str(subject))
    st.code(query,language="markdown")
