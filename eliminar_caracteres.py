#coding: utf-8
def eliminar_caracteres(string, carac1, carac2):
	nova_string = ""
	for i in range(len(string)):
		if string[i] != carac1 and string[i] != carac2:
			nova_string += string[i]
	return nova_string

