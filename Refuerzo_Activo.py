import random

# Datos de clima simulados: 1 representa "lluvia" y 0 representa "no lluvia"
clima = [random.choice([0, 1]) for _ in range(30)]

# Función para predecir si lloverá y tomar una acción (llevar un paraguas o no)
def predecir_y_actuar(datos):
    aciertos = 0  # Contador de predicciones correctas
    total = 0  # Contador de predicciones totales
    alpha = 0.1  # Factor de aprendizaje

    for dia in range(1, len(datos)):
        clima_hoy = datos[dia - 1]
        clima_manana_real = datos[dia]

        # Predicción: llevar paraguas si el día anterior llovió, de lo contrario, no llevarlo
        if clima_hoy == 1:
            prediccion = 1  # Llevar un paraguas
        else:
            prediccion = 0  # No llevar un paraguas

        # Evaluar la predicción
        recompensa = 1 if prediccion == clima_manana_real else 0
        aciertos += recompensa
        total += 1

        # Actualizar la estrategia en función de la recompensa
        if recompensa == 0:
            # Si la predicción fue incorrecta, ajustar la estrategia para la próxima vez
            if clima_hoy == 1:
                # Si llovió ayer, la estrategia es no llevar un paraguas si la predicción fue incorrecta
                alpha = min(1.0, alpha + 0.1)
            else:
                # Si no llovió ayer, la estrategia es llevar un paraguas si la predicción fue incorrecta
                alpha = max(0.0, alpha - 0.1)

        print(f'Día {dia}: Clima Real = {clima_manana_real}, Predicción = {prediccion}, Recompensa = {recompensa}')

    tasa_aciertos = aciertos / total
    print(f'Tasa de Aciertos: {tasa_aciertos:.2%}')

# Llamar a la función para predecir y actuar
predecir_y_actuar(clima)