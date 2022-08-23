from datetime import datetime
import webbrowser
message = input("Enter Message :").lower()
helloIntent = ["hi","hello","hey","wassup"]
byeIntent = ["bye","bie","tata","see you","goog night"]
dateIntent = ["date","show me the date","date please","whats the date"]
timeIntent = ["time","show me the time","time please","whats the time"]

if message in helloIntent :
    print("Hello")
elif message in byeIntent:
    print("Bye.. TC")
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
