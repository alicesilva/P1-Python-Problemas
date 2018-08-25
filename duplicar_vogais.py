#coding: utf-8
def duplicar_vogais(string):
	nova_string = ""
	for i in range(len(string)):
		if string[i] in "aeiouAEIOU":
			nova_string += string[i] * 2
		else:
			nova_string += string[i]
	
	return nova_string
