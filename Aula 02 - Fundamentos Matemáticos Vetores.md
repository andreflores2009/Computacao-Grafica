# Aula Prática: Fundamentos de Vetores com Python e OpenGL

## Objetivo da Aula

Nesta aula prática, vamos explorar os conceitos fundamentais de vetores utilizando Python e a biblioteca PyOpenGL. Vamos abordar a representação de pontos, vetores, operações com vetores como soma, multiplicação por escalar, magnitude e vetores unitários. Também implementaremos o produto escalar (Dot Product) e o produto vetorial (Cross Product).

## Pré-requisitos

- Conhecimentos básicos de Python.
- Instalação das bibliotecas `PyOpenGL` e `pygame` para renderização gráfica.

### Instalação das Bibliotecas

```bash
pip install PyOpenGL  pygame
```

## Vetores 2D utilizando Python, Pygame e OpenGL

### 1. **Importando as Bibliotecas Necessárias**

```python
import pygame
import sys
```

Neste trecho, estamos importando as bibliotecas `pygame` e `sys`. A biblioteca `pygame` é usada para criar jogos e outras aplicações multimídia, enquanto `sys` fornece acesso a funções e variáveis específicas do sistema, como sair do programa.

### 2. **Inicializando o Pygame**

```python
# Inicializa o Pygame
pygame.init()
```

Aqui, a função `pygame.init()` inicializa todos os módulos do Pygame que você está utilizando. Isso é necessário para configurar o ambiente antes de usá-lo para desenhar na tela ou capturar eventos.

### 3. **Configurações da Tela**

```python
# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Desenho de Vetores 2D com Pygame")
```

- `width` e `height` definem as dimensões da janela do jogo, 800x600 pixels.
- `pygame.display.set_mode()` cria a janela de exibição onde todo o conteúdo será desenhado.
- `pygame.display.set_caption()` define o título da janela.

### 4. **Definindo Cores**

```python
# Cores
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
```

As cores são definidas usando tuplas RGB, onde cada valor representa a intensidade de vermelho, verde e azul (de 0 a 255). Aqui, temos as seguintes cores:
- `white` (branco)
- `red` (vermelho)
- `black` (preto)

### 5. **Função para Desenhar um Vetor**

```python
# Função para desenhar um vetor
def draw_vector(start_pos, end_pos, color=red, width=2):
    pygame.draw.line(screen, color, start_pos, end_pos, width)
```

Esta função `draw_vector` é usada para desenhar um vetor na tela. Ela usa a função `pygame.draw.line()` para desenhar uma linha:
- `start_pos`: ponto inicial do vetor (x, y).
- `end_pos`: ponto final do vetor (x, y).
- `color`: cor da linha, com o valor padrão `red`.
- `width`: espessura da linha, com o valor padrão 2 pixels.

### 6. **Função Principal**

```python
def main():
    running = True
    while running:
        # Processa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Limpa a tela
        screen.fill(white)

        # Exemplo de vetores
        draw_vector((100, 100), (400, 300))  # Vetor de (100, 100) até (400, 300)
        draw_vector((400, 300), (600, 100))  # Vetor de (400, 300) até (600, 100)

        # Atualiza a tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()
```

- **Loop Principal:** A função `main()` contém um loop que continua executando enquanto `running` for `True`. Isso mantém o programa rodando até que o usuário decida fechá-lo.
- **Processamento de Eventos:** O loop `for event in pygame.event.get()` verifica todos os eventos que ocorrem na janela (como cliques de mouse ou pressionamentos de teclas). Se o evento for `pygame.QUIT` (quando o usuário clica no botão de fechar a janela), o programa define `running` como `False` e o loop é encerrado.
- **Limpeza da Tela:** `screen.fill(white)` preenche a tela com a cor branca, limpando o conteúdo anterior.
- **Desenho dos Vetores:** `draw_vector()` é chamado para desenhar dois vetores na tela.
- **Atualização da Tela:** `pygame.display.flip()` atualiza a tela com o novo conteúdo desenhado.
- **Finalização:** Quando o loop é encerrado, `pygame.quit()` finaliza o Pygame, e `sys.exit()` fecha o programa.

