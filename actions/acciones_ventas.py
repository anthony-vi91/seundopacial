import os
from menus.menu_ventas import mostrar_menu_ventas

def ejecutar_menu_ventas():
    while True:
        os.system("clear")
        mostrar_menu_ventas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Registrar venta (pendiente de implementación)")
            input("Continuar...")

        elif opcion == "2":
            print("Listar ventas (pendiente de implementación)")
            input("Continuar...")

        elif opcion == "3":
            break