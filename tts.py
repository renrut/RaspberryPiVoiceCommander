from gtts import gTTS
import os
import pyglet
import sys


command = "command.mp3"

def exitPyglet(dt):
    pyglet.app.exit()

#A text to speech method
def textToSpeech(comm):

	#uses google's tts api, saves it to command
	tts = gTTS(text=comm, lang='en')
	tts.save(command)
	#plays in pyglet. Should be changed to pygame for rpi
	comm = pyglet.media.load(command)
	comm.play()

	#exit pyglet after command. Kind of a hack
	pyglet.clock.schedule_once(exitPyglet, comm.duration)
	pyglet.app.run()
