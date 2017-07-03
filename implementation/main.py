import numpy
import sys
import re

# VARS
items = []
restrictions = []

# read filename from input
filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

number_of_items = int(re.findall(r'\d+', lines[0])[0])
max_weight = int(re.findall(r'\d+', lines[1])[0])

# read items

i = 3
while(lines[i] != ';\n'):
    regex_resut = re.findall(r'\d+', lines[i])
    item = (regex_resut[0], regex_resut[1], regex_resut[2])
    items.append(item)

    i = i + 1

