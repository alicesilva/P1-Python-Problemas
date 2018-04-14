# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Ataque mais positivo de um campeonato

n = int(raw_input())

soma = 0.0
maior = 0
lista_time = []
lista_gols = []

for i in range(n):
	time = raw_input()
	gols = int(raw_input())
	soma += gols
	lista_gols.append(gols)
	lista_time.append(time)
	
media = soma / n

for i in range(len(lista_gols)):
	if maior < lista_gols[i]:
		maior = lista_gols[i]
		
print "Time(s) com melhor ataque (%d gol(s)):" %maior

for i in range(len(lista_time)):
	if maior != 0:
		if maior == lista_gols[i]:
			time = lista_time[i]
			print "%s" %time

print
print "Média de gols marcados: %.1f" %media

