from constantes import *
import pygame
from simulacion import simulacion

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Proyecto Final")
FONT = pygame.font.SysFont("monospace", 16)


def main():
    while True:
        simulacion(window, FONT)
        pygame.display.update()


if __name__ == "__main__":
    main()
