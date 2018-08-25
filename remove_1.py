#coding: utf-8

def conta_vogais(palavra):
	n = 0
	for i in palavra:
		if i in 'aeiou':
			n+=1
	return n

def max_de_vogais_p_palavras(lista):
	n_max = 0
	for palavra in lista:
		n = 0
		for letra in palavra:
			if letra in 'aeiou':
				n += 1
			if n > n_max:
				n_max = n
	
	return n_max

def remove_palavras_com_mais_vogais(lista):
	
	rm = []
	n_max = max_de_vogais_p_palavras(lista)
	if n_max == 0:
		return
		
	for palavra in lista:
		if conta_vogais(palavra) >= n_max:
			rm.append(palavra)
	
	for i in rm:
		lista.remove(i)
	print lista
	print n_max
lista1 = ['arara', 'aeiou','tv', 'bacia','aaaa','eeeee']
assert remove_palavras_com_mais_vogais(lista1) == None
assert lista1 == ['tv','bacia']
