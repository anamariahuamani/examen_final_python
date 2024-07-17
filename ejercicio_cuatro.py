"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""

 
alumno = {
    1: {"nombre": "lucio", "edad": 28, "curso": "programacion de lenguaje"},
    2: {"nombre": "María", "edad": 22, "curso": "programacion"}
}

# Función para imprimir los registros del alumno
def imprimir_registros():
    for clave, valor in alumno.items():
        print(f"Registro {clave}: {valor}")

# Función para editar un campo de un registro específico
def editar_campo_registro(id_registro, campo, nuevo_valor):
    if id_registro in alumno:
        alumno[id_registro][campo] = nuevo_valor
        return "Campo actualizado correctamente."
    else:
        return "El registro no existe."

# Ejemplo de uso de las funciones
imprimir_registros()
print(editar_campo_registro(1, "edad", 26))
imprimir_registros()