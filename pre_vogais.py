#coding: utf-8
def pre_vogais(palavra):
	letras = []
	for i in range(len(palavra)):
		if i > 1 and palavra[i] in "aeiouAEIOU":
			if palavra[i-1] not in letras:
				letras.append(palavra[i-1].lower())
	return letras
