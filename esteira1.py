#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015.1
#questão: verifica esteira

def verifica_esteira(l1, l2):
	verifica = []
	for i in range(len(l1)):
		for j in range(len(l2)):
			if l2[j] == l1[i]:
				verifica.append(l2[j])
	
	if verifica == l2:
		return True
	else:
		return False

