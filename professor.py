# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Carga de trabalho de professor universitário

soma = 0
cont = 0

while True:
	horas = int(raw_input())
	if horas > 10 or horas + soma > 60:
		soma += 0
		cont += 1
	else:
		soma += horas
	if soma == 60:
		break
	

print "Rejeitadas = %d" %cont
print "Fim de semana!"
