#coding: utf-8
import math

a = float(raw_input())

if a != 0:
	b = float(raw_input())
	c = float(raw_input())
	delta = b ** 2 - 4 * a * c
	if delta < 0:
		print "A equação não possui raizes reais."
	elif delta == 0:
		raiz = - b / (2 * a)
		print raiz
	else:
		raiz1 = (- b + math.sqrt(delta)) / 2 * a
		raiz2 = (- b - math.sqrt(delta)) / 2 * a
		print raiz
		print raiz2
