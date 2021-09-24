import pygame, sys
from constantes import *

dragsImg = pygame.image.load(r'images/drags.JPG')       # Se carga la primera imagen
squareImg = pygame.image.load(r'images/square.png')     # Se carga la segunda imagen


def printTexto(title, font, x, y, window, color):
    """
        Esta función me ayuda a no tener que repetir este código cada vez que quiero poner
        texto en pantalla
    """
    label = font.render("{}".format(title), 1, color)   # Crea un label
    window.blit(label, (x, y))                          # Lo pone en pantalla en las coordenadas "x" y "y"


def dibujarVentana(window, FONT):
    """
        Esta función me ayuda a dibujar el título de la ventana y llenar el background del window.
    """
    # LLenar la ventana con el color "COLOR_WINDOW" desde las coordenadas (0, 0) hasta (WIDTH, HEIGHT)
    window.fill(COLOR_WINDOW, (0, 0, WIDTH, HEIGHT))

    # Dibujar título de esta ventana
    printTexto("Proyecto Final Simulador de Proyectiles", FONT, WIDTH / 2 - 400, 50, window, DATA_FONT_COLOR)


def botonCambiarVentana(window, FONT):
    """
        Esta función pone el botón con su texto para cambiar a la ventana de la simulación
    """
    x = WIDTH - 400
    y = HEIGHT - 75
    # Se dibuja el botón en la ventana "window", con el color "COLOR_SQUARE", en las coordenadas "x" y "y", con
    # un ancho de 300 y un alto de 40
    rect = pygame.draw.rect(window, COLOR_SQUARE, (x, y, 300, 40))

    # Se pone el texto encima del rectángulo
    printTexto("Ir a la simulación", FONT, x + 50, y + 7.5, window, (255, 255, 255))
    return rect


def dibujarInstrucciones(window, FONT):
    """
        Esta función simplemente se trata de poner en la ventana el texto necesario para que el usuario
        entienda como usar el programa
    """
    x = 490
    y = 200
    window.blit(dragsImg, (50, y))          # Se pone la imagen "dragsImg" en las coordenadas (50, y)
    printTexto("Estos inputs sirven para controlar el rebote y la", FONT, x, y, window, DATA_FONT_COLOR)
    printTexto("fricción percibida por el bloque.", FONT, x, y + 40, window, DATA_FONT_COLOR)
    printTexto("Para cambiar los valores solo arrastra el rango.", FONT, x, y + 80, window, DATA_FONT_COLOR)

    y = 320
    window.blit(squareImg, (50, y + 70))    # Se pone la imagen "squareImg" en las coordenadas (50, y + 70)
    printTexto("Para aplicarle fuerza al bloque, solo da click", FONT, x, y + 100, window, DATA_FONT_COLOR)
    printTexto("en la pantalla y al soltar el mouse, al bloque", FONT, x, y + 140, window, DATA_FONT_COLOR)
    printTexto("se le aplicará esa fuerza en esa dirección.", FONT, x, y + 180, window, DATA_FONT_COLOR)

    y = 620
    printTexto("Con este simulador aprenderás cómo se comporta", FONT, x, y, window, DATA_FONT_COLOR)
    printTexto("un objeto al aplicarle una fuerza en una dirección", FONT, x, y + 40, window, DATA_FONT_COLOR)
    printTexto("dada, y como el rebote y la fricción juegan su papel", FONT, x, y + 80, window, DATA_FONT_COLOR)
    printTexto("en el movimiento.", FONT, x, y + 120, window, DATA_FONT_COLOR)


def reglasSimulacion(window, ventana):
    # Aquí creo diferentes fonts para usarlos en el programa
    FONT_36_Arial = pygame.font.SysFont("Arial Bold", 36)
    FONT_60 = pygame.font.SysFont("Arial Bold", 60)
    FONT = pygame.font.SysFont("monospace", 25)

    dibujarVentana(window, FONT_60)                                 # Dibujar lo esencial de la ventana
    btnCambiarVentana = botonCambiarVentana(window, FONT_36_Arial)  # Poner el boton para cambair a la simulación
    dibujarInstrucciones(window, FONT)                              # Dibujar instrucciones

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            """
                Esto se pone por si el usuario da click en cerrar la pestaña
                Entonces se cierra la ventana y se cierra pygame
            """
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:                # Cuando el usuario de click en la ventana en general
            if event.button == 1:                               # Y si ese click llega a ser en el botón entonces...
                if btnCambiarVentana.collidepoint(event.pos):   # Se cambia de ventana
                    ventana.screen = 2
