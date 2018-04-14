# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Conversão de matrículas na UFCG

matricula = raw_input()

matricula_nova = "1"

for i in range(1,len(matricula)-5+1):
	matricula_nova += matricula[i]

for i in matricula[4]:
	matricula_nova += matricula[4] + "0"

for i in range(5,len(matricula)):
	matricula_nova += matricula[i]

print matricula_nova
