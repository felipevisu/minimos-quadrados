import random

from plot import plot, single_plot
from mmq import *

f = open("../data/Daegu_Real_Estate_data.csv", "r")
lines = f.readlines()
random.shuffle(lines)

size = len(lines)
cut = int(size*0.7) # Tamanho do conjunto de treino (70%)

positions = [1, 2, 4, 5, 9, 10, 13, 14, 15]

# Treino
values, results = get_data(lines, 0, cut, positions, spliter=',')
eq = mmq(values, results)

# Teste
values, results = get_data(lines, cut, size, positions, spliter=',')
test_results = run_test(values, results, eq)

# Erros
ae = absolute_error(results, test_results)
se = square_error(results, test_results)

# Prepara os dados para o plot
values = extended_array(values, transposed_array([results]))
values = extended_array(values, transposed_array([test_results]))

print('Equação:\n', eq)
print('Erro médio absoluto:', ae)
print('Erro médio quadrático:',se)

plot(values, 20)