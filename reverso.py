#coding: utf-8
def reverso(n):
	numero = str(n)
	novo_numero = ""
	for i in range(len(numero)):
		novo_numero += numero[(len(numero)-1-i)]
	return novo_numero
		
