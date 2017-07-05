import numpy
import sys
import re
from vns import *

# constants

NUM_ITEM = 0
PROFIT = 1
WEIGHT = 2

MAX_NUMBER_OF_ITERATIONS = 10
NUMBER_OF_NEIGHBORHOODS = 3

# read filename from input

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

line_num = 0

def find_line_with_numbers(line_num):
    while len(re.findall(r'\d+', lines[line_num])) == 0:
        line_num += 1
    return line_num

# vars

line_num = find_line_with_numbers(line_num)

number_of_items = int(re.findall(r'\d+', lines[line_num])[0])
line_num += 1

line_num = find_line_with_numbers(line_num)

max_weight = int(re.findall(r'\d+', lines[line_num])[0])

items = []
restrictions = numpy.zeros(shape=(number_of_items, number_of_items))
knapsack = []
knapsack_weight = 0

# read items

line_num += 1
line_num = find_line_with_numbers(line_num)

while(lines[line_num] != ';\n'):
    regex_result = re.findall(r'\d+', lines[line_num])
    item = (int(regex_result[0]), int(regex_result[1]), int(regex_result[2]))
    items.append(item)

    line_num += 1

# read restrictions

line_num = find_line_with_numbers(line_num)

while(lines[line_num] != ';\n'):
    regex_result = re.findall(r'\d+', lines[line_num])

    line = int(regex_result[0])
    column = int(regex_result[1])

    restrictions[line][column] = 1
    restrictions[column][line] = 1

    line_num += 1


# generate initial solution

items.sort(key=lambda (a,b,c): float(b)/c, reverse=True)

for i in range(0,number_of_items):
    if (max_weight - knapsack_weight) < items[-1][WEIGHT]:
        break
    if knapsack_has_space(max_weight, knapsack_weight, items[i]):
        if item_can_be_chosen(knapsack, items[i], restrictions):
            knapsack.append(items[i])
            knapsack_weight += items[i][WEIGHT]

print_knapsack(knapsack)

# execute search algorithm with vns meta-heuristic

N = [neighborhood0, neighborhood1, neighborhood2]

for i in range(0, MAX_NUMBER_OF_ITERATIONS):
    k = 0
    while (k < NUMBER_OF_NEIGHBORHOODS):
        neighborhood = N[k](knapsack)
        x1 = random_neighbor(neighborhood)

        x2 = find_local_maximum(x1)

        if (evaluate_solution(x2) > evaluate_solution(knapsack)):
            knapsack = x2
            k = 0
        else:
            k = k + 1
