import streamlit as st
import yaml
import os

# --- Page setup ---
st.set_page_config(page_title="My Recipe Book", page_icon="🍪", layout="centered")

#st.title("🍳 My Recipe Book")

# --- Load YAML recipes ---
recipe_files = [f for f in os.listdir("recipes") if f.endswith(".yaml")]
choice = st.sidebar.selectbox("Choose a recipe", recipe_files)

with open(os.path.join("recipes", choice), "r", encoding="utf-8") as f:
    recipe = yaml.safe_load(f)

# --- Example of explicit formatting (you control everything) ---

# Title section
st.markdown(f"<h1 style='color:#60207D; text-align:center; font-family:Georgia;'>{recipe['title']}</h1>",
    unsafe_allow_html=True)

# Image
if "image" in recipe:
    st.image(recipe["image"], caption=recipe.get("description", ""), use_container_width=True)

# Description
st.markdown("<h2 style='color:#4CAF50; font-family:Georgia;'>Description</h2>", unsafe_allow_html=True)
if "description" in recipe:
    st.markdown(recipe["description"], unsafe_allow_html=True)

# Ingredients section
st.markdown("<h2 style='color:#4CAF50; font-family:Georgia;'>Ingredients</h2>", unsafe_allow_html=True)

ingredients = recipe["ingredients"]

# Case 1: ingredients WITH subsections (dict)
if isinstance(ingredients, dict):
    for section, items in ingredients.items():
        st.markdown(
            f"<h3 style='font-family:Georgia; margin-left:10px;'>{section}</h3>",
            unsafe_allow_html=True
        )
        for item in items:
            st.markdown(
                f"<p style='font-size:18px; font-family:Georgia; margin-left:30px;'>• {item}</p>",
                unsafe_allow_html=True
            )

# Case 2: ingredients WITHOUT subsections (list)
elif isinstance(ingredients, list):
    for item in ingredients:
        st.markdown(
            f"<p style='font-size:18px; font-family:Georgia; margin-left:20px;'>• {item}</p>",
            unsafe_allow_html=True
        )

# Instructions
st.markdown("<h2 style='color:#4CAF50; font-family:Georgia;'>Instructions</h2>", unsafe_allow_html=True)

st.markdown(recipe["instructions"]}

            
# Notes section (optional)
if "notes" in recipe:
    st.markdown(
        f"<div style='background-color:#FFF3E0; padding:10px; border-radius:10px;'>💡 {recipe['notes']}</div>",
        unsafe_allow_html=True
    )

# Tags (optional)
if "tags" in recipe:
    st.markdown(
        "<p style='color:gray; font-size:14px;'>Tags: "
        + ", ".join(f"#{t}" for t in recipe["tags"])
        + "</p>",
        unsafe_allow_html=True
    )
















