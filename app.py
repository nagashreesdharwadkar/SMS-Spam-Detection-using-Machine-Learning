import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

import pickle
import string
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.markdown("""
<div class="title">
🛡️ SMS Spam Detection System
</div>

<div class="subtitle">
Detect whether an SMS is <b>Spam</b> or <b>Legitimate</b>
</div>
""", unsafe_allow_html=True)

input_sms = st.text_area(
    "✉️ Enter your SMS",
    placeholder="Type or paste your SMS here..."
)

if st.button("🔍 Predict"):
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    prediction = model.predict(vector_input)[0]
    # 4. Display
    if prediction == 1:
        st.markdown("""
        <div class="spam-card">
        <h3>🚨 Spam Message</h3>
        <p>This message appears to be spam. Avoid clicking suspicious links.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="success-card">
        <h3>✅ Legitimate Message</h3>
        <p>This message appears to be genuine and is not classified as spam.</p>
        </div>
        """, unsafe_allow_html=True)


st.markdown("""
<hr>
<div style='text-align:center;color:#bbbbbb;font-size:15px;'>
🛡 Stay Safe. Stay Smart. Avoid Spam.
<br><br>
</div>
""", unsafe_allow_html=True)