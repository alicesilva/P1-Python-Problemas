#coding: utf-8
nota1 = float(raw_input())
nota2 = float(raw_input())

media = (nota1 + nota2) / 2.0

if media >= 7 and media != 10:
	print "Aprovado"
elif media < 7:
	print "Reprovado"
elif media == 10:
	print "Aprovado com Disinção"
