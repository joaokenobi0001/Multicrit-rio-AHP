import numpy as np

def ahp(pairwise_matrix):
    eigvals, eigvecs = np.linalg.eig(pairwise_matrix)
    max_eigval = np.max(eigvals)
    eigvec = eigvecs[:, np.argmax(eigvals)]
    weights = eigvec / eigvec.sum()
    return weights.real

def consistency_ratio(pairwise_matrix, weights):
    n = pairwise_matrix.shape[0]
    RI = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45]
    lamda_max = np.max(np.linalg.eigvals(pairwise_matrix)).real
    CI = (lamda_max - n) / (n - 1)
    CR = CI / RI[n - 1]
    return CR

# Exemplo de matriz de comparação
pairwise_matrix = np.array([
    [1, 1/3, 3],
    [3, 1, 5],
    [1/3, 1/5, 1]
])

weights = ahp(pairwise_matrix)
cr = consistency_ratio(pairwise_matrix, weights)

print("Pesos:", weights)
print("Razão de Consistência (CR):", cr)
