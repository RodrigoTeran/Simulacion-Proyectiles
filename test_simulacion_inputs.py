from constantes import *


def mover_rectangulo_friccion():
    """
        Con este test vamos a ver si esta funcion me va a editar la friccion
        con un valor desde 0 a 0.02 inclusivamente
    """
    # En vex de valores random...
    # x, y = 320, 34
    # Vamos a usar muuuchos...

    min_drag_friccion = 20
    max_drag_friccion = 200
    for y in range(HEIGHT + 1):
        for x in range(WIDTH + 1):
            if x < min_drag_friccion:
                # por si el mouse del usuario esta muy a la izquierda, para que no lo mueva
                x = min_drag_friccion
            if x > max_drag_friccion:
                # por si el mouse del usuario esta muy a la derecha, para que no lo mueva
                x = max_drag_friccion
            xDragFriccion = x
            friccion = round(((xDragFriccion - min_drag_friccion) / (max_drag_friccion - min_drag_friccion)) * 0.02, 6)
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

    min_drag_rebote = 20
    max_drag_rebote = 200

    for y in range(HEIGHT + 1):
        for x in range(WIDTH + 1):
            if x < min_drag_rebote:
                # por si el mouse del usuario esta muy a la izquierda, para que no lo mueva
                x = min_drag_rebote
            if x > max_drag_rebote:
                # por si el mouse del usuario esta muy a la derecha, para que no lo mueva
                x = max_drag_rebote
            xDragRebote = x
            rebote = round((xDragRebote - min_drag_rebote) / (max_drag_rebote - min_drag_rebote), 2)
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
