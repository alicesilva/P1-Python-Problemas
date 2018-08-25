#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: lista com números opostos

def lista_so_com_oposto(lista):
	auxiliar = []
	for i in range(len(lista)-1,-1,-1):
		if -lista[i] not in lista:
			lista.pop(i)
