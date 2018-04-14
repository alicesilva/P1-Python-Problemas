# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Atendimentos no SAMU
atendimentos = []
soma = 0
for i in range(12):
	mes = int(raw_input())
	atendimentos.append(mes)
	soma += mes
	
media = soma / 12.0
print "Média mensal de atendimentos: %.2f" %(media)
print "----"

for i in range(len(atendimentos)):
	if atendimentos[i] > media:
		print "Mês %d: %d" %(i+1,atendimentos[i])
