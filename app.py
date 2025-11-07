import streamlit as st

st.title("🍳 My Recipe Book")

# Example recipe
recipe = {
    "title": "Chocolate Chip Cookies",
    "ingredients": [
        "2 cups flour",
        "1/2 cup sugar",
        "1 cup chocolate chips"
    ],
    "instructions": [
        "Preheat oven to 180°C.",
        "Mix ingredients.",
        "Bake for 12 minutes."
    ],
}

st.header(recipe["title"])
st.subheader("Ingredients")
st.write("\n".join(recipe["ingredients"]))

st.subheader("Instructions")
for step in recipe["instructions"]:
    st.markdown(f"- {step}")
