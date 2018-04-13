# coding: utf-8
# Alice Fernandes Silva /UFCG, 2015.1, Programaçao 1
# Densidade

m1 = float(raw_input())
v1 = float(raw_input())
m2 = float(raw_input())
v2 = float(raw_input())
m3 = float(raw_input())
v3 = float(raw_input())

d1 = m1/v1
d2 = m2/v2
d3 = m3/v3

if d1 < d2 and d1 < d3:
	print "O líquido 1, com densidade %.2f, irá ocupar a parte de cima do recipiente." %d1
elif d2 < d3 and d2 < d1:
	print "O líquido 2, com densidade %.2f, irá ocupar a parte de cima do recipiente." %d2
else:
	print "O líquido 3, com densidade %.2f, irá ocupar a parte de cima do recipiente." %d3
