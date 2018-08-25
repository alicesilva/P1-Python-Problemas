#coding: utf-8
numero = raw_input()

if len(numero) == 3:
	if int(numero[0]) > 1:
		print "%s centenas," %numero[0],
	else:
		print "%s centena," %numero[0],
	if int(numero[1]) > 1:
		print "%s dezenas e" %numero[1],
	else:
		print "%s dezena e" %numero[1],
	if int(numero[2]) > 1:
		print "%s unidades" %numero[2],
	else:
		print "%s unidade" %numero[2],
		
elif len(numero) == 2:
	if int(numero[0]) > 1:
		print "%s dezenas e" %numero[0],
	else:
		print "%s dezena e" %numero[0],
	if int(numero[1]) > 1:
		print "%s unidades" %numero[1],
	else:
		print "%s unidade" %numero[1],
	
else:
	if int(numero) > 1:
		print "%s unidades" %numero
	else:
		print "%s unidade" %numero
	
