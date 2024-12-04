import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My webpage", page_icon=":tada", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -----load assest-----
lottie_coding = load_lottieurl("https://lottie.host/5fce4ace-3465-4a2a-bfac-42c789c6c4f2/1IAVBpx2i6.lottie")


# ---------Header section---------

with st.container():
    st.subheader("Hi, I am Anusha :wave:")
    st.title("A full stack developer from India")
    st.write("I am passionate about leveraging Python to create innovative AI tools that engage users more effectively.")
    st.write("[Learn More](https://github.com/AnushaGaneshan06)")


with st.container():
    st.write("--------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do !!")
        st.write("##")
        st.write(
            """
            - I am Anusha, a Python Full Stack and Front-End Developer passionate about creating impactful digital solutions.
            - Specialize in building user-friendly interfaces and scalable back-end systems.
            - Aim to learn advanced Python programming and tackle more complex coding challenges.
            - Interested in deepening my knowledge of AI and its future applications with Python.
            
                [Learn More Here ](https://github.com/AnushaGaneshan06)

"""
        )
        with right_column:
            st.lottie(lottie_coding, height= 300, key="coding")
