import math
<<<<<<< HEAD
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def customFunc(x):
    return 1
=======
>>>>>>> 2e52f3590cfabfd741495580a6e375dcacafd9d4

def matrix_multiply_vector(matrix, vector):
    sum = 0
    new_vector = []
    for i in range(len(vector)):
        for j in range(len(vector)):
            sum += matrix[i][j] * vector[j]
            #print(sum)
        new_vector.append(sum)
        sum = 0
    #print(new_vector)
    return new_vector

def vector_norm(vector):
    sum = 0
    for i in range(len(vector)):
        sum += math.sqrt(vector[i] * vector[i])
    norm = sum
    return norm

def vector_diff(vector1, vector2):
    new_vector = []
    if (len(vector2) != len(vector1)):
        return
    for i in range(len(vector1)):
        new_vector.append(vector1[i] - vector2[i])
    return new_vector

def findGammaBorders(matrix):
    sum = 0
    sep_sum = 0
    g2_vector = []
    gamma1 = 0
    gamma2 = 0
    sum_vector = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
           sum += matrix[i][j]
           if (j != i):
               sep_sum += matrix[i][j]
        sum_vector.append(sum)
        g2_vector.append(sep_sum)
        sum = 0
    gamma2 = max(sum_vector)
    sum_vector.clear()
    print(f"gamma 2: {gamma2}")
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            sum_vector.append(matrix[i][j] - sep_sum)
    gamma1 = min(sum_vector)
    print(f"gamma 1: {gamma1}")
    return (gamma1, gamma2)
# (x^(n+1) - x^n) / tau + Ax^n = f => x^(n+1) = x^n - tau(Ax_n - b)
def simple_iterations(matrix, start_vector, free_coefs, epsilon):
    counter = 0
    answer_vector = []
    current_iteration_vector = [0] * len(start_vector)
    (gamma1, gamma2) = findGammaBorders(matrix)
    tau = 2 / (gamma1 + gamma2)
    while (True):
        answer_vector = current_iteration_vector.copy()
        start_vector = vector_diff(matrix_multiply_vector(matrix, answer_vector), free_coefs)
        for i in range(len(matrix[0])):
            current_iteration_vector[i] = answer_vector[i] - 0.01 * start_vector[i]
        start_vector.clear()
        print(f"norm: {vector_norm(vector_diff(current_iteration_vector, answer_vector))}")
        if (vector_norm(vector_diff(current_iteration_vector, answer_vector)) < epsilon):
            break
    print(f"Found solution with given precision {epsilon}")
    print(f"Answer is: {answer_vector}")
    return answer_vector

<<<<<<< HEAD
def simple_iterations_np(matrixx, free_coefss, epsilon:float):
    matrix = np.array(matrixx)
    free_coefs = np.array(free_coefss)

    mat_shape = np.shape(matrix)
    current_iteration_vector = np.zeros(mat_shape[1])
    while (True):
        answer_vector = current_iteration_vector.copy()
        start_vector = np.matmul(matrix, answer_vector) - free_coefs

        for i in range(mat_shape[1]):
            current_iteration_vector[i] = answer_vector[i] - 0.01 * start_vector[i]
        start_vector = np.zeros(mat_shape[1])
        #print(f"norm: {np.linalg.norm(current_iteration_vector - answer_vector)}")
        if (np.linalg.norm( current_iteration_vector - answer_vector) < epsilon):
            break
    print(f"Found solution with given precision {epsilon}")
    print(f"Answer is: {answer_vector}")

    return answer_vector

# Press the green button in the gutter to run the script.
=======
>>>>>>> 2e52f3590cfabfd741495580a6e375dcacafd9d4
if __name__ == '__main__':

    print("\tTask 1\t\n")
    start_vector = [0, 0, 0, 0, 0, 0, 0]
    free_coefs = [1, 1, 1, 1, 1, 1, 1]
    matrix = [[16, 1, 2, 0, 0, 0, 0],
              [1, 12, 1, 1, 0, 0, 0],
              [2, 1, 10, 0, 0, 0, 0],
              [0, 1, 0, 9, 1, 0, 0],
              [0, 0, 0, 1, 11, 1, 0],
              [0, 0, 0, 0, 1, 10, 1],
              [0, 0, 0, 0, 0, 1, 10]]

    print(f"Free coefs: {free_coefs}")
    print(f"Matrix: {matrix}")
    print(f"Start vector: {start_vector}")

<<<<<<< HEAD
    epsilon = [0.01, 0.001, 0.0001]
    f, ax = plt.subplots(1, 3, figsize=(9, 3))
    for i in range(3):
        ax[i].plot(simple_iterations(matrix, start_vector, free_coefs, epsilon[i]))
        ax[i].plot(simple_iterations_np(matrix, free_coefs, epsilon[i]))
        ax[i].legend(['Without NumPy', 'Numpy'])
        ax[i].set_title(f"Epsilon: {epsilon[i]}")
    plt.show()

    print('\tTask 2\t\n')

    def integralFunc(x): return np.cosh(x**2)
    xx = np.linspace(0,1,num=100)

    print('quad: ',"{0:.5f}".format(integrate.quad(integralFunc,0,1)[0]))
    print('quadrature: ',"{0:.5f}".format(integrate.quadrature(integralFunc,0,1)[0]))
    print('trapezoid: ',"{0:.5f}".format(integrate.trapz(integralFunc(xx),x=xx)))
    print('simpson: ',"{0:.5f}".format(integrate.simpson(integralFunc(xx),x=xx)))
=======
>>>>>>> 2e52f3590cfabfd741495580a6e375dcacafd9d4
