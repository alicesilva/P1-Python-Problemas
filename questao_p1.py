# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Questões para P1

total = 0
print "Relatório de novas questões:"
print

while True:
	colaborador = raw_input()
	if colaborador == "**":
		break
	soma = 0
	while True:
		questoes = raw_input()
		if questoes == "*":
			total += soma
			break
		soma += int(questoes)
	print "%s: %d" %(colaborador,soma)

print "---"
print "Total de novas questões: %d" %total
