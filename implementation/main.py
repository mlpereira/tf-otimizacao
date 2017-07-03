import numpy as np
import sys

filename = sys.argv[1]

for line in open(filename, 'r'):
    item = line.rstrip() # strip off newline and any other trailing whitespace
    ...