"""
    Readme:
        Este archivo guarda las posiciones del cubito
        para posteriormente graficarlas en excel.
        Se utiliza numpy con el único propósito de guardar la matriz en un archivo csv.
        Toda la manipulación de la matriz se hace con puro Python
"""
from constantes import *
import pygame

# Se utiliza numpy con el único propósito de guardar la matriz en un archivo csv
import numpy as np

# La matriz de posiciones, cada elemento va a ser una tupla (x, y)
matriz_posiciones = []

# La referencia del botón de pygame
boton_grabar_datos = None

# Para que no se guarden muchísimos valores de coordenadas en la matriz,
# Se guardan de 5 en 5
# Este "contador_para_matriz" lleva la referencia
contador_para_matriz = 5

# Y este "max_contador_para_matriz" es el que dicta el máximo valor del contador
max_contador_para_matriz = 5

# Esto sirve para saber cuántos archivos csc hemos generado y que cada vez se
# genere otro archivo y no se reescriban los datos
csv_number = 1

def print_texto(title, font, x, y, window, color):
    """
        Esta función me ayuda a no tener que repetir este código cada vez que quiero poner
        texto en pantalla
    """
    label = font.render("{}".format(title), 1, color)   # Crea un label
    window.blit(label, (x, y))   

def grabar(nueva_posicion, ventana):
  """
    Esta función sirve para guardar los valores (x, y) en la matriz y
    Crear el archivo csv
  """
  global contador_para_matriz, matriz_posiciones, csv_number
  if ventana.esta_grabando:   # Si esta en grabar
    # Y el contador está en su posición máxima, para que se guarden de 5 en 5,
    if contador_para_matriz >= max_contador_para_matriz:
      # Se va a guardar la tupla de coordenadas (x, y) en la matriz de posiciones
      matriz_posiciones.append(nueva_posicion)
      
      # Se reinicia el contador
      # Se le pone -1 ya que en la siguiente línea de código se le va a volver a añadir +1
      # Entonces empieza desde 0 en la siguiente iteración
      contador_para_matriz = -1
    
    # A cada iteración se le añade 1 valor al contador
    contador_para_matriz += 1
    
  elif len(matriz_posiciones) > 0:
    # Cuando ya no está grabando y nuestra matriz tiene datos
    # Entonces hay que guardarlos
    npArray = np.array(matriz_posiciones)
    np.savetxt(f"test_{csv_number}.csv", npArray, delimiter=',')
    
    # Se reinicia la matriz
    matriz_posiciones = []
    
    # Se añade 1 al contador de archivos csv
    csv_number += 1
  
def dibujar_boton_grabar_datos(window, ventana):
    global boton_grabar_datos
    """
        Esta función pone el botón con su texto para que el usuario pueda
        empezar a grabar los datos
    """
    if ventana.screen == 2:
      # Si ya estamos en la ventana de la simulación
      # Se pone este botón
      FONT = pygame.font.SysFont("Arial Bold", 23)
      x = WIDTH - 150
      y = 20
      
      # Se dibuja el botón en la ventana "window", con el color "COLOR_SQUARE", en las coordenadas "x" y "y", con
      # un ancho de 130 y un alto de 28
      rect = pygame.draw.rect(window, COLOR_SQUARE, (x, y, 130, 28))
      
      # Se guarda el rectángulo pygame en la referencia "boton_grabar_datos"
      boton_grabar_datos = rect
      
      if ventana.esta_grabando:
        # Si está grabando se ponen los rectpangulos rojos de stop
        pygame.draw.rect(window, COLOR_LINE, (x - 20, y, 7, 28))
        pygame.draw.rect(window, COLOR_LINE, (x - 30, y, 7, 28))
      
      # Texto
      print_texto("Guardar datos", FONT, x + 10, y + 7.5, window, (255, 255, 255))
        
      return rect