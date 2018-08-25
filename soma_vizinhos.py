#coding: utf-8

def soma_vizinhos(matriz,lin,col):
	soma = 0
	for i in range(len(matriz)):
		if lin == i + 1:
			for j in range(len(matriz[i])):
				if col == j + 1:
					for k in range(0,col):
						soma += matriz[i][k]
					for k in range(col,col+1):
						soma += matriz[i][k]
					for l in range(0,lin):
						soma += matriz[l][j]
					for l in range(lin,lin+1):
						soma += matriz[l][j]
				
	soma = soma - matriz[lin-1][col-1]
	print soma

matriz = [
[ 1, 2, 3],
[ 8, 10, 12],
[21, 24, 27],
]
soma_vizinhos(matriz, 2, 2)
soma_vizinhos(matriz, 1,2)
