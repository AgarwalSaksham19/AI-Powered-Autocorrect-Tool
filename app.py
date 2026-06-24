import streamlit as st

from utils.spell_corrector import correct_spelling
from utils.grammar_corrector import correct_grammar

st.set_page_config(
    page_title="AI-Powered Autocorrect Tool",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI-Powered Autocorrect Tool")

st.markdown("""
Improve text accuracy and fluency using NLP.

### Features
✅ Real-Time Correction

✅ Spell Checking

✅ Grammar Checking

✅ Download Corrected Text
""")

st.divider()

text = st.text_area(
    "Enter your text",
    height=250,
    placeholder="Example: I hav a dreem to becum data enginer"
)

if text.strip():

    with st.spinner("Analyzing text..."):

        spelling_fixed = correct_spelling(text)
        grammar_fixed = correct_grammar(spelling_fixed)

        final_text = grammar_fixed

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Original Text")
        st.text_area(
    "Original Text",
    value=text,
    height=250,
    disabled=True,
    label_visibility="collapsed"
)

    with col2:
        st.subheader("🚀 Corrected Text")
        st.text_area(
    "Corrected Text",
    value=final_text,
    height=250,
    disabled=True,
    label_visibility="collapsed"
)
    st.divider()

    st.subheader("🔍 Correction Pipeline")

    st.write("**Spell Corrected:**")
    st.info(spelling_fixed)

    st.write("**Grammar Corrected:**")
    st.info(grammar_fixed)

    st.download_button(
        label="📥 Download Corrected Text",
        data=final_text,
        file_name="corrected_text.txt",
        mime="text/plain"
    )

    st.metric(
        "Words",
        len(text.split())
    )

st.divider()

st.caption(
    "Built using Python, Streamlit, TextBlob, and LanguageTool"
)