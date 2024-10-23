#Creando una función que devuelva los numeros primos.
#Entre el 0 y el argumento que entregamos

def es_primo(num):
    """
    Verifica si un número es primo.

    Args:
        num (int): El número a verificar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primos_hasta(num):
    """
    Devuelve una lista de números primos hasta un número dado.

    Args:
        num (int): El límite superior para buscar números primos.

    Returns:
        list: Lista de números primos hasta el número dado.
    """
    primos = []
    for i in range(2, num + 1):
        if es_primo(i):
            primos.append(i)
    return primos

resultado = primos_hasta(50)
print(resultado)