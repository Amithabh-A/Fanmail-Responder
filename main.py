import streamlit as st
import query as po
from openai import OpenAI

# Set title and load API key
st.title("Gilderoy's Fan Service")
st.markdown("""
    <style>
        .title {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)


with open("pwd.pass",'r') as file:
    pwd = file.readlines()
    key = "" + pwd[0].strip()
    file.close()

client = OpenAI(api_key=key)
# Create three columns for layout
col1, col2, col3 = st.columns([1, 3, 1])

# Display the first image in the first column
with col1:
    st.image("./OIP.jpeg")

# Display the second image in the third column
with col3:
    st.image("./d46d7d093cccec7e54abac70dc67c6efbd25783d_hq.jpg")


# Display the prompt response in the second column
with col2:
    # Get user input
    subject = st.text_input("Enter a subject")
    if subject.rstrip() != "":
        # Get response from OpenAI API
        query = po.prompt(client, str(subject))
    
        # Display prompt response in the center
        st.header("Prompt Response")
        st.write(query, justify='center')






