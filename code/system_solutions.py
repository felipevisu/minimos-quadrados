def gauss(array):
    n = len(array)

    for i in range(0, n):
        # Producra o maior elemento da coluna
        max_element = abs(array[i][i])
        max_row = i
        for k in range(i+1, n):
            if abs(array[k][i]) > max_element:
                max_element = abs(array[k][i])
                max_row = k

        # Troca a linha máxima pela linha atual (coluna por coluna)
        for k in range(i, n+1):
            tmp = array[max_row][k]
            array[max_row][k] = array[i][k]
            array[i][k] = tmp

        # Processo de eliminação para tornar a matriz triangular superior
        for k in range(i+1, n):
            c = -array[k][i] / array[i][i]
            for j in range(i, n+1):
                if i == j:
                    array[k][j] = 0
                else:
                    array[k][j] += c * array[i][j]

    # Resolve o sistema
    solution = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        solution[i] = round(array[i][n] / array[i][i], 4)
        for k in range(i-1, -1, -1):
            array[k][n] -= array[k][i] * solution[i]

    return solution