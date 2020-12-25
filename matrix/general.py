def matrix_transponse(matrix):
    result = [[0, 0], [0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[j][i] = matrix[i][j]
    return result
