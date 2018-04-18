# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Abaixo da média

soma = 0
cont = 0
valores = []

while True:
	numero = raw_input()
	if numero == "fim":
		break
	soma += int(numero)
	cont += 1
	valores.append(int(numero))

media = float(soma) / cont

print "%.2f" %media

for i in range(len(valores)):
	if valores[i] < media:
		print "%d %d" %(i+1,valores[i])
