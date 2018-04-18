# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Consoantes

cont = 0

while True:
	palavra = raw_input()
	if palavra == "***":
		break
	if palavra[0] in "bcdfghjklmnpqrstvxywzBCDFGHJKLMNPQRSTVXYWZ":
		cont += 1

print "Palavras: %d" %cont
