

import sys

count=0
filename = sys.argv[1]

with open (filename, "r") as f:
    print (f.read())

with open(filename, "r") as f:
    for line in f:
        count = (0)
        count = count + line.count("e")
print(count)



