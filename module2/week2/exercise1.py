import numpy as np


def vector_length(v):
    return np.linalg.norm(v)


def dot_product(v1, v2):
    return v1.dot(v2)


def inverse_matrix(matrix):
    return np.linalg.inv(matrix)


def compute_cosine(v1, v2):
    dot_product = np.dot(v1, v2)
    # Compute the L2 norms (magnitudes) of the vectors
    norm_a = np.linalg.norm(v1)
    norm_b = np.linalg.norm(v2)
    # Compute the Cosine Similarity
    return dot_product / (norm_a * norm_b)


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


# vector = np.array([-2, 4, 9, 21])
# result = vector_length([vector])
# print(round(result, 2))

# v1 = np.array([0, 1, -1, 2])
# v2 = np.array([2, 5, 1, 0])
# result = v1 @ v2
# print(round(result, 2))

# x = np.array([[1, 2], [3, 4]])
# k = np.array([1, 2])
# print(x.dot(k))

# x = np.array([[-1, 2], [3, -4]])
# k = np.array([1, 2])
# print(x @ k)


# m = np.array([[-1, 1, 1], [0, -4, 9]])
# k = np.array([0, 2, 1])
# print(m @ k)

# m1 = np.array([[0, 1, 2], [2, -3, 1]])
# m2 = np.array([[1, -3], [6, 1], [0, -1]])
# print(m1 @ m2)

# m1 = np.eye(3)
# m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
# print(m1 @ m2)


# m1 = np.eye(2)
# m1 = np.reshape(m1, (-1, 4))[0]
# m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
# print(m1 @ m2)

# m1 = np. array([[1, 2], [3, 4]])
# m1 = np. reshape(m1, (-1, 4), "F")[0]
# m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
# result = m1@m2
# print(result)

# m1 = np. array([[-2, 6], [8, -4]])
# result = np.linalg.inv(m1)
# print(result)

# matrix = np. array([[0.9, 0.2], [0.1, 0.8]])
# eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
# print(eigenvectors)

x = np. array([1, 2, 3, 4])
y = np. array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))
