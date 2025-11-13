import streamlit as st
import os
import re
import frontmatter  # pip install python-frontmatter

# --- Page setup ---
st.set_page_config(page_title="My Recipes", layout="centered")

st.title("Recipes")

# --- Load Markdown recipes ---
recipe_files = [f for f in os.listdir("recipes") if f.endswith(".md")]
choice = st.sidebar.selectbox("Choose a recipe", recipe_files)

# --- Parse Markdown file ---
with open(os.path.join("recipes", choice), "r", encoding="utf-8") as f:
    post = frontmatter.load(f)

recipe = {
    "title": post.get("title", os.path.splitext(choice)[0]),
    "image": post.get("image", None),
    "tags": post.get("tags", []),
}

# --- Split Markdown into sections ---
content = post.content

def extract_section(header, text):
    """Extracts a section by its markdown header."""
    pattern = rf"##\s*{re.escape(header)}(.*?)(?=\n##|$)"
    match = re.search(pattern, text, re.S)
    if match:
        section = match.group(1).strip()
        lines = [line.strip("- ").strip() for line in section.splitlines() if line.strip()]
        return lines
    return []

ingredients = extract_section("🥣 Ingredients", content)
steps = extract_section("🧁 Steps", content)
notes = "\n".join(extract_section("💡 Notes", content))

# --- Display recipe ---
st.markdown(
    f"<h1 style='color:#FF7043; text-align:center; font-family:Georgia;'>{recipe['title']}</h1>",
    unsafe_allow_html=True
)

# Image
if recipe["image"]:
    st.image(recipe["image"], use_container_width=True)

# Ingredients section
st.markdown(
    "<h2 style='color:#4CAF50; font-family:Trebuchet MS;'>🥣 Ingredients</h2>",
    unsafe_allow_html=True
)
for item in ingredients:
    st.markdown(f"<p style='font-size:18px; margin-left:20px;'>• {item}</p>", unsafe_allow_html=True)

# Steps section
st.markdown(
    "<h2 style='color:#2196F3; font-family:Trebuchet MS;'>🧁 Steps</h2>",
    unsafe_allow_html=True
)
for i, step in enumerate(steps, 1):
    st.markdown(
        f"<p style='font-size:17px; margin-left:20px;'><b>Step {i}:</b> {step}</p>",
        unsafe_allow_html=True
    )

# Notes section (optional)
if notes:
    st.markdown(
        f"<div style='background-color:#FFF3E0; padding:10px; border-radius:10px;'>💡 {notes}</div>",
        unsafe_allow_html=True
    )

# Tags (optional)
if recipe["tags"]:
    st.markdown(
        "<p style='color:gray; font-size:14px;'>Tags: "
        + ", ".join(f"#{t}" for t in recipe["tags"])
        + "</p>",
        unsafe_allow_html=True
    )

