"""
Este módulo contiene una función para generar la serie de Fibonacci
hasta un número dado.
"""

def fibonacci(num):
    """
    Genera una lista de números de Fibonacci hasta que el último número sea
    mayor que el número dado.

    :param num: El límite superior para los números de Fibonacci.
    :return: Una lista de números de Fibonacci.
    """
    a,b = 0,1
    fibonacci_lista = []
    while b <= num:
        fibonacci_lista.append(b)
        a,b = b,a+b
    return fibonacci_lista
resultado = fibonacci(60)
print(resultado)
