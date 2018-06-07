# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Maiores e menores

n = int(raw_input())
menores = []
maiores = []

while True:
	sequencia = int(raw_input())
	if sequencia < 0:
		break
	if sequencia <= n:
		menores.append(sequencia)
	else:
		maiores.append(sequencia)

print menores
print n
print maiores
	
