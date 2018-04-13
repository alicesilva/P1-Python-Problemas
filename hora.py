#coding: utf-8
def conversao(hora):
	dados = hora.split(":")
	if 0 <= int(dados[0]) <= 11:
		dose = int(dados[0]) + 12
		
	if int(dados[0]) >= 12:
		mais_dose = int(dados[0]) + 12
		dose = mais_dose - 24
	if 0 < dose < 12:
		print "%d:%s" %(dose,dados[1])
		print "P"
	else:
		print "%d:%s" %(dose,dados[1])
		print "A"


while True:
	hora = raw_input()
	conversao(hora)
