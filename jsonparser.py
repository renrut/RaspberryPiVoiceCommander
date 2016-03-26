import json


'''
{u'outcomes': 
	[{u'entities': 
		{u'number': 
			[{u'type': u'value', u'value': 54}]
		}, 
		u'confidence': 0.459, 
		u'intent': u'change_channel', 
		u'_text': 
		u'change the channel to fifty four'
	}], 
	u'msg_id': u'2517a7f7-744e-4f28-9f1a-3e0c2105c2f7', 
	u'_text': u'change the channel to fifty four'
}

{u'outcomes': [{u'entities': {u'datetime': [{u'values': [{u'type': u'value', u'grain': u'minute', u'value': u'2016-03-19T19:09:00.000-05:00'}], u'type': u'value', u'grain': u'minute', u'value': u'2016-03-19T19:09:00.000-05:00'}]}, u'confidence': 0.728, u'intent': u'timer', u'_text': u'wake me up in five hours'}], u'msg_id': u'b7bed9af-c909-4b1b-a81e-4061a3770735', u'_text': u'wake me up in five hours'}
'''

"""
{"_text":" turn on the lights","msg_id":"2f6a81a8-9695-4989-9fb0-9955ce4bfc4c","outcomes":[{"_text":" turn on the lights","confidence":0.77,"entities":{},"intent":"power_lights"}]}"""


"""
[u' turn on the tv', 0.776, u'power_television', {u'outcomes': [{u'entities': {}, u'confidence': 0.776, u'intent': u'power_television', u'_text': u' turn on the tv'}], u'msg_id': u'0c469476-a5d3-4bed-b069-b41779eb6df5', u'_text': u' turn on the tv'}]
"""

def parse(JSON):
	try:
		text = JSON['_text']
		confidence = JSON['outcomes'][0]['confidence']
		intent = JSON['outcomes'][0]['intent']
		ret = [text, confidence, intent, JSON]
	except:
		ret = [None, None, None, None]
	return ret


def parseAlt(text, JSON):
	print "parsing..."
	try:
		text = text
		confidence = JSON['outcomes'][0]['confidence']
		intent = JSON['outcomes'][0]['intent']
		ret = [text, confidence, intent, JSON]
	except:
		ret = [None, None, None, None]
	return ret
	