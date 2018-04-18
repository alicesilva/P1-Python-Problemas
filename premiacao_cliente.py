# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Premiação cliente

cont_joao = 0
cont_julio = 0

while True:
	entrada = raw_input()
	if entrada == "fim":
		break
	dados = entrada.split()
	nome = dados[0]
	gastos = float(dados[1])
	
	if nome == "joao":
		cont_joao += 1
	else:
		cont_julio += 1
		
	if cont_julio > 2 or cont_joao > 2 or gastos >= 2000:
		break
		
if cont_joao > cont_julio or cont_joao > cont_julio or gastos >= 2000:
	print "%s foi o vencedor. Comprou mais de duas vezes no período." %nome

elif cont_joao < 2 and cont_julio < 2 and gastos >= 2000:
	print "%s foi o vencedor. Comprou mais R$ 2000.00 no período." %nome

elif cont_joao == cont_julio:
	print "Não houve vencedor."
