import streamlit as st
import requests

st.title("Speech-Based Mental Health Detection")

# Upload audio file
audio_file = st.file_uploader("Upload your audio file", type=['wav', 'mp3'])

if audio_file is not None:
    st.audio(audio_file, format='audio/wav')
    
    # Call backend API or process locally
    if st.button("Analyze"):
        # Call your backend processing (API call or local function)
        st.write("Analyzing...")
        # Display results here after processing
