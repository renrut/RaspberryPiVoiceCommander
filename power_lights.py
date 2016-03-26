import json
import tts
import os
import sys

def run(JSON):
	tts.textToSpeech("Toggling power on the lights")
	os.system("irsend SEND_ONCE lights KEY_POWER")
