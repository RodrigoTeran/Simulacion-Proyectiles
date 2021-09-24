from constantes import *


def checarLimites():
    """
        Con este test vamos a ver si si checa bien los límites
    """

    # Para simular que va desde 0 a 1 con valores decimales
    for posY in range(HEIGHT + 1):
        for posX in range(WIDTH + 1):
            # Checar límites de las posiciones
            if posY > (HEIGHT - ALTURA_PISO - LENGTH_SQUARE):
                posY = (HEIGHT - ALTURA_PISO - LENGTH_SQUARE)
            if posX >= WIDTH:
                posX = WIDTH - LENGTH_SQUARE
            if posX < 0:
                posX = 0

            # Checar que al final las posiciones no esten con valores que no deberian
            if posX < 0 or posX > WIDTH or posY > (HEIGHT - ALTURA_PISO - LENGTH_SQUARE):
                print("Error con:", posX, posY)
                break
        else:
            continue
        break
    else:
        print("Todo bien con checarLimites()")
        return


if __name__ == "__main__":
    print("Tests:\n")
    checarLimites()  # Esta funcion pasa correctamente
