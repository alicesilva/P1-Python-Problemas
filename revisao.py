#coding: utf-8
def soma_simetricos(valores):
	if len(valores) % 2 == 0:
		somas = []
		for i in range(len(valores)):
			if i < (len(valores)/2):
				soma = valores[i] + valores[len(valores)-i-1]
				somas.append(soma)
	if len(valores) % 2 != 0:
		somas = []
		for i in range(len(valores)):
			if i < (len(valores)/2):
				soma = valores[i] + valores[len(valores)-i-1]
				somas.append(soma)
		somas.append(valores[(len(valores)/2)])
			
	return somas


assert soma_simetricos([2, 5, 3, 9]) == [11, 8]
assert soma_simetricos([2, 5, 3, 9, 4]) == [6, 14, 3]
