import numpy as np

# Função para calcular os pesos usando AHP
def ahp(pairwise_matrix):
    eigvals, eigvecs = np.linalg.eig(pairwise_matrix)
    max_eigval = np.max(eigvals)
    eigvec = eigvecs[:, np.argmax(eigvals)]
    weights = eigvec / eigvec.sum()
    return weights.real

# Função para calcular a Razão de Consistência (CR)
def consistency_ratio(pairwise_matrix):
    n = pairwise_matrix.shape[0]
    RI = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45]
    lamda_max = np.max(np.linalg.eigvals(pairwise_matrix)).real
    CI = (lamda_max - n) / (n - 1)
    CR = CI / RI[n - 1]
    return CR

# Matriz de comparação dos critérios
criteria_matrix = np.array([
    [1, 1/2, 3],
    [2, 1, 4],
    [1/3, 1/4, 1]
])

# Matrizes de comparação dos carros para cada critério
# Exemplo para 3 carros: Carro A, Carro B, Carro C

# Critério Preço
price_matrix = np.array([
    [1, 1/3, 3],
    [3, 1, 5],
    [1/3, 1/5, 1]
])

# Critério Conforto
comfort_matrix = np.array([
    [1, 3, 1/5],
    [1/3, 1, 1/7],
    [5, 7, 1]
])

# Critério Desempenho
performance_matrix = np.array([
    [1, 5, 9],
    [1/5, 1, 4],
    [1/9, 1/4, 1]
])

# Calculando os pesos dos critérios
criteria_weights = ahp(criteria_matrix)
criteria_cr = consistency_ratio(criteria_matrix)

# Calculando os pesos dos carros para cada critério
price_weights = ahp(price_matrix)
price_cr = consistency_ratio(price_matrix)

comfort_weights = ahp(comfort_matrix)
comfort_cr = consistency_ratio(comfort_matrix)

performance_weights = ahp(performance_matrix)
performance_cr = consistency_ratio(performance_matrix)

# Calculando a pontuação final dos carros
final_scores = (price_weights * criteria_weights[0] +
                comfort_weights * criteria_weights[1] +
                performance_weights * criteria_weights[2])

# Identificando o melhor carro
best_car_index = np.argmax(final_scores)
car_names = ['Carro A', 'Carro B', 'Carro C']
best_car = car_names[best_car_index]

print("Pesos dos Critérios:", criteria_weights)
print("Razão de Consistência dos Critérios (CR):", criteria_cr)

print("Pesos dos Carros no Critério Preço:", price_weights)
print("Razão de Consistência do Critério Preço (CR):", price_cr)

print("Pesos dos Carros no Critério Conforto:", comfort_weights)
print("Razão de Consistência do Critério Conforto (CR):", comfort_cr)

print("Pesos dos Carros no Critério Desempenho:", performance_weights)
print("Razão de Consistência do Critério Desempenho (CR):", performance_cr)

print("Pontuações Finais dos Carros:", final_scores)
print("O melhor carro é:", best_car)
