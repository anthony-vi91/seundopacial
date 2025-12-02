import os
from menus.menu_principal import mostrar_menu_principal
from actions.acciones_usuarios import ejecutar_menu_usuarios
from actions.acciones_productos import ejecutar_menu_productos
from actions.acciones_ventas import ejecutar_menu_ventas

def main():
    while True:
        os.system("clear")
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_menu_productos()
        elif opcion == "2":
            ejecutar_menu_usuarios()
        elif opcion == "3":
            ejecutar_menu_ventas()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Continuar...")

if __name__ == "__main__":
    main()