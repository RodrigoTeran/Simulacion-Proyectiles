import math, sys, pygame
from constantes import *

clock = pygame.time.Clock()
gameTime = 0

# Constantes
GRAVEDAD = -9.81
xMouse = 600
xMousePunto = 600
yMouse = 600
sensibilidad = 6
alturaPiso = 50

# Variables que el usuario puede cambiar
rebote = 0.45  # 0 a 1
friccion = 0.005  # 0 a  0.02

# Variables del programa
velocidadInicialY = yMouse / sensibilidad
velocidadInicialX = xMouse / sensibilidad

deltaTiempo = 0.03
tiempo = 0

posX = WIDTH / 2 - LENGTH_SQUARE / 2
posY = HEIGHT - alturaPiso - LENGTH_SQUARE

tiempoAAlturaYMouse = (-velocidadInicialY + math.sqrt(velocidadInicialY ** 2 + 2 * GRAVEDAD * velocidadInicialY)) \
                      / (GRAVEDAD)
diffX = int(tiempoAAlturaYMouse / deltaTiempo)
deltaX = velocidadInicialX / diffX

primerGolpe = False
fire = False
isMouseDown = False

# -- Drags
# Rebote
estaEnDragRebote = False
xDragRebote = 81  # 45 %
minDragRebote = 20
maxDragRebote = 200

# Friccion
estaEnDragFriccion = False
xDragFriccion = 65  # 25 %
minDragFriccion = 20
maxDragFriccion = 200


def printTexto(data, title, font, x, y, window):
    label = font.render("{} {}".format(title, data), 1, DATA_FONT_COLOR)
    window.blit(label, (x, y))


def checarLimites():
    global posY, velocidadInicialY, posX, primerGolpe, tiempo, deltaX

    # Checar límites de las posiciones
    if posY > (HEIGHT - alturaPiso - LENGTH_SQUARE):
        posY = (HEIGHT - alturaPiso - LENGTH_SQUARE)
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
    global velocidadInicialY, tiempo, posX, deltaX, primerGolpe, deltaX, posY

    # Calcular posiciones
    posY = (HEIGHT - alturaPiso - LENGTH_SQUARE) - (velocidadInicialY * tiempo + GRAVEDAD * tiempo ** 2 / 2)
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
    global gameTime

    # Clock
    dt = clock.tick(FPS)
    gameTime += dt
    return dt


def dibujarPiso(window):
    pygame.draw.rect(window, COLOR_PISO, (0, HEIGHT - alturaPiso, WIDTH, alturaPiso))


def dibujarVentana(window, FONT, dt):
    # Dibujar background
    window.fill(COLOR_WINDOW, (0, 0, WIDTH, HEIGHT))

    # Dibujar labels
    printTexto(gameTime / 1000, "Tiempo de simulación: ", FONT, 20, 20, window)
    printTexto(round(1000 / dt, 2), "FPS: ", FONT, 20, 50, window)


def dibujarLineaGuia(window):
    xLine, yLine = pygame.mouse.get_pos()
    pygame.draw.line(window, COLOR_LINE, (xLine, yLine), (posX + LENGTH_SQUARE / 2, posY + LENGTH_SQUARE / 2))


def preDisparo():
    global isMouseDown, fire, posY, tiempo, primerGolpe, xMousePunto, yMouse, xMouse, velocidadInicialY, \
        velocidadInicialX, tiempoAAlturaYMouse, GRAVEDAD, diffX, deltaX

    # Reiniciar variables
    isMouseDown = False
    fire = True
    posY = HEIGHT - alturaPiso - LENGTH_SQUARE
    tiempo = 0
    primerGolpe = False
    xMouse, yMouse = pygame.mouse.get_pos()
    xMousePunto = xMouse
    yMouse = HEIGHT - yMouse
    xMouse = xMouse - posX

    velocidadInicialY = yMouse / sensibilidad
    velocidadInicialX = xMouse / sensibilidad

    tiempoAAlturaYMouse = (-velocidadInicialY + math.sqrt(abs(
        velocidadInicialY ** 2 + 2 * GRAVEDAD * velocidadInicialY))) \
                          / GRAVEDAD
    diffX = int(tiempoAAlturaYMouse / deltaTiempo)
    if diffX == 0:
        # Por si se divide por 0
        diffX += .0001
    deltaX = velocidadInicialX / diffX


def moverRectanguloRebote():
    global xDragRebote, rebote
    x, y = pygame.mouse.get_pos()
    if x < minDragRebote:
        x = minDragRebote
    if x > maxDragRebote:
        x = maxDragRebote
    xDragRebote = x
    rebote = round((xDragRebote - minDragRebote) / (maxDragRebote - minDragRebote), 2)


def dibujarDragRebote(window, FONT):
    # Label
    printTexto(rebote, "Rebote: ", FONT, 20, 100, window)

    # Drag
    pygame.draw.rect(window, COLOR_DRAGS, (20, 130 + LENGTH_SQUARE / 2 - 1, maxDragRebote - minDragRebote, 2))
    return pygame.draw.rect(window, COLOR_DRAGS, (xDragRebote, 130, LENGTH_SQUARE / 2, LENGTH_SQUARE))


def moverRectanguloFriccion():
    global xDragFriccion, friccion
    x, y = pygame.mouse.get_pos()
    if x < minDragFriccion:
        x = minDragFriccion
    if x > maxDragFriccion:
        x = maxDragFriccion
    xDragFriccion = x
    friccion = round(((xDragFriccion - minDragFriccion) / (maxDragFriccion - minDragFriccion)) * 0.02, 6)


def dibujarDragFriccion(window, FONT):
    # Label
    printTexto(round(friccion / 0.02, 2), "Fricción: ", FONT, 20, 160, window)

    # Drag
    pygame.draw.rect(window, COLOR_DRAGS, (20, 190 + LENGTH_SQUARE / 2 - 1, maxDragFriccion - minDragFriccion, 2))
    return pygame.draw.rect(window, COLOR_DRAGS, (xDragFriccion, 190, LENGTH_SQUARE / 2, LENGTH_SQUARE))


def simulacion(window, FONT):
    global gameTime, fire, posX, deltaX, velocidadInicialY, tiempo, friccion, primerGolpe, xMouse, xMousePunto, \
        yMouse, isMouseDown, posY, estaEnDragRebote, estaEnDragFriccion

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
        moverRectanguloRebote()
    if estaEnDragFriccion:
        moverRectanguloFriccion()

    # Dibujar linea guia
    if isMouseDown:
        dibujarLineaGuia(window)

    # Dibujar Piso
    dibujarPiso(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if dragReboteRectangulo.collidepoint(event.pos):
                    estaEnDragRebote = True
                elif dragFriccionRectangulo.collidepoint(event.pos):
                    estaEnDragFriccion = True
                elif not fire or velocidadInicialY < 1:
                    # Evento del mouse para dibujar linea guia
                    isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            estaEnDragRebote = False
            estaEnDragFriccion = False
            if isMouseDown:
                # Evento del mouse para disparar
                preDisparo()
