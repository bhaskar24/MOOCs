import sys
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    
    scores = {}
    count = 0

    for line1 in tweet_file:
	unencoded_line = line1.split(",")[3]
        encoded_line = unencoded_line.encode('utf-8')
	line_parts = encoded_line.split(" ")
	for word in line_parts:
	    if word in scores:
		scores[word] = scores[word] + 1
		count = count + 1
	    else:
		scores[word] = 1
		count = count + 1

    for term in scores:
	print(term+" "+str("%.8f" %(float(scores[term])/float(count))))

if __name__ == '__main__':
    main()
