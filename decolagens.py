# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Autorização de voos

tempo_disponivel = int(raw_input())
n = int(raw_input())

cont_aviao = 0
cont_decolagem = 0

while True:
	tempo_aviao = int(raw_input())
	cont_aviao += 1
	if tempo_aviao <= tempo_disponivel:
		tempo_disponivel -= tempo_aviao
		cont_decolagem += 1
	if cont_aviao == n:
		break
		
print "%d voo(s) autorizados." %cont_decolagem
