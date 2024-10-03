# Tutorial de uso del método RK4

En este tutorial, demostraremos cómo utilizar las funciones implementadas para resolver una ecuación diferencial utilizando el método RK4.

## Paso 1: Definir la función dinámica

Primero, definimos la función dinámica \( f(t, y) = -i[O, y(t)] \), donde \( O \) es una matriz y \( y(t) \) es el estado en el tiempo \( t \).

```python
def dyn_generator(O):
    def f(t, y):
        return -1j * np.dot(O, y)
    return f

