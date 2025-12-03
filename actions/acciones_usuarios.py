import os
from file_manager import FileManagerUsuario
from menus.menu_usuarios import mostrar_menu_usuarios

def ejecutar_menu_usuarios():
    fm_usuario = FileManagerUsuario()

    while True:
        os.system("clear")
        mostrar_menu_usuarios()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            usuario = fm_usuario.insert(nombre, edad)
            print(f"Usuario insertado: {usuario.to_line()}")
            input("Continuar...")

        elif opcion == "2":
            id = int(input("ID del usuario a actualizar: "))
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            if fm_usuario.update(id, nombre, edad):
                print(f"Usuario con ID {id} actualizado.")
            else:
                print(f"No se encontró un usuario con ID {id}.")
            input("Continuar...")

        elif opcion == "3":
            id = int(input("ID del usuario a eliminar: "))
            if fm_usuario.delete(id):
                print(f"Usuario con ID {id} eliminado.")
            else:
                print(f"No se encontró un usuario con ID {id}.")
            input("Continuar...")

        elif opcion == "4":
            id = int(input("ID del usuario a consultar: "))
            usuario = fm_usuario.get(id)
            if usuario:
                print(f"Usuario encontrado: {usuario.to_line()}")
            else:
                print(f"No se encontró un usuario con ID {id}.")
            input("Continuar...")

        elif opcion == "5":
            usuarios = fm_usuario.get_all()
            if usuarios:
                print("\nLista de usuarios:")
                for u in usuarios.values():
                    print(f"Usuario: {u.to_line()}")
            else:
                print("No hay usuarios registrados.")
            input("Continuar...")

        elif opcion == "6":
            break