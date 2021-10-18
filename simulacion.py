"""
    Readme:
        No se usa ninguna librería para hacer los cálculos...
        lo único que se utiliza es pygame pero para mostrar los gráficos...
        todas las operaciones con la fricción, rebote, gravedad, tiro parabólico, fuerzas, etc
        se hacen con puros ciclos, comparaciones, etc...
"""
import sys
import pygame
from guardar import grabar
from guardar import dibujar_boton_grabar_datos
from constantes import *

clock = pygame.time.Clock()         # Se inicializa un reloj para medir el tiempo de juego
game_time = 0                        # El total se pone primero en 0

# -------------- Constantes --------------
GRAVEDAD = -9.81

# Posicion en x del mouse con respecto al cuadrado negro, al principio no importa
# que valor ponga, cuando el usuario empiece a mover su mouse se va a editar este valor
x_mouse = 600

# Posicion en x del mouse con respecto a la ventana en general
x_mouse_punto = 600

# Posicion en y del mouse con respecto al cuadrado negro
y_mouse = 600

# Sensibilidad del vector. Es decir, si este valor cambia... el vector podrá dar
# más o menos fuerza con la misma longitud
# Esta valor es inverso, es decir.. si es mayor hay menor sensibilidad...
# si es menor hay mucha
sensibilidad = 6

# -------------- Variables que el usuario puede cambiar --------------
rebote = 0.45  # Puede ir de 0 a 1, tiene .45 porque al principio esta al 45%
friccion = 0.012667  # Puede ir de 0 a  0.02, tiene 0.012667 porque al principio esta al 63%

# Variables del programa
# Velocidades iniciales...
velocidad_inicial_y = y_mouse / sensibilidad
velocidad_inicial_x = x_mouse / sensibilidad

# El delta del tiempo nos da la posibilidad de qué tan rápido pasa el tiempo en la simulación
# Si aumentamos este valor el cubito va a ir muy rápido, pero si lo disminuimos va a ir muy lento
delta_tiempo = 0.06
tiempo = 0

# Posiciones en "x" y "y" del cubito que salta
pos_x = WIDTH / 2 - LENGTH_SQUARE / 2        # Posicion inicial: WIDTH / 2 - LENGTH_SQUARE / 2
pos_y = HEIGHT - ALTURA_PISO - LENGTH_SQUARE  # Posicion inicial: HEIGHT - alturaPiso - LENGTH_SQUARE


# -------------- Ecuaciones física --------------
# El "tiempo_a_altura_y_mouse" se refiere al tiempo ocupado en esta fórmula de la física para posteriormente conocer en qué
# posicion debería estar el cubo en x
tiempo_a_altura_y_mouse = (-velocidad_inicial_y + (abs(
        velocidad_inicial_y ** 2 + 2 * GRAVEDAD * velocidad_inicial_y)) ** .5) \
                          / GRAVEDAD

# Con "tiempo_a_altura_y_mouse" calculamos la nueva posición de x
diff_x = int(tiempo_a_altura_y_mouse / delta_tiempo)

# Ahora ya sabemos cuanto moverlo, sería el delta_x
if diff_x == 0:
    # Por si se divide por 0
    diff_x += .0001
delta_x = velocidad_inicial_x / diff_x

# -------------- Valores booleanos --------------
# Estos me dan información de si o no del programa

# primer_golpe se refiere a si el bloque ya tocó el piso, para empezar a restar en x con la fricción
primer_golpe = False

# Se refiere a si ya debemos disprara o no
fire = False

# Como el nombre lo dice, si el mouse esta abajo, para saber si dibujamos el vector fuerza o no
is_mouse_down = False

# -------------- Drags --------------
# Rebote
esta_en_drag_rebote = False     # Esto es para saber si esta el usuario cambiando esta valor
x_drag_rebote = 81             # Al principio esta al 45 %

# Se refiera a las coordenadas minimas y máximas que puede ir el cuardado del input que se desliza
min_drag_rebote = 20
max_drag_rebote = 200

