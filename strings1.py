#coding: utf-8
string1 = raw_input()
string2 = raw_input()

print "Compara duas strings"
print "String 1: %s" %string1
print "String 2: %s" %string2
print 'Tamanho de "%s": %d caracteres' %(string1,len(string1))
print 'Tamanho de "%s": %d caracteres' %(string2,len(string2))


if len(string1) == len(string2):
	print "As duas strings são de tamanhos iguais."
else:
	print "As duas strings são de tamanhos diferentes."

if string1 == string2:
	print "As duas strings possuem conteúdo igual."
else:
	print "As duas strings possuem conteúdo diferente."
