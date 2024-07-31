
# Aula Introdutória: Fundamentos de Computação Gráfica com OpenCV e Python

## Introdução

Nesta aula, vamos explorar os fundamentos da computação gráfica utilizando a biblioteca OpenCV com a linguagem Python. Nosso objetivo será instalar o software necessário e desenhar um quadrado em uma imagem.

## Instalação do Software e Bibliotecas

### 1. Instalação do Python

1. **Baixe e instale o Python**:
   - Acesse o site oficial do Python: [python.org](https://www.python.org/)
   - Baixe a versão mais recente do Python (certifique-se de marcar a opção "Add Python to PATH" durante a instalação).

### 2. Instalação do OpenCV

2. **Instale o OpenCV via pip**:
   - Abra o terminal ou prompt de comando.
   - Execute o comando:
     ```bash
     pip install opencv-python
     ```
3. **Instale o NumPy (necessário para manipulação de matrizes)**:
   - Execute o comando:
     ```bash
     pip install numpy
     ```

## Escrevendo o Código para Desenhar um Quadrado

### 1. Importando Bibliotecas

```python
import cv2
import numpy as np
```

### 2. Criando uma Imagem em Branco

```python
# Define o tamanho da imagem (altura, largura, canais de cor)
img = np.zeros((512, 512, 3), np.uint8)
```

### 3. Desenhando o Quadrado

```python
# Define as coordenadas do quadrado (ponto superior esquerdo e ponto inferior direito)
start_point = (100, 100)
end_point = (300, 300)

# Define a cor do quadrado em BGR (azul, verde, vermelho)
color = (255, 0, 0)  # Azul

# Define a espessura da linha (em pixels)
thickness = 2

# Desenha o quadrado na imagem
cv2.rectangle(img, start_point, end_point, color, thickness)
```

### 4. Exibindo a Imagem com o Quadrado

```python
# Exibe a imagem em uma janela
cv2.imshow('Quadrado', img)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas
cv2.destroyAllWindows()
```

## Código Completo

Aqui está o código completo para desenhar um quadrado usando OpenCV e Python:

```python
import cv2
import numpy as np

# Define o tamanho da imagem (altura, largura, canais de cor)
img = np.zeros((512, 512, 3), np.uint8)

# Define as coordenadas do quadrado (ponto superior esquerdo e ponto inferior direito)
start_point = (100, 100)
end_point = (300, 300)

# Define a cor do quadrado em BGR (azul, verde, vermelho)
color = (255, 0, 0)  # Azul

# Define a espessura da linha (em pixels)
thickness = 2

# Desenha o quadrado na imagem
cv2.rectangle(img, start_point, end_point, color, thickness)

# Exibe a imagem em uma janela
cv2.imshow('Quadrado', img)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas
cv2.destroyAllWindows()
```

## Estrutura da Aula

1. **Introdução**:
   - Apresentação do OpenCV e suas aplicações em Computação Gráfica.
   
2. **Instalação**:
   - Passo a passo da instalação do Python e OpenCV.
   
3. **Código Prático**:
   - Explicação e execução do código para desenhar um quadrado.

4. **Discussão**:
   - Análise do código e exploração de outras formas e cores.

## Recursos Adicionais

- [Documentação Oficial do OpenCV](https://docs.opencv.org/)
- [Tutoriais do OpenCV em Python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

Com este guia, você terá uma introdução prática e teórica sobre como usar o OpenCV com Python para criar gráficos simples.
