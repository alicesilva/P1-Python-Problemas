# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Merge invertido

def merge_invertido(l1,l2):
	lista_nova = []
	i=len(l1) -1
	j=len(l2)-1
	while i  > -1 and j > -1:
		if l1[i] > l2[j]:
			lista_nova.append(l1[i])
			i=i-1
		else:
			lista_nova.append(l2[j])
			j=j-1
	while i > -1:
		lista_nova.append(l1[i])
		i=i-1
	while j > -1:
		lista_nova.append(l2[j])
		j=j-1
	
	for i in range(len(lista_nova)-1):
		if lista_nova[i] < lista_nova[i+1]:
			lista_nova[i],lista_nova[i+1] = lista_nova[i+1], lista_nova[i]
		
		
	
	return lista_nova


