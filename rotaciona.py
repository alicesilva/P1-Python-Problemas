#coding: utf-8

def rotaciona(lista, N):
	for i in range(len(lista)-1,N-1,-1):
		lista[i] , lista[(i+N) % len(lista)] = lista[(i+N) % len(lista)],lista[i]
	
	print lista

lista = [1,2,3,5,6,4,7,8]
N = 3
rotaciona(lista, N)
