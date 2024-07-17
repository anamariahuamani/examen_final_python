"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
# Crear un diccionario con 5 registros de tiendas comerciales
tiendas_comerciales = {
    1: {"JESUSA": "Tienda A", "horario": "8:00 - 6:00"},
    2: {"JESUSA": "Tienda B", "horario": "9:30 - 8:30"},
    3: {"ROMINA": "Tienda C", "horario": "10:00 - 12:00"},
    4: {"ROMINA": "Tienda D", "horario": "8:30 - 7:30"},
    5: {"JESUSA": "Tienda E", "horario": "11:00 - 17:00"}
}

# Función para editar el nombre de una tienda comercial
def editar_nombre_tienda(id_tienda, nuevo_nombre):
    if id_tienda in tiendas_comerciales:
        tiendas_comerciales[id_tienda]["nombre"] = nuevo_nombre
        return "Nombre de la tienda actualizado exitosamente."
    else:
        return "La tienda no existe."

# Función para actualizar el horario de atención de una tienda comercial
def actualizar_horario_tienda(id_tienda, nuevo_horario):
    if id_tienda in tiendas_comerciales:
        tiendas_comerciales[id_tienda]["horario"] = nuevo_horario
        return "Horario de atención actualizado exitosamente."
    else:
        return "La tienda no existe."

# Función para eliminar una tienda comercial
def eliminar_tienda(id_tienda):
    if id_tienda in tiendas_comerciales:
        del tiendas_comerciales[id_tienda]
        return "Tienda eliminada correctamente."
    else:
        return "La tienda no existe."

# Ejemplos de uso de las funciones
print(tiendas_comerciales)
print(editar_nombre_tienda(3, "Nueva Tienda C"))
print(actualizar_horario_tienda(2, "9:00 - 18:00"))
print(eliminar_tienda(5))
print(tiendas_comerciales)