#coding: utf-8
cont_par = 0
cont_impar = 0

for i in range(10):
	numero = int(raw_input())
	if numero % 2 == 0:
		cont_par += 1
	else:
		cont_impar += 1

print "%d números pares" %cont_par
print "%d números ímpares" %cont_impar
