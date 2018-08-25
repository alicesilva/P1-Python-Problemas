#coding: utf-8
cont =  0
cont_inter = 0
cont_gremio = 0
cont_empates = 0
while True:
	entrada = raw_input()
	dados = entrada.split()
	inter = int(dados[0])
	gremio = int(dados[1])
	print "Novo grenal (1-sim 2-nao)"
	resposta = int(raw_input())
	cont += 1
	if inter > gremio:
		cont_inter += 1
	if gremio > inter:
		cont_gremio += 1
	if inter == gremio:
		cont_empates += 1
	if resposta == 2:
		break

print "%d grenais" %cont
print "Inter:%d" %cont_inter
print "Gremio:%d" %cont_gremio
print "Empates:%d" %cont_empates

if cont_inter > cont_gremio:
	print "Inter venceu mais"
elif cont_inter < cont_gremio:
	print "Gremio venceu mais"
elif cont_empates != 0:
	print "Nao houve vencedor"
