## Iluminação no OpenGL

A iluminação no OpenGL é um componente fundamental para criar realismo em cenas 3D. Ela simula como os objetos interagem com fontes de luz para produzir sombras, reflexos e variações de tonalidade, em função da posição e intensidade da luz, bem como das características dos materiais dos objetos. O OpenGL implementa um modelo de iluminação simplificado, baseado no modelo de iluminação de **Phong**, que leva em consideração a luz ambiente, difusa e especular.

A iluminação no OpenGL funciona basicamente em três partes principais: **fontes de luz**, **interação com os materiais dos objetos**, e **cálculo da intensidade da luz** em cada ponto da superfície de um objeto.

### Componentes da Iluminação no OpenGL

A iluminação no OpenGL é composta por três componentes principais:

1. **Luz Ambiente (Ambient Light)**:
   - A luz ambiente é a mais simples e é distribuída uniformemente por toda a cena. Ela simula a luz refletida indiretamente pelos objetos ao redor, ou seja, a luz que já foi espalhada por múltiplas superfícies e que ilumina todos os objetos igualmente, sem considerar a direção. Isso significa que a luz ambiente afeta todas as superfícies do objeto igualmente, não importa se elas estão voltadas para a fonte de luz ou não.
   - No OpenGL, a luz ambiente é configurada usando o comando `glLightfv` com o parâmetro `GL_AMBIENT`.

2. **Luz Difusa (Diffuse Light)**:
   - A luz difusa simula a luz que incide diretamente sobre a superfície de um objeto e é refletida de forma dispersa. Esse tipo de iluminação depende da orientação da superfície em relação à fonte de luz. A luz difusa é o que cria sombras suaves e realistas nas superfícies de um objeto, com a intensidade da luz diminuindo à medida que a superfície se orienta para longe da fonte de luz.
   - A luz difusa é configurada usando `glLightfv` com o parâmetro `GL_DIFFUSE`. Ela depende das **normais** das superfícies para determinar como a luz atinge o objeto.

3. **Luz Especular (Specular Light)**:
   - A luz especular é responsável por criar os brilhos intensos, como reflexos em superfícies polidas ou metálicas. A reflexão especular é mais concentrada e depende da posição do observador. Em superfícies altamente reflexivas, a luz especular é mais visível como pontos brilhantes, e em superfícies opacas, ela é mais dispersa.
   - No OpenGL, a luz especular é configurada com o parâmetro `GL_SPECULAR`, tanto para as luzes quanto para os materiais. O parâmetro `GL_SHININESS` determina a "concentração" do reflexo.

### Funcionamento da Iluminação no OpenGL

A iluminação em OpenGL é baseada em um **modelo local de iluminação**, o que significa que a luz é calculada individualmente para cada vértice ou fragmento, sem levar em consideração como a luz se espalha pela cena inteira. O cálculo da iluminação envolve várias variáveis, como:

1. **Posição da Luz**:
   - As fontes de luz em OpenGL podem ser posicionais (como uma lâmpada) ou direcionais (como a luz do sol). A posição da luz é especificada usando coordenadas 3D e afeta a forma como a luz é calculada em cada superfície.
   - Se `w = 0.0`, a luz é tratada como uma **luz direcional** (infinitamente distante, como a luz solar). Se `w = 1.0`, a luz é **posicional** (luz que vem de um ponto específico e se espalha em todas as direções).

2. **Normais das Superfícies**:
   - Cada face ou vértice de um objeto tem um **vetor normal**, que é perpendicular à superfície. Esse vetor normal é essencial para calcular a interação da luz difusa e especular, determinando como a luz incide em cada parte do objeto.
   - O ângulo entre o vetor normal da superfície e a direção da luz afeta a intensidade da luz difusa e especular.

3. **Materiais**:
   - Cada objeto na cena tem propriedades de material que determinam como ele interage com a luz. Esses materiais incluem componentes como:
     - **Cor ambiente** (GL_AMBIENT): A quantidade de luz ambiente que o objeto reflete.
     - **Cor difusa** (GL_DIFFUSE): A quantidade de luz difusa refletida.
     - **Cor especular** (GL_SPECULAR): A intensidade dos reflexos especulares.
     - **Brilho** (GL_SHININESS): Controla a concentração do reflexo especular.

4. **Modelo de Shading**:
   - O OpenGL permite escolher entre dois modelos de shading:
     - **Flat Shading**: Cada polígono tem uma cor uniforme, e a iluminação é calculada apenas para um vértice, resultando em uma aparência mais "dura" e menos realista.
     - **Smooth Shading (Gouraud)**: A iluminação é calculada para cada vértice, e os valores são interpolados entre os vértices ao longo das superfícies, resultando em transições suaves de iluminação e uma aparência mais realista.

