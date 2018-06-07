# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Embaralhador

def gira_esquerda(sequencia):
	caracteres = sequencia.split()
	for i in range(len(caracteres)-1,0,-1):
		caracteres[i] , caracteres[(i + 1) % len(caracteres)] = caracteres[(i + 1) % len(caracteres)], caracteres[i]
	nova_sequencia = ""
	for i in range(len(caracteres)-1):
		nova_sequencia += caracteres[i] + " "
	nova_sequencia += caracteres[-1]
	return nova_sequencia

def gira_direita(sequencia):
	caracteres = sequencia.split()
	caracteres[0], caracteres[-1] = caracteres[-1], caracteres[0]
	for i in range(len(caracteres)-2):
		caracteres[i], caracteres[i+1] = caracteres[i+1], caracteres[i]
	nova_sequencia = ""
	for i in range(len(caracteres)-1):
		nova_sequencia += caracteres[i] + " "
	nova_sequencia += caracteres[-1]	
	return nova_sequencia

def intercala(sequencia):
	caracteres = sequencia.split()
	for i in range(len(caracteres)-1):
		if i % 2 == 0:
			caracteres[i], caracteres[i+1] = caracteres[i+1], caracteres[i]
	nova_sequencia = ""
	for i in range(len(caracteres)-1):
		nova_sequencia += caracteres[i] + " "
	nova_sequencia += caracteres[-1]
	return nova_sequencia

sequencia = raw_input()
while True:	
	operacao = raw_input()
	if operacao == "fim":
		break
	if operacao == "GE":
		sequencia = gira_esquerda(sequencia)
		print sequencia
	if operacao == "GD":
		sequencia = gira_direita(sequencia)
		print sequencia
	if operacao == "I":
		sequencia = intercala(sequencia)
		print sequencia
