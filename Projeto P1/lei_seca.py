#coding: utf-8
import pygame
from pygame.locals import *
from sys import exit
from random import randrange
 
#iniciando o jogo
pygame.init()

pygame.font.init()
font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)

#Detalhes da tela
largura = 600
altura = 570
 
tela = pygame.display.set_mode((largura, altura),0,32)
 
imagem_fundo = pygame.image.load('Editada3.png')

carro = {
	'superficie': pygame.image.load('carro2.png').convert_alpha(),
    'posicao': [randrange(200), randrange(500)],
    'speed': {
        'x': 0,
        'y': 0
    }
}
 
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
			
def get_rect(obj):
    return Rect(obj['posicao'][0],
                obj['posicao'][1],
                obj['superficie'].get_width(),
                obj['superficie'].get_height())


def carro_collided():
    carro_rect = get_rect(carro)
    for vinho in vinhos:
        if carro_rect.colliderect(get_rect(vinho)):
            return True
    return False			
			
			
collided = False			
			
			
 
velocidade = {
		'x': 0,
		'y': 0
		}
 
while True:
	carro['speed'] = {
        'x': 0,
        'y': 0
    }	
    
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
		carro['speed']['x'] = -20
	elif pressed_keys[K_RIGHT]:
		carro['speed']['x'] = 20
	else:
		carro['speed']['x'] = 0
 
	tela.blit(imagem_fundo, (0, 0))
	#posicao[0] += velocidade['x']
 
	#Para não deixar a barra desaparecer do plano:
	'''
	if posicao[0] > 459 :
		posicao[0] -= 20
	if posicao[0] < 2:
		posicao[0] += 20
	'''
 
	queda_cerveja()
	queda_vinho()
 
	for cerveja in cervejas:
		tela.blit(cerveja['superficie'], cerveja['posicao'])
	remover_cerveja()
 
	
	for vinho in vinhos:
		tela.blit(vinho['superficie'], vinho['posicao'])
	remover_vinho()
	
	if not collided:
		collided = carro_collided()
		carro['posicao'][0] += carro['speed']['x']
		carro['posicao'][1] += carro['speed']['y']

		tela.blit(carro['superficie'], carro['posicao'])
	else:
		text = game_font.render('GAME OVER', 1, (255, 0, 0))
		tela.blit(text, (400, 300))

 
	pygame.display.update()
	tempo = clock.tick(30)





# O jogo terá bebidas nn alcoolicas -> Contará como pnts!
# O jogo terá bebidas alcoolicas -> Acrescentar na barra de teor alcoolico!
# Pesquisar o teor alccolico das bebidas selecionadas
# Bebidas na = refrigerante, agua, suco, "chocolate", cafe
# Bebidas a = cerveja, vinho, uisque, caipirinha
# Pesquisar:
# Niveis de jogo, colisao, diminuir o numero de bebidas caindo






