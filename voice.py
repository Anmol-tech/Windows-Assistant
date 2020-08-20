import speech_recognition as sr

microphone = sr.Microphone()
r = sr.Recognizer()
class listener:
    def listen(self):
        r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
                print("Recognizing...")    
                query = r.recognize_google(audio, language='en-in') 
                print(f"User said: {query}\n")  

            except Exception as e:
                # print(e)    
                print("Say that again please...")
                return "None" 
            return query

       