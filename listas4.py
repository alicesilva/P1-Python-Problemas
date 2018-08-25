#coding: utf-8
vetor = ["a","c","v","d","e","f","g","t","u","i"]
cont = 0
consoantes = []

for i in range(len(vetor)):
	if vetor[i] in "BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
		cont += 1
		consoantes.append(vetor[i])

for i in consoantes:
	print i