# Friccion
esta_en_drag_friccion = False  # Esto es para saber si esta el usuario cambiando esta valor
x_drag_friccion = 130         # Al principio esta al 63 %

# Se refiera a las coordenadas minimas y máximas que puede ir el cuardado del input que se desliza
min_drag_friccion = 20
max_drag_friccion = 200


def print_texto(data, title, font, x, y, window, color=DATA_FONT_COLOR):
    """
        Esta función me ayuda a no tener que repetir este código cada vez que quiero poner
        texto en pantalla
    """
    label = font.render("{} {}".format(title, data), 1, color)
    window.blit(label, (x, y))


def checar_limites():
    """
        Esta función me ayuda a que el cuadrado no se salga de los límites de la pantalla
    """
    global pos_y, velocidad_inicial_y, pos_x, primer_golpe, tiempo, delta_x

    # Checar límites de las posiciones
    if pos_y > (HEIGHT - ALTURA_PISO - LENGTH_SQUARE):
        pos_y = (HEIGHT - ALTURA_PISO - LENGTH_SQUARE)
        tiempo = 0
        velocidad_inicial_y = velocidad_inicial_y * rebote
        primer_golpe = True
    if pos_x >= WIDTH:
        pos_x = WIDTH - LENGTH_SQUARE
        delta_x = 0
    if pos_x < 0:
        pos_x = 0
        delta_x = 0


def disparar(window):
    """
        Esta función es la que se ancarga de mover al cuadrado cuando se dispara
        Primero cambia las posiciones, checa los límites, y dibuja el cuadrado rojo
        que muestra donde disparamos
    """
    global velocidad_inicial_y, tiempo, pos_x, delta_x, primer_golpe, delta_x, pos_y

    # Calcular posiciones
    pos_y = (HEIGHT - ALTURA_PISO - LENGTH_SQUARE) - (velocidad_inicial_y * tiempo + GRAVEDAD * tiempo ** 2 / 2)
    pos_x += delta_x

    # Modificar variantes
    if primer_golpe:
        if -0.03 < delta_x < 0.03:
            delta_x = 0
        else:
            if delta_x > 0:
                delta_x = delta_x - friccion
            else:
                delta_x = delta_x + friccion
    tiempo += delta_tiempo

    # Checar limites
    checar_limites()

    # Dibujar target
    pygame.draw.rect(window, COLOR_TARGET, (x_mouse_punto, HEIGHT - y_mouse, LENGTH_TARGET, LENGTH_TARGET))


def actualizar_reloj():
    """
        Esta función sirve para cambiar el tiempo que se muestra en el reloj con cada iteración
    """
    global game_time

    # Clock
    dt = clock.tick(FPS)
    game_time += dt
    return dt


def dibujar_piso(window):
    """
        Esta función sirve para dibujar el piso de la simulación
    """
    pygame.draw.rect(window, COLOR_PISO, (0, HEIGHT - ALTURA_PISO, WIDTH, ALTURA_PISO))


def dibujar_ventana(window, FONT, dt):
    """
        Esta función sirve para dibujar lo esencial en la ventana, como
        ponerle color al window
    """
    # LLenar la ventana con el color "COLOR_WINDOW" desde las coordenadas (0, 0) hasta (WIDTH, HEIGHT)
    window.fill(COLOR_WINDOW, (0, 0, WIDTH, HEIGHT))

    # Dibujar labels
    print_texto(game_time / 1000, "Tiempo: ", FONT, 20, 20, window)
    if round(1000 / dt, 2) < 400:
        # Esto es si los FPS estan algo bajos, para que se alerte que probablemente el programa este lento
        print_texto(round(1000 / dt, 2), "FPS: (bajo)...", FONT, 20, 50, window, COLOR_TARGET)
    else:
        # Esto es cuando los FPS estan normal
        print_texto(round(1000 / dt, 2), "FPS: ", FONT, 20, 50, window)


