# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Calculadora

while True:
	entrada = raw_input()
	if entrada == "5":
		break
	dados = entrada.split()
	if dados[0] == "1":
		for i in range(1,len(dados)):
			operacao = int(dados[1]) + int(dados[2])
		print operacao
	if dados[0] == "2":
		for i in range(1,len(dados)):
			operacao = int(dados[1]) - int(dados[2])
		print operacao
	if dados[0] == "3":
		for i in range(1,len(dados)):
			operacao = int(dados[1]) * int(dados[2])
		print operacao
			
	if dados[0] == "4":
		if int(dados[2]) != 0:
			for i in range(len(dados)):
				operacao = int(dados[1]) / int(dados[2])
			print operacao
		else:
			print "Erro: Divisão por 0"

	


