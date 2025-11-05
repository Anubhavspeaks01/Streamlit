import streamlit as st

st.title("💖 Love Finder App")

if st.button("Girl with age 19"):
    st.success("Congratulations! You found your match ❤️")



add_qualities=st.checkbox("Add more qualities")

if add_qualities:
    st.write("Qualitites added")

girl_type=st.radio("Pick your type: ",["Hot","Smart","cute","Naughty","Sexy"])
st.write(f"Selected base {girl_type}")

flavour=st.selectbox("choose flavour",["height","motu","cutie"])

time=st.slider("time level",0,5,2)
st.write(f"time level {time}")

st.number_input("How many girls",min)