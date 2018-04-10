# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Percentual de reajuste

salario_atual = float(raw_input("Valor atual? "))
salario_novo = float(raw_input("Novo valor? "))

if salario_atual == 0.00:
	reajuste = ((salario_atual + salario_novo) / 100.0) * 100
	print "Reajuste de %.1f%%" %(reajuste)
elif salario_atual < 0.00:
	print "Impossivel salário negativo"
else:
	reajuste = (salario_novo - salario_atual) / salario_atual * 100
	print "Reajuste de %.1f%%" %(reajuste)