### 7. **Executando o Programa**

```python
if __name__ == "__main__":
    main()
```

Este trecho verifica se o script está sendo executado diretamente (não importado como um módulo) e chama a função `main()` para iniciar o programa.

### Resultado 

<p align="center">
    <img src="https://github.com/user-attachments/assets/9ea8e18c-4e8e-41c0-87fd-dd07fd2537a8" alt="Resultado">
</p>p>

### Conclusão

Esse código é uma introdução simples ao uso de Pygame para desenhar vetores 2D. Ele configura uma janela gráfica, permite que você desenhe 
linhas que representam vetores e processa eventos para manter o programa rodando até que o usuário decida fechá-lo. Este é um ótimo ponto de
partida para quem deseja aprender sobre a manipulação de gráficos 2D com Python e Pygame.

## Vetores 3D utilizando Python, Pygame e OpenGL

Este código é um exemplo de como criar uma visualização 3D interativa usando `Pygame` para a janela e eventos de entrada, juntamente com `PyOpenGL` para renderização 3D. Vou explicar o código em detalhes, dividindo-o em partes-chave:

### Importações
```python
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
```
Essas importações incluem:
- `pygame`: Uma biblioteca para criar jogos e gráficos, usada aqui para criar a janela e gerenciar eventos.
- `OpenGL.GL` e `OpenGL.GLU`: Módulos do PyOpenGL que fornecem funções para desenhar formas e manipular a câmera em um espaço 3D.

### Variáveis de controle de rotação
```python
rotation_x = 0
rotation_y = 0
mouse_down = False
last_pos = (0, 0)
```
Essas variáveis são usadas para:
- `rotation_x` e `rotation_y`: Controlar a rotação do objeto em torno dos eixos X e Y, respectivamente.
- `mouse_down`: Verificar se o botão esquerdo do mouse está sendo pressionado.
- `last_pos`: Armazena a posição do mouse na última vez que foi movido.

### Função `draw_vector`
```python
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
```
Esta função desenha três eixos (X, Y, Z) e um vetor customizado no espaço 3D:
- `glBegin(GL_LINES)` e `glEnd()` definem o início e o fim do desenho de linhas.
- `glColor3f` define a cor do vetor atual.
- `glVertex3f` define os pontos de início e fim de cada vetor.

### Função principal `main`
```python
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
```
Esta é a função principal do programa:
- **Inicialização e Configuração**:
  - `pygame.init()` inicializa todas as funcionalidades do Pygame.
  - `display = (800, 600)` define o tamanho da janela.
  - `pygame.display.set_mode` cria a janela com buffer duplo (`DOUBLEBUF`) e contexto OpenGL (`OPENGL`).
  - `gluPerspective` define a perspectiva da câmera.
  - `glTranslatef(0.0, 0.0, -5)` posiciona a câmera a 5 unidades "atrás" do centro da cena.

- **Loop Principal**:
  - O loop principal (`while True`) lida com eventos como fechar a janela (`pygame.QUIT`), pressionar ou soltar o botão do mouse, e mover o mouse. Dependendo dos movimentos do mouse, as variáveis `rotation_x` e `rotation_y` são ajustadas, permitindo a rotação do vetor e dos eixos desenhados.
  - `glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)` limpa a tela para a próxima renderização.
  - `glLoadIdentity()` reseta a matriz de transformações, essencial para evitar acúmulos de transformações em cada quadro.
  - `glRotatef` aplica as rotações baseadas na interação do mouse.
  - `draw_vector()` desenha os vetores e eixos.
  - `pygame.display.flip()` atualiza a janela com o que foi desenhado.
  - `pygame.time.wait(10)` adiciona um pequeno delay para que o programa não consuma todos os recursos do CPU.

### Resultado 
<p align="center">
     <img src="https://github.com/user-attachments/assets/be7bd64e-9498-4ade-ab42-47ce1a9985c9" alt="Resultado 3D">
</p>


### Resumo
Este código cria uma janela onde vetores e eixos 3D são desenhados e podem ser rotacionados usando o mouse. É um exemplo básico, mas poderoso, de como criar gráficos 3D interativos usando Pygame e OpenGL.


