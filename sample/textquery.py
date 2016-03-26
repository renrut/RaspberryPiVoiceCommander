import wit
import time

wit.init()
while(True):
	wit.voice_query_start("GQ5ETCLIQOZNLVEQWLCRMZK7IGGGYP23")
	time.sleep(5)
	response = wit.voice_query_stop()
	print("Response: {}".format(response))
wit.close()

