#"Jarvis Voice Assistant is a Python-based desktop assistant that uses speech recognition to open websites, play music, and read news based on voice commands."


import speech_recognition as sr     # For converting speech to text
import webbrowser                   # To open web pages
import pyttsx3                      # For text-to-speech
import music_library                # Your custom music dictionary (make sure it exists)

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# ---- Voice settings -----
engine.setProperty('rate', 160)                # Speech rate
engine.setProperty('volume', 1.0)              # Volume level
voices = engine.getProperty('voices')          
engine.setProperty('voice', voices[1].id)      # Selecting a voice (adjust index as needed)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle voice commands
def processCommand(c):
    print(c)  # Print the command received
    
    if c.lower() == "open google":
        webbrowser.open("https://google.com")

    elif c.lower() == "open youtube":
        webbrowser.open("https://youtube.com")

    elif c.lower() == "open instagram":
        webbrowser.open("https://instagram.com")

    elif c.lower() == "open whatsapp":
        webbrowser.open("https://whatsapp.com")

    elif c.lower().startswith("play"):
        # Extract the song name after "play"
        song = c.lower().replace("play", "").strip()

        # Check if song exists in music_library
        if song in music_library.music:
            link = music_library.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have the song {song}")

    elif "news" in c.lower():
        speak("Opening today's news")
        webbrowser.open("https://timesofindia.indiatimes.com/defaultinterstitial.cms?b=/")

# Main execution block
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)  # Calibrate to background noise
                audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Listen for trigger word
                word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Jarvis activated")

                # Listen for the actual command
                with sr.Microphone() as source:
                    print("Jarvis Activated!")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=5, phrase_time_limit=8)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)
