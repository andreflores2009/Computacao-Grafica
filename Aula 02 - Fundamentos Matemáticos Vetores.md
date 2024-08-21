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

![image](https://github.com/user-attachments/assets/9ea8e18c-4e8e-41c0-87fd-dd07fd2537a8)


### Conclusão

Esse código é uma introdução simples ao uso de Pygame para desenhar vetores 2D. Ele configura uma janela gráfica, permite que você desenhe 
linhas que representam vetores e processa eventos para manter o programa rodando até que o usuário decida fechá-lo. Este é um ótimo ponto de
partida para quem deseja aprender sobre a manipulação de gráficos 2D com Python e Pygame.



