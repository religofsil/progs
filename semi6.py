# "import sys" help us make programms for Windows or Mac or anything else
# .decode(sys.stdin.encoding) should be written after raw_input in case we use import sys

l=[1, 2, 3]
for i in l:
    i=i+5
    for i in l:
        i=i+1
        print i
