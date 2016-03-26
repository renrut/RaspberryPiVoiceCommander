from gtts import gTTS
import os
import pyglet
import sys


command = "command.mp3"

comm = sys.argv
say = ""
comm = comm[1:]
for comms in comm:
    say += comms
    say += " "

print say
tts = gTTS(text=say, lang='en')
tts.save(command)

print command
comm = pyglet.media.load(command)
comm.play()


def exitPyglet(dt):
    pyglet.app.exit()
#exit pyglet after command. Kind of a hack
pyglet.clock.schedule_once(exitPyglet, comm.duration)
pyglet.app.run()
