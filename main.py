import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


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
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        audio = listener.listen(source)

    data = " "
    try:
        data = listener.recognize_google(audio)
        speak("You said {}".format(data))

    except sr.UnknownValueError:
        print("Could not understand")

    except sr.RequestError:
        print("Request error")

    return data


def play_youtube(search_text):
    video = search_text.replace('play', '')
    speak('playing' + video)
    pywhatkit.playonyt(video)


def search_google(search_text):
    topic = search_text.replace('search', '')
    speak('searching for {}'.format(topic))
    pywhatkit.search(topic)


def tell_date_and_time():
    today_day = datetime.datetime.now().strftime("%A")
    today_date = datetime.date.today().strftime("%B %d, %Y")
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    speak('Today is {}, the date is {} and the current time is {}'.format(today_day, today_date, current_time))


def search_wikipedia(search_text):
    topic = search_text.replace('wikipedia', '')
    info = wikipedia.summary(topic, 5)
    speak(info)


def run_text():
    speak('Input your command')
    command_text = input()

    if command_text == 'exit':
        speak("Goodbye!")
        exit(0)

    if 'play' in command_text:
        play_youtube(command_text)

    elif 'search' in command_text:
        search_google(command_text)

    elif 'time' in command_text:
        tell_date_and_time()

    elif 'wikipedia' in command_text:
        search_wikipedia(command_text)

    elif 'joke' in command_text:
        speak(pyjokes.get_joke())


def run_voice():
    command = take_command()

    if command == 'exit':
        speak("GOODBYE!")
        exit(0)

    if 'play' in command:
        play_youtube(command)

    elif 'search' in command:
        search_google(command)

    elif 'time' in command:
        tell_date_and_time()

    elif 'wikipedia' in command:
        search_wikipedia(command)

    elif 'joke' in command:
        speak(pyjokes.get_joke())


def run(mode):
    if mode == 0:
        run_text()
    elif mode == 1:
        run_voice()


def main():
    speak('I am active and listening')
    speak('If you want to speak enter 1, else enter 0')
    choice = int(input())
    while True:
        run(choice)


main()
