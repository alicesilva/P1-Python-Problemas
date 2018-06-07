# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Obfuscation

def obfuscation(palavra):
	dados = palavra.split()
	nova_palavra = ""
	if palavra[-1] == " ":
		for i in range(len(dados)):
			nova_palavra += dados[i] + "*" * len(dados[i])
	else:
		for i in range(len(dados)-1):
			nova_palavra += dados[i] + "*" * len(dados[i])
		nova_palavra += dados[-1]
	
	n = ""	
	for i in range(len(nova_palavra)):
		if nova_palavra[i] != "*":
			if nova_palavra[i] == nova_palavra[i].upper():
				n += nova_palavra[i].lower()
			elif nova_palavra[i] == nova_palavra[i].lower():
				n += nova_palavra[i].upper()
		else:
			n += nova_palavra[i]
		
	obfuscada = ""
	letras_maiores = ["A","B","E","G","I","L","S","O"]
	letras_menores = ["a","b","e","g","i","l","s","o"]
	numeros = ["4","8","3","6","1","7","5","0"]
	
	for i in range(len(n)):
		if n[i] in letras_maiores:
			for j in range(len(letras_maiores)):
				if n[i] == letras_maiores[j]:
					obfuscada += numeros[j]
		elif n[i] in letras_menores:
			for j in range(len(letras_menores)):
				if n[i] == letras_menores[j]:
					obfuscada += numeros[j]
		elif n[i] in numeros:
			for j in range(len(numeros)):
				if n[i] == numeros[j]:
					obfuscada += letras_maiores[j]
					
				
		else:
			obfuscada += n[i]
		
	return obfuscada




while True:
	palavra = raw_input()
	if palavra == "fim":
		break
	res = obfuscation(palavra)
	print res
	
	
			
			
