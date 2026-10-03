import streamlit as st

st.title("Book or Wait ✈️")

name = st.text_input("Your name")
days = st.slider("Days left before departure", 1, 49, 20)
airline = st.selectbox("Airline", ["Vistara", "Indigo", "AirAsia"])

if st.button("Check"):
    if days < 7:
        st.error(f"{name}, buy now. Prices jump close to departure.")
    else:
        st.success(f"{name}, you may have time to wait on {airline}.")
