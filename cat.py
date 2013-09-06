#!/usr/bin/env python


import os, sys
for element in sys.argv[1:]:
    if os.path.isfile(element):
        file = open(element)
        print file.read()
        file.close()
    elif os.path.isdir(element):
        print element + " is a directory, skipping for now"
    else:
        print "cat: " + element + ": No such file or directory"
