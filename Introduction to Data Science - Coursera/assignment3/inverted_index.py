import sys
import json

f = open(sys.argv[1])

for line in f:
    data = json.loads(line)
    print data[1].split()



