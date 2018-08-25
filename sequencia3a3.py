#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: sequência invertida

def inverte3a3(s):
	nova_s = ""
	for i in range(len(s)-1,-1,-1):
		if i % 3 == 0:
			for i in range(i, i+3):
				nova_s += s[i]
	
	return nova_s

