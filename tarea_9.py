def candles(a: list[int]) -> int:
    
    """
    Args:
        a (list[int]): The candles heights.
    
    Returns:
        int: The number of candles that are tallest
    """
    # Encontramos la altura maxima.
    altura_maxima = max(a)
    
    #Contar cuántas velas tienen esa altura máxima
    altura_maxima_cantidad = a.count(altura_maxima)
    
    return altura_maxima_cantidad

if __name__ == "__main__":
    print(candles([4, 4, 1, 3])) # 2
    print(candles([1, 1, 1, 1, 1])) # 5
    print(candles([5, 3, 1, 3, 5, 3, 1, 3, 5])) # 3
    print(candles([10000, 10001, 10002, 10002, 10000])) # 2
    print(candles([999, 1000, 99, 912, 100])) # 1
