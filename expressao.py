#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: expressão regular simples

def is_substring_expr(str1,str2):
	palavras = str2.split("*")
	comeco = ""
	for i in range(0,len(palavras[0])):
		comeco += str1[i]
	j = len(str1) - len(palavras[-1])
	final = ""
	for i in range(j,len(str1)):
		final += str1[i]
	if comeco == palavras[0] and final == palavras[1]:
		return True
	else:
		return False
	