def dibujar_linea_guia(window):
    """
        Esta función sirve para dibujar el vector Fuerza
    """
    x_line, y_line = pygame.mouse.get_pos() # Agarra las posiciones en "x" y "y" del mouse

    # Dibuja una línea desde (x_line, y_line), hasta la posicion del cuadrado
    pygame.draw.line(window, COLOR_LINE, (x_line, y_line), (pos_x + LENGTH_SQUARE / 2, pos_y + LENGTH_SQUARE / 2))


def pre_disparo():
    global is_mouse_down, fire, pos_y, tiempo, primer_golpe, x_mouse_punto, y_mouse, x_mouse, velocidad_inicial_y, \
        velocidad_inicial_x, tiempo_a_altura_y_mouse, GRAVEDAD, diff_x, delta_x
    """
        Esta funcion se encarga a preparar todas las variables antes de disprar.
        Las reinicia.
    """
    # Reiniciar variables
    is_mouse_down = False
    fire = True
    pos_y = HEIGHT - ALTURA_PISO - LENGTH_SQUARE
    tiempo = 0
    primer_golpe = False
    x_mouse, y_mouse = pygame.mouse.get_pos()
    x_mouse_punto = x_mouse
    y_mouse = HEIGHT - y_mouse
    x_mouse = x_mouse - pos_x

    velocidad_inicial_y = y_mouse / sensibilidad
    velocidad_inicial_x = x_mouse / sensibilidad

    tiempo_a_altura_y_mouse = (-velocidad_inicial_y + (abs(
        velocidad_inicial_y ** 2 + 2 * GRAVEDAD * velocidad_inicial_y)) ** .5) \
                          / GRAVEDAD
    diff_x = int(tiempo_a_altura_y_mouse / delta_tiempo)
    if diff_x == 0:
        # Por si se divide por 0
        diff_x += .0001
    delta_x = velocidad_inicial_x / diff_x


def mover_rectangulo_rebote():
    """
        Esta funcion se encarga de mover el input que cambia el rebote del cuadrado
    """
    global x_drag_rebote, rebote
    x, _ = pygame.mouse.get_pos()
    if x < min_drag_rebote:
        # por si el mouse del usuario esta muy a la izquierda, para que no lo mueva
        x = min_drag_rebote
    if x > max_drag_rebote:
        # por si el mouse del usuario esta muy a la derecha, para que no lo mueva
        x = max_drag_rebote
    x_drag_rebote = x
    rebote = round((x_drag_rebote - min_drag_rebote) / (max_drag_rebote - min_drag_rebote), 2)


def dibujar_drag_rebote(window, FONT):
    """
        Esta funcion ayuda a dibujar el label que esta arriba del input y el input para saber el valor del rebote
    """
    # Dibuja el texto
    print_texto(rebote, "Rebote: ", FONT, 20, 100, window)

    # Dibuja el input
    pygame.draw.rect(window, COLOR_DRAGS, (20, 130 + LENGTH_SQUARE / 2 - 1, max_drag_rebote - min_drag_rebote, 2))
    return pygame.draw.rect(window, COLOR_DRAGS, (x_drag_rebote, 130, LENGTH_SQUARE / 2, LENGTH_SQUARE))


def mover_rectangulo_friccion():
    """
        Esta funcion se encarga de mover el input que cambia la friccion del cuadrado
    """
    global x_drag_friccion, friccion
    x, _ = pygame.mouse.get_pos()
    if x < min_drag_friccion:
        # por si el mouse del usuario esta muy a la izquierda, para que no lo mueva
        x = min_drag_friccion
    if x > max_drag_friccion:
        # por si el mouse del usuario esta muy a la derecha, para que no lo mueva
        x = max_drag_friccion
    x_drag_friccion = x
    friccion = round(((x_drag_friccion - min_drag_friccion) / (max_drag_friccion - min_drag_friccion)) * 0.02, 6)


