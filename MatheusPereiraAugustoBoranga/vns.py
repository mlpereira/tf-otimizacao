from random import randint
from random import shuffle

# constantes
NUM_ITEM = 0
PROFIT = 1
WEIGHT = 2

# numero de vizinhancas
NUMBER_OF_NEIGHBORHOODS = 3

# funcao para gerar um vizinho aleatorio dada uma vizinhanca
def random_neighbour(knapsack, max_weight, knapsack_weight, vizinhanca, items, restrictions):
    new_knapsack = knapsack[:]
    # a ultima vizinhanca gera uma mochila totalmente nova
    if vizinhanca == NUMBER_OF_NEIGHBORHOODS or vizinhanca >= len(new_knapsack):
        new_knapsack = []
        knapsack_weight = 0
    else:
        # remove x itens aleatorios da mochila onde x = numero da vizinhanca
        for i in range(0, vizinhanca):
            index = randint(0,len(new_knapsack) - 1)
            knapsack_weight -= new_knapsack[index][WEIGHT]
            new_knapsack.pop(index)

    # filtra o array de itens para respeitar as restricoes de peso e conflito
    possible_items = items_that_can_be_chosen(new_knapsack, max_weight, knapsack_weight, items, restrictions)

    # insere itens na mochila ate que nenhum item possa ser inserido
    while possible_items != []:
        index = randint(0,len(possible_items) - 1)
        new_knapsack.append(possible_items[index])
        knapsack_weight += possible_items[index][WEIGHT]
        possible_items = items_that_can_be_chosen(new_knapsack, max_weight, knapsack_weight, items, restrictions)

    return new_knapsack

# funcoes auxiliares
# verifica se um item pode ser escolhido baseado nos conflitos e se ele ja esta na mochila
def item_can_be_chosen(knapsack, item, restrictions):
    for i in knapsack:
        if restrictions[i[NUM_ITEM]][item[NUM_ITEM]] or i[0] == item[0]:
            return False
    return True

# filtra um array de itens para respeitar as restricoes de peso e conflito
def items_that_can_be_chosen(knapsack, max_weight, knapsack_weight, items, restrictions):
    return filter(lambda item: item_can_be_chosen(knapsack, item, restrictions) and knapsack_has_space(max_weight, knapsack_weight, item), items)

# verifica se um item cabe na mochila
def knapsack_has_space(max_weight, knapsack_weight, item):
    return item[WEIGHT] <= (max_weight - knapsack_weight)

# funcao para encontrar um maximo local dada uma solucao (hill climbing)
def find_local_maximum(initial, max_weight, knapsack_weight, items, restrictions):
    initial_value = evaluate_solution(initial)

    biggest_solution = initial
    biggest_value = initial_value

    neighborhood = []

    # gera x vizinhos sendo x = max(tamanho da mochila * 2, 100)
    # para mochilas com menos de 50 itens, gera 100 vizinhos
    # para mochilas com mais de 50 itens, gera itens*2 vizinhos
    for i in range(0, max(len(initial)*2, 100)):
        vizinho = random_neighbour(initial, max_weight, calculate_knapsack_weight(initial), 1, items, restrictions)
        neighborhood.append(vizinho)

    # avalia os vizinhos gerados
    for n in neighborhood:
        value = evaluate_solution(n)

        if value > biggest_value:
            biggest_value = value
            biggest_solution = n

    if biggest_value > initial_value:
        return find_local_maximum(biggest_solution, max_weight, calculate_knapsack_weight(biggest_solution), items, restrictions)
    else:
        return initial

# calcula o lucro de uma mochila
def evaluate_solution(knapsack):
    value = 0
    for item in knapsack:
        value += item[PROFIT]

    return value

# calcula o peso de uma mochila
def calculate_knapsack_weight(knapsack):
    weight = 0
    for item in knapsack:
        weight += item[WEIGHT]

    return weight

# printa uma mochila
def print_knapsack(knapsack):
    total_weight = 0
    total_profit = 0
    for item in knapsack:
        total_weight += item[WEIGHT]
        total_profit += item[PROFIT]
        print "Id: " + str(item[NUM_ITEM]) + " - Peso: " + str(item[WEIGHT]) + " - Lucro: " + str(item[PROFIT])
    print "########################################################"
    print "Peso total: " + str(total_weight) + " - Lucro total: " + str(total_profit)
