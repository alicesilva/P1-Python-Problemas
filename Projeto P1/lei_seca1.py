# coding: utf-8
# Projeto P1/UFCG 2015.1/Alice Silva e Ivyna Alves
import pygame
from pygame.locals import *
from sys import exit
from random import randrange
 
#iniciando o jogo
pygame.init()
 
#Detalhes da tela
largura = 600
altura = 570
 
tela = pygame.display.set_mode((largura, altura),0,32)
# Mudar a imagem
imagem_fundo = pygame.image.load("Editada3.png")
# Mudar para um carro!
carro = pygame.image.load('carro2.png')
 
pygame.display.set_caption('Projeto P1')
 
posicao = [200,500]
 
clock = pygame.time.Clock()
# Criar funcoes para a criacao das imagens e sorteio
# Usar o módulo sprite para detectar colisões!
 
def cria_cerveja():
	return {
		'superficie' : pygame.image.load('beer2.png'),
		'posicao': [randrange(600), -64],
		'speed': randrange(1,11)
	}
def cria_vinho():
	return {
		'superficie': pygame.image.load('vinho2.png'),
		'posicao': [randrange(600), -64],
		'speed': randrange(1,11)
	}

 
# Fazer niveis alterando a velocidade e a imagem de fundo

 
velocidade_vinho = 120
velocidade_letra = 120
velocidade_leite = 120
 
cervejas = []
 
def queda_cerveja():
	for cerveja in cervejas:
		cerveja['posicao'][1] += cerveja['speed']
 
def remover_cerveja():
	for cerveja in cervejas:
		if cerveja['posicao'][1] > 540:
			cervejas.remove(cerveja)	
 
vinhos = []
 
def queda_vinho():
	for vinho in vinhos:
		vinho['posicao'][1] += vinho['speed']
 
def remover_vinho():
	for vinho in vinhos:
		if vinho['posicao'][1] > 540:
			vinhos.remove(vinho)
 

velocidade = {
		'x': 0,
		'y': 0
		}
 
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
 
	# Está com "tecla contínua de velocidade" = barra, ou seja,
	# so precisa pressionar as teclas de direcao um vez
	if not velocidade_letra:
		velocidade_letra = 90
		cervejas.append(cria_cerveja())
	else:
		velocidade_letra -= 1

	if not velocidade_vinho:
		velocidade_vinho = 90
		vinhos.append(cria_vinho())
	else:
		velocidade_vinho -= 1

 
	pressed_keys = pygame.key.get_pressed()
	# Só está movimentando na horizontal
	# Se quiser adicionar mais comandos para outras
	# teclas é só colocar elif ou adicionar if
 
	if pressed_keys[K_LEFT]:
		velocidade['x'] = -20
	elif pressed_keys[K_RIGHT]:
		velocidade['x'] = 20
	else:
		velocidade['x'] = 0
 
	tela.blit(imagem_fundo, (0, 0))
	posicao[0] += velocidade['x']
 
	#Para não deixar a barra desaparecer do plano:
 
	if posicao[0] > 459 :
		posicao[0] -= 20
	if posicao[0] < 2:
		posicao[0] += 20
 
	tela.blit(carro,(posicao))
 
	queda_cerveja()
	queda_vinho()
 
	for cerveja in cervejas:
		tela.blit(cerveja['superficie'], cerveja['posicao'])
	remover_cerveja()
 
	for coco in cocos:
		tela.blit(coco['superficie'], coco['posicao'])
	remover_coco()
 
	for vinho in vinhos:
		tela.blit(vinho['superficie'], vinho['posicao'])
	remover_vinho()
 
	for leite in leites:
		tela.blit(leite['superficie'], leite['posicao'])
	remover_leite()
 
	pygame.display.update()
	tempo = clock.tick(30)
 
# O jogo terá bebidas nn alcoolicas -> Contará como pnts!
# O jogo terá bebidas alcoolicas -> Acrescentar na barra de teor alcoolico!
# Pesquisar o teor alccolico das bebidas selecionadas
# Bebidas na = refrigerante, agua, suco, "chocolate", cafe
# Bebidas a = cerveja, vinho, uisque, caipirinha
# Pesquisar:
# Niveis de jogo, colisao, diminuir o numero de bebidas caindo
