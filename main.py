import streamlit as st
st.title("Hello Anubhav & Amit")
st.subheader("Brewed with streammlit")
st.text("Welcome to your interactive app")
st.write("Choose your favourite food")
food=st.selectbox("Your fav chai :",["Chickenn","Mutton","Egg"])
st.write(f"You choose {food},Excellent choice")
st.success("Your food is breweed")