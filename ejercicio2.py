"""
Programa que calcula una aproximación de π utilizando la serie de Leibniz.

También calcula los errores absoluto, relativo y cuadrático comparando con el valor real de π.
"""

import numpy as np  # Para usar el valor real de π
import matplotlib.pyplot as plt  # Para generar gráficos

def leibniz_pi(n):
    """Calcula una aproximación de π usando la serie de Leibniz con n términos."""
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

# Valores de N a evaluar
N_values = [10, 100, 1000, 10000]
true_pi = np.pi  # Valor real de π
errors_abs = []
errors_rel = []
errors_cuad = []

# Calculamos la aproximación de π y los errores para cada N
for N in N_values:
    approx_pi = leibniz_pi(N)
    error_abs = abs(true_pi - approx_pi)
    error_rel = error_abs / true_pi
    error_cuad = error_abs ** 2

    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_cuad.append(error_cuad)

    print(f"N={N}: Aproximación= {approx_pi}, Error absoluto={error_abs}, Error relativo={error_rel}")

# Graficamos los errores en función de N
plt.figure()
plt.plot(N_values, errors_abs, label="Error absoluto", marker="o")
plt.plot(N_values, errors_rel, label="Error relativo", marker="s")
plt.xscale("log")  # Escala logarítmica en el eje X
plt.yscale("log")  # Escala logarítmica en el eje Y
plt.xlabel("Número de términos (N)")
plt.ylabel("Error")
plt.legend()
plt.title("Errores en la Aproximación de π usando la Serie de Leibniz")
plt.grid()
plt.show()