### Exemplo de Iluminação no OpenGL

Aqui está um exemplo de como a iluminação funciona no OpenGL, com um cubo simples iluminado por uma fonte de luz:

```python
def init_lighting():
    glEnable(GL_LIGHTING)        # Ativa o sistema de iluminação
    glEnable(GL_LIGHT0)          # Habilita a luz 0 (a primeira fonte de luz)
    
    # Definindo as propriedades da luz ambiente, difusa e sua posição
    light_ambient = [0.2, 0.2, 0.2, 1.0]   # Luz ambiente fraca
    light_diffuse = [0.8, 0.8, 0.8, 1.0]   # Luz difusa brilhante
    light_position = [0, 2, 0, 1.0]        # Posição da luz (acima do objeto)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)    # Aplicando a luz ambiente
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)    # Aplicando a luz difusa
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)  # Definindo a posição da luz

    # Definindo propriedades do material do cubo
    material_specular = [1.0, 1.0, 1.0, 1.0]   # Reflexão especular (brilho)
    material_shininess = [50.0]                # Brilho do material

    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)  # Aplicando a reflexão especular
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess) # Aplicando o brilho

    glEnable(GL_COLOR_MATERIAL)  # Habilita as cores dos materiais
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)  # Define como as cores do material se comportam com a luz
```

### 1. **Ativando o Sistema de Iluminação**
```python
glEnable(GL_LIGHTING)    # Habilita o sistema de iluminação
```
Esse comando ativa o sistema de iluminação do OpenGL. Sem ele, nenhum efeito de luz será aplicado aos objetos na cena, e tudo parecerá plano e uniforme. A iluminação em OpenGL precisa ser habilitada explicitamente, pois, por padrão, ela vem desabilitada. Quando ativada, o OpenGL começa a considerar as fontes de luz, o comportamento dos materiais, e como a luz interage com as superfícies dos objetos, criando efeitos de sombra, reflexo, e brilho.

```python
glEnable(GL_LIGHT0)      # Ativa a luz 0
```
Esse comando ativa a primeira fonte de luz (conhecida como `GL_LIGHT0`) no OpenGL. O OpenGL suporta até oito fontes de luz distintas (de `GL_LIGHT0` a `GL_LIGHT7`), e você pode configurar as propriedades de cada uma individualmente. A luz `GL_LIGHT0` é a primeira e mais comumente usada. Sem ativar uma luz específica, mesmo que a iluminação esteja habilitada com `glEnable(GL_LIGHTING)`, nada será iluminado.

### 2. **Configurando as Propriedades da Luz**
```python
light_ambient = [0.2, 0.2, 0.2, 1.0]   # Luz ambiente (luz fraca que preenche todo o ambiente)
```
Esse é o vetor que define a **luz ambiente** para a luz `GL_LIGHT0`. A luz ambiente é uma luz suave e uniforme que afeta todos os objetos na cena igualmente, sem criar sombras ou reflexos. Ela preenche as áreas que não estão diretamente iluminadas pela luz difusa ou especular. A estrutura do vetor `[r, g, b, a]` representa os componentes de cor vermelho, verde, azul e alfa (transparência). Aqui, a luz ambiente tem baixa intensidade (`0.2` para cada componente de cor), criando um efeito fraco de iluminação geral.

```python
light_diffuse = [0.8, 0.8, 0.8, 1.0]   # Luz difusa (luz principal que ilumina o objeto)
```
Esse vetor define a **luz difusa** da fonte `GL_LIGHT0`. A luz difusa é a principal responsável por iluminar diretamente os objetos, criando sombras e destacando as formas do objeto conforme a sua posição em relação à luz. O vetor `[0.8, 0.8, 0.8, 1.0]` define a cor da luz, neste caso, uma luz branca brilhante com intensidade de `0.8` para cada componente de cor (vermelho, verde, azul). Esse tipo de luz considera a direção e o ângulo da superfície dos objetos, criando um efeito de luz mais realista.

```python
light_position = [0, 2, 0, 0.0]  # Posição da luz
```
Esse vetor define a **posição da luz** `GL_LIGHT0` no espaço 3D. O vetor `[x, y, z, w]` define a localização da luz:
- `x = 0`, `y = 2`, `z = 0` indica que a luz está localizada diretamente acima do objeto (2 unidades acima no eixo y).
- `w = 0.0` indica que essa é uma **luz direcional**, o que significa que a luz é emitida uniformemente de uma direção específica, como a luz do sol. Se `w` fosse `1.0`, a luz seria uma **luz pontual**, que emite luz de um ponto específico, se espalhando em todas as direções.

