import speech_recognition as sr
import pyttsx3
import openai


r = sr.Recognizer()


def SpeakTest(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[6].id) 
    engine.say(command)
    engine.runAndWait()

while(True):

    with sr.Microphone() as source2:
        openai.api_key = "FILL_WITH_YOUR_OWN_KEY"

        r.adjust_for_ambient_noise(source=source2, duration=0.2)

        print("Start speak")
        audio2 = r.listen(source2)

        Mytext = r.recognize_google(audio2,language="id")
        Mytext = Mytext.lower()

        print("Speak Result:" + Mytext)

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=Mytext,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human","AI"]
        )

        answer = str(response.choices[0].text)

        print(answer)

        SpeakTest(answer)


