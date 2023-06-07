import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia

listener = speech_recognition.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(say):
    engine.say(say)
    engine.runAndWait()
    return talk


def talk_command():
    try:
        with speech_recognition.Microphone() as source:
            print("listening.............")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "friday" in command:
                command = command.replace("friday", " ")
                talk(command)
                print(command)


    except:
        pass
    return command


def friday_run():
    program = talk_command()
    if "play" in program:
        song = program.replace("play", " ")
        talk(song)
        print(song)
        pywhatkit.playonyt(song)


friday_run()

def friday_openwebsite():
    program = talk_command()
    if "search" in program:
        search = program.replace("search", " ")
        talk(search)
        print(search)
        pywhatkit.search(search)

friday_openwebsite()

def open_wikipedia():
    program = talk_command()
    if "open_wikipedia" in program:
        topic = program.replace("open_wikipedia", " ")
        talk(topic)
        wikipedia.summary(topic)
        wikipedia.set_lang("tamil")



open_wikipedia()
