# Data Mining
# Date 06/10/2022
# Resume: Abre um arquivo csv e gera uma amostra a partir dele.

import csv
import random

print("Digite o nome do arquivo com extensão .csv ou .data: ", end='')
arquivo = input()

informacao = []
quantidade = 0
with open(arquivo, 'r') as file:
	for linha in file:
		informacao.append(linha)
		quantidade+=1

print("O arquivo tem ",quantidade, " linhas")
print("Digite o tamanho da amostra: ", end='')
tamanho = int(input())

indices = []
for i in range(tamanho):
	aleatorio = random.randrange(1,tamanho)
	indices.append(aleatorio)
indices.sort()

amostra = open("amostra.csv", "w")
for i in range(tamanho):
	linha = informacao[indices[i]]
	amostra.write(linha)
amostra.close()


