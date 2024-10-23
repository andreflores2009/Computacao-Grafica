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

    # Ativando iluminação
    glEnable(GL_LIGHTING)    # Habilita o sistema de iluminação
    glEnable(GL_LIGHT0)      # Ativa a luz 0

    # Configura as propriedades da luz
    light_ambient = [0.2, 0.2, 0.2, 1.0]   # Luz ambiente (luz fraca que preenche todo o ambiente)
    light_diffuse = [0.8, 0.8, 0.8, 1.0]   # Luz difusa (luz principal que ilumina o objeto)
    light_position = [0, 2, 0, 0.0]  # Posição da luz

    # Aplicando as propriedades
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Configura os materiais do objeto para interagir com a luz
    material_specular = [1.0, 1.0, 1.0, 1.0]
    material_shininess = [50.0]
    
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

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
    glNormal3f(0.0, 1.0, 0.0)  # Normal apontando para cima
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)

    # Base
    glNormal3f(0.0, -1.0, 0.0)  # Normal apontando para baixo
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Frente
    glNormal3f(0.0, 0.0, 1.0)  # Normal apontando para frente
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Traseira
    glNormal3f(0.0, 0.0, -1.0)  # Normal apontando para trás
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)

    # Esquerda
    glNormal3f(-1.0, 0.0, 0.0)  # Normal apontando para a esquerda
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # Direita
    glNormal3f(1.0, 0.0, 0.0)  # Normal apontando para a direita
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
