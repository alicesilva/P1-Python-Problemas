#coding: utf-8
def formato(data):
	dados = data.split("/")
	mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
	if int(dados[0]) > 31 or 1 <= int(dados[1]) >= 12:
		print "NULL"
	else:
		print "%s de %s de %s." %(dados[0], mes[int(dados[1])-1], dados[2])
		

data = raw_input()
formato(data)
