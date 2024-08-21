
## Adição de Vetores

A adição de vetores é uma operação que combina dois vetores para criar um novo vetor. O vetor resultante é encontrado somando as componentes correspondentes dos vetores originais.

### Como Funciona:
![image](https://github.com/user-attachments/assets/370546dc-e89c-4b07-a2af-fd91c674336d)


### Interpretação Geométrica:

Geometricamente, a adição de vetores pode ser visualizada colocando o "final" de um vetor no "início" do outro. O vetor resultante é o vetor que vai do início do primeiro vetor até o final do segundo vetor. Isso é conhecido como o método "paralelogramo" ou "triângulo".

## Multiplicação de Vetor por Escalar

Multiplicar um vetor por um escalar é uma operação que redimensiona o vetor sem alterar sua direção (a menos que o escalar seja negativo, o que inverte a direção).

### Como Funciona:

![image](https://github.com/user-attachments/assets/8402ccbf-4e8a-48a9-9959-a141da07bb16)

### Interpretação Geométrica:

Geometricamente, multiplicar um vetor por um escalar `k` estica ou comprime o vetor. Se `k > 1`, o vetor é alongado; se `0 < k < 1`, o vetor é encurtado; se `k < 0`, além de ser redimensionado, a direção do vetor é invertida.


## Magnitude de um vetor

![image](https://github.com/user-attachments/assets/a8dd0c87-cadf-4059-b8ce-2d24aed7d6a5)

### Significado da Magnitude

- Fisicamente: Se o vetor representa um deslocamento no espaço, a magnitude seria a distância percorrida.
- Em termos de vetores de força: A magnitude indicaria a intensidade da força.

A magnitude é sempre um número não negativo. Um vetor nulo (onde todas as componentes são zero) tem uma magnitude de zero.

## Vetor Unitário / Normalizado
Um vetor unitário é um vetor que tem magnitude igual a 1. Vetores unitários são muito úteis em diversas aplicações de matemática e física porque mantêm a direção de um vetor, mas normalizam seu tamanho, facilitando cálculos e manipulações.

### Como Normalizar um Vetor

![image](https://github.com/user-attachments/assets/26792b84-33e1-401a-955c-2a26507972bf)

### Exemplo Prático

![image](https://github.com/user-attachments/assets/f290bc40-2d4d-431f-8f1a-3bd242beb1bb)

### Propriedades dos Vetores Unitários

- Direção: Um vetor unitário tem a mesma direção que o vetor original, mas sua magnitude é sempre 1.
- Facilita Cálculos: Vetores unitários são frequentemente usados para simplificar problemas em física, computação gráfica e geometria, especialmente em situações que envolvem direção, como ao definir uma direção no espaço, mas onde a magnitude não é relevante.

### Aplicações dos Vetores Unitários

- Direção em Espaço 3D: Em computação gráfica, vetores unitários são usados para representar direções em espaço tridimensional, como a direção de uma câmera, uma luz ou a orientação de um objeto.
- Vetores Normais: Em geometria computacional, os vetores normais às superfícies são geralmente representados como vetores unitários.
- Cálculos em Física: Em física, vetores unitários são usados para representar direções de forças, velocidades e outras grandezas vetoriais, mantendo a direção, mas ignorando a magnitude original.

Um vetor unitário é um vetor de magnitude 1 que aponta na mesma direção que o vetor original. A normalização é o processo de converter qualquer vetor em um vetor unitário, dividindo cada componente pela magnitude do vetor original. Vetores unitários são amplamente usados em diversas disciplinas para simplificar cálculos e representar direções no espaço.

## Propriedades Matemáticas Relacionadas a Vetores e Escalares

### Escalares

Escalares são simplesmente números comuns que podem ser inteiros, racionais, reais ou complexos, dependendo do contexto. Em álgebra linear e geometria vetorial, um escalar é um número que multiplica um vetor, modificando sua magnitude sem alterar sua direção (no caso de multiplicação por um número positivo).

### Vetores

Vetores são objetos matemáticos que possuem tanto magnitude (ou comprimento) quanto direção. Eles podem ser representados como uma sequência ordenada de números que correspondem às suas componentes em diferentes direções.

Aqui está a versão ajustada para Markdown simples, sem notação LaTeX, mas ainda clara e compreensível:

![image](https://github.com/user-attachments/assets/aa0aa064-5b7a-4a56-9418-ef992ae5604d)
![image](https://github.com/user-attachments/assets/7cac1cd6-8a3d-4fb8-9973-b5d5731d4e9f)


Essas propriedades são fundamentais em álgebra linear e são usadas para manipular vetores e escalares de maneira consistente e previsível. Elas garantem que as operações com vetores e escalares sigam padrões matemáticos bem definidos.


## Produto Escalar

O produto escalar, também conhecido como **dot product** em inglês, é uma operação matemática que pode ser realizada entre dois vetores. O resultado do produto escalar é um número escalar (daí o nome "produto escalar"), e essa operação possui várias aplicações importantes na matemática, física e engenharia.

![image](https://github.com/user-attachments/assets/b37d3f0d-c0b5-4ae7-a7f5-4f715e1027a7)


### Interpretação Geométrica

![image](https://github.com/user-attachments/assets/857f11fa-aaf2-4742-a9c6-d25e17d0edf4)

### Aplicações do Produto Escalar

- **Verificar ortogonalidade:** Se o produto escalar de dois vetores é zero, eles são ortogonais (perpendiculares).
- **Projeções:** O produto escalar pode ser usado para calcular a projeção de um vetor sobre outro.
- **Cálculo de ângulo entre vetores:** Usando a fórmula geométrica, é possível calcular o ângulo entre dois vetores.

## Produto Vetorial

O produto vetorial, também conhecido como **cross product** em inglês, é uma operação entre dois vetores em um espaço tridimensional que resulta em um novo vetor. Esse novo vetor é perpendicular (ou ortogonal) aos dois vetores originais, e sua magnitude está relacionada à área do paralelogramo formado pelos dois vetores.

### Definição de Produto Vetorial

![image](https://github.com/user-attachments/assets/6da6f66f-c894-4544-9b51-71b75da01eb2)

### Passo a Passo para Calcular o Produto Vetorial

![image](https://github.com/user-attachments/assets/04337e90-a523-426c-9c8e-fe8faacfad8f)

### Exemplo Prático

![image](https://github.com/user-attachments/assets/80337d3c-53ca-45c5-8d31-d6c2caa794aa)

### Interpretação Geométrica

[image](https://github.com/user-attachments/assets/37129658-b0af-4051-a93d-d06b8d3be564)

### Propriedades do Produto Vetorial

![image](https://github.com/user-attachments/assets/c6d4995f-a6e4-409c-8874-236b59f30509)

O produto vetorial segue a regra da mão direita, conforme imagem abaixo
- O indicador aponta na direção do vetor a;
- A palma da mão (ou dedo médio) aponta na direção do vetor b;
- O produto vetorial aponta na direção do polegar:
- 
  ![image](https://github.com/user-attachments/assets/70199f32-099b-4651-ab99-70baf608846a)


### Aplicações do Produto Vetorial

- **Cálculo de Torque:** Em física, o torque é calculado como o produto vetorial entre a força aplicada e o vetor posição.
- **Determinação de uma Normal:** Em computação gráfica, o produto vetorial é usado para encontrar o vetor normal a uma superfície.
- **Cálculo da Área:** O produto vetorial pode ser usado para calcular a área de um paralelogramo formado por dois vetores.

Para criar um exemplo utilizando a biblioteca `NumPy` em Python que demonstra o cálculo do produto vetorial (cross product) entre dois vetores, siga o exemplo abaixo:

## Exemplo de Produto Vetorial usando NumPy

```python
import numpy as np

# Definindo os vetores A e B
vetor_a = np.array([2, 3, 4])
vetor_b = np.array([5, 6, 7])

# Calculando o produto vetorial (cross product)
produto_vetorial = np.cross(vetor_a, vetor_b)

# Exibindo o resultado
print(f"Vetor A: {vetor_a}")
print(f"Vetor B: {vetor_b}")
print(f"Produto Vetorial (A x B): {produto_vetorial}")
```

### Como funciona o código:

1. **Definição dos Vetores:**
   - `vetor_a` e `vetor_b` são definidos como arrays NumPy, cada um com três componentes representando vetores em um espaço tridimensional.

2. **Cálculo do Produto Vetorial:**
   - A função `np.cross()` é usada para calcular o produto vetorial entre `vetor_a` e `vetor_b`.

3. **Exibição do Resultado:**
   - O código exibe os vetores originais e o vetor resultante do produto vetorial.

### Saída esperada:

Ao executar o código, a saída será:

```
Vetor A: [2 3 4]
Vetor B: [5 6 7]
Produto Vetorial (A x B): [-3  6 -3]
```

### Interpretação do Resultado:

![image](https://github.com/user-attachments/assets/8eae3ba9-4405-4595-b4d6-f8000e8bd54e)
