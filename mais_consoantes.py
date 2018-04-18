# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Mais consoantes

cont_palavra = 0

while True:
	palavra = raw_input()
	cont_palavra += 1
	cont_consoantes = 0
	cont_vogais = 0
	for i in palavra:
		if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
			cont_consoantes += 1
		elif i in "aeiouAEIOU":
			cont_vogais += 1
	if cont_consoantes > cont_vogais:
		break

print cont_palavra
