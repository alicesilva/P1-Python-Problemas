#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: subsequênica 1,2,3

def tem123plus(l):
	cont = 0
	for i in range(len(l)):
		if l[i] == 1:
			cont += 0
			for j in range(i,len(l)):
				cont += 0
				if l[j] == 2:
					cont += 0
					for k in range(j,len(l)):
						if l[k] == 3:
							cont += 1
						else:
							cont += 0
	
	if cont > 0:		
		for i in range(len(l)):
			if l[i] == 1:
				return i
				break
	if cont == 0:
		return -1



