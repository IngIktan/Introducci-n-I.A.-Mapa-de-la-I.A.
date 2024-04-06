# Daniel Alejandro Flores Sepulveda
# Heurística para estimar el número de personas que votan por un partido en un distrito.

def estimar_votantes_por_partido(distribucion_votantes, preferencias_partido):
    total_votantes = sum(distribucion_votantes.values())  # Calcular el total de votantes en el distrito
    proporcion_votantes_partido = preferencias_partido / 100  # Convertir el porcentaje de preferencias a proporción
    votantes_por_partido = total_votantes * proporcion_votantes_partido  # Calcular el número estimado de votantes
    return int(votantes_por_partido)  # Devolver el número estimado como un entero

# Ejemplo de uso
distribucion_votantes = {'Distrito A': 1000, 'Distrito B': 1500, 'Distrito C': 800}
preferencias_partido = 30  # Supongamos que el partido tiene un 30% de apoyo en el distrito

# Estimar el número de votantes para el partido en el Distrito B
distrito = 'Distrito B'
votantes_estimados = estimar_votantes_por_partido(distribucion_votantes, preferencias_partido)
print(f"Se estima que {votantes_estimados} personas votarán por el partido en el {distrito}.")
