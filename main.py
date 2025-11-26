from file_manager import FileManager

def mostrar_menu():
    print("\n---MENU---")
    print("1. Insertar usuario")
    print("2. Actualizar usuario")
    print("3. Eliminar usuario")
    print("4. Consultar usuario por ID")
    print("5. Listar todos los usuarios")
    print("6. Salir")

def main():
    fm = FileManager()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            usuario = fm.insert(nombre, edad)
            print(f"Usuario insertado: {usuario.to_line()}")

        elif opcion == "2":
            id = int(input("ID del usuario a actualizar: "))
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            if fm.update(id, nombre, edad):
                print(f"Usuario con ID {id} actualizado.")
            else:
                print(f"No se encontró un usuario con ID {id}.")

        elif opcion == "3":
            id = int(input("ID del usuario a eliminar: "))
            if fm.delete(id):
                print(f"Usuario con ID {id} eliminado.")
            else:
                print(f"No se encontró un usuario con ID {id}.")

        elif opcion == "4":
            id = int(input("ID del usuario a consultar: "))
            usuario = fm.get(id)
            if usuario:
                print(f"Usuario encontrado: {usuario.to_line()}")
            else:
                print(f"No se encontró un usuario con ID {id}.")

        elif opcion == "5":
            usuarios = fm.get_all()
            if usuarios:
                print("\nLista de usuarios:")
                for u in usuarios.values():
                    #print(f"ID: {u.id}, Nombre: {u.nombre}, Edad: {u.edad}")
                    print(f"Usuario: {u.to_line()}")
            else:
                print("No hay usuarios registrados.")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()