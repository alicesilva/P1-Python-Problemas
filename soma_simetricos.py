#coding: utf-8
def soma_simetricos(valores):
	if len(valores) % 2 == 0:
		somas = []
		for i in range(len(valores)):
			if i < (len(valores)/2):
				soma = valores[i] + valores[len(valores) - 1 - i]
				somas.append(soma)
	else:
		somas = []
		for i in range(len(valores)):
			if i < (len(valores)/2):
				soma = valores[i] + valores[len(valores) - 1 - i]
				somas.append(soma)
		
		somas.append(valores[len(valores)/2])
	return somas
	
