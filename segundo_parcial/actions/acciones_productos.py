import os
from file_manager import FileManagerProducto
from menus.menu_productos import mostrar_menu_productos

def ejecutar_menu_productos():
    fm_producto = FileManagerProducto()

    while True:
        os.system("clear")
        mostrar_menu_productos()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            producto = fm_producto.insert(nombre, precio)
            print(f"Producto insertado: {producto.to_line()}")
            input("Continuar...")

        elif opcion == "2":
            id = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre: ")
            precio = float(input("Nuevo precio: "))
            if fm_producto.update(id, nombre, precio):
                print(f"Producto con ID {id} actualizado.")
            else:
                print(f"No se encontró producto con ID {id}.")
            input("Continuar...")

        elif opcion == "3":
            id = int(input("ID del producto a eliminar: "))
            if fm_producto.delete(id):
                print(f"Producto con ID {id} eliminado.")
            else:
                print(f"No se encontró producto con ID {id}.")
            input("Continuar...")

        elif opcion == "4":
            id = int(input("ID del producto a consultar: "))
            producto = fm_producto.get(id)
            if producto:
                print(f"Producto encontrado: {producto.to_line()}")
            else:
                print(f"No se encontró producto con ID {id}.")
            input("Continuar...")

        elif opcion == "5":
            productos = fm_producto.get_all()
            if productos:
                print("\nLista de productos:")
                for p in productos.values():
                    print(f"Producto: {p.to_line()}")
            else:
                print("No hay productos registrados.")
            input("Continuar...")

        elif opcion == "6":
            break