import speech_recognition as sr

r=sr.Recognizer()
hasil=""

with sr.Microphone() as source :
    print("Recordd...")
    audio = r.listen(source)
 
    
    try:
        text= r.recognize_google(audio,)
        print('{}',format(text))
        
    except  :
        print("Eror, Try Again!!")
        
