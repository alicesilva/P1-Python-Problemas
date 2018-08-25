#coding: utf-8
data = raw_input("Data de Nascimento: ")

elementos = data.split("/")

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

print "Você nasceu em  %s de %s de %s." %(elementos[0],meses[int(elementos[1])-1],elementos[2])
