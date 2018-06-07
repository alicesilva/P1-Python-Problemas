# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015.1
# Cria senha

def criaSenhaFraca(palavra):
	nova_senha = ""
	for i in range(len(palavra)):
		nova_senha += palavra[i]
	return nova_senha


def criaSenhaForte(palavra):
	letras_menores = ["o","i","l","e","a","b","t"]
	letras_maiores = ["O","I","L","E","A","B","T"]
	numeros = [0,1,1,3,4,6,7]
	nova_senha = ""
	for i in range(len(palavra)):
		if palavra[i] in letras_menores:
			for j in range(len(letras_menores)):
				if palavra[i] == letras_menores[j]:
					nova_senha += str(numeros[j])
		elif palavra[i] in letras_maiores:
			for j in range(len(letras_maiores)):
				if palavra[i] == letras_maiores[j]:
					nova_senha += str(numeros[j])
		else:
			nova_senha += palavra[i]
	return nova_senha

while True:
	palavras = raw_input()
	if palavras == "***":
		break
	dados = palavras.split()
	if dados[1] == "fraco":
		palavra = dados[0]
		print "((%s))" %criaSenhaFraca(palavra)
	elif dados[1] == "forte":
		palavra = dados[0]
		print "((%s))" %criaSenhaForte(palavra)
	
		


			
	
