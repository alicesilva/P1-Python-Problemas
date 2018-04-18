# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# No limite

numeros = []

while True:
	indices = raw_input()
	if indices == "-":
		break
	numeros.append(indices)

limite = float(raw_input())

soma = 0
cont = 0

for i in range(len(numeros)):
	soma += float(numeros[i])
	cont += 1
	media = float(soma) / cont
	if media > limite:
		print "media = %.1f" %media
		print "num = %d" %(i + 1)
		break
	if cont == len(numeros):
		print "limite não alcançado"
		break
	
