#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: matriz menor

def matriz_menor(M1,M2):
	nova_M = []
	for i in range(len(M1)):
		for j in range(len(M2)):
			if i == j:
				menores = []
				for k in range(len(M1[i])):
					for l in range(len(M2[j])):
						if k == l:
							if M1[i][k] <= M2[j][l]:
								menores.append(M1[i][k])
							else:
								menores.append(M2[j][l])
				nova_M.append(menores)
	
	return nova_M



