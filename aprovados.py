# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Percentual de alunos aprovados

contador = 0.0
n = int(raw_input())

for i in range(n):
	media = raw_input()
	
	if media != "F":
		
		if float(media) >= 5.0:
			contador += 1
	else:
		pass

percentual = (contador / n) * 100

print "%.0f%% (%d/%d) de aprovados" %(percentual,contador,n)
