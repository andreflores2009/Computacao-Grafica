import pygame
import sys

# Inicializando o pygame
pygame.init()

# Configurando a tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Vetores em 2D")

# Definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Função para desenhar um vetor
def draw_vector(screen, origin, vector, color=RED):
    pygame.draw.line(screen, color, origin, (origin[0] + vector[0], origin[1] - vector[1]), 3)
    pygame.draw.circle(screen, color, (origin[0] + vector[0], origin[1] - vector[1]), 5)

# Vetor exemplo
vector = (200, 150)
origin = (400, 300)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenchendo a tela
    screen.fill(WHITE)

    # Desenhando o vetor
    draw_vector(screen, origin, vector)

    # Atualizando a tela
    pygame.display.flip()

# Encerrando o pygame
pygame.quit()
sys.exit()
