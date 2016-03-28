from gtts import gTTS
import os
import pygame
import sys
import time

command = "command.mp3"

#A text to speech method
def textToSpeech(comm):

	#uses google's tts api, saves it to command
	tts = gTTS(text=comm, lang='en')
	tts.save(command)
	# setup mixer to avoid sound lag

	pygame.mixer.quit()
	pygame.mixer.pre_init(16384, -16, 2, 1024*3)
	pygame.mixer.init()
	pygame.init()	
	pygame.mixer.music.load(command)
	pygame.mixer.music.play()
