Aqui está um tutorial em formato `.md` baseado no artigo "Adding Colour" do NeHe:

---

# Fundamentos de Computação Gráfica - Adicionando Cor

## Introdução
Neste tutorial, vamos aprender a adicionar cores aos nossos polígonos usando OpenGL. Veremos dois tipos de coloração: coloração plana e coloração suave. A coloração plana aplica uma única cor ao objeto inteiro, enquanto a coloração suave mistura cores em vértices específicos, criando um gradiente entre eles.

### Requisitos
- OpenGL configurado no ambiente
- Conhecimento básico de C++ ou Python com PyOpenGL

## Passos

### 1. Adicionando Cor ao Triângulo
No código abaixo, usamos **glColor3f(r, g, b)** para definir a cor de cada vértice do triângulo. Isso cria uma coloração suave, onde as cores misturam-se entre os vértices.

```cpp
glBegin(GL_TRIANGLES);
    glColor3f(1.0f, 0.0f, 0.0f); // Vermelho no topo
    glVertex3f(0.0f, 1.0f, 0.0f);
    
    glColor3f(0.0f, 1.0f, 0.0f); // Verde no canto inferior esquerdo
    glVertex3f(-1.0f, -1.0f, 0.0f);
    
    glColor3f(0.0f, 0.0f, 1.0f); // Azul no canto inferior direito
    glVertex3f(1.0f, -1.0f, 0.0f);
glEnd();
```

### 2. Adicionando Cor ao Quadrado
Aqui, aplicamos uma única cor ao quadrado, resultando em uma coloração plana.

```cpp
glColor3f(0.5f, 0.5f, 1.0f);  // Azul claro
glBegin(GL_QUADS);
    glVertex3f(-1.0f, 1.0f, 0.0f);  // Canto superior esquerdo
    glVertex3f(1.0f, 1.0f, 0.0f);   // Canto superior direito
    glVertex3f(1.0f, -1.0f, 0.0f);  // Canto inferior direito
    glVertex3f(-1.0f, -1.0f, 0.0f); // Canto inferior esquerdo
glEnd();
```

### 3. Alterando entre Tela Cheia e Modo Janela
Para alternar entre os modos de tela cheia e janela, utilize a tecla F1.

```cpp
if (keys[VK_F1]) {
    keys[VK_F1] = FALSE;
    KillGLWindow();
    fullscreen = !fullscreen;
    if (!CreateGLWindow("Tutorial NeHe - Adicionando Cor", 640, 480, 16, fullscreen)) {
        return 0;
    }
}
```

## Conclusão
Com este tutorial, você aprendeu a aplicar cores em polígonos simples utilizando OpenGL, criando efeitos de coloração plana e suave.

Para mais informações, acesse o [tutorial original](https://nehe.gamedev.net/tutorial/adding_colour/13003/).
