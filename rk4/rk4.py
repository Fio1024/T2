#!/usr/bin/env python

import numpy as np

def dyn_generator(oper, state):
    """Esta función define la evolución temporal de un sistema basado en el operador `oper` el estado inicial `state`.

    Args:
        oper (np.array): Operador lineal
        state (np.array): Estado inicial

    Returns:
        (np.array): El estado resultante

    Examples:
        >>> import numpy as np
        >>> oper = np.array([[0, 1], [1, 0]])
        >>> state = np.array([[1, 0], [0, 0]])
        >>> dyn_generator(oper, state)
        [[0.-0.j 0.+1.j]
         [0.-1.j 0.-0.j]]
    """
    return -1j * (np.dot(oper, state) - np.dot(state, oper))

def rk4(func, oper, state, h):
    """Esta función aplica el método RK4 para calcular el siguiente estado del sistema, dado un generador dinámico, un operador y un estado inicial.

    Args:
        func (callable): Función que describe el sistema de ecuaciones diferenciales.
        oper (np.array): Operador utilizado por la función `func` para determinar la dinámica.
        state (np.array): El estado resultando.
        h (float): Incremento.

    Returns:
        (np.array): El estado calculado usando el método RK4.

    Examples:
        >>> import numpy as np
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.1)
        [[0.99003333+0.j         0.        +0.09933333j]
         [0.        -0.09933333j 0.00996667+0.j        ]]
    """
    k1 = h * func(oper, state)
    k2 = h * func(oper, state + k1 / 2)
    k3 = h * func(oper, state + k2 / 2)
    k4 = h * func(oper, state + k3)

    return state + (k1 + 2*k2 + 2*k3 + k4) / 6
