#coding: utf-8
def prench_vetor(n):
	lista = []
	lista.append(n)
	soma = n
	for i in range(9):
		soma *= 2
		lista.append(soma)
	for i in range(len(lista)):
		print "N[%d] = %d" %(i,lista[i])
	return lista

		
n = int(raw_input())
prench_vetor(n)

		
