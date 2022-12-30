import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime  # pip install datetime
import wikipedia  # pip install wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male or Female voice selection


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis your AI Voice Assistant. Please tell me how can I help you")


def takeCommand():
    # It takes microphone input from the user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Takes speech input from the user
        print("I am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # Recognize the speech and follows the command
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # If the speech is not clear
        print("Please say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open blackboard' in query:
            webbrowser.open("learn.upes.ac.in")

        elif 'open student portal' in query:
            webbrowser.open("sappro.delhi.upes.ac.in")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'the weather' in query:
            webbrowser.open("www.accuweather.com")
