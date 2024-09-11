import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

fullscreen = False

def init():
    """Inicializa as configurações OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Cor de fundo preta
    glClearDepth(1.0)                  # Definir profundidade de fundo
    glEnable(GL_DEPTH_TEST)            # Habilitar teste de profundidade
    glDepthFunc(GL_LEQUAL)             # Tipo de teste de profundidade
    glShadeModel(GL_SMOOTH)            # Habilitar sombreamento suave
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 640.0 / 480.0, 0.1, 100.0)  # Projeção perspectiva
    glMatrixMode(GL_MODELVIEW)

def draw():
    """Função que desenha o triângulo e o quadrado."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpar tela e buffer de profundidade
    glLoadIdentity()  # Resetar a matriz de visualização
    
    # Desenhar o triângulo
    glTranslatef(-1.5, 0.0, -6.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 1.0, 0.0)  # Vértice superior
    glVertex3f(-1.0, -1.0, 0.0)  # Vértice inferior esquerdo
    glVertex3f(1.0, -1.0, 0.0)  # Vértice inferior direito
    glEnd()
    
    # Desenhar o quadrado
    glTranslatef(3.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 1.0, 0.0)  # Topo esquerdo
    glVertex3f(1.0, 1.0, 0.0)  # Topo direito
    glVertex3f(1.0, -1.0, 0.0)  # Base direita
    glVertex3f(-1.0, -1.0, 0.0)  # Base esquerda
    glEnd()

def main():
    global fullscreen
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
                if event.key == K_F1:
                    fullscreen = not fullscreen
                    pygame.display.quit()
                    pygame.display.init()
                    if fullscreen:
                        pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL | FULLSCREEN)
                    else:
                        pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
                    init()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
