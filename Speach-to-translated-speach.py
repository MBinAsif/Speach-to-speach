import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from cryptography.fernet import Fernet
import pyttsx3

import sys
print(sys.executable)
print(sys.path)


# Function to encrypt the spoken words
def encrypt(text, key):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text.encode())
    return encrypted_text

# Function to translate spoken words and speak the result
def translate_and_encrypt(source_language, target_language, encrypt_text):
    # Initialize the speech recognition module
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        st.write("Say something:")
        audio = recognizer.listen(source)

    # Google Web Speech API for speech-to-text conversion
    try:
        spoken_text = recognizer.recognize_google(audio, language=source_language)
        st.write("You said:", spoken_text)

        # Translate spoken words to the selected target language
        translator = Translator()
        translated_text = translator.translate(spoken_text, dest=target_language).text
        st.write("Translated text:", translated_text)

        # Speak the translated text
        speak(translated_text, target_language)

        # Encryption key for security
        encryption_key = Fernet.generate_key()

        # Encrypt the translated text if the user chooses encryption
        if encrypt_text:
            encrypted_text = encrypt(translated_text, encryption_key)
            st.write("Encrypted text:", encrypted_text)
        else:
            encrypted_text = None

        # Store the translated text and encryption status in session state
        if 'translation_history' not in st.session_state:
            st.session_state.translation_history = []
        
        st.session_state.translation_history.append({
            'spoken_text': spoken_text,
            'translated_text': translated_text,
            'encrypted_text': encrypted_text
        })

    except sr.UnknownValueError:
        st.write("Sorry, could not understand audio.")
    except sr.RequestError as e:
        st.write(f"Could not request results from Google Web Speech API; {e}")

def speak(text, language):
    # Initialize the text-to-speech engine with SAPI5 voices
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if language == "hindi":
        engine.setProperty('voice', voices[0].id)  # Select Hindi voice
    elif language == "urdu":
        engine.setProperty('voice', voices[1].id)  # Select Urdu voice

    engine.say(text)
    engine.runAndWait()

# Streamlit UI
st.title("Speech Translation and Encryption")

# Language selection
language_options = ["en", "es", "fr", "de", "hindi", "urdu"]
language_names = ["English", "Spanish", "French", "German", "Hindi", "Urdu"]

source_language = st.selectbox("Select Source Language:", language_names, index=0)
target_language = st.selectbox("Select Target Language:", language_names, index=1)

# Checkbox for encryption
encrypt_text = st.checkbox("Encrypt Text")

# Button to trigger translation and encryption
if st.button("Translate and Encrypt"):
    translate_and_encrypt(source_language, target_language, encrypt_text)

# Navigation to the Translation History tab
if 'translation_history' in st.session_state and st.session_state.translation_history:
    st.title("Translation History")
    st.table(st.session_state.translation_history)

# Organize the UI in tabs
tabs = ["Translation History"]
selected_tab = st.sidebar.radio("Select Tab", tabs)

if selected_tab == "Translation History":
    if 'translation_history' in st.session_state and st.session_state.translation_history:
        st.title("Translation History")
        st.table(st.session_state.translation_history)
    else:
        st.write("No translation history yet.")
