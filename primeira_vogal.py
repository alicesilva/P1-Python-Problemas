# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Imprime primeira vogal

palavra = raw_input()
for i in palavra:
	if i in "aeiouAEIOU":
		print i
		break
else:
	print "-"
