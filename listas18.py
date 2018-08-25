#coding: utf-8
votos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print "Enquete: Quem foi o melhor jogador?"
print

while True:
	voto = int(raw_input("Número do jogador (0=fim): "))
	if voto < 0 or voto > 23:
		print "Informe um valor entre 1 e 23 ou 0 para sair!"
	if voto == 0:
		break
	if 1 <= voto <= 23:
		votos[voto-1] = votos[voto-1] + 1

cont = 0
for i in range(len(votos)):
	if votos[i] != 0:
		cont += votos[i]
print
print "Resultado da votação:"
print
print "Foram computados %d votos." %cont
print
print "Jogador Votos           %"


maior = votos[0]	
for i in range(len(votos)):
	if votos[i] != 0:
		print "%d %15.0d %15.1f%%" %(i+1,votos[i],(float(votos[i])/cont) * 100)
	if votos[i] > maior:
		maior = votos[i]
		jogador = i + 1

print "O melhor jogador foi o número %d, com %d votos, correspondendo a %.1f%% do total de votos." %(jogador,maior,(float(maior)/cont) * 100)
