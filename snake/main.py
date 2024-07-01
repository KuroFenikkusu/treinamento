# configurações iniciais
import pygame
import random

pygame.init()

pygame.display.set_caption("Python Game")

largura, altura = 1200, 800

tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

# Cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# parametros snake

size_square = 20
speed_game = 15


def generate_food():
    food_x = round(random.randrange(0, largura - size_square) / 20.0) * 20.0
    food_y = round(random.randrange(0, altura - size_square) / 20.0) * 20.0
    return food_x, food_y

def draw_food(size, food_x, food_y):
    pygame.draw.rect(tela, verde, [food_x, food_y, size, size])

def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0],pixel[1], size, size ])

def select_speed(tecla):
    if tecla == pygame.K_DOWN:
        speed_x = 0
        speed_y = size_square
    elif tecla == pygame.K_UP:
        speed_x = 0
        speed_y = -size_square
    elif tecla == pygame.K_RIGHT:
        speed_x = size_square
        speed_y = 0
    elif tecla == pygame.K_LEFT:
        speed_x = -size_square
        speed_y = 0
    return speed_x, speed_y
    
def draw_points(points):
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontos: {points}", True, vermelho)
    tela.blit(texto, [1, 1])

def play_game():
    fim_jogo = False

    x = largura  / 2
    y  = altura / 2

    speed_x = 0
    speed_y = 0

    size_snake = 1
    pixels = []

    food_x, food_y = generate_food()
    

    while not fim_jogo:
        tela.fill(preto)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)

# criar um loop infinito


# desenhar os objetos do jogo na tela
        # score
        draw_points(size_snake -1)


        # snake
        pixels.append([x, y])
        if len(pixels) > size_snake:
            del pixels[0]
        # snake bateu na própria snake
        for pixel in pixels[:-1]:
            if pixel  == [x, y]:
                fim_jogo = True
        #
        draw_snake(size_square, pixels)
       # snake bateu na wall
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += speed_x
        y += speed_y

        # food
        draw_food(size_square, food_x, food_y)
        if x == food_x and  y == food_y:
            size_snake += 1
            food_x, food_y = generate_food()


        # atualizar tela
        pygame.display.update()
        relogio.tick(speed_game)
# criar a logica de terminar o jogo
play_game()