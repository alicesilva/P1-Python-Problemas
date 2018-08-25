#coding: utf-8
nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())

media = (nota1 + nota2 + nota3) / 3.0

if media >= 7.0 and media < 10.0:
	print "Aprovado"
elif media < 7.0:
	print "Reprovado"
elif media == 10.0:
	print "Aprovado com Distinção"


