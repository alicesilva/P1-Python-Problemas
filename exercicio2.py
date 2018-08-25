#coding: utf-8
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
if numero1 <= numero2 and numero1 <= numero3 and numero2 < numero3:
	print numero1
	print numero2
	print numero3
elif numero1<numero2 and numero2<numero3 and numero3<numero2:
	print numero1
	print numero3
	print numero2
elif numero1 > numero2 and numero2 < numero3 and numero1 < numero3:
	print numero2
	print numero1 
	print numero3
elif numero1 > numero2 and numero2<numero3 and numero3<numero1:
	print numero2
	print numero3
	print numero1
elif numero3<numero1 and numero3<numero2 and numero1<numero2:
	print numero3
	print numero1
	print numero2
else:
	print numero3
	print numero2
	print numero1
print
print numero1
print numero2
print numero3
