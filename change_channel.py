import json
import tts
import os
import sys

def run(JSON):
	channelNums = []
	tts.textToSpeech("Changing the channel")
	#TODO:get channel number from json
	for c in channelNums:
		os.system("irsend SEND_ONCE insignia KEY_" + c)
		os.system("sleep .5")

