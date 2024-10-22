import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model('next_word_lstm.h5')

with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Function to predict the next words
def predict_next_word(model, tokenizer, seed_text, max_sequence_len, next_words):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict(token_list, verbose=0)
        predicted = np.argmax(predicted, axis=-1).item()
        output_word = tokenizer.index_word[predicted]
        seed_text += " " + output_word
    return seed_text

import pandas as pd

corpus = pd.read_csv('corpus.csv')

st.write(corpus[:10],)

# streamlit app
st.title("Next Words Prediction with Bi-Directional LSTM")
input_text = st.text_input("Enter the starting 3-4 Words from above Phrases or Enter your own words")
next_words = st.number_input("Enter the number of Words to predict",min_value=1, value=3, step=1)
if st.button("Predict Next Words"):
    max_sequence_len = model.input_shape[1] + 1
    complete_sentence = predict_next_word(model, tokenizer, input_text, max_sequence_len,next_words)
    st.write(complete_sentence)