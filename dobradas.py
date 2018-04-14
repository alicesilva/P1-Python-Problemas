# coding:utf-8
# Aluna:Alice Fer4nandes Silva/UFCG, 2015.1, Programação 1
# Palavra com letras dobradas
n = int(raw_input())
cont_dobradas = 0
dobradas = []
lista_palavra = []

for i in range(n):
	palavra = raw_input()
	lista_palavra.append(palavra)
	for i in range(len(palavra)-1):
		if palavra[i] == palavra[i+1]:
			dobradas.append(palavra)
			cont_dobradas += 1
			break
					
print "%d palavra(s) com letras dobradas:" %cont_dobradas

for item in dobradas:
	print item
	
print "---"
print "%d palavra(s) sem letras dobradas:" %(n-cont_dobradas)

for item in range(len(lista_palavra)):
	if lista_palavra[item] not in dobradas:
		print lista_palavra[item]
