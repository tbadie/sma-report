#! /usr/bin/python

import sys

if len(sys.argv) < 3:
    print "Usage: ./select filename startline step"
    exit (1)

infile = open(sys.argv[1])

lines = infile.readlines()

startline = int(sys.argv[2])
keep = int(sys.argv[3])

out = open(sys.argv[1] + "-" + str(startline), 'w')

i = 1
start = True


for l in lines:
    # if start:
    #     out.write(l)
    #     start = False
    if  i >= startline and (i - startline) % keep == 0:
        out.write(l)
    i += 1

infile.close()
out.close

