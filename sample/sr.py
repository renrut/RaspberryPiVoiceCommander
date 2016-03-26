import speech_recognition as sr
from difflib import SequenceMatcher
import os
import sys
import csv

keyword = "turner" #default value
keywordThresh = .8
WIT_AI_KEY = "GQ5ETCLIQOZNLVEQWLCRMZK7IGGGYP23" # Wit.ai keys are 32-character uppercase alphanumeric strings
threshhold = 0.7
commandFile = "commands.csv"
commandList = []


#loads list of commands
def loadCommands():
    with open(commandFile, 'rb') as csvfile:
        comreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in comreader:
            commandList.append(row)

def checkCommand(com):
    command = com.split(" ")
    for word in command:    #checking each word for keyword
        if soundsLike(keyword, word) >= keywordThresh: #determining if similarity is enough
            print("----------------------MATCH!-------------------")
            ind = command.index(word)
            newcommand = command[ind:]
            print("You said " + ' '.join(command))
            print("Interpreting as " + keyword + " " + ' '.join(newcommand[1:]) + "\n")
            #DO STUFF HERE
            parseCommand(newcommand)
            #Return because we don't want to keep parsing the sentence
            return


def parseCommand(com):
    print(com)

#tries to compare the word with the keyword
#TODO: Make a 1-liner
def soundsLike(key, com):
    ratio = SequenceMatcher(None, key, com).ratio()
    print ("Similarity: " + key + ":" + com + ":" + str(ratio))
    return ratio





#testStrings = ["hey rowshon turn on the television", "roshon can you turn on the tv", "on the television"]
print ("loading commands....")
loadCommands()
print commandList

# for s in testStrings:
#     checkCommand(s)
r = sr.Recognizer()
while(True):
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    try:
        command = r.recognize_wit(audio, key=WIT_AI_KEY)
        print("You said " + command)
        checkCommand(command)
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))
