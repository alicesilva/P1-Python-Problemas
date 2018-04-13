# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Status de uma disciplina
nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
faltas = int(raw_input())
media = (nota1 + nota2 + nota3) / 3.0
presenca = ((30 - faltas) / 30.0) * 100.0
if presenca >= 75.0:
	if media < 4.0:
		print "reprovado por nota"
	elif 4.0 <= media < 7.0:
		print "prova final"
	else:
		print "aprovado por media"
else:
	print "reprovado por faltas"
