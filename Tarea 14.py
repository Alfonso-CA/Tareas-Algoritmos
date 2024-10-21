def ele_dup(A):
    
    unicos = []  # Lista para almacenar elementos únicos
    
    if not A:
        return 0
      
    unicos.append(A[0]) 
    
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            unicos.append(A[i])
    
    # El número de elementos únicos
    k = len(unicos)
    
    # Regresar el número de elementos únicos
    return k, unicos

# Ejemplo de uso
Arreglo = [1,1,1,3,3,3,5,5,7,9,9,11]
k, unicos = ele_dup(Arreglo)
print(f"Cantidad de elementos unicos: {k}")
print(f"Arreglo con elementos unicos: {unicos}")
