#coding: utf-8
salario = float(raw_input())
if salario<=400.00:
	salario_novo = salario + 0.15*salario
	reajuste = salario_novo - salario
	print "Novo salario: %.2f" %(salario_novo)
	print "Reajuste ganho: %.2f" %(reajuste)
	print "Em percentual: 15 %"
elif salario>=400.01 and salario <= 800.00:
	salario_novo = salario + 0.12 * salario
	reajuste = salario_novo - salario
	print "Novo salario: %.2f" %(salario_novo)
	print "Reajuste ganho: %.2f" %(reajuste)
	print "Em percentual: 12 %"
elif salario>=800.01 and salario <= 1200.00:
	salario_novo = salario + 0.10 * salario
	reajuste = salario_novo - salario
	print "Novo salario: %.2f" %(salario_novo)
	print "Reajuste ganho: %.2f" %(reajuste)
	print "Em percentual: 10 %"
elif salario>=1200.01 and salario <= 2000.00:
	salario_novo = salario + 0.07 * salario
	reajuste = salario_novo - salario
	print "Novo salario: %.2f" %(salario_novo)
	print "Reajuste ganho: %.2f" %(reajuste)
	print "Em percentual: 7 %"
else:
	salario_novo = salario + 0.04 * salario
	reajuste = salario_novo - salario
	print "Novo salario: %.2f" %(salario_novo)
	print "Reajuste ganho: %.2f" %(reajuste)
	print "Em percentual: 4 %"
	
