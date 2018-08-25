#coding: utf-8
numero1 = float(raw_input())
numero2 = float(raw_input())
numero3 = float(raw_input())

primeiro = numero1
segundo = numero2
terceiro = numero3

if segundo > primeiro > terceiro:
	primeiro = numero2
	segundo = numero1
	terceiro = numero3
elif primeiro > terceiro > segundo:
	primeiro = numero1
	segundo = numero3
	terceiro = numero2
elif segundo > terceiro > primeiro:
	primeiro = numero3
	segundo = numero1
	terceiro = numero2

	
