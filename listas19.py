#coding: utf-8
votos = [0,0,0,0,0,0]
opcoes = ["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]

while True:
	voto = int(raw_input())
	if voto == 0:
		break
	if 1 <= voto <= 6:
		votos[voto-1] = votos[voto-1] + 1

soma = 0
maior = votos[0]
posicao = 0

for i in range(len(votos)):
	soma += votos[i]
	if votos[i] > maior:
		maior = votos[i]
		posicao = i
	

print "Sistema Operacional     Votos   %"
print "-------------------     -----   ---"
print "Windows Server           %d      %.0f%%" %(votos[0],(float(votos[0])/soma)*100)
print "Unix                     %d      %.0f%%" %(votos[1],(float(votos[1])/soma)*100)
print "Linux                    %d      %.0f%%" %(votos[2],(float(votos[2])/soma)*100)
print "Netware                  %d      %.0f%%" %(votos[3],(float(votos[3])/soma)*100)
print "Mac OS                   %d      %.0f%%" %(votos[4],(float(votos[4])/soma)*100)
print "Outro                    %d      %.0f%%" %(votos[5],(float(votos[5])/soma)*100)

print "-------------------     -----"
print "Total %20.0d" %soma
print
print "O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.0f%% dos votos." %(opcoes[posicao],maior,(float(maior)/soma * 100))
