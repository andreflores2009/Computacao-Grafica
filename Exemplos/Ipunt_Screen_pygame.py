import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Janela de Entrada")

# Defina as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
cinza = (200, 200, 200)

# Configure a fonte
fonte = pygame.font.Font(None, 36)
fonte_menor = pygame.font.Font(None, 24)

# Variáveis de entrada
texto_entrada = ''
ativo = False
retangulo_texto = pygame.Rect(100, 100, 600, 40)
retangulo_botao = pygame.Rect(100, 150, 100, 40)
corretangulo_texto = cinza
corretangulo_botao = cinza
texto_botao = "Enviar"

# Função para desenhar o retângulo e o texto
def desenhar_entrada():
    pygame.draw.rect(tela, corretangulo_texto, retangulo_texto, 2)
    texto_surface = fonte.render(texto_entrada, True, preto)
    tela.blit(texto_surface, (retangulo_texto.x + 5, retangulo_texto.y + 5))

def desenhar_botao():
    pygame.draw.rect(tela, corretangulo_botao, retangulo_botao)
    texto_surface = fonte_menor.render(texto_botao, True, preto)
    tela.blit(texto_surface, (retangulo_botao.x + 10, retangulo_botao.y + 10))

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicao_mouse = evento.pos
            if retangulo_texto.collidepoint(posicao_mouse):
                ativo = True
                corretangulo_texto = branco
            else:
                ativo = False
                corretangulo_texto = cinza
            
            if retangulo_botao.collidepoint(posicao_mouse):
                print(f"Texto enviado: {texto_entrada}")
                texto_entrada = ''
                ativo = False
                corretangulo_texto = cinza

        elif evento.type == pygame.KEYDOWN and ativo:
            if evento.key == pygame.K_BACKSPACE:
                texto_entrada = texto_entrada[:-1]
            elif evento.key == pygame.K_RETURN:
                print(f"Texto enviado: {texto_entrada}")
                texto_entrada = ''
                ativo = False
                corretangulo_texto = cinza
            else:
                texto_entrada += evento.unicode

    # Atualize a tela
    tela.fill(branco)
    desenhar_entrada()
    desenhar_botao()
    pygame.display.flip()
