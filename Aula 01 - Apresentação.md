
# Aula Introdutória: Fundamentos de Computação Gráfica com OpenCV e Python

## Introdução

Nesta aula, vamos explorar os fundamentos da computação gráfica utilizando a biblioteca OpenCV com a linguagem Python. Nosso objetivo será instalar o software necessário e desenhar um quadrado em uma imagem.

#### O que é o OpenCV?

OpenCV (Open Source Computer Vision Library) é uma biblioteca de código aberto amplamente utilizada para visão computacional e aprendizado de máquina. Criada inicialmente pela Intel, é agora mantida pela OpenCV.org e é uma das bibliotecas mais populares para processamento de imagens e vídeos. Ela oferece mais de 2500 algoritmos otimizados que podem ser usados para uma vasta gama de tarefas, desde simples operações de imagem até complexas análises de vídeo e visão computacional.

#### Principais Características do OpenCV

1. **Código Aberto e Gratuito**: OpenCV é open-source, o que significa que qualquer pessoa pode acessar, modificar e distribuir seu código.
2. **Compatibilidade Multiplataforma**: Funciona em diversos sistemas operacionais, incluindo Windows, Linux, macOS e Android.
3. **Ampla Documentação e Suporte da Comunidade**: Possui uma vasta documentação oficial e uma comunidade ativa que contribui com tutoriais, fóruns e exemplos de uso.
4. **Integração com Bibliotecas de Aprendizado de Máquina**: Pode ser facilmente integrado com bibliotecas de aprendizado de máquina como TensorFlow, Keras e PyTorch, permitindo a implementação de modelos complexos de visão computacional.

#### Aplicações do OpenCV em Computação Gráfica

1. **Processamento de Imagens**:
   - **Filtros e Transformações**: Aplicação de filtros, transformações geométricas, correções de cor e histogramas.
   - **Detecção de Bordas**: Técnicas como o filtro de Sobel e Canny para detecção de bordas em imagens.

2. **Análise de Vídeo**:
   - **Rastreamento de Objetos**: Identificação e rastreamento de objetos em tempo real.
   - **Detecção de Movimento**: Análise de movimento em sequências de vídeo.

3. **Reconhecimento de Objetos e Padrões**:
   - **Detecção Facial**: Algoritmos para detecção de rostos humanos em imagens e vídeos.
   - **Reconhecimento de Caracteres**: Implementação de OCR (Reconhecimento Óptico de Caracteres) para leitura automática de texto em imagens.

4. **Realidade Aumentada (AR)**:
   - **Posicionamento e Rastreamento**: Utilização de marcadores para posicionamento de objetos virtuais em ambientes reais.

5. **Visão Computacional para Robótica**:
   - **Navegação Autônoma**: Processamento de imagens para orientação e navegação de robôs.
   - **Mapeamento e Localização**: SLAM (Simultaneous Localization and Mapping) para criação de mapas em tempo real.

6. **Projetos de Pesquisa e Desenvolvimento**:
   - **Análise Médica**: Processamento de imagens médicas para diagnósticos.
   - **Análise Industrial**: Inspeção de qualidade e controle de processos em linhas de produção.

### Passo a Passo da Instalação do Python, OpenCV e IDE para Desenvolvimento

#### 1. Instalação do Python

1. **Baixe e instale o Python**:
   - Acesse o site oficial do Python: [python.org](https://www.python.org/).
   - Clique em "Downloads" e selecione a versão mais recente do Python para o seu sistema operacional.
   - Baixe o instalador e execute-o.
   - Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.
   - Siga as instruções do instalador para concluir a instalação.

2. **Verifique a instalação do Python**:
   - Abra o terminal ou prompt de comando.
   - Execute o comando:
     ```bash
     python --version
     ```
   - Você deve ver a versão do Python instalada.

#### 2. Instalação do OpenCV

1. **Abra o terminal ou prompt de comando**.
2. **Instale o OpenCV via pip**:
   - Execute o comando:
     ```bash
     pip install opencv-python
     ```
3. **Instale o NumPy (necessário para manipulação de matrizes)**:
   - Execute o comando:
     ```bash
     pip install numpy
     ```

#### 3. Escolha e Instalação da IDE

### Visual Studio Code (VS Code)

1. **Baixe e instale o Visual Studio Code**:
   - Acesse o site oficial do VS Code: [code.visualstudio.com](https://code.visualstudio.com/).
   - Baixe o instalador para o seu sistema operacional e execute-o.
   - Siga as instruções do instalador para concluir a instalação.

2. **Instale a extensão do Python**:
   - Abra o VS Code.
   - Clique no ícone de extensões na barra lateral esquerda ou pressione `Ctrl+Shift+X`.
   - Pesquise por "Python" e instale a extensão oficial do Python (desenvolvida pela Microsoft).

3. **Configure o ambiente Python no VS Code**:
   - Abra o VS Code.
   - Clique em `File > Open Folder` e selecione o diretório onde deseja salvar seu projeto.
   - Abra o terminal integrado no VS Code (``Ctrl+` ``).
   - Crie um ambiente virtual (opcional, mas recomendado) executando os seguintes comandos no terminal integrado:
     ```bash
     python -m venv venv
     source venv/bin/activate  # No Windows: venv\Scripts\activate
     ```
   - Certifique-se de que o VS Code está usando o interpretador Python correto. Abra a paleta de comandos (`Ctrl+Shift+P`), digite `Python: Select Interpreter` e selecione o interpretador do seu ambiente virtual.

#### 4. Escrevendo o Código para Desenhar um Quadrado

1. **Crie um novo arquivo Python**:
   - No VS Code, clique em `File > New File` ou use o atalho `Ctrl+N`.
   - Salve o arquivo com a extensão `.py`, por exemplo, `desenhar_quadrado.py`.

2. **Adicione o código para desenhar o quadrado**:

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

3. **Execute o código**:
   - Certifique-se de que o ambiente virtual está ativado (se você criou um).
   - No terminal integrado do VS Code, execute o script Python:
     ```bash
     python desenhar_quadrado.py
     ```
   - Uma janela será exibida mostrando a imagem com o quadrado desenhado.


## Recursos Adicionais

- [Documentação Oficial do OpenCV](https://docs.opencv.org/)
- [Tutoriais do OpenCV em Python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

Com este guia, você terá uma introdução prática e teórica sobre como usar o OpenCV com Python para criar gráficos simples.
