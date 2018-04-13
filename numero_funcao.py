#coding: utf-8

def numero(n):
	if n > 00:
		return "P"
	else:
		return "N"


assert numero(8) == "P"
assert numero(0) == "N"
assert numero(-8) == "N"
