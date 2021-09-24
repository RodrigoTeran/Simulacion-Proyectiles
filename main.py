from constantes import *                # Constantes del programa
import pygame                           # Librería para mostrar solo los gráficos
from reglas import reglasSimulacion     # Primera ventana
from simulacion import simulacion       # Segunda ventana

pygame.init()                                       # Inicializa pygame
window = pygame.display.set_mode((WIDTH, HEIGHT))   # Crea la venta con un ancho y alto
pygame.display.set_caption("Proyecto Final")        # Le pone título a la ventana: "Proyecto Final"

# Ventana
"""
    Cree esta clase para poder editar sus propiedades
    desde otros archivos y conservar los cambios
"""
class Ventana:
    def __init__(self):
        self.screen = 1


ventana = Ventana()


def main():
    while True:                     # Así se maneja pygame, en cada iteración del bucle se actualiza la pantalla
        if ventana.screen == 1:
            # Ventana que muestra las reglas y lo que trata el programa
            reglasSimulacion(window, ventana)
        elif ventana.screen == 2:
            # Ventana que muestra la simulación de proyectiles
            simulacion(window)
        pygame.display.update()     # Se actualiza la ventana


if __name__ == "__main__":
    # Inicia el programa
    main()
