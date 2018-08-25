#coding: utf-8
numero1 = float(raw_input())
numero2 = float(raw_input())
numero3 = float(raw_input())

maior = numero1

if maior < numero2 and numero2 > numero3:
	maior = numero2
elif maior < numero3 and numero3 > numero2:
	maior = numero3
else:
	maior = numero1

print maior

menor = numero1

if menor > numero2 and numero2 < numero3:
	menor = numero2
elif menor > numero3 and numero3 < numero2:
	menor = numero3
else:
	menor = numero1

print menor
