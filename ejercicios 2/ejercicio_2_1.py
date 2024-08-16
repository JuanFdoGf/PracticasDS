#Hoy falto el profesor de clases y los estudiantes van a realizar la clase, 
#uno de ellos sera el profesor y otro su asistente.

# A. Pedir el nombre y la edad de los estudiantes que vinieron a clase y ordenar los datos de menor a mayor.
# B. El mayor de la clase sera el profesor y el menor su asistente: Indicar sus nombres.1234567890

def obtener_estudiantes(cantidad_de_estudiantes):
    
    #Creando la lista con los estudiantes
    estudiantes = []
    
    #Creando un bucle para solicitar la información de cada estudiante
    for _ in range(cantidad_de_estudiantes):
        nombre = input('Ingrese el nombre del estudiante ')
        edad = int(input('Ingrese la edad del estudiante '))
        estudiante = (nombre,edad)
        
        #Agregando la información a la lista
        estudiantes.append(estudiante)
        
    #Ordenando la lista de menor a mayor segun la edad    
    estudiantes.sort(key=lambda x:x[1])
    
    #Estidiantes[x] devuelve una tupla con (nombre,edad) despues accedemos al nombre
    #para definir al asistente y el profesor
    asistente = estudiantes[0][0]
    profesor = estudiantes[-1][0]
    
    #Retornamos una tupla
    return asistente,profesor

#Desempaquetamos lo que nos retorna la función
asistente_resultado,profesor_resultado = obtener_estudiantes(5)

#Enseñar el resultado
print(f'El profesor es {profesor_resultado} y su asistente es {asistente_resultado}')