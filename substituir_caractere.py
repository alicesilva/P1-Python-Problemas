#coding: utf-8
def substituir_caractere(string, carac1, carac2):
	nova_string = ""
	for i in range(len(string)):
		if string[i] != carac1:
			nova_string += string[i]
		else:
			nova_string += carac2
	
	return nova_string

