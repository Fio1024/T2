# Método RK4 (Runge-Kutta de Cuarto Orden)

El método Runge-Kutta de cuarto orden (RK4) es un método numérico para resolver ecuaciones diferenciales ordinarias de la forma:
\[
\frac{dy}{dt} = f(t, y)
\]

El algoritmo del método RK4 consiste en calcular cuatro "pendientes" \( k_1 \), \( k_2 \), \( k_3 \), y \( k_4 \) en cada paso, que se combinan para obtener una estimación más precisa de \( y \) en el siguiente paso.

Los coeficientes se calculan como:
\[
k_1 = f(t_n, y_n)
\]
\[
k_2 = f(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_1)
\]
\[
k_3 = f(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_2)
\]
\[
k_4 = f(t_n + h, y_n + hk_3)
\]

Luego, la actualización de \( y \) se da por:
\[
y_{n+1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)
\]

