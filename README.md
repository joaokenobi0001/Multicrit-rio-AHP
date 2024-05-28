# Multicrit-rio-AHP
Esse código implementa o método de Análise Hierárquica de Processos, uma técnica de tomada de decisão utilizada para avaliar e priorizar diferentes opções com base em uma série de critérios. A seguir, explico detalhadamente cada parte do código.

eigvals, eigvecs = np.linalg.eig(pairwise_matrix): Calcula os valores e vetores próprios da matriz de comparação por pares.
max_eigval = np.max(eigvals): Encontra o maior valor próprio.
eigvec = eigvecs[:, np.argmax(eigvals)]: Seleciona o vetor próprio correspondente ao maior valor próprio.
weights = eigvec / eigvec.sum(): Normaliza o vetor próprio para obter os pesos, dividindo cada elemento pela soma total dos elementos.
return weights.real: Retorna os pesos, garantindo que sejam valores reais (sem componentes imaginárias).

