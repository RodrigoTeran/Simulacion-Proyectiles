"""
    Readme:
        No se usa ninguna librería para hacer los cálculos...
        lo único que se utiliza es pygame pero para mostrar los gráficos...
        todas las operaciones con la fricción, rebote, gravedad, tiro parabólico, fuerzas, etc
        se hacen con puros ciclos, comparaciones, etc...
"""
import sys
import pygame
from constantes import *

clock = pygame.time.Clock()         # Se inicializa un reloj para medir el tiempo de juego
gameTime = 0                        # El total se pone primero en 0

# -------------- Constantes --------------
GRAVEDAD = -9.81

# Posicion en x del mouse con respecto al cuadrado negro, al principio no importa
# que valor ponga, cuando el usuario empiece a mover su mouse se va a editar este valor
xMouse = 600

# Posicion en x del mouse con respecto a la ventana en general
xMousePunto = 600

# Posicion en y del mouse con respecto al cuadrado negro
yMouse = 600

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
velocidadInicialY = yMouse / sensibilidad
velocidadInicialX = xMouse / sensibilidad

# El delta del tiempo nos da la posibilidad de qué tan rápido pasa el tiempo en la simulación
# Si aumentamos este valor el cubito va a ir muy rápido, pero si lo disminuimos va a ir muy lento
deltaTiempo = 0.04
tiempo = 0

# Posiciones en "x" y "y" del cubito que salta
posX = WIDTH / 2 - LENGTH_SQUARE / 2        # Posicion inicial: WIDTH / 2 - LENGTH_SQUARE / 2
posY = HEIGHT - ALTURA_PISO - LENGTH_SQUARE  # Posicion inicial: HEIGHT - alturaPiso - LENGTH_SQUARE


# -------------- Ecuaciones física --------------
# El "tiempoAAlturaYMouse" se refiere al tiempo ocupado en esta fórmula de la física para posteriormente conocer en qué
# posicion debería estar el cubo en x
tiempoAAlturaYMouse = (-velocidadInicialY + (abs(
        velocidadInicialY ** 2 + 2 * GRAVEDAD * velocidadInicialY)) ** .5) \
                          / GRAVEDAD

# Con "tiempoAAlturaYMouse" calculamos la nueva posición de x
diffX = int(tiempoAAlturaYMouse / deltaTiempo)

# Ahora ya sabemos cuanto moverlo, sería el deltaX
if diffX == 0:
    # Por si se divide por 0
    diffX += .0001
deltaX = velocidadInicialX / diffX

# -------------- Valores booleanos --------------
# Estos me dan información de si o no del programa

# primerGolpe se refiere a si el bloque ya tocó el piso, para empezar a restar en x con la fricción
primerGolpe = False

# Se refiere a si ya debemos disprara o no
fire = False

# Como el nombre lo dice, si el mouse esta abajo, para saber si dibujamos el vector fuerza o no
isMouseDown = False

# -------------- Drags --------------
# Rebote
estaEnDragRebote = False     # Esto es para saber si esta el usuario cambiando esta valor
xDragRebote = 81             # Al principio esta al 45 %

# Se refiera a las coordenadas minimas y máximas que puede ir el cuardado del input que se desliza
minDragRebote = 20
maxDragRebote = 200

# Friccion
estaEnDragFriccion = False  # Esto es para saber si esta el usuario cambiando esta valor
xDragFriccion = 130         # Al principio esta al 63 %

# Se refiera a las coordenadas minimas y máximas que puede ir el cuardado del input que se desliza
minDragFriccion = 20
maxDragFriccion = 200


def printTexto(data, title, font, x, y, window, color=DATA_FONT_COLOR):
    """
        Esta función me ayuda a no tener que repetir este código cada vez que quiero poner
        texto en pantalla
    """
    label = font.render("{} {}".format(title, data), 1, color)
    window.blit(label, (x, y))


def checarLimites():
    """
        Esta función me ayuda a que el cuadrado no se salga de los límites de la pantalla
    """
    global posY, velocidadInicialY, posX, primerGolpe, tiempo, deltaX

    # Checar límites de las posiciones
    if posY > (HEIGHT - ALTURA_PISO - LENGTH_SQUARE):
        posY = (HEIGHT - ALTURA_PISO - LENGTH_SQUARE)
        tiempo = 0
        velocidadInicialY = velocidadInicialY * rebote
        primerGolpe = True
    if posX >= WIDTH:
        posX = WIDTH - LENGTH_SQUARE
        deltaX = 0
    if posX < 0:
        posX = 0
        deltaX = 0


