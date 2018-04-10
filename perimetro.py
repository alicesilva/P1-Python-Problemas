# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Perímetro de um triângulo
import math
x1 = int(raw_input())
y1 = int(raw_input())
x2 = int(raw_input())
y2 = int(raw_input())
x3 = int(raw_input())
y3 = int(raw_input())
d1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
d2 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
d3 = math.sqrt((x2-x3)**2 + (y2-y3)**2)
perimetro = d1 + d2 + d3
print "O perímetro é de %.2f" %(perimetro)
