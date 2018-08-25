#coding: utf-8
def eliminar_vogais(string):
	nova_string = ""
	for i in range(len(string)):
		if string[i] not in "aeiouAEIOU":
			nova_string += string[i]
	
	return nova_string
