import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variáveis globais para armazenar os ângulos de rotação
rtri = 0.0
rquad = 0.0
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
    """Função que desenha o triângulo e o quadrado com rotação."""
    global rtri, rquad

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpar tela e buffer de profundidade
    glLoadIdentity()  # Resetar a matriz de visualização
    
    # Rotação e desenho do triângulo
    glTranslatef(-1.5, 0.0, -6.0)
    glRotatef(rtri, 0.0, 1.0, 0.0)  # Rotaciona no eixo Y
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Vermelho
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()

    # Rotação e desenho do quadrado
    glLoadIdentity()
    glTranslatef(1.5, 0.0, -6.0)
    glRotatef(rquad, 1.0, 0.0, 0.0)  # Rotaciona no eixo X
    glColor3f(0.5, 0.5, 1.0)  # Azul claro
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

    # Atualizar os ângulos de rotação
    rtri += 0.2  # Rotação do triângulo
    rquad -= 0.15  # Rotação do quadrado

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
