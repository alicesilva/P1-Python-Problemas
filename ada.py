# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Avaliação de desempenho acadêmico
numero_semestre = int(raw_input())
ensino = int(raw_input())
producao_intelec = int(raw_input())
orientacao = int(raw_input())
adm = int(raw_input())
media = (ensino + producao_intelec + orientacao + adm) / 4.0
if numero_semestre >= 4:
	if ensino < 320 or producao_intelec < 100 or orientacao < 20: 
		print "Promoção indeferida. Pontuação mínima não alcançada."
	elif media < 140:
		print "Promoção indeferida. Média insuficiente."
	else:
		print "Promoção deferida. Parabéns!"
else:
	print "Promoção indeferida. Número de semestres insuficiente."


