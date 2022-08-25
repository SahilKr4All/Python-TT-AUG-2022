from datetime import datetime
import webbrowser,os,glob,random
helloIntent = ["hi","hello","hey","wassup"]
byeIntent = ["bye","bie","tata","see you","goog night"]
dateIntent = ["date","show me the date","date please","whats the date"]
timeIntent = ["time","show me the time","time please","whats the time"]
musicIntent = ["music","play music","song","play song"]
chat = True
while chat == True:
    message = input("Enter Message :").lower()

    if message in helloIntent :
        print("Hello")
        
    elif message in byeIntent:
        print("Bye.. TC")
        chat=False
        
    elif message in dateIntent:
        dt = datetime.now()
        print(dt.strftime("%d/%m/%y,%a"))
        
    elif message in timeIntent:
        dt = datetime.now()
        print(dt.strftime("%I-%M-%S,%p"))
        
    elif message.startswith("open"):
        #path = message[5:]+".com"
        path = message.split()[-1]+".com"
        webbrowser.open(path)
        
    elif message in musicIntent:
        files = glob.glob("*.mp3")
        song = random.choice(files)
        os.startfile(song)
