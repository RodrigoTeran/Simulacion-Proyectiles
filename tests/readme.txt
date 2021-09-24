Algunas funciones no se les va a poder aplicar tests ya que no usan variables que cambien mucho
con la simulación
Por ejemplo:
    - la función: actualizarReloj()
        solo actualiza el valor del reloj...
    - la función: printTexto()
        solo pone texto en la ventana... sabría solo viendo la ventana si algo no funciona

Las funciones que sí se probaron son:
    - checarLimites()
        ya que como a cada instante el cuadrado se esta moviendo por la ventana se necesita checar
        que no se vaya por los costados y que el usuario siempre pueda mover el cuadrado
    - moverRectanguloRebote()
        esta función es importante ya que es una de las funciones que interactuan con los movimientos
        del usuario. Se necesita que no importa que haga el usuario, los valores que arroje sean los
        correctos
    - moverRectanguloFriccion()
        al igual que "moverRectanguloRebote()", esta función e simportante, pero aún más se necesita
        checar ya que sus valores van del 0 al 0.02
        No pueden salirse de ese límite tan especial
    - disparar()
        si no funciona esta función, el programa no serviría :)
        Por eso es importante que las nuevas posiciones que arroje esta función sean coherentes.
        - Se checa que si el movimiento es para delante, la x no sea negativa.
        - Se checa que la altura máxima posible sí sea alcanzada.