import speech_recognition as sr
mic=sr.Recognizer()
print ("cool")

while True:
    
    with sr.Microphone() as call:
        print("program started")
        lion=mic.listen(call)
        google=mic.recognize_google(lion)

        if 'lion' in google:
            
            with sr.Microphone() as source:
                print("listening.........\n\n")
                cmd=mic.listen(source)

                #google 
                google=mic.recognize_google(cmd)
                print(google)

        else:
            pass
