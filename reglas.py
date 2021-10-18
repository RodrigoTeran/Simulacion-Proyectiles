import pygame, sys
from constantes import *

drags_img = pygame.image.load(r'drags.JPG')       # Se carga la primera imagen
square_img = pygame.image.load(r'square.png')     # Se carga la segunda imagen


def print_texto(title, font, x, y, window, color):
    """
        Esta función me ayuda a no tener que repetir este código cada vez que quiero poner
        texto en pantalla
    """
    label = font.render("{}".format(title), 1, color)   # Crea un label
    window.blit(label, (x, y))                          # Lo pone en pantalla en las coordenadas "x" y "y"


def dibujar_ventana(window, FONT):
    """
        Esta función me ayuda a dibujar el título de la ventana y llenar el background del window.
    """
    # LLenar la ventana con el color "COLOR_WINDOW" desde las coordenadas (0, 0) hasta (WIDTH, HEIGHT)
    window.fill(COLOR_WINDOW, (0, 0, WIDTH, HEIGHT))

    # Dibujar título de esta ventana
    print_texto("Proyecto Final Simulador de Proyectiles", FONT, WIDTH / 2 - 400, 50, window, DATA_FONT_COLOR)


def boton_cambiar_ventana(window, FONT):
    """
        Esta función pone el botón con su texto para cambiar a la ventana de la simulación
    """
    x = WIDTH - 400
    y = HEIGHT - 75
    # Se dibuja el botón en la ventana "window", con el color "COLOR_SQUARE", en las coordenadas "x" y "y", con
    # un ancho de 300 y un alto de 40
    rect = pygame.draw.rect(window, COLOR_SQUARE, (x, y, 300, 40))

    # Se pone el texto encima del rectángulo
    print_texto("Ir a la simulación", FONT, x + 50, y + 7.5, window, (255, 255, 255))
    return rect


def dibujar_instrucciones(window, FONT):
    """
        Esta función simplemente se trata de poner en la ventana el texto necesario para que el usuario
        entienda como usar el programa
    """
    x = 490
    y = 200
    window.blit(drags_img, (50, y))          # Se pone la imagen "drags_img" en las coordenadas (50, y)
    print_texto("Estos inputs sirven para controlar el rebote y la", FONT, x, y, window, DATA_FONT_COLOR)
    print_texto("fricción percibida por el bloque.", FONT, x, y + 40, window, DATA_FONT_COLOR)
    print_texto("Para cambiar los valores solo arrastra el rango.", FONT, x, y + 80, window, DATA_FONT_COLOR)

    y = 320
    window.blit(square_img, (50, y + 70))    # Se pone la imagen "square_img" en las coordenadas (50, y + 70)
    print_texto("Para aplicarle fuerza al bloque, solo da click", FONT, x, y + 100, window, DATA_FONT_COLOR)
    print_texto("en la pantalla y al soltar el mouse, al bloque", FONT, x, y + 140, window, DATA_FONT_COLOR)
    print_texto("se le aplicará esa fuerza en esa dirección.", FONT, x, y + 180, window, DATA_FONT_COLOR)

    y = 620
    print_texto("Con este simulador aprenderás cómo se comporta", FONT, x, y, window, DATA_FONT_COLOR)
    print_texto("un objeto al aplicarle una fuerza en una dirección", FONT, x, y + 40, window, DATA_FONT_COLOR)
    print_texto("dada, y como el rebote y la fricción juegan su papel", FONT, x, y + 80, window, DATA_FONT_COLOR)
    print_texto("en el movimiento.", FONT, x, y + 120, window, DATA_FONT_COLOR)


def reglas_simulacion(window, ventana):
    """
        Esta función es la principal. Aquí se para la referencia a window desde el archivo main.py
        Además también se le pasa el objeto ventana para saber si dibujar las reglas o no por su atributo
        "screen".
    """
    # Aquí creo diferentes fonts para usarlos en el programa
    FONT_36_Arial = pygame.font.SysFont("Arial Bold", 36)
    FONT_60 = pygame.font.SysFont("Arial Bold", 60)
    FONT = pygame.font.SysFont("monospace", 25)

    dibujar_ventana(window, FONT_60)                                 # Dibujar lo esencial de la ventana
    btnCambiarVentana = boton_cambiar_ventana(window, FONT_36_Arial)  # Poner el boton para cambair a la simulación
    dibujar_instrucciones(window, FONT)                              # Dibujar instrucciones

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
