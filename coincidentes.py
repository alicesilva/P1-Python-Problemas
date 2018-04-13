# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Coincidentes

palavra1 = raw_input()
palavra2 = raw_input()

cont = 0
letras = []
indices = []

if len(palavra1) <= len(palavra2):
	for i in range(len(palavra1)):
		if palavra1[i] == palavra2[i]:
			cont += 1
			letras.append(palavra1[i])
			indices.append(i)
else:
	for i in range(len(palavra2)):
		if palavra2[i] == palavra1[i]:
			cont += 1
			letras.append(palavra2[i])
			indices.append(i)

porcentagem = cont / float(len(palavra1) + len(palavra2)) * 100

print "Letras coincidentes"

if len(letras) != 0:
	for i in range(len(letras)):
		print "'%s' na posição %d" %(letras[i],indices[i]+1)

print "Total de letras coincidentes: %d (%.0f%%)" %(cont,porcentagem)
