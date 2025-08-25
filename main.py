from urllib import response
import speech_recognition as sr
import webbrowser
import pyttsx3
import difflib
import requests
import google.generativeai as genai
music = {
    "dil diyan gallan": "https://www.youtube.com/watch?v=SAcpESN_Fk4",
    "tera hone laga hoon": "https://www.youtube.com/watch?v=rTuxUAuJRyY",
    "tuhi meri sab hain": "https://www.youtube.com/watch?v=16e78n5x5mE",
    "labon ko": "https://www.youtube.com/watch?v=-FP2Cmc7zj4",   # lowercase
    "satranga": "https://www.youtube.com/watch?v=HrnrqYxYrbk",
    "apna bana le": "https://www.youtube.com/watch?v=u2NAuswnTKs"
}


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="vj90n2lSHsqFSObvTObFTQZbQCgnJYFvIKMDomvd"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiProcess(command):
    # Configure Gemini API key 
    genai.configure(api_key="AIzaSyBfirPB0QU9aMsg-cp_vTV7Pe23hCe3ZsU")

    # Pick a Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Start a chat session
    chat = model.start_chat()

    # Combine system + user instruction (Gemini doesn’t have role separation like OpenAI)
    prompt = f"System: You are Alfred, a helpful assistant.\nUser: {command}"

    # Send the prompt to Gemini
    response = chat.send_message(prompt)

    return response.text.strip()

def processCommand(c):
   print(c)
   if "open google" in c.lower():
        webbrowser.open("http://www.google.com")
   elif "open youtube" in c.lower():
        webbrowser.open("http://www.youtube.com")
   elif "open github" in c.lower():
        webbrowser.open("http://www.github.com")    
   elif "open linkedin" in c.lower():
        webbrowser.open("http://www.linkedin.com")
   elif "open facebook" in c.lower():
        webbrowser.open("http://www.facebook.com")
   elif "open twitter" in c.lower() or "open x" in c.lower():
        webbrowser.open("http://www.twitter.com")  # or x.com
   elif "open instagram" in c.lower():
        webbrowser.open("http://www.instagram.com")
   elif "open reddit" in c.lower():
        webbrowser.open("http://www.reddit.com")
   elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
   elif "open gmail" in c.lower():
        webbrowser.open("http://mail.google.com")
   elif "open stackoverflow" in c.lower():
        webbrowser.open("http://stackoverflow.com")
   elif "open amazon" in c.lower():
        webbrowser.open("http://www.amazon.com")
   elif "open netflix" in c.lower():
        webbrowser.open("http://www.netflix.com")
   elif "open spotify" in c.lower():
        webbrowser.open("http://www.spotify.com")
   elif "open wikipedia" in c.lower():
        webbrowser.open("http://www.wikipedia.org")
   elif "open chatgpt" in c.lower():
        webbrowser.open("https://chat.openai.com")
   elif "open quora" in c.lower():
        webbrowser.open("http://www.quora.com")
   elif "open pinterest" in c.lower():
        webbrowser.open("http://www.pinterest.com")
   elif "open telegram" in c.lower():
        webbrowser.open("https://web.telegram.org")
   elif "open discord" in c.lower():
       webbrowser.open("https://discord.com")
   elif c.lower().startswith("play"):
    link = c.lower().replace("play", "").strip()
    found = False   
    # find the closest match from your library
    closest_match = difflib.get_close_matches(link, music.keys(), n=1, cutoff=0.5)
    
    if closest_match:
        song = closest_match[0]
        webbrowser.open(music[song])
        found = True
    
    if not found:
        print("Song not found in library")
   elif "news" in c.lower():
    r = requests.get( f"https://api.thenewsapi.com/v1/news/all?language=en&api_token={newsapi}")
    
    if r.status_code == 200:
        data = r.json()   # Convert response to Python dict

        # Loop through articles and speak their headlines
        for article in data.get("data", []):   # "data" holds list of articles
            speak(article.get("title"))
    else:
        print("Error:", r.status_code, r.text)
   else:
       #let OpenAI come in the chat..
       response = aiProcess(command)
       speak(response)
if __name__ == "__main__":
  speak(" Alfred is activated")
  while True:
    #listen for the wake up call(Alferd)
    r = sr.Recognizer()
    
    
        
        # recognize speech using google..
    print("Recognizing....")
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=6, phrase_time_limit=12)
        word = r.recognize_google(audio)
        if(word.lower()=="alfred"):
           speak("Hi sir , what can I do for you?")
           #listen for the commandscmd = c.lower().replace(" ", "") 
           with sr.Microphone() as source:
            print("Alfred is listening...")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            processCommand(command)
    except Exception as e:
        print("Error; {0}".format(e))

