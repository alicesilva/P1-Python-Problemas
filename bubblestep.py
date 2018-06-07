# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Bubble step

while True:
	sequencia = raw_input()
	if sequencia == "fim":
		break
	dados = sequencia.split()
	nova_sequencia = ""
	for i in range(len(dados)-1):
		if int(dados[i]) >= int(dados[i+1]):
			dados[i], dados[i+1] = dados[i+1], dados[i]
		nova_sequencia += dados[i] + " "
	nova_sequencia += dados[-1]
	
	print nova_sequencia
