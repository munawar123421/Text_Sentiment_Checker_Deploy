# app.py
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Simple Sentiment Checker", layout="centered")
st.title("📝 Simple Sentiment Checker")

st.write("Enter some text, and this app will tell you if the sentiment is positive, negative, or neutral.")

# Text input
user_input = st.text_area("Type your text here:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        
        if polarity > 0:
            st.success(f"Positive sentiment 😊 (polarity={polarity:.2f})")
        elif polarity < 0:
            st.error(f"Negative sentiment 😞 (polarity={polarity:.2f})")
        else:
            st.info(f"Neutral sentiment 😐 (polarity={polarity:.2f})")
