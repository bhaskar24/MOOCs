import sys
import json

sentiment_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

states = {}
for lines in tweet_file:
	data = json.loads(lines)
	try:
		if data['place']['country_code'] == 'US':
			print data['user']['location']
			
	except:
		pass



