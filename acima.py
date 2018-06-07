# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Acima de

def acima_de(N,L):
	L1 = []
	for i in range(len(L)):
		if L[i] > N:
			L1.append(i)
	
	return L1
