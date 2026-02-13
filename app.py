import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK data
nltk.download('stopwords', quiet=True)

# Load model and vectorizer
model = pickle.load(open("nb_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf.pkl", "rb"))

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

st.title("📩 SMS Spam Classifier")

input_sms = st.text_area("Enter SMS message")

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("Please enter a message")
    else:
        cleaned = clean_text(input_sms)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚫 Spam Message")
        else:
            st.success("✅ Not Spam (Ham)")
