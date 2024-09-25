# Tutorial de Formas 3D: Pirâmide e Cubo

## Introdução
Neste tutorial, expandiremos os conceitos anteriores ao transformar o triângulo e o quadrado em objetos verdadeiramente 3D: uma pirâmide e um cubo. Adicionaremos lados e coloriremos as faces individualmente para criar uma pirâmide suavemente colorida e um cubo com cores distintas em cada face.

### 1. Desenhando a Pirâmide
Vamos começar pela pirâmide, que será desenhada com faces triangulares. Cada face da pirâmide compartilha o ponto superior e as cores das faces serão suavemente mescladas.

A pirâmide será desenhada ao redor de um eixo central para garantir que a rotação ocorra de forma correta. O topo da pirâmide será localizado no ponto (0, 1, 0), enquanto a base da pirâmide estará centrada ao redor de (0, -1, 0). Assim, o objeto será balanceado ao redor de seu eixo Y.

#### 1.1. Frente da Pirâmide
Desenhamos a face frontal da pirâmide usando três vértices: o topo (vermelho), o ponto esquerdo inferior (verde) e o ponto direito inferior (azul).

```python
glColor3f(1.0, 0.0, 0.0)   # Vermelho (topo)
glVertex3f(0.0, 1.0, 0.0)   # Vértice superior
glColor3f(0.0, 1.0, 0.0)   # Verde (esquerda)
glVertex3f(-1.0, -1.0, 1.0) # Vértice inferior esquerdo
glColor3f(0.0, 0.0, 1.0)   # Azul (direita)
glVertex3f(1.0, -1.0, 1.0)  # Vértice inferior direito
```

#### 1.2. Outros Lados da Pirâmide
Cada face subsequente compartilha o ponto do topo e alterna as cores dos pontos inferiores para criar uma mistura suave entre os lados da pirâmide. A rotação acontece com a função `glRotatef`.

Aqui está uma explicação detalhada da função `draw_pyramid()`:

```python
def draw_pyramid():
    """Desenha a pirâmide."""
    global rtri
    glLoadIdentity()
    glTranslatef(-1.5, 0.0, -6.0)
    glRotatef(rtri, 0.0, 1.0, 0.0)
    
    glBegin(GL_TRIANGLES)
    
    # Frente
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Direita
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Traseira
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    # Esquerda
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    
    glEnd()
```

#### `global rtri`
Define que a variável `rtri` (responsável pela rotação da pirâmide) será usada e atualizada dentro da função.

#### `glLoadIdentity()`
Reseta a matriz de transformação, garantindo que todas as operações futuras sejam aplicadas a uma nova base de coordenadas.

#### `glTranslatef(-1.5, 0.0, -6.0)`
Move a pirâmide para a esquerda e um pouco para trás, posicionando-a corretamente na cena 3D.

#### `glRotatef(rtri, 0.0, 1.0, 0.0)`
Aplica uma rotação à pirâmide no eixo Y. O valor de `rtri` determina o ângulo de rotação.

#### `glBegin(GL_TRIANGLES)`
Inicia a definição dos vértices que formam as faces da pirâmide. Cada face será um triângulo.

#### Desenhando as Faces
As quatro faces da pirâmide são desenhadas uma por uma:
- **Face frontal**: Define três vértices, começando com o ponto superior e dois pontos na base. As cores aplicadas são vermelho no topo, verde à esquerda e azul à direita.
- **Face direita**: Define o ponto superior (vermelho) e alterna as cores nos vértices inferiores para manter a suavidade das cores.
- **Face traseira e esquerda**: Seguem o mesmo padrão, alternando as cores entre verde e azul nos vértices inferiores.

#### `glEnd()`
Finaliza o desenho da pirâmide, aplicando todas as operações de desenho.

---

### 2. Desenhando o Cubo
O cubo será composto por seis faces quadradas, cada uma com uma cor diferente para fácil visualização. Cada face é desenhada com quatro vértices dispostos em ordem anti-horária.

#### 2.1. Topo do Cubo
O topo do cubo será desenhado um pouco acima do centro, usando as coordenadas Y positivas. Cada vértice será especificado para formar a face superior.

```python
glColor3f(0.0, 1.0, 0.0)  # Verde
glVertex3f(1.0, 1.0, -1.0)  # Canto superior direito
glVertex3f(-1.0, 1.0, -1.0) # Canto superior esquerdo
glVertex3f(-1.0, 1.0, 1.0)  # Canto inferior esquerdo
glVertex3f(1.0, 1.0, 1.0)   # Canto inferior direito
```

#### 2.2. Outras Faces do Cubo
Cada face do cubo é desenhada de forma semelhante à face superior, com a rotação aplicada a partir do centro para dar o efeito de rotação tridimensional.

---

### 3. Movimentação e Rotação
Tanto a pirâmide quanto o cubo são rotacionados continuamente ao longo de seus eixos X, Y e Z. As rotações são controladas pelas variáveis `rtri` e `rquad`, que são incrementadas a cada quadro:

```python
rtri += 0.2  # Rotação da pirâmide
rquad -= 0.15  # Rotação do cubo
```

### 4. Ciclo Principal
A cada iteração do ciclo principal, o buffer de cor e profundidade é limpo, os objetos são desenhados, e o conteúdo da tela é atualizado:

```python
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
draw_pyramid()
draw_cube()
pygame.display.flip()
```

---

## Conclusão
Com este tutorial, criamos uma pirâmide suavemente colorida e um cubo com faces distintas em um ambiente 3D, aplicando rotação para dar a impressão de profundidade e movimento. Teste modificar as cores ou a rotação para explorar mais possibilidades!
