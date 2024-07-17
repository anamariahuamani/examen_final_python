"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return list(filter(es_primo, lista))


entrada = [1, 6, 3, 7, 5, 13, 1, 8, 9, 12]
primos = filtrar_primos(entrada)
print(primos)