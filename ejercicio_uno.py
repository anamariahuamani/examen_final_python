"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
def encontrar_menor_mayor(lista):
    if not lista:
        return "La lista está vacía"
    
    diccionario = {"menor": min(lista), "mayor": max(lista)}
    return diccionario


entrada = [4, 7, 10, 4, 1, 0]
resultado = encontrar_menor_mayor(entrada)
print(resultado)