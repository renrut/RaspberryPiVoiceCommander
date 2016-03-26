import wit
import json
import sys
import os
import tts
import jsonparser
import speech_recognition as sr
import power_television
import power_lights
import change_channel

CONFIDENCE = .5
verified = False
KEY = "mark"


#checks for a key in the text
def checkForKey(text):
	if KEY in text:
		print "Key in text"
		return True


tok = "GQ5ETCLIQOZNLVEQWLCRMZK7IGGGYP23"
#main loop
def take_command():
	tts.textToSpeech("How may I help you?")
	wit.init()
	commandJSON = json.loads('{}'.format(wit.voice_query_auto(tok)))

	parsed = jsonparser.parse(commandJSON)
	verify(parsed)
	wit.close()

def text_command(text):
	import wit
  	wit.init()

  	# Let's hack!
  	commandJSON = json.loads('{}'.format(wit.text_query(text, tok)))
  	wit.close()

	parsed = jsonparser.parseAlt(text,commandJSON)

	#if confidence is low
	if parsed[1] < .5:
		take_command()
	else:
		verify(parsed)
  	# Wrapping up

#verifies that it is, indeed, a command
#gives list [u'turn on the television', 0.729, u'power_television']
def verify(command):
	print command
	print "\n"

	text = command[0]
	conf = command[1]
	intent = command[2]
	JSON = command[3]

	if text is None:
		print "Command not detected"
		return
	
	if 'UNKNOWN' in intent or conf < .5:
		print "Try again"
		tts.textToSpeech("I didn't quite catch that")
		take_command()
	else:
		print intent
		if "nevermind" in intent:
			return
		else:
			try:
				eval(intent + ".run(JSON)")
			except:
				print "Try again"
				tts.textToSpeech("I didn't quite catch that")
				take_command()



while True:
	# obtain audio from the microphone
	r = sr.Recognizer()

	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)

	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    aud = r.recognize_google(audio)
	    print("Google Speech Recognition thinks you said " + aud)
	    aud = aud.lower()
	    if KEY in aud:
	    	com = aud.replace(KEY, "")
	    	print "Command is " + com
	    	if com is not " " or com is not "":
	    		text_command(com)
	    	else:
	    		take_command()

	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))




