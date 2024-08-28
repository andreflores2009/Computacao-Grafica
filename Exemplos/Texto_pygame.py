import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Exemplo de Texto com Pygame")

# Defina as cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Configure a fonte
fonte = pygame.font.Font(None, 24)  # Nenhuma fonte específica e tamanho 74
texto = fonte.render('Olá, Pygame!', True, preto)  # Texto a ser exibido

# Defina a posição do texto
posicao_texto = (200, 250)  # (x, y)

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preencha o fundo com uma cor
    tela.fill(branco)

    # Desenhe o texto na tela na posição definida
    tela.blit(texto, posicao_texto)

    # Atualize a tela
    pygame.display.flip()
