# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Primeiro acima da média

soma = 0
cont = 0
valores = []

while True:
	indices = raw_input()
	if indices == "fim":
		break
	valores.append(float(indices))
	soma += float(indices)
	cont += 1

media = soma / cont

for i in range(len(valores)):
	if valores[i] > media:
		print "%d, %.2f > %.2f" %(i,valores[i],media)
		break
	
