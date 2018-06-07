# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Vogais adjacentes

def tem_vogais_adjacentes(palavra):
	cont = 0
	for i in range(len(palavra)-1):
		if palavra[i] in "aeiouAEIOU" and palavra[i+1] in "aeiouAEIOU":
			cont += 1
			return "sim"
			break
	if cont ==  0:
		return "nao"
		
assert tem_vogais_adjacentes("orfeu") == "sim"
assert tem_vogais_adjacentes("brasil") == "nao"
assert tem_vogais_adjacentes("voo") == "sim"

palavra = raw_input()
imprimir = tem_vogais_adjacentes(palavra)
print imprimir
	
