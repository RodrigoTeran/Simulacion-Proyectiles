from constantes import *


def mover_rectangulo_friccion():
    """
        Con este test vamos a ver si esta funcion me va a editar la friccion
        con un valor desde 0 a 0.02 inclusivamente
    """
    # En vex de valores random...
    # x, y = 320, 34
    # Vamos a usar muuuchos...

    minDragFriccion = 20
    maxDragFriccion = 200
    for y in range(HEIGHT + 1):
        for x in range(WIDTH + 1):
            if x < minDragFriccion:
                # por si el mouse del usuario esta muy a la izquierda, para que no lo mueva
                x = minDragFriccion
            if x > maxDragFriccion:
                # por si el mouse del usuario esta muy a la derecha, para que no lo mueva
                x = maxDragFriccion
            xDragFriccion = x
            friccion = round(((xDragFriccion - minDragFriccion) / (maxDragFriccion - minDragFriccion)) * 0.02, 6)
            if friccion < 0 or friccion > 0.02:
                # Esto significa que no paso la prueba
                print("Error con: ", y, x)
                break
        else:
            continue
        break
    else:
        print("Todo bien con mover_rectangulo_friccion()")
        return


def mover_rectangulo_rebote():
    """
        Con este test vamos a ver si esta funcion me va a editar el rebote
        con un valor desde 0 a 1 inclusivamente
    """
    # En vex de valores random...
    # x, y = 320, 34
    # Vamos a usar muuuchos...

    minDragRebote = 20
    maxDragRebote = 200

    for y in range(HEIGHT + 1):
        for x in range(WIDTH + 1):
            if x < minDragRebote:
                # por si el mouse del usuario esta muy a la izquierda, para que no lo mueva
                x = minDragRebote
            if x > maxDragRebote:
                # por si el mouse del usuario esta muy a la derecha, para que no lo mueva
                x = maxDragRebote
            xDragRebote = x
            rebote = round((xDragRebote - minDragRebote) / (maxDragRebote - minDragRebote), 2)
            if rebote < 0 or rebote > 1:
                # Esto significa que no paso la prueba
                print("Error con: ", y, x)
                break
        else:
            continue
        break
    else:
        print("Todo bien con mover_rectangulo_rebote()")
        return


if __name__ == "__main__":
    print("Tests:\n")
    mover_rectangulo_friccion()  # Esta funcion pasa correctamente
    mover_rectangulo_rebote()    # Esta funcion pasa correctamente
