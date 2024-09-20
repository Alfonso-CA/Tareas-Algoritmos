def suma_de_pares_en_una_matriz(matriz):
 
 suma_pares = 0
 n = len(matriz)

 for i in range(n):
    for j in range(n):
       if matriz[i][j] % 2 == 0:        
     # Si el número es par
        suma_pares += matriz[i][j]
        
 return suma_pares

matriz1 = [ [1, 2], [3, 4]] # Resultado esperado: 2 + 4 = 6
print(suma_de_pares_en_una_matriz(matriz1))  

matriz2 = [ [5, 8, 12], [7, 10, 3], [2, 1, 6]] # Resultado esperado: 8 + 12 + 10 + 2 + 6 = 38
print(suma_de_pares_en_una_matriz(matriz2)) 

matriz3 = [ [11, 14, 5, 8], [13, 18, 20, 3], [6, 7, 10, 9], [2, 15, 22, 16]] # Resultado esperado: 14 + 8 + 18 + 20 + 6 + 10 + 2 + 22 + 16 = 116
print(suma_de_pares_en_una_matriz(matriz3))  