def disparar(window):
    """
        Esta función es la que se ancarga de mover al cuadrado cuando se dispara
        Primero cambia las posiciones, checa los límites, y dibuja el cuadrado rojo
        que muestra donde disparamos
    """
    global velocidadInicialY, tiempo, posX, deltaX, primerGolpe, deltaX, posY

    # Calcular posiciones
    posY = (HEIGHT - ALTURA_PISO - LENGTH_SQUARE) - (velocidadInicialY * tiempo + GRAVEDAD * tiempo ** 2 / 2)
    posX += deltaX

    # Modificar variantes
    if primerGolpe:
        if -0.03 < deltaX < 0.03:
            deltaX = 0
        else:
            if deltaX > 0:
                deltaX = deltaX - friccion
            else:
                deltaX = deltaX + friccion
    tiempo += deltaTiempo

    # Checar limites
    checarLimites()

    # Dibujar target
    pygame.draw.rect(window, COLOR_TARGET, (xMousePunto, HEIGHT - yMouse, LENGTH_TARGET, LENGTH_TARGET))


def actualizarReloj():
    """
        Esta función sirve para cambiar el tiempo que se muestra en el reloj con cada iteración
    """
    global gameTime

    # Clock
    dt = clock.tick(FPS)
    gameTime += dt
    return dt


def dibujarPiso(window):
    """
        Esta función sirve para dibujar el piso de la simulación
    """
    pygame.draw.rect(window, COLOR_PISO, (0, HEIGHT - ALTURA_PISO, WIDTH, ALTURA_PISO))


def dibujarVentana(window, FONT, dt):
    """
        Esta función sirve para dibujar lo esencial en la ventana, como
        ponerle color al window
    """
    # LLenar la ventana con el color "COLOR_WINDOW" desde las coordenadas (0, 0) hasta (WIDTH, HEIGHT)
    window.fill(COLOR_WINDOW, (0, 0, WIDTH, HEIGHT))

    # Dibujar labels
    printTexto(gameTime / 1000, "Tiempo: ", FONT, 20, 20, window)
    if round(1000 / dt, 2) < 400:
        # Esto es si los FPS estan algo bajos, para que se alerte que probablemente el programa este lento
        printTexto(round(1000 / dt, 2), "FPS: (bajo)...", FONT, 20, 50, window, COLOR_TARGET)
    else:
        # Esto es cuando los FPS estan normal
        printTexto(round(1000 / dt, 2), "FPS: ", FONT, 20, 50, window)


def dibujarLineaGuia(window):
    """
        Esta función sirve para dibujar el vector Fuerza
    """
    xLine, yLine = pygame.mouse.get_pos() # Agarra las posiciones en "x" y "y" del mouse

    # Dibuja una línea desde (xLine, yLine), hasta la posicion del cuadrado
    pygame.draw.line(window, COLOR_LINE, (xLine, yLine), (posX + LENGTH_SQUARE / 2, posY + LENGTH_SQUARE / 2))


def preDisparo():
    global isMouseDown, fire, posY, tiempo, primerGolpe, xMousePunto, yMouse, xMouse, velocidadInicialY, \
        velocidadInicialX, tiempoAAlturaYMouse, GRAVEDAD, diffX, deltaX
    """
        Esta funcion se encarga a preparar todas las variables antes de disprar.
        Las reinicia.
    """
    # Reiniciar variables
    isMouseDown = False
    fire = True
    posY = HEIGHT - ALTURA_PISO - LENGTH_SQUARE
    tiempo = 0
    primerGolpe = False
    xMouse, yMouse = pygame.mouse.get_pos()
    xMousePunto = xMouse
    yMouse = HEIGHT - yMouse
    xMouse = xMouse - posX

    velocidadInicialY = yMouse / sensibilidad
    velocidadInicialX = xMouse / sensibilidad

    tiempoAAlturaYMouse = (-velocidadInicialY + (abs(
        velocidadInicialY ** 2 + 2 * GRAVEDAD * velocidadInicialY)) ** .5) \
                          / GRAVEDAD
    diffX = int(tiempoAAlturaYMouse / deltaTiempo)
    if diffX == 0:
        # Por si se divide por 0
        diffX += .0001
    deltaX = velocidadInicialX / diffX


