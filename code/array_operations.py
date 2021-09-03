# Multiplica duas matrizes
def mult_array(array_1, array_2):
    l1, c1 = len(array_1), len(array_1[0])
    l2, c2 = len(array_2), len(array_2[0])

    if c1 != l2:
        return False

    for i in range(1, l1):
        if len(array_1[i]) != c1:
            return False

    for i in range(1, l2):
        if len(array_2[i]) != c2:
            return False

    new_array = []

    for i in range(l1):
        new_line = []
        for j in range(c2):
            soma = 0
            for k in range(c1):
                soma += array_1[i][k]*array_2[k][j]
            new_line.append(soma)
        new_array.append(new_line)

    return new_array


# Gera a transposta de uma matriz
def transposed_array(array):
    l = len(array)
    c = len(array[0])

    for i in range(1, l):
        if len(array[i]) != c:
            return False

    new_array = []
    for i in range(c):
        new_line = []
        for j in range(l):
            new_line.append(array[j][i])
        new_array.append(new_line)

    return new_array


# Gera a matriz extendida de um sistema
def extended_array(array, vector):
    if len(array) != len(vector):
        return False

    for i in range(len(array)):
        array[i].append(vector[i][0])

    return array


# Soma dois vetores
def sum_vector(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        return False

    new_vector = []
    for i in range(len(vector_1)):
        new_vector.append(vector_1[i]+vector_2[i])

    return new_vector


# Soma duas matrizes
def sum_array(array_1, array_2):
    if len(array_1) != len(array_2):
        return False

    new_array = []
    for i in range(len(array_1)):
        new_array.append(sum_vector(array_1[i], array_2[i]))

    return new_array


# Multiplica um vetor por um escalar
def vector_scalar(vector, scalar):
    for i in range(len(vector)):
        vector[i] = vector[i]*scalar

    return vector


# Multiplica uma matriz por um escalar
def array_scalar(array, scalar):
    for i in range(len(array)):
        array[i] = vector_scalar(array[i], scalar)

    return array


# Algorítmo de Laplace para encontrar determinante
def laplace(array):
    size = len(array)

    if size == 1:
        return array[0][0]

    if size == 2:
        return array[0][0]*array[1][1] - array[0][1]*array[1][0]

    vector_d = []
    for i in range(size):
        temp_array = array.copy()
        temp_array.pop(0)
        temp_array = transposed_array(temp_array)
        temp_array.pop(i)
        temp_array = transposed_array(temp_array)
        vector_d.append(laplace(temp_array))

    vector_a = []
    for i in range(size):
        vector_a.append((-1)**(i)*vector_d[i])

    soma = 0
    for i in range(size):
        soma += array[0][i]*vector_a[i]

    return soma


# Determinante de uma matriz
def det(array):
    size = len(array)
    for i in range(size):
        if size != len(array[i]):
            return False
    
    return laplace(array)