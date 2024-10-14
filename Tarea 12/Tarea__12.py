# Diccionario para almacenar los resultados de Fibonacci ya calculados
fib_cache = {}

def fib(n):
    # Retorna el resultado si ya fue calculado previamente
    if n in fib_cache:
        return fib_cache[n]
    
    # Condición base para los casos 0 y 1
    if n < 2:
        fib_cache[n] = n  # Guardamos el resultado en el diccionario
        return n  
    
    # Cálculo recursivo del número de Fibonacci
    fib_cache[n] = fib(n-1) + fib(n-2)  # Guardamos el resultado en el diccionario
    return fib_cache[n]

# Prueba la función con n = 8, que debe devolver 21
print(fib(8))   # Salida: 21

# Repetimos la prueba para verificar el uso del caché
print(fib(8))   # Salida: 21 (desde el caché)

# Muestra el contenido del diccionario fib_cache
print(fib_cache)  # Resultados almacenados
