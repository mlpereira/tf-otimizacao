from random import randint
from random import shuffle

NUM_ITEM = 0
PROFIT = 1
WEIGHT = 2

# functions to generate neighborhood

def neighborhood0(array):
    return [array, array]

def neighborhood1(array):
    return [array, array, array]

def neighborhood2(array):
    return [array, array, array, array]

def random_neighbour(knapsack, max_weight, knapsack_weight, items_to_remove, items, restrictions):
    if items_to_remove == 0 or items_to_remove >= len(knapsack):
        #zera a mochila
        knapsack = []
        knapsack_weight = 0
        #print "Removeu todos itens da mochila"
    else:
        #remove items_to_remove itens da mochila
        for i in range(0, items_to_remove):
            index = randint(0,len(knapsack) - 1)
            knapsack_weight -= knapsack[index][WEIGHT]
            #print "Removeu item " + str(knapsack[index][NUM_ITEM])
            knapsack.pop(index)

    #embaralha itens para adicionar itens aleatorios
    shuffle(items)

    #adiciona todos itens que conseguir
    for item in items:
        if item_can_be_chosen(knapsack, item, restrictions):
            if knapsack_has_space(max_weight, knapsack_weight, item):
                knapsack.append(item)
                knapsack_weight += item[WEIGHT]
                #print "Adicionou item " + str(item[NUM_ITEM])

    #print knapsack

    return knapsack

# knapsack functions
def item_can_be_chosen(knapsack, item, restrictions):
    for i in knapsack:
        if restrictions[i[NUM_ITEM]][item[NUM_ITEM]] or i[0] == item[0]:
            return False
    return True

def knapsack_has_space(max_weight, knapsack_weight, item):
    return item[WEIGHT] <= (max_weight - knapsack_weight)

def find_local_maximum(initial, max_weight, knapsack_weight, items, restrictions):
    initial_value = evaluate_solution(initial)

    print "VALOR INICIAL: " + str(initial_value)
    biggest_solution = initial
    biggest_value = initial_value

    # supondo que usaremos o criterio 0 pra achar os vizinhos aqui
    neighborhood = []
    for i in range(0, len(initial)**2):
        vizinho = random_neighbour(initial, max_weight, knapsack_weight, 1, items, restrictions)
        #print ("$$$$$$$$")
        vizinho.sort(key=lambda (a,b,c): a)
        #print vizinho
        neighborhood.append(vizinho)

    for n in neighborhood:
        value = evaluate_solution(n)
        print "Valor da vizinhanca " + str(value)

        if value > biggest_value:
            biggest_value = value
            biggest_solution = n

    if biggest_value > initial_value:
        return find_local_maximum(biggest_solution, max_weight, knapsack_weight, items, restrictions)
    else:
        return initial


def evaluate_solution(knapsack):
    value = 0
    for item in knapsack:
        value += item[PROFIT]

    return value

def calculate_knapsack_weight(knapsack):
    weight = 0
    for item in knapsack:
        weight += item[WEIGHT]

    return weight

# other functions

def print_knapsack(knapsack):
    total_weight = 0
    total_profit = 0
    for item in knapsack:
        total_weight += item[WEIGHT]
        total_profit += item[PROFIT]
        print "Id: " + str(item[NUM_ITEM]) + " - Peso: " + str(item[WEIGHT]) + " - Lucro: " + str(item[PROFIT])
    print "########################################################"
    print "Peso total: " + str(total_weight) + " - Lucro total: " + str(total_profit)

def random_neighbor(neighborhood):
    index = randint(0,len(neighborhood) - 1)
    return neighborhood[index]
