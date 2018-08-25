#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: busca em matriz

def busca_matriz(m,e):
	for i in range(len(m)):
		cont = 0
		for j in range(len(m[i])):
			if m[i][j] == e:
				a = i
				b = j
				cont += 1
				break
		break
	if cont == 0:
		return None
	else:
		tupla = (a,b)
		return tupla



