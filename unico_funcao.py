# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Único

def unico(string):
	nova_string = ""
	for i in range(len(string)-1):
		if string[i] != string[i+1]:
			nova_string += string[i]
	
	if len(string) != 0:
		nova_string += string[-1]
	
	return nova_string
