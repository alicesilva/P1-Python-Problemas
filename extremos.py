# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Classificação de elementos utilizando a média dos extremos
contador_maior = 0
contador_menor = 0
lista = []
n = int(raw_input())

for i in range(n):
	numero = int(raw_input())
	lista.append(numero)
	maior = lista[0]
	menor = lista[0]
	
for item in lista:
	if maior < item:
		maior = item
		
for item in lista:
	if menor > item:
		menor = item

media = (maior + menor) / 2.0

print "Menor número: %d" %(menor)
print "Maior número: %d" %(maior)
print "Média dos extremos: %.2f" %(media)

for item in range(len(lista)):
	if lista[item] > media:
		contador_maior += 1
	elif lista[item] == media:
		pass
	else:
		contador_menor += 1
			
print "%d número(s) abaixo da média" %(contador_menor)
print "%d número(s) acima da média"  %(contador_maior)
