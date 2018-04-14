# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Quantidade de números pares e ímpares

contador_par = 0
contador_impar = 0
soma_par = 0
soma_impar = 0

n = int(raw_input())

for i in range(n):
	numero = int(raw_input())
	if numero % 2 == 0:
		contador_par += 1
		soma_par += numero
	else:
		contador_impar += 1
		soma_impar += numero

media_par = float(soma_par) / contador_par
media_impar = float(soma_impar) / contador_impar

print "pares: %d" %(contador_par)
print "ímpares: %d" %(contador_impar)
print "média pares: %.1f" %(media_par)
print "média ímpares: %.1f" %(media_impar)
