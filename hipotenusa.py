# Calculo da hipotenusa de um triângulo retângulo
import math
catetoa = float(raw_input("Medida do Cateto 1? "))
catetob = float(raw_input("Medida do Cateto 2? "))
hipotenusa = math.sqrt(catetoa ** 2 + catetob ** 2)
print "Medida da Hipotenusa: %.2f" % (hipotenusa)
