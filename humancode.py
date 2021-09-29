import os
import pyttsx3
print("welcome to My tools")
pyttsx3.speak("welcome to my tools")
i=0
while(i<10):
	p=input("chat with me asper your requirements: ")
	i+=1
	pyttsx3.speak("you entered"+p+"wait for some time I am searching it")

	if(("run" in p) and ("chrome" in p)):
		os.system("chrome")
	elif(("run" in p) and ("notepad" in p)):
		os.system("notepad")
	elif(("run" in p) and("windows media player" in p)):
		os.system("wmplayer")
	elif(("run" in p) and ("dev-cpp" in p)):
		os.system("devcppPortable")
	elif("speak" in p):
		q=input("enter what you want to listen: ")
		pyttsx3.speak(q)
	elif(("tell" in p) and ("date" in p)):
		os.system("date")
	elif(("tell" in p) and ("time" in p)):
		os.system("time")
	else:
		print("impossible")
		pyttsx3.speak("not available in this tools")
print("Thank You For Using My Tool")
