import streamlit as st
import pandas as pd
import joblib
from utils import preprocessor

from huggingface_hub import hf_hub_download

REPO_ID = "amosfyy/10_2_model"
FILENAME = "model_.joblib"

def run():

    model_path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    model = joblib.load(model_path)

    st.title("Sentiment Analysis")
    st.text("Basic app to detect the sentiment of text.")
    st.text("")
    userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Input text HERE')
    st.text("")
    predicted_sentiment = ""
    if st.button("Predict"):
        predicted_sentiment = ???
        if predicted_sentiment == 1:
            output = 'positive 👍'
        else:
            output = 'negative 👎'
        sentiment=f'Predicted sentiment of "{userinput}" is {output}.'
        st.success(???)

if __name__ == "__main__":
    run()
