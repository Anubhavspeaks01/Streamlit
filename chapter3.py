import streamlit as st
st.title("Chai taste Poll")

col1,col2=st.columns(2)
with col1:
    st.header("Masala chai")
    st.image("C:/Users/singh/Downloads/Masala-Chai.webp",width=100)
    vote1= st.button("Vote Masala chai")

with col2:
    st.header("Adrak chai")
    st.image("C:/Users/singh/Downloads/masala-Chai.webp",width=100)
    vote2= st.button("Vote Adrak chai")

if vote1:
    st.success("Thanks for voting masala chai")

elif vote2:
    st.success("Thanks for voting Adrak")

name=st.sidebar.text_input("Enter your name")
tea=st.sidebar.selectbox("choose you chai",["masala","kesar","adrak"])
st.write(f"Welcome {name} and your {tea} is ready")   

with st.expander("Show chai making instruction"):
    st.write("""
             1.Boil water
             2.Add milk
             3. Serve hot broo
             """)

st.markdown('## Welocme to chai App')
st.markdown('>>Blockquote')