
# Fundamentos de Computação Gráfica - Seu Primeiro Polígono

## Introdução
Neste tutorial, vamos aprender a desenhar dois tipos de polígonos utilizando OpenGL: um triângulo e um quadrado. Para isso, utilizaremos as funções básicas de desenho de polígonos, como **glBegin**/**glEnd**, e funções para movimentação, como **glTranslatef**.

### Requisitos
- Ambiente configurado com OpenGL
- Conhecimento básico em C++ (ou outra linguagem compatível com OpenGL)

## Passos

### 1. Criando a Janela OpenGL
Primeiro, precisamos garantir que temos uma janela OpenGL funcional. Use o código base da criação da janela conforme visto em outros tutoriais.

### 2. Desenhando o Triângulo
Para desenhar o triângulo, utilizamos a função **glBegin(GL_TRIANGLES)** e definimos os três vértices do triângulo com **glVertex3f**. Cada vértice será especificado em um plano 3D, com as coordenadas X, Y e Z.

```cpp
glBegin(GL_TRIANGLES);
    glVertex3f( 0.0f, 1.0f, 0.0f); // Vértice superior
    glVertex3f(-1.0f,-1.0f, 0.0f); // Vértice inferior esquerdo
    glVertex3f( 1.0f,-1.0f, 0.0f); // Vértice inferior direito
glEnd();
```

### 3. Desenhando o Quadrado
Para o quadrado, utilizamos **glBegin(GL_QUADS)** e definimos quatro vértices. O quadrado será desenhado no sentido horário, começando do topo esquerdo.

```cpp
glBegin(GL_QUADS);
    glVertex3f(-1.0f, 1.0f, 0.0f); // Topo esquerdo
    glVertex3f( 1.0f, 1.0f, 0.0f); // Topo direito
    glVertex3f( 1.0f,-1.0f, 0.0f); // Base direita
    glVertex3f(-1.0f,-1.0f, 0.0f); // Base esquerda
glEnd();
```

### 4. Movimentando Objetos na Tela
Utilizamos **glTranslatef** para mover os objetos no espaço 3D. Por exemplo, para desenhar o triângulo à esquerda da tela e o quadrado à direita, movemos o triângulo para a esquerda (-1.5 na coordenada X) e o quadrado para a direita (+3.0 na coordenada X).

```cpp
glTranslatef(-1.5f, 0.0f, -6.0f); // Move o triângulo para a esquerda
// Desenho do triângulo...

glTranslatef(3.0f, 0.0f, 0.0f);   // Move o quadrado para a direita
// Desenho do quadrado...
```

## Considerações Finais
Neste tutorial, cobrimos os fundamentos de como criar polígonos simples em uma janela OpenGL. Aprendemos como desenhar triângulos e quadrados, além de como mover objetos pela tela. Esses conceitos são essenciais para o desenvolvimento de gráficos mais complexos.

Para mais informações, acesse o [tutorial original](https://nehe.gamedev.net/tutorial/your_first_polygon/13002/).
