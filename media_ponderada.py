# coding: utf-8
# Alice Fernandes/UFCG, Programação 1
# Recebe notas, ponderações da nota e calcula média

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
ponderacao_nota1 = float(raw_input())
ponderacao_nota2 = float(raw_input())
ponderacao_nota3 = 100 - (ponderacao_nota1 + ponderacao_nota2)
media = nota1*(ponderacao_nota1 / 100.0) + nota2*(ponderacao_nota2/100.0) + nota3*(ponderacao_nota3 / 100.0)
print "Média Final: %.1f" % (media)
