#coding: utf-8
#Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
#Movimento uniformemente variado

posicao_inic = float(raw_input("Posição inicial? "))
veloc_inicial = float(raw_input("Velocidade inicial? "))
tempo = float(raw_input("Tempo? "))
aceler = float(raw_input("Aceleração? "))
veloc_final = veloc_inicial + aceler * tempo
veloc_media = veloc_inicial + (aceler * tempo) / 2.0
posicao_final = posicao_inic + veloc_inicial*tempo + (aceler*tempo ** 2)/2.0

print
print "Dados da questão\n================"
print "   Posição inicial: %.2f m" %(posicao_inic)
print "Velocidade inicial: %.2f m/s" %(veloc_inicial)
print "        Aceleração: %.2f m/s2" %(aceler)
print "             Tempo: %.2f s" %(tempo)
print "  Velocidade final: %.2f m/s" %(veloc_final)
print "  Velocidade média: %.2f m/s" %(veloc_media)
print "     Posição final: %.2f m" %(posicao_final)

