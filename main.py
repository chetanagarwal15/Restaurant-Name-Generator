import streamlit as st
from langchain_helper import generate_restaurant
st.title("🍽️ Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ("Indian", "Italian", "Mexican", "Arabic", "American", "Chinese")
)

if st.sidebar.button("Generate"):
    response = generate_restaurant(cuisine)

    st.header(response["restaurant_name"])

    st.write("**Menu Items**")
    for item in response["menu_items"].split(","):
        st.write("-", item.strip())