import numpy
import sys
import re

# read filename from input
filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

# VARS
number_of_items = int(re.findall(r'\d+', lines[0])[0])
max_weight = int(re.findall(r'\d+', lines[1])[0])

items = []
restrictions = numpy.zeros(shape=(number_of_items, number_of_items))


# read items

i = 3
while(lines[i] != ';\n'):
    regex_result = re.findall(r'\d+', lines[i])
    item = (regex_result[0], regex_result[1], regex_result[2])
    items.append(item)

    i = i + 1

# read restrictions
i = i + 3

while(lines[i] != ';\n'):
    print lines[i]
    regex_result = re.findall(r'\d+', lines[i])
    # print regex_result
    line = int(regex_result[0])
    column = int(regex_result[1])

    restrictions[line][column] = 1
    restrictions[column][line] = 1

    i = i + 1

print restrictions
