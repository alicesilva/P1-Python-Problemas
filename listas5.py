#coding: utf-8
vetor = []
vetor_par = []
vetor_impar = []

for i in range(20):
	numero = int(raw_input())
	vetor.append(numero)
	if numero % 2 == 0:
		vetor_par.append(numero)
	else:
		vetor_impar.append(numero)
		
print "Vetor:",vetor
print "Vetor par:",vetor_par
print "Vetor ímpar:",vetor_impar
	
