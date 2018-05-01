# coding: utf-8
# Aluna:Alice Fernandes Silva/UFCG, 2015.1, Programação 1
# Letras Aletrnadas

def letras_alternadas(string):
	nova_string = ""
	for i in range(len(string)):
		if i % 2 == 0:
			nova_string += string[i]
	return nova_string

assert letras_alternadas("casa") == 'cs'
assert letras_alternadas("exemplo") == 'eepo'
assert letras_alternadas("") == ''
assert letras_alternadas("alice") == 'aie'
		
