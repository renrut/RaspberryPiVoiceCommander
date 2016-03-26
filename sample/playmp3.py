import sys
import pyglet

command = sys.argv
command = command[1]
print command
comm = pyglet.media.load(command)
comm.play()


def exitPyglet(dt):
    pyglet.app.exit()
#exit pyglet after command. Kind of a hack
pyglet.clock.schedule_once(exitPyglet, comm.duration)
pyglet.app.run()
