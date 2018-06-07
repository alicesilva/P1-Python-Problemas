# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015.1
# Agenda telefônica

nomes = []
telefones = []

while True:
	operacao = raw_input()
	if operacao == "inserir":
		n = int(raw_input())
		for i in range(n):
			nome = raw_input()
			telefone = raw_input()
			nomes.append(nome)
			telefones.append(telefone)
	
		for i in range(len(nomes)):
			for j in range(len(nomes)-1):
				if nomes[j] > nomes[j+1]:
					nomes[j], nomes[j+1] = nomes[j+1], nomes[j]
					telefones[j], telefones[j+1] = telefones[j+1], telefones[j]
	elif operacao == "buscar":
		nome = raw_input()
		if nome in nomes:
			for i in range(len(nomes)):
				if nome == nomes[i]:
					print "Nome: %s" %nomes[i]
					print "Fone: %s" %telefones[i]
					print "----------"
		elif nomes not in nomes:
			print "Nome inexistente"
			print "----------"
	elif operacao == "imprimir":
		for i in range(len(nomes)):
			print "Nome: %s" %nomes[i]
			print "Fone: %s" %telefones[i]
			print "----------"
	
	if operacao == "finalizar":
		break
			
		
