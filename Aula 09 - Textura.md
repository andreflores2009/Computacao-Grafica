### Aula: Aplicação de Textura em OpenGL

Nesta aula, vamos aprender como aplicar texturas a um cubo 3D utilizando o OpenGL em Python. O processo envolve carregar uma imagem e mapear a textura para as faces do cubo.

#### 1. Carregamento da Textura
O primeiro passo é carregar a imagem da textura e convertê-la para um formato que o OpenGL possa usar.

```python
def load_texture():
    texture_surface = pygame.image.load('local_sua_img.png')
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
```

- **`pygame.image.load()`**: Carrega a imagem da textura.
- **`glTexImage2D()`**: Envia a imagem da textura para a GPU.
- **`glTexParameterf()`**: Define como a textura será mapeada e filtrada.

#### 2. Mapeamento de Texturas nas Faces
Após carregar a textura, podemos aplicá-la ao cubo. Cada face do cubo terá coordenadas de textura definidas com **`glTexCoord2f()`**.

```python
def draw_cube():
    glBindTexture(GL_TEXTURE_2D, 1)  # Vincula a textura
    glBegin(GL_QUADS)

    # Exemplo para uma das faces:
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    
    # (Outras faces seguem o mesmo padrão)
    glEnd()
```

- **`glTexCoord2f()`**: Define as coordenadas de textura para mapear a imagem nos vértices do cubo.

#### 3. Rotação do Cubo
Para fazer com que o cubo gire, incrementamos a variável de rotação a cada frame.

```python
rquad += 0.2
glRotatef(rquad, 1, 1, 1)  # Aplica rotação no cubo
```

Isso cria o efeito de rotação contínua.

#### 4. Loop Principal

No loop principal, a textura é carregada, o cubo é desenhado e a janela é atualizada.

```python
def main():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()
    load_texture()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
```

- **`load_texture()`** carrega a textura antes de entrar no loop de renderização.
- **`glClear()`** limpa a tela para o próximo frame.
- **`pygame.display.flip()`** atualiza a janela exibindo o cubo com textura.

### Conclusão

Aplicar texturas no OpenGL envolve carregar uma imagem, enviar os dados para a GPU e mapeá-los para os vértices do objeto. Neste exemplo, aplicamos texturas em um cubo 3D, criando um efeito visual interessante com a rotação contínua.

### Resultado
![image](https://github.com/user-attachments/assets/6262c023-c806-4bad-8ac8-edbf4f9a54ba)

## Exemplo 2

Vamos repetir o processo de aplicação de textura, mas agora aplicaremos a textura em uma esfera. Vamos seguir um procedimento semelhante ao que fizemos para o cubo.

### 1. Carregando a Textura

Primeiro, vamos carregar a textura que será aplicada à esfera, utilizando a mesma função `load_texture()`:

```python
def load_texture():
    texture_surface = pygame.image.load('C:/Users/Dell/Downloads/bricks2.jpg')
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
```

### 2. Aplicando a Textura à Esfera

Agora, modificamos a função `draw_sphere()` para aplicar a textura na esfera:

```python
def draw_sphere():
    """Desenha uma esfera com textura."""
    
    glPushMatrix()
    glTranslatef(0.0, 0.0, -12.0)  # Posiciona a esfera no centro
    
    glBindTexture(GL_TEXTURE_2D, 1)  # Vincula a textura
    
    # Desenha a superfície da esfera com textura
    textured_sphere = gluNewQuadric()
    gluQuadricTexture(textured_sphere, GL_TRUE)  # Habilita textura na esfera
    gluSphere(textured_sphere, 2, 32, 32)  # Desenha a esfera com textura
    
    glPopMatrix()
```

### 3. Loop Principal

O loop principal continua o mesmo, chamando a função `draw_sphere()` em vez de `draw_cube()`:

```python
def main():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()
    load_texture()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_sphere()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
```

### Resultado 
![image](https://github.com/user-attachments/assets/eb864315-a56d-48c5-9561-1334bdd7348d)



https://github.com/user-attachments/assets/5734e0d0-3555-463f-a981-6527118e735a


### Conclusão

Neste exemplo, carregamos uma textura e aplicamos à superfície de uma esfera, criando um efeito visual mais realista. O OpenGL facilita a aplicação de texturas em objetos complexos como esferas com o uso de `gluQuadricTexture()` e `gluSphere()`. Experimente diferentes imagens de textura para ver como elas são aplicadas na superfície curva da esfera.

### Exercício:

1. Tente substituir a imagem da textura por outra imagem.
2. Ajuste as coordenadas de textura para observar como diferentes partes da imagem são mapeadas no cubo.

