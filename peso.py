# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Peso ideal com função

def calculaPeso(sexo, altura):
	if sexo == "m" or sexo == "M":
		peso_ideal = 72.7 * altura - 58
	if sexo == "f" or sexo == "F":	
		peso_ideal = 62.1 * altura - 44.7
	
	return peso_ideal

while True:
	entrada = raw_input()
	if entrada == "****":
		break
	
	dados = entrada.split()
	sexo = dados[0]
	altura = float(dados[1])
	res = calculaPeso(sexo, altura)
	if sexo == "m" or sexo == "M":
		print "Homem: peso ideal é %.1f" %res
	if sexo == "f" or sexo == "F":
		print "Mulher: peso ideal é %.1f" %res

	
		
