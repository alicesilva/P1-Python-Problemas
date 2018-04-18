# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Aula de médias

soma = 0
cont = 0
valores = []

while True:
	numeros = float(raw_input())
	soma += numeros
	cont += 1
	valores.append(numeros)
	if soma >= 100:
		break
		
media = soma / cont

print "Quantidade de números lidos: %d" %cont
print "Soma dos números lidos: %.2f" %soma
print "Média = %.2f" %media
print

print "Abaixo da média"
for i in range(len(valores)):
	if valores[i] < media:
		print "%.2f (%do)" %(valores[i],i+1)

print
print "Acima da média"
for i in range(len(valores)):
	if valores[i] > media:
		print "%.2f (%do)" %(valores[i],i+1)
