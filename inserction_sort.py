# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Insertion sort

def insertion_sort(numeros):
	for i in range(1,len(numeros)):
		for j in range(1,len(numeros)):
			if numeros[j] < numeros[j-1]:
				numeros[j-1], numeros[j] = numeros[j], numeros[j-1]
