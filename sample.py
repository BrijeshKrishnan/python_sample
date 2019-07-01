import speech_recognition as sr     # import the library
import requests
import time

def getSpeech():	
	r = sr.Recognizer()                 # initialize recognizer
	with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.

		while(True):
		    print("Speak Anything :")
		    audio = r.listen(source)        # listen to the source
		    r.adjust_for_ambient_noise(source)
		    try:
		        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
		        print("You said : {}".format(text))
		        call_textToCommand(format(text))
		    except:
		        print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly
		        pass

def call_textToCommand(speech_text):
	command_list = ["google", "yahoo"]
	indices = [i for i, s in enumerate(command_list) if speech_text.upper() in s.upper()]
	print (indices)
	if len(indices) > 0:
		execute_command(command_list[indices[0]])

def execute_command(command):
	print("Executing.....#: {%s}"%command)
	openurl_function(command)	
	pass
def build_cmd(cmd):
	cmd ="http://www."+cmd+".com"
	return(cmd)


def openurl_function(cmd):
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.keys import Keys

    from selenium import webdriver
    driver = webdriver.Ie(r"C:\\IEDriver\\IEDriverServer.exe")
    
    driver.get(build_cmd(cmd))
    time.sleep(3)
    driver.maximize_window()
    print("page opened")
    return


if __name__== "__main__":
	getSpeech()

