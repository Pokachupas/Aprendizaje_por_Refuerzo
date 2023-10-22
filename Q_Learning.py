import random

# Definición de estados, acciones y recompensas ficticias
estados = ["Caballo A en primer lugar", "Caballo B en primer lugar"]
acciones = ["Apuesta por Caballo A", "Apuesta por Caballo B"]
recompensas = {
    ("Caballo A en primer lugar", "Apuesta por Caballo A"): 10,
    ("Caballo A en primer lugar", "Apuesta por Caballo B"): -5,
    ("Caballo B en primer lugar", "Apuesta por Caballo A"): -5,
    ("Caballo B en primer lugar", "Apuesta por Caballo B"): 15,
}

# Inicialización de la tabla Q con valores ficticios
tabla_q = {estado: {accion: 0 for accion in acciones} for estado in estados}

# Parámetros de aprendizaje
factor_aprendizaje = 0.1  # Tasa de aprendizaje
factor_descuento = 0.9   # Factor de descuento (importancia de las recompensas futuras)
epsilon = 0.2            # Probabilidad de exploración

# Función para seleccionar una acción con base en la estrategia epsilon-greedy
def seleccionar_accion(estado):
    if random.uniform(0, 1) < epsilon:
        return random.choice(acciones)  # Exploración aleatoria
    else:
        return max(tabla_q[estado], key=tabla_q[estado].get)  # Explotación de la mejor acción

# Simulación de episodios de apuestas
num_episodios = 1000
for _ in range(num_episodios):
    estado = random.choice(estados)  # Estado inicial aleatorio
    for _ in range(10):  # 10 pasos de tiempo en cada episodio
        accion = seleccionar_accion(estado)
        recompensa = recompensas.get((estado, accion), 0)
        siguiente_estado = random.choice(estados)  # Estado siguiente aleatorio

        # Actualización de la tabla Q usando la fórmula de Q-Learning
        tabla_q[estado][accion] += factor_aprendizaje * (recompensa + factor_descuento * max(tabla_q[siguiente_estado].values()) - tabla_q[estado][accion])

        estado = siguiente_estado

# Uso del modelo Q-Learning para tomar decisiones
estado_actual = "Caballo B en primer lugar"
accion_optima = max(tabla_q[estado_actual], key=tabla_q[estado_actual].get)
print(f"Estado actual: {estado_actual}")
print(f"Acción óptima: {accion_optima}")