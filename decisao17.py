#coding: utf-8
ano = int(raw_input())

if ano % 4.0 == 0:
	if ano % 100.0 == 0:
		if ano % 400.0 == 0:
			print "É bissexto"
		else:
			print "Não é bissexto"
	else:
		print "É bissexto"
else:
	print "Não é bissexto."
