# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Mastery learning

print "Mastery Learning"
print "Cálculo da nota na unidade"
print

nota1 = float(raw_input("Nota? "))
nota2 = float(raw_input("Nota? "))


if nota1 > nota2:
	nota1, nota2 = nota2, nota1
	
media = (nota1+nota2)/2.0

penalizacao = 0.0


while media < 6.0:
	print "Média: %.1f (cursando)" %media
	print "Penalização: %.1f" %penalizacao
	print
	nota = float(raw_input("Nota? "))
	if nota > nota1:
		nota1 = nota
	media = (nota1 + nota2) / 2
	penalizacao += 0.5
	if nota1 > nota2:
		nota1, nota2 = nota2, nota1

if media > 6:
	print "Média: %.1f (aprovado)" %media
	print "Penalização: %.1f" %penalizacao
	print
	
print "==="
print "Notas válidas: %.1f e %.1f" %(nota2,nota1)
print "Média parcial na unidade: %.1f" %(media)
print "Penalizações: %.1f" %penalizacao
print "Média final na unidade: %.1F" %(media-penalizacao)

