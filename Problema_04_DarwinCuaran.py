"""Fase 5. Conteo de títulos de una videoteca digital."""

# Cada fila contiene: título, año, calificación y género.
# Datos ficticios creados para comprobar las condiciones del problema.
CATALOGO = [
    ["Horizonte", 2022, 9, "Aventura"],
    ["Nuevo comienzo", 2020, 8, "Drama"],
    ["La ciudad", 2019, 9, "Suspenso"],
    ["Una tarde", 2023, 7, "Comedia"],
    ["Viaje al sur", 2018, 6, "Aventura"],
    ["El encuentro", 2021, 8, "Drama"],
    ["Última estación", 2020, 7, "Suspenso"],
]

CALIFICACION_MINIMA = 8
ANIO_LIMITE = 2020


def contar_titulos(catalogo, calificacion_minima, anio_limite):
    """Cuenta los títulos que cumplen ambos límites, incluidos sus iguales."""
    cantidad = 0
    for titulo in catalogo:
        anio = titulo[1]
        calificacion = titulo[2]
        if calificacion >= calificacion_minima and anio >= anio_limite:
            cantidad += 1
    return cantidad


def mostrar_resultado():
    """Presenta los criterios y el número de títulos que los cumplen."""
    total = contar_titulos(CATALOGO, CALIFICACION_MINIMA, ANIO_LIMITE)
    print("VIDEOTECA DIGITAL")
    print(f"Calificación mínima: {CALIFICACION_MINIMA}")
    print(f"Año mínimo: {ANIO_LIMITE}")
    print(f"Total de títulos que cumplen ambos criterios: {total}")


if __name__ == "__main__":
    mostrar_resultado()
