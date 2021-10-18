from constantes import *


def disparar():
    """
        Con este test vamos a ver si:
            - Se checa que si el movimiento es para delante, la x no sea negativa.
            - Se checa que la altura máxima posible sí sea alcanzada.
    """
    GRAVEDAD = -9.81
    tiempo = 0.1
    posX = 0
    posY = HEIGHT
    deltaTiempo = 0.04
    sensibilidad = 6
    alturaMaximaCorrecta = False

    # Movimiento hacia la derecha
    for yMouse in range(HEIGHT - ALTURA_PISO, -1, -1):
        velocidadInicialY = yMouse / sensibilidad
        tiempoAAlturaYMouse = (-velocidadInicialY + (abs(
            velocidadInicialY ** 2 + 2 * GRAVEDAD * velocidadInicialY)) ** .5) \
                              / GRAVEDAD
        diffX = int(tiempoAAlturaYMouse / deltaTiempo)

        maximaAltura = (-(velocidadInicialY ** 2)) / (2 * GRAVEDAD)

        for xMouse in range(WIDTH + 1):
            velocidadInicialX = xMouse / sensibilidad
            if diffX == 0:
                # Por si se divide por 0
                diffX += .0001
            deltaX = velocidadInicialX / diffX

            # Calcular si sí alcanzó la altura máxima posible
            if (HEIGHT - ALTURA_PISO - LENGTH_SQUARE) - (
                    velocidadInicialY * tiempo + GRAVEDAD * tiempo ** 2 / 2) > posY:
                if abs(abs(posY) - (HEIGHT - ALTURA_PISO - LENGTH_SQUARE) == maximaAltura) < 10:
                    alturaMaximaCorrecta = True
            else:
                posY = (HEIGHT - ALTURA_PISO - LENGTH_SQUARE) - (
                        velocidadInicialY * tiempo + GRAVEDAD * tiempo ** 2 / 2)
                posX += deltaX
                tiempo += deltaTiempo

                # Checar que la posición nunca sea menor que 0, ya que este movimiento es para delante
                if posX < 0:
                    print("Error con posX:", posX)
                    break
        else:
            continue
        break
    else:
        if alturaMaximaCorrecta:
            print("Todo bien con disparar()")
        else:
            print("Altura máxima no alcanzada")
        return


if __name__ == '__main__':
    print("Tests:\n")
    disparar()  # Esta funcion pasa correctamente