def moverRectanguloRebote():
    """
        Esta funcion se encarga de mover el input que cambia el rebote del cuadrado
    """
    global xDragRebote, rebote
    x, y = pygame.mouse.get_pos()
    if x < minDragRebote:
        # por si el mouse del usuario esta muy a la izquierda, para que no lo mueva
        x = minDragRebote
    if x > maxDragRebote:
        # por si el mouse del usuario esta muy a la derecha, para que no lo mueva
        x = maxDragRebote
    xDragRebote = x
    rebote = round((xDragRebote - minDragRebote) / (maxDragRebote - minDragRebote), 2)


def dibujarDragRebote(window, FONT):
    """
        Esta funcion ayuda a dibujar el label que esta arriba del input y el input para saber el valor del rebote
    """
    # Dibuja el texto
    printTexto(rebote, "Rebote: ", FONT, 20, 100, window)

    # Dibuja el input
    pygame.draw.rect(window, COLOR_DRAGS, (20, 130 + LENGTH_SQUARE / 2 - 1, maxDragRebote - minDragRebote, 2))
    return pygame.draw.rect(window, COLOR_DRAGS, (xDragRebote, 130, LENGTH_SQUARE / 2, LENGTH_SQUARE))


def moverRectanguloFriccion():
    """
        Esta funcion se encarga de mover el input que cambia la friccion del cuadrado
    """
    global xDragFriccion, friccion
    x, y = pygame.mouse.get_pos()
    if x < minDragFriccion:
        # por si el mouse del usuario esta muy a la izquierda, para que no lo mueva
        x = minDragFriccion
    if x > maxDragFriccion:
        # por si el mouse del usuario esta muy a la derecha, para que no lo mueva
        x = maxDragFriccion
    xDragFriccion = x
    friccion = round(((xDragFriccion - minDragFriccion) / (maxDragFriccion - minDragFriccion)) * 0.02, 6)


def dibujarDragFriccion(window, FONT):
    """
        Esta funcion ayuda a dibujar el label que esta arriba del input y el input para saber el valor de la friccion
    """
    # Dibuja el texto
    printTexto(round(friccion / 0.02, 2), "Fricción: ", FONT, 20, 160, window)

    # Dibuja el input
    pygame.draw.rect(window, COLOR_DRAGS, (20, 190 + LENGTH_SQUARE / 2 - 1, maxDragFriccion - minDragFriccion, 2))
    return pygame.draw.rect(window, COLOR_DRAGS, (xDragFriccion, 190, LENGTH_SQUARE / 2, LENGTH_SQUARE))


def simulacion(window):
    global gameTime, fire, posX, deltaX, velocidadInicialY, tiempo, friccion, primerGolpe, xMouse, xMousePunto, \
        yMouse, isMouseDown, posY, estaEnDragRebote, estaEnDragFriccion

    """
        Esta es la funcion principal, se ocupa de iniciar todo y llamar a las funciones correspondientes cuando
        sea necesario
    """
    FONT = pygame.font.SysFont("monospace", 16)         # Creo unos fonts

    # Actualizar Reloj
    dt = actualizarReloj()

    # Dibujar ventana y labels
    dibujarVentana(window, FONT, dt)

    if fire:
        # Disparar
        disparar(window)

    # Dibujar rectángulo
    pygame.draw.rect(window, COLOR_SQUARE, (posX, posY, LENGTH_SQUARE, LENGTH_SQUARE))

    # Dibujar drag rebote
    dragReboteRectangulo = dibujarDragRebote(window, FONT)

    # Dibujar drag fricción
    dragFriccionRectangulo = dibujarDragFriccion(window, FONT)

    # Checar drags
    if estaEnDragRebote:
        # El usuario esta moviendo el input rebote
        moverRectanguloRebote()
    if estaEnDragFriccion:
        # El usuario esta moviendo el input friccion
        moverRectanguloFriccion()

    # Dibujar linea guia o vector fuerza
    if isMouseDown:
        dibujarLineaGuia(window)

    # Dibujar Piso
    dibujarPiso(window)

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
                    estaEnDragRebote = True
                elif dragFriccionRectangulo.collidepoint(event.pos):    # Se checa si el click fue al input friccion
                    estaEnDragFriccion = True
                elif not fire or velocidadInicialY < 1:                 # Se checa si puede ya dibujar el vector
                    # Se espera a que el cuadrado no este todavia rebotando y que el fire sea Falso
                    # Evento del mouse para dibujar linea guia
                    isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:          # Cuando el usuario quita el click en la ventana en general
            # Entonces ya no esta moviendo los inputs
            estaEnDragRebote = False
            estaEnDragFriccion = False
            if isMouseDown:  # Y si antes se habia dibujado la linea guia... entonces quiere disparar
                # Evento del mouse para disparar
                preDisparo()
