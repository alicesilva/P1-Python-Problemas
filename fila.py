# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Fila por altura

def insere_na_fila(fila,nome,altura):
	alturas = []
	for tupla in fila:
		a, b = tupla
		alturas.append(b)
		
	if altura < alturas[0]:
		nova_tupla = nome, altura
		fila.insert(0,nova_tupla)

	elif alturas[-1] < altura:
		nova_tupla = nome, altura
		fila.insert(len(fila),nova_tupla)
	
	else:
		for i in range(len(alturas)-1):
			if alturas[i] < altura and altura < alturas[i+1]:
				nova_tupla = nome, altura
				fila.insert(i+1,nova_tupla)
				
	return fila
