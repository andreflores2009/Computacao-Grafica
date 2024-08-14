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