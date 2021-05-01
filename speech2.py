import speech_recognition as sr
from gtts import gTTS
import os

def main():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("Speak Anything: ")
		audio = r.listen(source)
	try: 
		text = r.recognize_google(audio)
		print("You said: "+ text)
		language = 'en'
		output = gTTS(text=text,lang=language, slow=False)

		output.save("output.mp3")

		os.system("start output.mp3")

	except Exception as e:
		print("Unclear Voice, Please try again..." + str(e))
		
if __name__=="__main__":
	main() 

  