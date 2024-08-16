def obtener_estudiantes(cantidad_de_estudiantes):
    """
    Solicita la información de una cantidad específica de estudiantes, los ordena por edad
    y retorna el nombre del estudiante más joven (asistente) y el más viejo (profesor).
    Args:
        cantidad_de_estudiantes (int): El número de estudiantes a ingresar.
    Returns:
        tuple: Una tupla con el nombre del asistente y el nombre del profesor.
    """
    if cantidad_de_estudiantes <= 0:
        raise ValueError("La cantidad de estudiantes debe ser un número positivo.")
    
    estudiantes = []

    for _ in range(cantidad_de_estudiantes):
        nombre = input('Ingrese el nombre del estudiante ')
        while True:
            try:
                edad = int(input('Ingrese la edad del estudiante '))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la edad.")
        estudiante = (nombre, edad)
        estudiantes.append(estudiante)

    estudiantes.sort(key=lambda x: x[1])
    asistente = estudiantes[0][0]
    profesor = estudiantes[-1][0]
    return asistente, profesor

asistente_resultado, profesor_resultado = obtener_estudiantes(5)
print(f'El profesor es {profesor_resultado} y su asistente es {asistente_resultado}')