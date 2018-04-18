# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Adivinhe o número

n = int(raw_input())

cont = 0

while True:
	palpite = int(raw_input("palpite? "))
	cont += 1
	if palpite == n:
		break
	if palpite > n:
		print "alto"
	else:
		print "baixo"

print "Você acertou em %d tentativas." %cont
