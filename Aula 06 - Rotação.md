Aqui está um tutorial no formato `.md` sobre rotação de objetos usando OpenGL, baseado no conteúdo do tutorial "Rotation" do NeHe:

---

# Fundamentos de Computação Gráfica - Rotação de Objetos

## Introdução
Neste tutorial, aprenderemos a aplicar rotação em objetos desenhados com OpenGL. Usaremos as funções básicas de rotação para girar um triângulo e um quadrado em torno dos eixos X, Y e Z.

### Requisitos
- Ambiente configurado com OpenGL
- Familiaridade com conceitos de transformação em computação gráfica

## Passos

### 1. Configuração Inicial
Declare duas variáveis globais para armazenar o ângulo de rotação de cada objeto. Essas variáveis serão atualizadas em cada frame para criar o movimento contínuo.

```cpp
GLfloat rtri;  // Ângulo para o triângulo
GLfloat rquad; // Ângulo para o quadrado
```

### 2. Rotação do Triângulo
A função **glRotatef** é usada para rotacionar o triângulo no eixo Y.

```cpp
glTranslatef(-1.5f, 0.0f, -6.0f); // Move o triângulo para a esquerda
glRotatef(rtri, 0.0f, 1.0f, 0.0f); // Rotaciona no eixo Y

glBegin(GL_TRIANGLES);
    glColor3f(1.0f, 0.0f, 0.0f); // Vermelho
    glVertex3f( 0.0f, 1.0f, 0.0f);
    glColor3f(0.0f, 1.0f, 0.0f); // Verde
    glVertex3f(-1.0f,-1.0f, 0.0f);
    glColor3f(0.0f, 0.0f, 1.0f); // Azul
    glVertex3f( 1.0f,-1.0f, 0.0f);
glEnd();
```

### 3. Rotação do Quadrado
Resete a matriz de visualização, mova o quadrado para a direita e aplique a rotação no eixo X.

```cpp
glLoadIdentity();
glTranslatef(1.5f, 0.0f, -6.0f); // Move o quadrado para a direita
glRotatef(rquad, 1.0f, 0.0f, 0.0f); // Rotaciona no eixo X

glColor3f(0.5f, 0.5f, 1.0f); // Cor uniforme
glBegin(GL_QUADS);
    glVertex3f(-1.0f, 1.0f, 0.0f);
    glVertex3f( 1.0f, 1.0f, 0.0f);
    glVertex3f( 1.0f,-1.0f, 0.0f);
    glVertex3f(-1.0f,-1.0f, 0.0f);
glEnd();
```

### 4. Atualização dos Ângulos de Rotação
Atualize as variáveis de ângulo para aplicar a rotação contínua.

```cpp
rtri += 0.2f;  // Rotação para o triângulo
rquad -= 0.15f; // Rotação para o quadrado
```

### 5. Teste de Tela Cheia
Adicione um mecanismo para alternar entre os modos de janela e tela cheia com a tecla `F1`.

```cpp
if (keys[VK_F1]) {
    keys[VK_F1] = FALSE;
    KillGLWindow();
    fullscreen = !fullscreen;
    if (!CreateGLWindow("NeHe - Rotação", 640, 480, 16, fullscreen)) {
        return 0;
    }
}
```

![image](https://github.com/user-attachments/assets/d4920659-4855-4ff7-8044-794bf30ffa36)


