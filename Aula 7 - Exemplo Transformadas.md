
### 1. **Imports**

```python
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
```

- `pygame`: Usado para criar a janela de exibição e gerenciar eventos (como pressionamento de teclas).
- `OpenGL.GL`: Importa funções da biblioteca OpenGL para desenhar formas e aplicar transformações.
- `OpenGL.GLUT`: (não usado diretamente neste código) pode ser útil para eventos e animações no OpenGL.
- `OpenGL.GLU`: Usado para funções de utilidade, como `gluPerspective` para configurar a visão 3D.

### 2. **Variáveis Globais**

```python
rtri = 0.0
rquad = 0.0
fullscreen = False
```

- `rtri`: Armazena o ângulo de rotação do triângulo.
- `rquad`: Armazena o ângulo de rotação do quadrado.
- `fullscreen`: Controla se a aplicação está em modo tela cheia ou janela.

### 3. **Função `init()`**

```python
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
```

Essa função configura o ambiente OpenGL:

- `glClearColor`: Define a cor de fundo (preto neste caso).
- `glClearDepth`: Define a profundidade máxima (1.0 = plano mais distante).
- `glEnable(GL_DEPTH_TEST)`: Habilita o teste de profundidade para garantir que o OpenGL desenhe objetos em ordem correta de proximidade.
- `glDepthFunc(GL_LEQUAL)`: Define como o OpenGL decide se um pixel deve ser desenhado com base na profundidade.
- `glShadeModel(GL_SMOOTH)`: Ativa o sombreamento suave (interpolação de cores).
- `gluPerspective`: Configura a projeção perspectiva (campo de visão de 45 graus, proporção de 640x480, profundidade de visualização entre 0.1 e 100.0).
- `glMatrixMode`: Configura a matriz de projeção e visualização para configurar a câmera 3D.

### 4. **Função `draw()`**

```python
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
```

- `glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)`: Limpa a tela e o buffer de profundidade antes de desenhar.
- **Triângulo**:
  - `glTranslatef(-1.5, 0.0, -6.0)`: Move o triângulo para a esquerda e para trás, posicionando-o corretamente.
  - `glRotatef(rtri, 0.0, 1.0, 0.0)`: Rotaciona o triângulo ao longo do eixo Y.
  - `glBegin(GL_TRIANGLES)`: Começa a desenhar o triângulo, definindo suas três vértices com cores diferentes.
- **Quadrado**:
  - `glLoadIdentity`: Reseta a matriz antes de desenhar o quadrado.
  - `glTranslatef(1.5, 0.0, -6.0)`: Move o quadrado para a direita e para trás.
  - `glRotatef(rquad, 1.0, 0.0, 0.0)`: Rotaciona o quadrado ao longo do eixo X.
  - `glBegin(GL_QUADS)`: Desenha o quadrado com suas quatro vértices.
- **Rotação**:
  - A cada chamada, `rtri` e `rquad` são atualizados, fazendo o triângulo e o quadrado rotacionarem continuamente.

### 5. **Função `main()`**

```python
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
```

- `pygame.init()`: Inicializa o Pygame.
- `pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)`: Cria uma janela de 640x480 em modo de buffer duplo com suporte a OpenGL.
- `init()`: Chama a função de inicialização do OpenGL.
- **Loop principal**:
  - Verifica os eventos do Pygame:
    - Se o botão de fechar (`QUIT`) for clicado ou a tecla `ESC` for pressionada, o loop para e o programa termina.
    - Se a tecla `F1` for pressionada, alterna entre o modo janela e o modo tela cheia.
  - Chama a função `draw()` para desenhar o triângulo e o quadrado.
  - `pygame.display.flip()`: Atualiza a tela para mostrar o novo frame.
  - `pygame.time.wait(10)`: Espera 10 milissegundos entre os frames, controlando a taxa de atualização.
