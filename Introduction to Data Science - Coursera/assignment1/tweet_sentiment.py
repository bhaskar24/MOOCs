import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
	scores[term] = int(score)

    for line1 in tweet_file:
	unencoded_line = line1.split(",")[3]
        encoded_line = unencoded_line.encode('utf-8')
	line_parts = encoded_line.split(" ")
	count = 0
	for word in line_parts:
	   if word in scores:
		count = count + scores[word]
	print(float(count))

if __name__ == '__main__':
    main()
