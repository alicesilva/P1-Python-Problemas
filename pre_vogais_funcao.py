# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Pré-vogais

def pre_vogais(palavra):
	letras = []
	for i in range(1,len(palavra)):
		if palavra[i] in "AEIOUaeiou":
			if palavra[i-1].lower() in letras:
				break
			else:
				letras.append(palavra[i-1].lower())
	
	return letras

