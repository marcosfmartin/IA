import numpy as np


def print_matrix(matrix):
    print(np.matrix(matrix))


def find_blank (matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[i][j] == ' ':
                return i,j
            