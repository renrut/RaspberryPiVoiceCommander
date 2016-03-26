# RaspberryPiVoiceCommander
A voice commander for the raspberry pi.

#Note
This is still a work in progress...

#Motive
I created this to automate a few things in my dorm room. I tried to make it as modular as possible so that scripts are easy to write.

#Dependencies
This requires several python dependencies:
-wit
-json
-speech_recognition
-pyglet
-gtts

It also requires you to have lirc installed on your pi. I recommend the following tutorial for installing lirc and creating config files.
http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/

#Setting up wit
This project uses wit.ai to define an intent. There is plenty of documentation available on their website for python projects. All you need to do is add your token to the tok var on the main project.

#Creating your own scripts

I included a few scripts. They use python os.system command in order to call irsend. It's a little hacky, but works well and keeps things modularized.

Each script is in a file named after the intent defined on wit and has a method called run method that takes in a JSON object. I did this because of the funky way wit formats their json files so keys change depending on the intent. Since they can't all always be parsed the same, I figured the method could do the additional parsing to keep everything modularized.