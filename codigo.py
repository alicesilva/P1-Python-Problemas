# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Números oscilantes

codigo = raw_input()
for i in range(len(codigo)-1):
	if int(codigo[i]) % 2 == 0 and int(codigo[i+1]) % 2 != 0 or\
		int(codigo[i]) % 2 != 0 and int(codigo[i+1]) % 2 == 0:
			print "verdadeiro: %d algarismos." %len(codigo)
			break
	else:
		print "falso: %d algarismos." %len(codigo)
		break
			
	
