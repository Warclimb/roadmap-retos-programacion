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
user = "warclimb"
edad = 37
lenguaje = "Cobol"

# añadir datos al archivo
def add_data():
    with open("warclimb.txt","a+") as file:
        file.write(f"Nombre: {user}\n")
        file.write(f"Edad: {edad}\n")
        file.write(f"Lenguaje de programación favorito: {lenguaje}\n")
 add_data()
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


 