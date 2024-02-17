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
x_cobra = int(largura/2)
y_cobra= int(altura/2)

x_maca = randint(40,600)
y_maca = randint(50,430)

pontos = 0
fonte = pygame.font.SysFont('arial',40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('janela do jogo')
relogio = pygame.time.Clock()
lista_cobra = []
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY = [0] = x
        #XeY = [1] = y
        
       
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))


while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
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
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x_cobra = x_cobra + 20  
    if pygame.key.get_pressed()[K_UP]:
        y_cobra = y_cobra - 20 
    if pygame.key.get_pressed()[K_DOWN]:
        y_cobra = y_cobra + 20   
        
           

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20)) 
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20)) 
    

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()
        
    tela.blit(texto_formatado, (450,40))    
    
    
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    
    aumenta_cobra(lista_cobra)

    


   # pygame.draw.circle(tela,(0,0,255), (300,260), 40)   
   # pygame.draw.line(tela, (255,255,0),(390,0), (390,600), 5)   
    pygame.display.update()       
    