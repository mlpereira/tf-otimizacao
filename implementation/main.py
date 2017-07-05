import numpy
import sys
import re
from vns import *

# constantes
NUM_ITEM = 0
PROFIT = 1
WEIGHT = 2

# numero de iteracoes
MAX_NUMBER_OF_ITERATIONS = 10

# numero de vizinhancas
NUMBER_OF_NEIGHBORHOODS = 3

# leitura dos dados
filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

line_num = 0

def find_line_with_numbers(line_num):
    while len(re.findall(r'\d+', lines[line_num])) == 0:
        line_num += 1
    return line_num

line_num = find_line_with_numbers(line_num)

number_of_items = int(re.findall(r'\d+', lines[line_num])[0])
line_num += 1

line_num = find_line_with_numbers(line_num)

max_weight = int(re.findall(r'\d+', lines[line_num])[0])

items = []
restrictions = numpy.zeros(shape=(number_of_items, number_of_items))
knapsack = []
knapsack_weight = 0

# leitura dos dados - itens
line_num += 1
line_num = find_line_with_numbers(line_num)

while(lines[line_num] != ';\n'):
    regex_result = re.findall(r'\d+', lines[line_num])
    item = (int(regex_result[0]), int(regex_result[1]), int(regex_result[2]))
    items.append(item)

    line_num += 1

# leitura dos dados - retricoes
line_num = find_line_with_numbers(line_num)

while(lines[line_num] != ';\n'):
    regex_result = re.findall(r'\d+', lines[line_num])

    line = int(regex_result[0])
    column = int(regex_result[1])

    restrictions[line][column] = 1
    restrictions[column][line] = 1

    line_num += 1

# geracao da solucao inicial
# ordena os itens por custo beneficio
items.sort(key=lambda (a,b,c): float(b)/c, reverse=True)

for i in range(0,number_of_items):
    if (max_weight - knapsack_weight) < items[-1][WEIGHT]:
        break
    if knapsack_has_space(max_weight, knapsack_weight, items[i]):
        if item_can_be_chosen(knapsack, items[i], restrictions):
            knapsack.append(items[i])
            knapsack_weight += items[i][WEIGHT]


# execucao o VNS
for i in range(0, MAX_NUMBER_OF_ITERATIONS):
    print "i = " + str(i)
    k = 1
    # laco por todas vizinhancas
    while (k <= NUMBER_OF_NEIGHBORHOODS):
        # Gera aleatoriamente um x1
        x1 = random_neighbour(knapsack, max_weight, knapsack_weight, k, items, restrictions)

        # Encontra um maximo local a partir de x1
        x2 = find_local_maximum(x1, max_weight, knapsack_weight, items, restrictions)

        # Verifica se o maximo local encontrado eh melhor que a solucao ate o momento
        if (evaluate_solution(x2) > evaluate_solution(knapsack)):
            # Altera a solucao
            knapsack = x2
            # print "Solucao ate o momento: " + str(evaluate_solution(knapsack))
            knapsack_weight = calculate_knapsack_weight(knapsack)
            # Volta para a vizinhanca 1
            k = 1
        else:
            k = k + 1

#print_knapsack(knapsack)
print "Profit: " + str(evaluate_solution(knapsack))
print "Weight: " + str(calculate_knapsack_weight(knapsack))
