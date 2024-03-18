''' * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 '''

# lineas con datos
user1 = "warclimb"
edad1 = 37
lenguaje1 = "Cobol"

# añadir datos al archivo
def add_data(user, edad, lenguaje):
    with open("warclimb.txt","a+",encoding="utf-8") as file:
        file.write(f"Nombre: {user}\n")
        file.write(f"Edad: {edad}\n")
        file.write(f"Lenguaje de programación favorito: {lenguaje}\n")


if __name__ == "__main__":
    # add_data(user1, edad1, lenguaje1)

'''
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.'''



 