#coding: utf-8
def palindromo(n):
	numero = str(n)
	novo_numero = ""
	
	for i in range(len(numero)):
		novo_numero += numero[len(numero)- i- 1]
	
	if novo_numero == n:
		return True
	else:
		return False
	
