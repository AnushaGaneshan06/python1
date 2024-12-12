from PIL import Image
import streamlit as st 


# ------load assets-------
img_contact_form = Image.open("images/1.png")
img_contact_form2 = Image.open("images/2.png")


# ---------Header section---------

with st.container():
    st.subheader("Hi, Iam Anusha :wave:")
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
            - Python Full Stack and Front-End Developer passionate about creating impactful digital solutions.
            - Specialize in building user-friendly interfaces and scalable back-end systems.
            - Aim to learn advanced Python programming and tackle more complex coding challenges.
            - Interested in deepening my knowledge of AI and its future applications with Python.
            
                [Learn More Here ](https://github.com/AnushaGaneshan06)

"""
        )
        


# PROEJECT
with st.container():
    st.write("----")
    st.header("My Project")
    st.write("##")
    imgae_column, text_column = st.columns((1, 2))
    with imgae_column:
        #insert image
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Lottie Animation inside ypur streamlit App")
        st.write("""
            Learn More about Streamlit !!
            Animation on our website engaging anf fun and lottie files are easiest way to inder in the tutorial.
""")
        st.markdown("[Watch Vedio](https://www.youtube.com/watch?v=VqgUkExPvLY)")


with st.container():
    imgae_column,text_column = st.columns((1, 2))
    with imgae_column:
        st.image(img_contact_form2)
    with text_column:
        st.subheader("Integrate Lottie Animation inside ypur streamlit App")
        st.write("""
            Learn More about Streamlit !!
            Animation on our website engaging anf fun and lottie files are easiest way to inder in the tutorial.
""")
        st.markdown("[Watch Vedio](https://www.youtube.com/watch?v=VqgUkExPvLY)")




# ---------contact--------
st.write("----")
st.write("####")
st.write("#### Contact Form")
with st.form(key="user_form"):
    name = st.text_input("Enter your name: ")
    email = st.text_input("Enter your email: ")
    feedback = st.text_area("Provide your feebvack")

    #submit
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.success("Form submission successfully")
    st.write("### Submit Information")
    st.write(f"**Name** {name}")
    st.write(f"**email** {email}")
    st.write(f"**Feedback** {feedback}")
  