### 3. **Aplicando as Propriedades da Luz**
```python
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
glLightfv(GL_LIGHT0, GL_POSITION, light_position)
```
Esses três comandos aplicam as propriedades configuradas anteriormente (`light_ambient`, `light_diffuse`, e `light_position`) à luz `GL_LIGHT0`. O comando `glLightfv` define diferentes aspectos da luz:
- `GL_AMBIENT`: Define a componente de luz ambiente.
- `GL_DIFFUSE`: Define a componente de luz difusa.
- `GL_POSITION`: Define a posição (ou direção) da luz.

Esses valores são aplicados ao sistema de iluminação para a fonte de luz `GL_LIGHT0`.

### 4. **Configurando Materiais para Interagir com a Luz**
```python
material_specular = [1.0, 1.0, 1.0, 1.0]
```
Esse vetor define a **componente especular** do material que está sendo renderizado. A reflexão especular é o brilho intenso que aparece em superfícies quando a luz atinge diretamente a superfície. Essa reflexão é mais forte em materiais brilhantes, como metal ou vidro. O vetor `[1.0, 1.0, 1.0, 1.0]` indica que o material refletirá a luz branca de maneira especular, com máxima intensidade.

```python
material_shininess = [50.0]
```
Esse valor define o **brilho** do material. O brilho afeta o tamanho e a intensidade do reflexo especular. Um valor mais alto significa que o reflexo será mais pequeno e concentrado (mais como um ponto brilhante), enquanto um valor mais baixo resultará em um reflexo maior e mais difuso. No caso de `50.0`, o brilho está configurado para um reflexo moderadamente pequeno e concentrado, sugerindo uma superfície com uma certa quantidade de polimento.

### 5. **Aplicando as Propriedades do Material**
```python
glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
```
Esse comando aplica a propriedade especular ao **lado frontal** do objeto (ou seja, as faces que estão voltadas para a câmera). Isso faz com que o material tenha reflexões especulares de acordo com o valor de `material_specular`, que, neste caso, reflete a luz branca com intensidade total.

```python
glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)
```
Esse comando aplica o **brilho** ao material do lado frontal do objeto, usando o valor de `material_shininess`. Isso controla o quão concentrado o reflexo especular será, criando um brilho mais intenso em áreas específicas dependendo da iluminação.

### Vetor Normal
A função `glNormal3f(x, y, z)` é usada no OpenGL para definir o **vetor normal** de uma superfície ou de um vértice. O **vetor normal** é um vetor que é perpendicular à superfície e é essencial para que o OpenGL calcule corretamente como a luz interage com a superfície de um objeto. Para cada face do cubo, definimos um vetor normal específico que indica a direção para a qual a face está apontando.

No contexto de um cubo, cada face tem um vetor normal que aponta diretamente para fora da face em uma direção perpendicular. Ao definir as normais de maneira adequada para cada face do cubo, estamos informando ao OpenGL como calcular a iluminação em cada uma dessas superfícies.

### Explicação do comando:

```python
# Direita
glNormal3f(1.0, 0.0, 0.0)
```

Este comando define a normal para a **face direita** do cubo, ou seja, a face que está voltada para a direita no espaço tridimensional. O vetor `(1.0, 0.0, 0.0)` indica que:

- **1.0** na direção do eixo **x** significa que a face está apontando para o **lado positivo do eixo X**.
- **0.0** na direção do eixo **y** significa que não há inclinação ou direção vertical (nem para cima nem para baixo).
- **0.0** na direção do eixo **z** significa que não há inclinação ou direção para frente ou para trás.

Em outras palavras, essa normal indica que a face está perpendicular ao eixo X e "olhando" para a direita.

### Por que precisamos de normais?

As **normais** são fundamentais para o cálculo da iluminação, porque a maneira como a luz incide sobre uma superfície depende do **ângulo entre a direção da luz** e a **normal** da superfície. O OpenGL usa as normais para determinar o quão fortemente uma luz afeta uma superfície:

1. **Luz difusa**: A luz difusa é calculada com base no **ângulo entre a direção da luz e a normal** da superfície. Se a luz incide diretamente na superfície (ou seja, a direção da luz é paralela à normal), a superfície receberá a máxima intensidade de luz. Se a luz incide em um ângulo oblíquo, a intensidade da luz será menor.

2. **Luz especular**: A luz especular (os brilhos ou reflexos) também depende da direção da normal, pois o cálculo da reflexão especular leva em consideração o vetor normal para calcular a direção de reflexão da luz.

### Aplicação no Cubo

Em um cubo 3D, cada uma das seis faces está voltada para uma direção diferente. Para que a iluminação funcione corretamente e cada face reflita a luz de acordo com sua orientação, precisamos definir normais diferentes para cada face. Veja como isso se aplica ao cubo:

