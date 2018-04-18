# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Chave segura

chave = raw_input()

cont_vogais = 0
cont_iguais = 0


for i in range(len(chave)-2):
	if chave[i] == chave[i+1] == chave[i+2]:
		cont_iguais += 1
		print "Chave insegura. 3 caracteres consecutivos iguais."
		break 
	if chave[i] in "aieouAEIOU":
		cont_vogais += 1
	if cont_vogais > 5:
		print "Chave insegura. 6 vogais."
		break

if cont_iguais == 0 and cont_vogais <= 5:
	print "Chave segura!"
