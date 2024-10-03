t0 = 0
y0 = np.array([...])  # Estado inicial
O = np.array([...])   # Matriz O

f = dyn_generator(O)
y = rk4(f, t0, y0, h, n_steps)

