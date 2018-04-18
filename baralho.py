# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Guerra baralho

cont_j1 = 0
cont_j2 = 0
cont_empate = 0

while True:
	entrada = raw_input()
	dados = entrada.split()
	jogador1 = int(dados[0])
	jogador2 = int(dados[1])
	if entrada == "0 0":
		break
	if jogador1 > jogador2:
		cont_j1 += 1
	elif jogador2 > jogador1:
		cont_j2 += 1
	else:
		cont_empate += 1
		
print "Jogador 1: %d, Jogador 2: %d, Empates: %d" %(cont_j1,cont_j2,cont_empate)
