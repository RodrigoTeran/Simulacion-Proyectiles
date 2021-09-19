import pygame, sys
from constantes import *

dragsImg = pygame.image.load(r'images/drags.JPG')
squareImg = pygame.image.load(r'images/square.png')


def printTexto(title, font, x, y, window, color):
    label = font.render("{}".format(title), 1, color)
    window.blit(label, (x, y))


def dibujarVentana(window, FONT):
    # Dibujar background
    window.fill(COLOR_WINDOW, (0, 0, WIDTH, HEIGHT))

    # Dibujar labels
    printTexto("Proyecto Final Simulador de Proyectiles", FONT, WIDTH / 2 - 400, 50, window, DATA_FONT_COLOR)


def botonCambiarVentana(window, FONT):
    x = WIDTH - 400
    y = HEIGHT - 75
    rect = pygame.draw.rect(window, COLOR_SQUARE, (x, y, 300, 40))
    printTexto("Ir a la simulación", FONT, x + 50, y + 7.5, window, (255, 255, 255))
    return rect


def dibujarInstrucciones(window, FONT):
    x = 490
    y = 200
    window.blit(dragsImg, (50, y))
    printTexto("Estos inputs sirven para controlar el rebote y la", FONT, x, y, window, DATA_FONT_COLOR)
    printTexto("fricción percibida por el bloque.", FONT, x, y + 40, window, DATA_FONT_COLOR)
    printTexto("Para cambiar los valores solo arrastra el rango.", FONT, x, y + 80, window, DATA_FONT_COLOR)

    y = 320
    window.blit(squareImg, (50, y + 70))
    printTexto("Para aplicarle fuerza al bloque, solo da click", FONT, x, y + 100, window, DATA_FONT_COLOR)
    printTexto("en la pantalla y al soltar el mouse, al bloque", FONT, x, y + 140, window, DATA_FONT_COLOR)
    printTexto("se le aplicará esa fuerza en esa dirección.", FONT, x, y + 180, window, DATA_FONT_COLOR)

    y = 620
    printTexto("Con este simulador aprenderás cómo se comporta", FONT, x, y, window, DATA_FONT_COLOR)
    printTexto("un objeto al aplicarle una fuerza en una dirección", FONT, x, y + 40, window, DATA_FONT_COLOR)
    printTexto("dada, y como el rebote y la fricción juegan su papel", FONT, x, y + 80, window, DATA_FONT_COLOR)
    printTexto("en el movimiento.", FONT, x, y + 120, window, DATA_FONT_COLOR)


def reglasSimulacion(window, ventana):
    FONT_36_Arial = pygame.font.SysFont("Arial Bold", 36)
    FONT_60 = pygame.font.SysFont("Arial Bold", 60)
    FONT = pygame.font.SysFont("monospace", 25)

    dibujarVentana(window, FONT_60)
    btnCambiarVentana = botonCambiarVentana(window, FONT_36_Arial)
    dibujarInstrucciones(window, FONT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if btnCambiarVentana.collidepoint(event.pos):
                    ventana.screen = 2
