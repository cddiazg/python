def es_primo (numero):
    
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    
    for i in range(2, numero):
        if numero % 2 == 0:
            print("No es primo", 2, "es divisor")
            return False
    print("Es primo")
    return True

numero = int(input("Ingrese el numero"))