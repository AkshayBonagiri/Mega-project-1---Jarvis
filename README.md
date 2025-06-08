
# Jarvis Virtual Assistant

Jarvis Virtual Assistant is a Python-based voice-controlled desktop assistant that performs tasks like opening websites, playing music, and reading news based on spoken commands.

## 🎯 Features

- 🎤 Voice command recognition using `speech_recognition`
- 🗣️ Text-to-speech feedback with `pyttsx3`
- 🌐 Opens websites like Google, YouTube, Instagram, WhatsApp
- 🎶 Plays music from a custom music library
- 📰 Reads daily news by opening a news website
- 🧠 Wake-word activated: responds to "Jarvis"

## 🛠️ Technologies Used

- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- Custom `music_library` module (dictionary of song names and links)

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   https://github.com/AkshayBonagiri/Jarvis-Virtual-Assistant.git
   cd jarvis-virtual-assistant

## Install dependencies:
-pip install speechrecognition pyttsx3 pyaudio

## Working:
Say "Jarvis" to activate, then give commands like:
-Open Google
-Play <song name> note: you should create a music library, which has a dictionary of the song names and URL and import it into main.py
-Example of music library:
music = {
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
}

## NOTE:
-Ensure your microphone is working and accessible.
-The music command relies on exact match with keys from music_library.

