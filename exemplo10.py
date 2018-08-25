#coding: utf-8
nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
nota4 = float(raw_input())
media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4  * 1) / 10
print "Media: %.1f" % (media)
if media >= 7.0:
	print "Aluno aprovado."
if media < 5.0:
	print "Aluno reprovado."
if media >= 5.0 and media <= 6.9:
	print "Aluno em exame."
	nota_exame = float(raw_input())
	print "Nota do exame: %.1f" %(nota_exame)
	nova_media = (nota_exame + media) / 2
	if nova_media >= 5.0:
		print "Aluno aprovado."
		print "Media final: %.1f" %(nova_media)
	elif nova_media <= 4.9:
		print "Aluno reprovado."
		print "Média final: %.1f" %(nova_media)
