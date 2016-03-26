import json
import tts
import os
import sys

def run(JSON):
	tts.textToSpeech("Toggling power on the television?")
	os.system("irsend SEND_ONCE insignia KEY_POWER")