from array_operations import *
from system_solutions import *
from math import sqrt, fabs

# Prepara os dados para o método dos Mínimos Quadrados
def get_data(lines, begin, end, positions, y=0, spliter=None):
    values = []
    results = []

    for i in range(begin, end):
        line = lines[i].split(spliter)
        try:
            new_line = [1, ]
            for j in positions:
                new_line.append(float(line[j]))
            results.append(float(line[y]))
            values.append(new_line)
        except:
            pass

    return values, results


# Método dos Mínimos Quadrados
def mmq(values, results):
    G = values
    Gt = transposed_array(G)
    GtG = mult_array(Gt, G)

    Y = transposed_array([results])
    GtY = mult_array(Gt, Y)

    E = extended_array(GtG, GtY)
    solution = gauss(E)
    return solution


# Executa os testes utilizando a equação do MMQ
def run_test(values, results, eq):
    response = []

    for i in range(len(values)):
        result = 0
        for j in range(len(values[i])):
            result += values[i][j] * eq[j]
        response.append(result)

    return response


# Erro médio absoluto
def absolute_error(original, test):
    size = len(original)
    error = 0
    for i in range(len(original)):
        error += fabs(original[i] - test[i])
    return error/size


# Erro médio quadrático
def square_error(original, test):
    size = len(original)
    error = 0
    for i in range(len(original)):
        error += (original[i] - test[i])**2
    return error/size