import os
try:
    import speech_recognition as sr
    from mahdix import *
    import pyttsx3
except:
    os.system('pip install SpeechRecognition')
    os.system('pip install pyaudio')
    os.system('pip install mahdix')
    os.system('pip install pyttsx3')
clear()

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")
        return None
def open_brou(link):
    os.system(f'start {link}')
def main():
    while True:
        text = speech_to_text().lower()
        if text:
            print(f"Original Text: {text}")
            sleep(1)
            text_to_speech(text)
            if "Who are you" in text:
                text_to_speech("Hello! How can I help you?")
            elif "open youtube" in text:
                open_brou("https://www.youtube.com")
            elif "open google" in text:
                open_brou("https://www.google.com")
            elif "facebook" in text:
                open_brou("https://www.facebook.com")
            elif "open github" in text:
                text_to_speech("Goodbye! Have a great day.")
            else:
                text_to_speech("Sorry, I didn't understand that. Can you please repeat?")


if __name__ == "__main__":
    main()