- **Face direita**: A normal é `(1.0, 0.0, 0.0)` porque a face está apontando para o lado positivo do eixo X.
- **Face esquerda**: A normal é `(-1.0, 0.0, 0.0)` porque a face está apontando para o lado negativo do eixo X.
- **Face superior**: A normal é `(0.0, 1.0, 0.0)` porque a face está apontando para cima (positivo no eixo Y).
- **Face inferior**: A normal é `(0.0, -1.0, 0.0)` porque a face está apontando para baixo (negativo no eixo Y).
- **Face frontal**: A normal é `(0.0, 0.0, 1.0)` porque a face está apontando para frente (positivo no eixo Z).
- **Face traseira**: A normal é `(0.0, 0.0, -1.0)` porque a face está apontando para trás (negativo no eixo Z).

Cada vez que desenhamos uma face do cubo, devemos definir a normal correspondente para que o OpenGL saiba como essa face está orientada no espaço 3D. Isso permite que o sistema de iluminação calcule corretamente a quantidade de luz que atinge a face e a forma como ela deve ser refletida.

### Exemplo completo com as normais definidas

Aqui está um exemplo de como todas as normais são definidas para o cubo:

```python
def draw_cube():
    glBindTexture(GL_TEXTURE_2D, 1)  # Vincula a textura
    glBegin(GL_QUADS)
    
    # Face superior
    glNormal3f(0.0, 1.0, 0.0)  # Normal apontando para cima
    glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0, 1.0, 1.0)
    
    # Face inferior
    glNormal3f(0.0, -1.0, 0.0)  # Normal apontando para baixo
    glTexCoord2f(0.0, 1.0); glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, -1.0)
    
    # Face frontal
    glNormal3f(0.0, 0.0, 1.0)  # Normal apontando para frente
    glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
    
    # Face traseira
    glNormal3f(0.0, 0.0, -1.0)  # Normal apontando para trás
    glTexCoord2f(0.0, 1.0); glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0, 1.0, -1.0)
    
    # Face esquerda
    glNormal3f(-1.0, 0.0, 0.0)  # Normal apontando para a esquerda
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
    
    # Face direita
    glNormal3f(1.0, 0.0, 0.0)  # Normal apontando para a direita
    glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, -1.0)
    
    glEnd()
```

### Como funcionam as normais em uma esfera?

Cada ponto na superfície da esfera tem uma normal que aponta diretamente para fora da superfície, em uma direção radial. Isso significa que, para qualquer ponto na superfície da esfera, a normal é um vetor que começa no centro da esfera e vai até a superfície. Esse comportamento é exatamente o que `gluSphere` já faz internamente.

### Iluminação com `gluSphere`

Quando você usa a função `gluSphere`, o OpenGL gera automaticamente os vértices da esfera e suas respectivas normais. Isso garante que a iluminação seja calculada corretamente, de acordo com a posição da fonte de luz, resultando em efeitos realistas de luz difusa e especular.

Por exemplo, com as normais corretamente definidas, você verá que as áreas da esfera que estão voltadas diretamente para a fonte de luz serão iluminadas mais intensamente (luz difusa), enquanto as áreas opostas serão mais escuras, criando um efeito de sombra.

### Explicação do código fornecido:

```python
def draw_sphere():
    """Desenha uma esfera com textura."""
    glLoadIdentity()  # Reseta a matriz de transformações
    glPushMatrix()    # Salva a matriz de transformação atual
    glTranslatef(2.5, 0.0, -12.0)  # Move a esfera para a posição desejada no espaço 3D
    
    glBindTexture(GL_TEXTURE_2D, 1)  # Vincula a textura à esfera
    
    # Cria uma nova esfera quadrática (gluNewQuadric) e habilita a aplicação de textura nela
    textured_sphere = gluNewQuadric()
    gluQuadricTexture(textured_sphere, GL_TRUE)  # Habilita a textura na esfera
    
    # Desenha a esfera com raio 2, com 32 subdivisões longitudinais e 32 subdivisões latitudinais
    gluSphere(textured_sphere, 2, 32, 32)
    
    glPopMatrix()  # Restaura a matriz de transformação anterior
```

Aqui:
- **`gluSphere`** desenha a esfera e, internamente, calcula as normais para cada vértice da esfera.
- **Texturas** estão habilitadas e aplicadas à superfície da esfera.
- **Iluminação**: As normais calculadas pelo `gluSphere` garantem que a iluminação funcione corretamente, de modo que a luz incidente na esfera interaja com ela de maneira realista.

## Resultado 

![image](https://github.com/user-attachments/assets/d94c7ee4-7fc3-4407-9665-c37aa48fc1a0)



https://github.com/user-attachments/assets/6129a5b6-2169-441c-8d18-527f142e06f3



