import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(sentence):
    if sentence == 'exit':
        exit(0)
    else:
        engine.say(sentence)
        engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def run_text():
    speak('Input your command')
    text = input()

    if text == 'exit':
        speak("GOODBYE!")
        exit(0)

    if 'play' in text:
        song = text.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)

    elif 'search' in text:
        topic = text.replace('search', '')
        speak('searching for' + topic)
        pywhatkit.search(topic)

    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is: {}".format(time))

    elif 'who is' in text:
        person = text.replace('who is', '')
        info = wikipedia.summary(person, 1)
        speak(info)

    elif 'what is' in text:
        thing = text.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        speak(info)

    elif 'joke' in text:
        speak(pyjokes.get_joke())


def run_voice():
    command = take_command()
    if command == 'exit':
        speak("GOODBYE!")
        exit(0)

    if 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)

    elif 'search' in command:
        topic = command.replace('search', '')
        speak('searching for' + topic)
        pywhatkit.search(topic)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is: {}".format(time))

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        speak(info)

    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        speak(info)

    elif 'joke' in command:
        speak(pyjokes.get_joke())


speak('I am active and listening. Do you wanna speak?')
speak('If you want to speak enter 1, else enter 0')
choice = int(input())
while True:
    if choice == 0:
        run_text()
    elif choice == 1:
        run_voice()
    else:
        speak('Try again')
        choice = int(input())
