# coding: utf-8
# Calculo da situação do aluno em uma disciplina
print "== Estágio 1 =="

peso1 = float(raw_input("Peso? "))
nota1 = float(raw_input("Nota? "))

print "== Estágio 2 =="

peso2 = float(raw_input("Peso? "))
nota2 = float(raw_input("Nota? "))

print "== Estágio 3 =="
peso3 = float(raw_input("Peso? "))
nota3 = float(raw_input("Nota? "))

media_parcial = peso1*nota1 + peso2*nota2 + peso3*nota3

nota_final1 = (5.0 - media_parcial * 0.6)/0.4
nota_final2 = (7.0 - media_parcial * 0.6)/0.4

print "== Resultados =="
print "Média parcial: %.1f" %(media_parcial)
print "Nota na final, pra média 5.0 = %.1f" %(nota_final1)
print "Nota na final, pra média 7.0 = %.1f" %(nota_final2)

