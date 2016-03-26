import os
import sys

not_executed = 1


time = sys.argv


while(not_executed):
dt = list(time.localtime())
hour = dt[3]
minute = dt[4]
if hour == 5 and minute == 45:
os.popen2("open /Users/jun/shout.mp3")
not_executed = 0
