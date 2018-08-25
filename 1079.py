#coding: utf-8
n = int(raw_input())

lista_media = []

for i in range(n):
	testes = raw_input()
	dados = testes.split()
	for i in range(len(dados)):
		nota1 = float(dados[0])
		nota2 = float(dados[1])
		nota3 = float(dados[2])
	media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10.0
	lista_media.append(media)
		
for item in range(len(lista_media)):
	print "%.1f" %lista_media[item]
