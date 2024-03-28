import streamlit as st
import query as po
from openai import OpenAI
st.title("Gilderoy's Fan Service")
with open("pwd.pass",'r') as file:
    pwd = file.readlines()
    key = "" + pwd[0].strip()
    file.close()
client = OpenAI(api_key=key)
subject = st.text_input("Enter a subject")
if subject.rstrip()!="":
    query = po.prompt(client,str(subject))
    st.code(query,language="markdown")