def dibujar_drag_friccion(window, FONT):
    """
        Esta funcion ayuda a dibujar el label que esta arriba del input y el input para saber el valor de la friccion
    """
    # Dibuja el texto
    print_texto(round(friccion / 0.02, 2), "Fricción: ", FONT, 20, 160, window)

    # Dibuja el input
    pygame.draw.rect(window, COLOR_DRAGS, (20, 190 + LENGTH_SQUARE / 2 - 1, max_drag_friccion - min_drag_friccion, 2))
    return pygame.draw.rect(window, COLOR_DRAGS, (x_drag_friccion, 190, LENGTH_SQUARE / 2, LENGTH_SQUARE))


def simulacion(window, ventana):
    global game_time, fire, pos_x, delta_x, velocidad_inicial_y, tiempo, friccion, primer_golpe, x_mouse, x_mouse_punto, \
        y_mouse, is_mouse_down, pos_y, esta_en_drag_rebote, esta_en_drag_friccion

    """
        Esta es la funcion principal, se ocupa de iniciar todo y llamar a las funciones correspondientes cuando
        sea necesario
    """
    FONT = pygame.font.SysFont("monospace", 16)         # Creo unos fonts

    # Actualizar Reloj
    dt = actualizar_reloj()

    # Dibujar ventana y labels
    dibujar_ventana(window, FONT, dt)

    if fire:
        # Disparar
        disparar(window)

    # Dibujar rectángulo
    pygame.draw.rect(window, COLOR_SQUARE, (pos_x, pos_y, LENGTH_SQUARE, LENGTH_SQUARE))

    # Dibujar drag rebote
    dragReboteRectangulo = dibujar_drag_rebote(window, FONT)

    # Dibujar drag fricción
    dragFriccionRectangulo = dibujar_drag_friccion(window, FONT)

    # Checar drags
    if esta_en_drag_rebote:
        # El usuario esta moviendo el input rebote
        mover_rectangulo_rebote()
    if esta_en_drag_friccion:
        # El usuario esta moviendo el input friccion
        mover_rectangulo_friccion()

    # Dibujar linea guia o vector fuerza
    if is_mouse_down:
        dibujar_linea_guia(window)

    # Dibujar Piso
    dibujar_piso(window)
    
    """
        Funcionalidad para guardar los datos en un archivo csv
    """
    # se guarda la referencia del botón para poder saber si se le da click
    boton_grabar_datos = dibujar_boton_grabar_datos(window, ventana)
    
    if not (not fire or velocidad_inicial_y < 1):
        # Checa que el cubito no este quieto, ya que solo se guardarían muchos datos iguales
        grabar((pos_x, HEIGHT - pos_y), ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            """
                Esto se pone por si el usuario da click en cerrar la pestaña
                Entonces se cierra la ventana y se cierra pygame
            """
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:        # Cuando el usuario de click en la ventana en general
            if event.button == 1:                       # Y si ese click es click izquierdo...
                if dragReboteRectangulo.collidepoint(event.pos):        # Se checa si el click fue al input rebote
                    esta_en_drag_rebote = True
                elif dragFriccionRectangulo.collidepoint(event.pos):    # Se checa si el click fue al input friccion
                    esta_en_drag_friccion = True
                elif boton_grabar_datos.collidepoint(event.pos):
                    # Se cambia el evento de grabar
                    ventana.esta_grabando = not ventana.esta_grabando
                    
                    # Si se apagó el evento, entonces se tienen que guardar los valores obtenidos
                    if not ventana.esta_grabando:
                        grabar((pos_x, HEIGHT - pos_y), ventana)
                elif (not fire or velocidad_inicial_y < 1):
                    # Se checa si puede ya dibujar el vector
                    # Se espera a que el cuadrado no este todavia rebotando y que el fire sea Falso
                    # Evento del mouse para dibujar linea guia
                    is_mouse_down = True

        if event.type == pygame.MOUSEBUTTONUP:          # Cuando el usuario quita el click en la ventana en general
            # Entonces ya no esta moviendo los inputs
            esta_en_drag_rebote = False
            esta_en_drag_friccion = False
            if is_mouse_down:  # Y si antes se habia dibujado la linea guia... entonces quiere disparar
                # Evento del mouse para disparar
                pre_disparo()
