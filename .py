"""
Programa para calcular la precisión de máquina en punto flotante.

Este código encuentra el valor más pequeño (epsilon) que, al sumarse a 1.0, sigue siendo distinguible de 1.0 en la 
representación de punto flotante del sistema.
"""

epsilon = 1.0  # Inicializamos epsilon en 1.0
iteracion = 0  # Contador de iteraciones

# Reducimos epsilon dividiéndolo entre 2 hasta que 1.0 + epsilon ya no sea diferente de 1.0
while 1.0 + epsilon != 1.0:
    epsilon /= 2
    iteracion += 1
    print(f"Iteración {iteracion}: Precisión de máquina = {epsilon}")

# Volvemos al último valor válido de epsilon
epsilon *= 2
print(f"\nPrecisión de máquina final calculada: {epsilon}")
