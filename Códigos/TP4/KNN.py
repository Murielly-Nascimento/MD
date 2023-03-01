# Algoritmo KNN
from math import sqrt

# Calcula a distância Euclidiana
# Parâmetros instância1 e instância2
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1): # Percorre os atributos da instância
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

# Encontra os vizinhos mais próximos
# Parâmetros: Os dados de teste, uma instância, o número de K vizinhos
def get_neighbors(train, test_row, num_neighbors): 
	distances = list() 
	for train_row in train:
		dist = euclidean_distance(test_row, train_row) # Calcula a distância Euclidiana entre um ponto dos dados de treinamento e uma instância
		distances.append((train_row, dist)) # Adiciona a lista
	distances.sort(key=lambda tup: tup[1]) # Ordena a lista de distâncias
	neighbors = list() # A lista dos Vizinhos a uma instância 
	for i in range(num_neighbors): # Dado o número de vizinhos
		neighbors.append(distances[i][0]) # Adiciona os vizinhos mais próximos
	return neighbors

# Faz uma classificação preditiva com base nos valores vizinhos
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors) # Lista dos vizinhos	
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

# Testa o algortimo KNN
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]
prediction = predict_classification(dataset, dataset[0], 3)
print('Expected %d, Got %d.' % (dataset[0][-1], prediction))