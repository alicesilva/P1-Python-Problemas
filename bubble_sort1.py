#coding: utf-8
def bubble_sort(lista):
	trocas = 0
	trocou = False
	for i in range(len(lista)):
		for j in range(0, len(lista) - i -1):
			if lista[j] > lista[j+1]:
				lista[j], lista[j+1] = lista[j+1],lista[j]
				trocas += 1
				trocou = True
				if not trocou:
					break
	return lista
	
lista = [3,5,6,7,8,1,10,3,0,19,20]
print bubble_sort(lista)
