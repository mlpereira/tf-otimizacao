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

    
# other functions

def random_neighbor(neighborhood):
    index = randint(0,len(neighborhood) - 1)
    return neighborhood[index]