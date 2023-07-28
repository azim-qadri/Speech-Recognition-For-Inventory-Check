import speech_recognition as sr


fruits = ['apple', 'orange', 'kiwi', 'mango', 'grapes', 'apricots', 'lychee', 'blueberries', 'raspberries', 'strawberries']
# Initialize the recognizer
r = sr.Recognizer()
# use the microphone as source for input
with sr.Microphone() as source:
    # wait for a second to let the recognizer
    # adjust the energy threshold based on
    # the surrounding noise Level
    r.adjust_for_ambient_noise(source, duration=0.2)
    # listens user input
    audio = r.listen(source)
    # using google to recognize audio
    fruit = r.recognize_google(audio)
    fruit = fruit.lower()
    if fruit in fruits:
        print(f'{fruit} is present in inventory')
    else:
        print(f'{fruit} is not present in inventory')





