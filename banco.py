# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Digito verificador

numero = raw_input()
primeira_parte = 0
segunda_parte = 0

for i in range(0,len(numero),2):
	primeira_parte += int(numero[i])

for x in range(1,len(numero),2):
	segunda_parte += int(numero[x])

digito = primeira_parte * segunda_parte % 11.0

if digito == 10.0:
	print "%s-X" %(numero)
else:
	print "%s-%0.f" %(numero,digito)
