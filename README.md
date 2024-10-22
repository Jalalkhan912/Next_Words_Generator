# Shakespeare Sonnets Text Generation

## Overview
The Shakespeare Sonnets Text Generation project is an AI-powered application that generates text resembling Shakespearean poetry. It uses a **Bidirectional LSTM (Bi-LSTM)** model trained on the **Shakespeare sonnets dataset**. This interactive application allows users to input a few initial words and specify how many more words they want the model to generate. The user interface is implemented with **Streamlit** for easy interaction.

## Features
- **Text Generation:** Generate Shakespearean-style text from initial user input.
- **Word Count Customization:** Users can specify the number of words to generate.
- **Interactive Streamlit UI:** Provides an easy-to-use interface to interact with the model.

## Model Details
- **Bidirectional LSTM (Bi-LSTM):** Trained on Shakespeare's sonnets dataset to understand poetic language from both directions (forward and backward).
- **Training Data:** The sonnets dataset is sourced from **Project Gutenberg** and includes all of Shakespeare's published sonnets.

## How It Works
1. **User Input:** Users provide initial words and the desired number of words to generate.
2. **Prediction:** The Bi-LSTM model predicts the next words based on the input.
3. **Display Results:** The generated text is displayed on the Streamlit UI.

## Use Cases
- **Creative Writing:** Assists poets and writers by generating text in Shakespearean style.
- **Educational Tool:** Helps students and educators explore and analyze Shakespearean language.
- **AI Experimentation:** Demonstrates the capabilities of Bidirectional LSTM in text generation tasks.

## Future Improvements
- **Character-Level Generation:** Generate text character by character for more fluid results.
- **Temperature Control:** Implement temperature control to influence the creativity of generated text.
- **Additional Corpora:** Train the model on other literary works to expand its text generation capabilities.
