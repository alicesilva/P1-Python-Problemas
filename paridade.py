# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Paridade

while True:
	sequencia = raw_input()
	cont = 0
	for i in range(len(sequencia)-1):
		if sequencia[i] == "1":
			cont += 1
	if cont % 2 == 0 and sequencia[-1] == "1" or \
	cont % 2 != 0 and sequencia[-1] == "0":
		break

print "ERRO"



