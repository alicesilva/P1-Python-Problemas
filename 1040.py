#coding: utf-8
entrada = raw_input()
entrada1 = entrada.split()
nota1 = float(entrada1[0])
nota2 = float(entrada1[1])
nota3 = float(entrada1[2])
nota4 = float(entrada1[3])
media = (nota1*2 +nota2*3 + nota3*4 + nota4*1) / 10
if media >= 7.0:
	print "Media: %.1f" %(media)
	print "Aluno aprovado."
elif media < 5.0:
	print "Media: %.1f" %(media)
	print "Aluno reprovado."
else:
	print "Media: %.1f" %(media)
	print "Aluno em exame."
	nota = float(raw_input())
	print "Nota do exame: %.1f" %(nota)
	media1 = (nota + media) / 2
	if media1 >= 5.0:
		print "Aluno aprovado."
	else:
		print "Aluno reprovado."
	print "Media final: %.1f" %(media1)
