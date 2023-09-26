import random

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def siguiente_primo(n):
    if n < 2:
        n = 2
    else:
        n += 1

    while True:
        if es_primo(n):
            return n
        n += 1

def mediana_de_tres(num1, num2, num3):
    numeros_ordenados = sorted([num1, num2, num3])
    return numeros_ordenados[1]

def generar_contrasena_aleatoria():
    longitud = random.randint(7, 10)
    contrasena = ""
    
    for _ in range(longitud):
        caracter_aleatorio = chr(random.randint(33, 126))
        contrasena += caracter_aleatorio
    
    return contrasena

def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = (cateto1**2 + cateto2**2)**0.5
    return hipotenusa
