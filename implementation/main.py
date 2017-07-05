import numpy
import sys
import re
from vns import *

# constants

NUM_ITEM = 0
PROFIT = 1
WEIGHT = 2

MAX_NUMBER_OF_ITERATIONS = 10
NUMBER_OF_NEIGHBORHOODS = 10

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
print evaluate_solution(knapsack)

# print("1111111111111")
print knapsack_id_sum(knapsack)

random_item_max_weight(items, 300)

for i in range(0, MAX_NUMBER_OF_ITERATIONS):
    print "i = " + str(i)
    k = 1
    while (k <= NUMBER_OF_NEIGHBORHOODS):
        print (k)
        # print("2222222222222")
        # print knapsack_id_sum(knapsack)
        if k < NUMBER_OF_NEIGHBORHOODS:
            x1 = random_neighbour(knapsack, max_weight, knapsack_weight, k, items, restrictions)
        else:
            x1 = random_neighbour(knapsack, max_weight, knapsack_weight, 0, items, restrictions)
        #print ("Entrou")
        # print("3333333333333")
        # print knapsack_id_sum(knapsack)
        x2 = find_local_maximum(x1, max_weight, knapsack_weight, items, restrictions)
        #print("JORGE")
        # print knapsack_id_sum(knapsack)
        #print ("Saiu")
        # print ("################")
        # print knapsack_id_sum(x2)
        # print evaluate_solution(x2)
        # print knapsack_id_sum(knapsack)
        # print evaluate_solution(knapsack)
        # print ("XXXXXXXXXXXXXXXX")
        if (evaluate_solution(x2) > evaluate_solution(knapsack)):
            knapsack = x2
            knapsack_weight = calculate_knapsack_weight(knapsack)
            print "Melhorou com k = " + str(k)
            print evaluate_solution(x2)
            k = 1
        else:
            k = k + 1

print_knapsack(knapsack)

result = evaluate_solution(knapsack)
print "\n\nSolution found: " + str(result)