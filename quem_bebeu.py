#coding:  utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: quem bebeu mais menos

def quem_bebeu_mais_menos(sabado,domingo):
	sabados = []
	cont = 0
	for i in range(len(sabado)):
		cont += 1
	j = 0
	while j < cont: 
		soma_sabado = 0
		for k in range(0,cont):
			soma_sabado += sabado[k][j]
		j += 1
		sabados.append(soma_sabado)
	
	domingos = []
	cont = 0
	for i in range(len(domingo)):
		cont += 1
	j = 0
	while j < cont: 
		soma_domingo = 0
		for k in range(0,cont):
			soma_domingo += domingo[k][j]
		j += 1
		domingos.append(soma_domingo)
	
	somas = []
	for i in range(len(sabados)):
		soma = sabados[i] + domingos[i]
		somas.append(soma)
	
	mais = 1
	maior = somas[0]
	for i in range(1,len(somas)):
		if somas[i] > maior:
			maior = somas[i]
			mais = i+1
	
	menos = 1
	menor = somas[0]
	for i in range(1,len(somas)):
		if somas[i] < menor:
			menor = somas[i]
			menos = i+1
	
	tupla = (mais, menos)
	
	return tupla



