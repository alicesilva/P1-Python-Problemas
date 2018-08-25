#coding: utf-8
contador_par = 0
contador_impar = 0
contador_positivo = 0
contador_negativo = 0

for i in range(5):
	numero = int(raw_input())
	if numero % 2 == 0:
		contador_par += 1
	else:
		contador_impar += 1
	if numero != 0:
		if numero > 0:
			contador_positivo +=1
		else:
			contador_negativo += 1

print "%d valor(es) par(es)" %contador_par
print "%d valor(es) impar(es)" %contador_impar
print "%d valor(es) positivo(s)" %contador_positivo
print "%d valor(es) negativo(s)" %contador_negativo
