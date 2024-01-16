# Speech Translation and Encryption

This project is a simple application that allows users to speak in one language, have their speech translated to another language, and optionally encrypt the translated text for added security. The project uses several Python libraries for speech recognition, translation, text-to-speech, and encryption. Below is an overview of the libraries used and their respective roles:

## Libraries Used:

### 1. [Streamlit](https://www.streamlit.io/)
   - **Role**: Streamlit is a web application framework that simplifies the process of creating interactive and user-friendly web applications for data science and machine learning. In this project, Streamlit is used to build the user interface.

### 2. [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
   - **Role**: The SpeechRecognition library provides a simple interface to interact with various speech recognition engines. It is used here to capture and convert spoken words into text using Google Web Speech API.

### 3. [Googletrans](https://pypi.org/project/googletrans/)
   - **Role**: Googletrans is a Python wrapper for Google Translate. It is used to translate the recognized speech from the source language to the target language.

### 4. [Cryptography](https://pypi.org/project/cryptography/)
   - **Role**: The Cryptography library is used for data encryption. It provides the Fernet symmetric key encryption scheme, utilized in this project to encrypt translated text.

### 5. [Pyttsx3](https://pypi.org/project/pyttsx3/)
   - **Role**: Pyttsx3 is a text-to-speech conversion library in Python. It is used to convert the translated text into spoken words.

## Explanation of Code:

### 1. Translation and Encryption Functions:
   - The `translate_and_encrypt` function captures audio input, transcribes it using the Google Web Speech API, translates it, speaks the translation, and optionally encrypts the translated text.

### 2. Encryption Function (`encrypt`):
   - The `encrypt` function uses the Fernet symmetric key encryption to encrypt the given text.

### 3. Text-to-Speech Function (`speak`):
   - The `speak` function uses Pyttsx3 to convert text into spoken words. It supports different voices based on the selected language.

### 4. Streamlit UI:
   - The Streamlit UI includes language selection dropdowns, a checkbox for encryption, and a button to trigger the translation and encryption process.

### 5. Translation History:
   - The application keeps track of translation history using Streamlit's session state, storing spoken text, translated text, and encrypted text (if applicable).

## How to Run:

1. Install the required libraries: `streamlit`, `speech_recognition`, `googletrans`, `cryptography`, `pyttsx3`.
   ```bash
   pip install streamlit speech_recognition googletrans cryptography pyttsx3
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run your_script_name.py
   ```

3. Access the application through your web browser.

## Contributors:

- **Author**: Muhammad Bin Asif
- **Maintainer**: mbinasifmba18@gmail.com

Feel free to contribute, report issues, or suggest improvements!
