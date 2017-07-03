import numpy
import sys
import re

NUM_ITEM = 0
PROFIT = 1
WEIGHT = 2

# read filename from input
filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

# VARS
number_of_items = int(re.findall(r'\d+', lines[0])[0])
max_weight = int(re.findall(r'\d+', lines[1])[0])

items = []
restrictions = numpy.zeros(shape=(number_of_items, number_of_items))
knapsack = []
knapsack_weight = 0


# read items

i = 3
while(lines[i] != ';\n'):
    regex_result = re.findall(r'\d+', lines[i])
    item = (int(regex_result[0]), int(regex_result[1]), int(regex_result[2]))
    items.append(item)

    i = i + 1

# read restrictions
i = i + 3

while(lines[i] != ';\n'):
    regex_result = re.findall(r'\d+', lines[i])

    line = int(regex_result[0])
    column = int(regex_result[1])

    restrictions[line][column] = 1
    restrictions[column][line] = 1

    i = i + 1

items.sort(key=lambda (a,b,c): float(b)/c, reverse=True)

for i in range(0,number_of_items):
    if (max_weight - knapsack_weight) < items[-1][WEIGHT]:
        break
    if items[i][WEIGHT] < (max_weight - knapsack_weight):
        knapsack.append(items[i])
        knapsack_weight += items[i][WEIGHT]
