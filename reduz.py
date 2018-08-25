#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: reduz matriz

def reduz_matriz(m):
	cont = 0
	if len(m) != 0:
		linha = 0
		for i in range(len(m)):
			linha += 1
		coluna = 0
		for j in range(len(m[0])):
			coluna += 1
		if linha > 3:
			m.pop(0)
			cont += coluna
			linha -= 1
			if linha > 3:
				m.pop(-1)
				cont += coluna
		if coluna > 3: 
			for i in range(len(m)-1,-1,-1):
				del m[i][0]
				cont += 1
			coluna -= 1
			if coluna > 3:
				for i in range(len(m)-1,-1,-1):
					del m[i][-1]
					cont += 1
	return cont




		
