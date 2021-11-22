import speech_recognition as sr
mic=sr.Recognizer()
print ("cool")
with sr.Microphone() as call:
    print("program started")
    lion=mic.listen(call)
    google=mic.recognize_google(lion)
    print(google)