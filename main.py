from constantes import *
import pygame
from simulacion import simulacion
from reglas import reglasSimulacion

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Proyecto Final")

# Ventana
class Ventana:
    def __init__(self):
        self.screen = 1


ventana = Ventana()


def main():
    while True:
        if ventana.screen == 1:
            reglasSimulacion(window, ventana)
        elif ventana.screen == 2:
            simulacion(window)
        pygame.display.update()


if __name__ == "__main__":
    main()
