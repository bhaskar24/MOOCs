import sys
import json
from collections import Counter

tweet_file = open(sys.argv[1])

hash_tags = []
for tweets in tweet_file:
	try:
		data = json.loads(tweets)
		for hashtags in data['entities']['hashtags']:
			hash_tags.append(hashtags['text'])
	except:
		pass

for words in Counter(hash_tags).most_common(10):
	print words[0], words[1]




