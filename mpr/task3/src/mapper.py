#!/usr/bin/env python

import sys
import string
import numpy

for line in sys.stdin:
    line = line.strip()
    # split the line into words
    words = line.split(",")
    license_type = words[2]
    total_amount = float(words[12]) #+float(words[13])+float(words[14])+float(words[15])
    try:
        if license_type:
            print(str(license_type)+"\t"+str([1,total_amount]))
    except ValueError:
        continue
     

