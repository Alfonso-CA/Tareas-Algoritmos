def Palindromo(x):

    original = x
    reverso = 0
    
    while x > 0:
        digito = x % 10
        reverso = reverso * 10 + digito
        x //= 10  
    return original == reverso

def Resultado(x):

    if x < 1 or x > 10000: # Definimos el rango
        print("Fuera de rango")
    elif Palindromo(x):
        print(f"{x} es un palíndromo.")
    else:
        print(f"{x} no es un palíndromo.")

#Ejecución 

if __name__=='__main__':

    while(True):
    
        x = int(input("\nIngresa un numero: "))  # Ejemplo de uso

        Resultado(x)
