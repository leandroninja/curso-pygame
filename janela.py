import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

pygame.mixer_music.set_volume(5)
musica_de_fundo = pygame.mixer.music.load('Invincible.mp3') 
pygame.mixer_music.play(-1)

barulho_colisao = pygame.mixer.Sound('coin.wav')
barulho_colisao.set_volume(1)

largura = 640
altura = 480
# varialvel x,y controla movimento do retangulo
x = int(largura/2)
y = int(altura/2)

x_azul = randint(40,600)
y_azul = randint(50,430)

pontos = 0
fonte = pygame.font.SysFont('arial',40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('janela do jogo')
relogio = pygame.time.Clock()


while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.QUIT()
           exit()
        
        '''

        if event.type == KEYDOWN:
            if event.key == K_LEFT: 
                x = x - 20  
            if event.key == K_RIGHT:
                x = x + 20
            if event.key == K_UP:
                y = y - 20 
            if event.key == K_DOWN:
                y = y + 20'''
            

    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20  
    if pygame.key.get_pressed()[K_UP]:
        y = y - 20 
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 20   
        
           

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) 
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50)) 
    

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()
        
    tela.blit(texto_formatado, (450,40))    

    


   # pygame.draw.circle(tela,(0,0,255), (300,260), 40)   
   # pygame.draw.line(tela, (255,255,0),(390,0), (390,600), 5)   
    pygame.display.update()       
    