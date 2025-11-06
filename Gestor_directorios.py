import os
import time
from colorama import Fore, Style, init

# Inicializa colorama (para mostrar colores)
init(autoreset=True)

# Lista para guardar el historial de acciones
historial = []

def registrar_accion(accion):
    # Guarda cada acción realizada
    historial.append(accion)

def mostrar_menu():
    # Muestra el menú principal
    print("\n--- GESTOR DE ARCHIVOS Y CARPETAS ---")
    print("Adrián Rosiña - Proyecto MPO")
    print(f"Carpeta actual: {Fore.CYAN}{os.getcwd()}{Style.RESET_ALL}")
    print("--------------------------------------")
    print("1. Ver contenido de la carpeta")
    print("2. Crear una carpeta nueva")
    print("3. Crear un archivo de texto")
    print("4. Añadir texto a un archivo")
    print("5. Borrar archivo o carpeta")
    print("6. Ver información de un archivo o carpeta")
    print("7. Cambiar de carpeta (entrar o volver atrás)")
    print("8. Cambiar nombre de archivo o carpeta")
    print("9. Ver historial de acciones")
    print("10. Ver tamaño total de la carpeta actual")
    print("0. Salir")
    print("--------------------------------------")

def listar_contenido():
    # Lista los archivos y carpetas
    try:
        contenido = os.listdir()
        if not contenido:
            print("La carpeta está vacía.")
            return
        print("\nContenido actual:\n")
        for elemento in contenido:
            if os.path.isdir(elemento):
                print(Fore.BLUE + "[CARPETA]" + Style.RESET_ALL, elemento)
            else:
                print(Fore.GREEN + "[ARCHIVO]" + Style.RESET_ALL, elemento)
        registrar_accion("Listó el contenido de la carpeta")
    except Exception as e:
        print("No se pudo mostrar el contenido:", e)

def crear_directorio():
    nombre = input("Nombre de la nueva carpeta: ")
    try:
        if os.path.exists(nombre):
            print("Ya existe algo con ese nombre.")
            return
        os.mkdir(nombre)
        print("Carpeta creada con éxito:", nombre)
        registrar_accion("Creó carpeta: " + nombre)
    except Exception as e:
        print("Error al crear la carpeta:", e)

def crear_archivo():
    nombre = input("Nombre del nuevo archivo (.txt): ")
    try:
        if os.path.exists(nombre):
            print("Ese archivo ya existe.")
            return
        texto = input("Escribe algo dentro del archivo:\n")
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(texto)
        print("Archivo creado correctamente:", nombre)
        registrar_accion("Creó archivo: " + nombre)
    except Exception as e:
        print("Error al crear el archivo:", e)

def escribir_en_archivo():
    nombre = input("Archivo al que quieres añadir texto: ")
    try:
        if not os.path.exists(nombre):
            print("El archivo no existe.")
            return
        texto = input("Escribe lo que quieras añadir:\n")
        with open(nombre, "a", encoding="utf-8") as f:
            f.write("\n" + texto)
        print("Texto añadido correctamente.")
        registrar_accion("Añadió texto en: " + nombre)
    except Exception as e:
        print("No se pudo escribir en el archivo:", e)

def eliminar_elemento():
    nombre = input("Nombre del archivo o carpeta a borrar: ")
    try:
        if not os.path.exists(nombre):
            print("No existe ese archivo o carpeta.")
            return
        if os.path.isdir(nombre):
            os.rmdir(nombre)
            print("Carpeta borrada:", nombre)
        else:
            os.remove(nombre)
            print("Archivo borrado:", nombre)
        registrar_accion("Borró: " + nombre)
    except OSError:
        print("No se puede borrar la carpeta (¿está vacía?).")
    except Exception as e:
        print("Error al borrar:", e)

def mostrar_informacion():
    nombre = input("Nombre del archivo o carpeta: ")
    try:
        if not os.path.exists(nombre):
            print("No existe ese elemento.")
            return
        tipo = "Carpeta" if os.path.isdir(nombre) else "Archivo"
        tamaño = os.path.getsize(nombre)
        fecha = time.ctime(os.path.getmtime(nombre))
        print("\n--- Información ---")
        print("Nombre:", nombre)
        print("Tipo:", tipo)
        print("Tamaño:", tamaño, "bytes")
        print("Última modificación:", fecha)
        registrar_accion("Consultó información de: " + nombre)
    except Exception as e:
        print("Error al mostrar la información:", e)

def cambiar_directorio():
    # Permite moverse entre carpetas
    print("\n1. Entrar en una carpeta")
    print("2. Volver atrás")
    op = input("Elige una opción: ")
    try:
        if op == "1":
            nombre = input("Nombre de la carpeta a la que quieres entrar: ")
            if os.path.isdir(nombre):
                os.chdir(nombre)
                print("Ahora estás en:", os.getcwd())
                registrar_accion("Entró en carpeta: " + nombre)
            else:
                print("Esa carpeta no existe.")
        elif op == "2":
            os.chdir("..")
            print("Volviste a:", os.getcwd())
            registrar_accion("Retrocedió una carpeta")
        else:
            print("Opción no válida.")
    except Exception as e:
        print("Error al cambiar de carpeta:", e)

def renombrar_elemento():
    nombre = input("Nombre actual del archivo o carpeta: ")
    if not os.path.exists(nombre):
        print("No existe ese elemento.")
        return
    nuevo = input("Nuevo nombre: ")
    try:
        os.rename(nombre, nuevo)
        print("Renombrado con éxito:", nombre, "→", nuevo)
        registrar_accion("Renombró " + nombre + " a " + nuevo)
    except Exception as e:
        print("Error al renombrar:", e)

def mostrar_historial():
    # Muestra todas las acciones realizadas
    if not historial:
        print("Aún no hay historial.")
        return
    print("\n--- Historial de acciones ---")
    for i, acc in enumerate(historial, 1):
        print(str(i) + ".", acc)

def mostrar_tamaño_total():
    # Calcula el tamaño total de los archivos del directorio actual
    try:
        total = 0
        for f in os.listdir():
            if os.path.isfile(f):
                total += os.path.getsize(f)
        print("Tamaño total de los archivos:", total, "bytes")
        registrar_accion("Consultó tamaño total")
    except Exception as e:
        print("No se pudo calcular el tamaño:", e)

def main():
    # Bucle principal
    while True:
        mostrar_menu()
        op = input("Elige una opción (0-10): ")

        if op == "1":
            listar_contenido()
        elif op == "2":
            crear_directorio()
        elif op == "3":
            crear_archivo()
        elif op == "4":
            escribir_en_archivo()
        elif op == "5":
            eliminar_elemento()
        elif op == "6":
            mostrar_informacion()
        elif op == "7":
            cambiar_directorio()
        elif op == "8":
            renombrar_elemento()
        elif op == "9":
            mostrar_historial()
        elif op == "10":
            mostrar_tamaño_total()
        elif op == "0":
            print("Saliendo... ¡Gracias por usar mi gestor! :)")
            break
        else:
            print("Opción no válida, prueba otra vez.")

if __name__ == "__main__":
    main()