import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Variáveis de rotação
rtri = 0.0
rquad = 0.0

def init():
    """Configuração inicial do OpenGL com iluminação."""
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 640.0 / 480.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def load_texture():
    texture_surface = pygame.image.load('bricks2.jpg')
    texture_data = pygame.image.tostring(texture_surface, "RGB", True)
    width, height = texture_surface.get_rect().size

    glEnable(GL_TEXTURE_2D)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)


def draw_sphere():
    """Desenha uma esfera com textura."""
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(2.5, 0.0, -12.0)  # Posiciona a esfera no centro
    
    glBindTexture(GL_TEXTURE_2D, 1)  # Vincula a textura
    
    # Desenha a superfície da esfera com textura
    textured_sphere = gluNewQuadric()
    gluQuadricTexture(textured_sphere, GL_TRUE)  # Habilita textura na esfera
    gluSphere(textured_sphere, 2, 32, 32)  # Desenha a esfera com textura
    
    glPopMatrix()

def draw_cube():
    """Desenha o cubo com normais para iluminação."""
    global rquad
    
    glLoadIdentity()
    glTranslatef(-1.5, 0.0, -7.0)
    glRotatef(rquad, 1.0, 1.0, 1.0)

    glBindTexture(GL_TEXTURE_2D, 1)  # Vincula a textura
    glBegin(GL_QUADS)
    
    # Topo

    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)

    # Base
 
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Frente
  
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Traseira
  
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)

    # Esquerda
  
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # Direita
 
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    
    glEnd()


def main():
    global rtri, rquad
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()
    load_texture()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        draw_sphere()
        rtri += 0.2
        rquad -= 0.15
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
