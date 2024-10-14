def fib(n):
    # Función para calcular el enésimo número de Fibonacci
    if n < 2:
        # Si n es 0 o 1, el resultado es n
        return n
    else:
        # Calcular el número de Fibonacci usando la relación recursiva
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

# Llamar a la función fib con el valor 8
print(fib(7))  # Prueba la función con n = 7, que debe devolver 13
print(fib(8))  # Prueba la función con n = 8, que debe devolver 21
print(fib(9))  # Prueba la función con n = 9, que debe devolver 34