#coding: utf-8
while True:
	nome = raw_input("Atleta: ")
	if nome == "":
		break
	print
	
	ordem = ["Primeiro Salto:","Segundo Salto:","Terceiro Salto:","Quarto Salto:","Quinto Salto:"]
	soma = 0
	saltos = []
	
	for i in range(len(ordem)):
		print ordem[i],
		salto = raw_input()
		codigo = salto.split()
		saltos.append(float(codigo[0]))

	
	print
	print "Resultado final:"
	print "Atleta: %s" %nome
	print "Saltos:",
	for i in range(len(saltos)):
		soma += saltos[i]
		print "%s -" %saltos[i],
		
	
	media = soma / 5
			
	print
	print "Média dos saltos: %.1f m" %media
	print

