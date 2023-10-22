import random

# Datos de temperatura diaria simulados
temperaturas = [random.randint(0, 100) for _ in range(30)] 

# Algoritmo de diferencia temporal para predecir la temperatura del día siguiente
def predecir_temperatura_siguiente_dia(datos):
    temperaturas_predichas = []  # Almacenar las temperaturas predichas
    alpha = 0.1  # Factor de aprendizaje (puede ajustarse)

    for dia, temperatura in enumerate(datos[:-1], 1):  # Excluimos el último día
        temperatura_siguiente = datos[dia]  # Temperatura real del día siguiente
        predicción = temperatura + alpha * (temperatura_siguiente - temperatura)
        temperaturas_predichas.append(predicción)

        print(f'Día {dia}: Temperatura Real = {temperatura}°C, Predicción = {predicción:.2f}°C')

    return temperaturas_predichas

# Llamar a la función para predecir la temperatura del siguiente día
temperaturas_predichas = predecir_temperatura_siguiente_dia(temperaturas)

# Imprimir la predicción del último día
ultimo_dia = len(temperaturas)
print(f'Día {ultimo_dia}: Temperatura Real = {temperaturas[ultimo_dia - 1]}°C, Predicción = {temperaturas_predichas[-1]:.2f}°C')
