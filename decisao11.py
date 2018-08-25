#coding: utf-8
salario = float(raw_input())

print "o salário antes do reajuste: R$ %.2f" %salario

if salario <= 280:
	reajuste = 20/100.0 * salario
	print "o percentual de aumento aplicado: 20%"
	print "o valor do aumento: R$ %.2f" %reajuste
elif 280 < salario < 700:
	reajuste = 15/100.0 * salario
	print "o percentual de aumento aplicado: 15%"
	print "o valor do aumento: R$ %.2f" %reajuste
elif 700 < salario < 1500:
	reajuste = 10/100.0 * salario
	print "o percentual de aumento aplicado: 10%"
	print "o valor do aumento: R$ %.2f" %reajuste
elif salario >= 1500:
	reajuste = 5/100.0 * salario
	print "o percentual de aumento aplicado: 5%"
	print "o valor do aumento: R$ %.2f" %reajuste

salario_novo = salario + reajuste

print "o novo salário, após o aumento: R$ %.2f" %salario_novo
	
