# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Unidades e medidas

medida_metros = int(raw_input())
medida_centimetro = medida_metros * 100
medida_jarda = medida_centimetro / 91.44
medida_polegadas = medida_jarda * 36
medida_pes = medida_jarda * 3
print "Jardas: %.3f yd" %(medida_jarda)
print "Pés: %.3f ft" %(medida_pes)
print "Polegadas: %.3f in" %(medida_polegadas)
