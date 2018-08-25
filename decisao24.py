#coding: utf-8
numero1 = raw_input()
numero2 = raw_input()
operacao = raw_input("Qual operação deseja realizar? ")

if operacao == "soma" or operacao == "SOMA" or operacao == "Soma":
	soma = numero1 + numero2
	print soma
	if soma % 2 == 0:
		print "É par"
	else:
		print "É ímpar"
	if soma >= 0:
		print "É positivo"
	else:
		print "É negativo"
	for i in range(len(str(soma))):
		if soma[i] == ".":
			print "É decimal"
			
