#coding: utf-8
def frequencia(L):
	diferentes = []
	iguais = []
	for i in range(len(L)):
		if L[i] not in diferentes:
			diferentes.append(L[i])
		else:
			iguais.append(L[i])
	cont = 0
	for i in range(len(diferentes)):
		if diferentes[i] not in iguais:
			print diferentes[i], "ocorre 1 vez"
		for i in range(len(iguais)):
			if diferentes[i] == iguais[i]:
				cont += 1
	print cont
	print diferentes
	print iguais
	

L = [-1.7, 3.0, 0.0, 1.5, 0.0, -1.7, 2.3, -1.7]
frequencia(L)
		
		
