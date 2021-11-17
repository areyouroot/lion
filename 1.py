import speech_recognition as sr
mic=sr.Recognizer()
print ("cool")

with sr.Microphone() as source:
    print("listening.........\n\n")
    cmd=mic.listen(source)
    
    #google
    print(" google view ")
    google=mic.recognize_google(cmd)
    print(google)
