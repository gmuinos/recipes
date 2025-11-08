import streamlit as st
import os

st.set_page_config(page_title="My Recipe Book", page_icon="🍳")

st.title("🍽️ My Recipe Book")

# --- Load all markdown files ---
recipe_files = [f for f in os.listdir("recipes") if f.endswith(".md")]
recipe_names = [f.replace(".md", "") for f in recipe_files]

choice = st.sidebar.selectbox("Choose a recipe", recipe_names)

# --- Load the selected recipe ---
file_path = os.path.join("recipes", f"{choice}.md")
with open(file_path, "r", encoding="utf-8") as f:
    recipe_content = f.read()

# --- Display the markdown content ---
st.markdown(recipe_content, unsafe_allow_html=True)
