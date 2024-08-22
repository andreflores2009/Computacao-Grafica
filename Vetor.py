import pygame
import sys

# Inicializando o pygame
pygame.init()

#Tamanho da tela
screen_h = 400
screen_w = 600

# Configurando a tela
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Vetores em 2D")

# Definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)
GRAY = (200,200,200)

# Função para desenhar um vetor
def draw_vector(screen, origin, vector, color):
    pygame.draw.line(screen, color, origin, (origin[0] + vector[0], origin[1] - vector[1]), 3)
    pygame.draw.circle(screen, color, (origin[0] + vector[0], origin[1] - vector[1]), 5)

# Desenha um grid
def draw_grid(screen, color):
    for x in range (0, screen_w, 10):
        pygame.draw.line(screen, color,(x,0),(x,screen_h))
    for y in range (0, screen_h, 10):
        pygame.draw.line(screen, color,(0,y),(screen_w,y))

#Desenha coordenadas
def draw_axis(sreen, colorX, colorY):
    pygame.draw.line(screen, colorX,(0,screen_h/2),(screen_w,screen_h/2),3)
    pygame.draw.line(screen, colorY,(screen_w/2,0),(screen_w/2,screen_h),3)

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
    
    #Desenhando Grid
    draw_grid(screen, GRAY)

    draw_axis(screen,RED, BLUE)

    # Desenhando o vetor
    draw_vector(screen, origin, vector,BLACK)

    


    # Atualizando a tela
    pygame.display.flip()

# Encerrando o pygame
pygame.quit()
sys.exit()