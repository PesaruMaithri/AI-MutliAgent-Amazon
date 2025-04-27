
import streamlit as st
from main import main

st.title("Market Research & Use Case Generator - Amazon")

company_name = st.text_input("Enter Company Name (default: Amazon)", "Amazon")

if st.button("Generate Insights"):
    use_cases, resources = main(company_name)

    st.subheader("Top Use Cases:")
    for uc in use_cases:
        st.write(f"- {uc}")

    st.subheader("Resource Links:")
    for link in resources:
        st.markdown(f"[{link}]({link})")
