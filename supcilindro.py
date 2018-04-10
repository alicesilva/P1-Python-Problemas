# coding: utf-8
# Calculo da superfície do cilindro

import math
print "Cálculo da Superfície de um Cilindro\n---"

med_dia = float(raw_input("Medida do diâmetro? "))
med_alt = float(raw_input("Medida da altura? "))
raio = med_dia / 2.0
area_total = 2*(math.pi)*raio*(med_alt+raio)

print "---"
print "Área calculada: %.2f" %(area_total)
