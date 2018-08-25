#coding: utf-8
area = float(raw_input())
if area <= 108:
	print "1 lata"
	print "R$ 80.00"
else:
	latas = area/108.0
	precos1 = latas * 80.00
	print "%.1f latas" %latas
	print "R$ %.2f" %precos1

if area <= 21.6:
	print "1 galão"
	print "R$ 25.00"
else:
	galoes = area/21.6
	precos2 = galoes * 25.00
	print "%.1f galões" %galoes
	print "R$ %.2f" %precos2



	
