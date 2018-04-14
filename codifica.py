# coding: utf-8
# Aluna:Alice Fernandes Silva/UFCG, 2015.1, Programação 1
# Criptografando uma senha

palavra = raw_input()

contador_troca = 0
senha = ""

for i in range(1,len(palavra)):
	if palavra[i] in "aA":
		senha += "4"
		contador_troca += 1
	elif palavra[i] in "eE":
		senha += "3"
		contador_troca += 1
	elif palavra[i] in "iI":
		senha += "1"
		contador_troca += 1
	elif palavra[i] in "oO":
		senha += "0"
		contador_troca += 1
	else:
		senha += palavra[i]
		
print "%s (%d troca(s))" %(palavra[0]+senha,contador_troca)
