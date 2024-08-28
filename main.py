import speech_recognition as sr
from AppOpener import open,close
import os
import webbrowser,pyautogui
def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("gismen...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
        return text
    except sr.UnknownValueError as r:
        print(f"erroria {r}")
        


while True:
    niga = speechrecognition()
    name = "Jarvis"
    google = "google"
    write = "write"
    links = [".com", ".net", ".org", ".gov", ".co", ".edu"]
    if niga:
        if name in niga:
            if "open" in niga:
                open(niga,match_closest=True)
            elif "shutdown" in niga:
                os.system("shutdown /s /t 20")

        
            elif google in niga:
                contains_links = any(link in niga for link in links)
                if contains_links:
                        niga = niga.replace(google,"").strip()
                        new_link = "".join(niga.split())
                        webbrowser.open("https://" + new_link)

                else:
                     newlink1 = niga.strip("google")
                     webbrowser.get().open("https://www.google.com/search?q=" + newlink1)



            elif write in niga: 
                niga = niga.replace(write,"").strip()
                pyautogui.write(niga)
                print(f"daiwera {niga}")