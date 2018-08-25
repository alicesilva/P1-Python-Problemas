#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: labir move direita

def move_direita(labirinto):
	for i in range(len(labirinto)):
		for j in range(len(labirinto[i])-1):
			if labirinto[i][j] == "*" and labirinto[i][j+1] == " ":
				labirinto[i][j], labirinto[i][j+1] = labirinto[i][j+1], labirinto[i][j]
				break
	
	for i in range(len(labirinto)):
		for j in range(len(labirinto[i])):
			if labirinto[i][j] == "*":
				a = i
				b = j
	tupla = (a,b)
	return tupla




