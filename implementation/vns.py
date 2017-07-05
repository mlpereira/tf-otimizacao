from random import randint

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

# knapsack functions

def item_has_conflict(knapsack, item, restrictions):
    for i in knapsack:
        if restrictions[i[NUM_ITEM]][item[NUM_ITEM]]:
            return True
    return False

def knapsack_has_space(max_weight, knapsack_weight, item):
    return item[WEIGHT] < (max_weight - knapsack_weight)

def find_local_minimum(instance):
    return instance

def evaluate_solution(knapsack):
    value = 0
    for item in knapsack:
        value += item[PROFIT]

    return value

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
