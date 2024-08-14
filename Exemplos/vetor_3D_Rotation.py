import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Variáveis de controle de rotação
rotation_x = 0
rotation_y = 0
mouse_down = False
last_pos = (0, 0)

def draw_vector():
    glBegin(GL_LINES)
    
    # Desenhando o eixo X (vermelho)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    
    # Desenhando o eixo Y (verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    
    # Desenhando o eixo Z (azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)
    
    # Desenhando um vetor customizado (laranja)
    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.5, 0.5, 0.5)
    
    glEnd()

def main():
    global rotation_x, rotation_y, mouse_down, last_pos
    
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    
    # Posicionando a câmera
    glTranslatef(0.0, 0.0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_down = True
                    last_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
            elif event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    x, y = event.rel
                    rotation_x += y
                    rotation_y += x

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Aplicando as rotações baseadas no movimento do mouse
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)

        draw_vector()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
