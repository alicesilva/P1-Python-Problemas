# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Mais ocorrência caractere

palavras = []

while True:
	palavra = raw_input()
	if palavra == "fim":
		break
	palavras.append(palavra)

caractere = raw_input()
N = int(raw_input())

lista1 = []
for i in range(len(palavras)):
	cont_acima = 0
	for item in palavras[i]:
		if item == caractere:
			cont_acima += 1
			if cont_acima > N:
				lista1.append(palavras[i])
				print palavras[i]
				break

if len(lista1) == 0:
	print "Nenhuma palavra encontrada."
