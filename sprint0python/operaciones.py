def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multi (a, b):
    return a * b

def divi (a, b):
    try:
        return a / b
    #Con esta excepción, se comprueba que no se divida entre 0.
    except ZeroDivisionError:
        return "No se puede dividir entre 0."