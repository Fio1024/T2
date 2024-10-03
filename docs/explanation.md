# Explicación

El método Runge-Kutta de cuarto orden es una técnica numérica que se utiliza para aproximar soluciones de ecuaciones diferenciales de la forma:

$$
\frac{dy}{dt} = f(t, y(t))
$$

donde $f(t, y)$ describe cómo varía el sistema a lo largo del tiempo, y $y(t)$ representa el estado del sistema en el instante $t$, en el caso específico $f(t, \mathbf{y}) = −i[\mathbf{O}, \mathbf{y}(t)]$, donde no existe una dependencia explícita del tiempo en la función $f(t, \mathbf{y})$.


El método RK4 proporciona una estimación más precisa en cada paso temporal a través de cuatro sub-pasos intermedios ($k_1$, $k_2$, $k_3$, $k_4$), que se calculan de la siguiente manera:

$$
y_{n+1} = y_n + \frac{1}{6} \left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$

Donde:

$$
\begin{aligned}
k_1 &= h \cdot f(t_n, y_n) \\
k_2 &= h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right) \\
k_3 &= h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right) \\
k_4 &= h \cdot f\left(t_n + h, y_n + k_3\right) \\
\end{aligned}
$$
