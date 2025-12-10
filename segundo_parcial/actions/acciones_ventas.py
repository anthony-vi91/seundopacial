import os
from file_manager import FileManagerVenta, FileManagerDetalleVenta, FileManagerProducto, FileManagerUsuario
from menus.menu_ventas import mostrar_menu_ventas

def ejecutar_menu_ventas():
    fm_venta = FileManagerVenta()
    fm_detalle = FileManagerDetalleVenta()
    fm_producto = FileManagerProducto()
    fm_usuario = FileManagerUsuario()

    while True:
        os.system("clear")
        mostrar_menu_ventas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- REGISTRAR VENTA ---\n")

            # Validar usuario existente
            while True:
                id_usuario = int(input("Ingrese ID del usuario: "))
                usuario = fm_usuario.get(id_usuario)
                if usuario:
                    print(f"Usuario encontrado: {usuario.to_line()}")
                    break
                else:
                    print("ERROR: Usuario no existe. Intente nuevamente.")

            # Crear cabecera (total 0)
            venta = fm_venta.insert(id_usuario)
            print(f"Venta creada con ID: {venta.id}")

            total = 0.0

            # Registrar detalles
            while True:
                print("\nIngresando detalle...")

                id_producto = int(input("ID del producto: "))
                producto = fm_producto.get(id_producto)
                if not producto:
                    print("ERROR: producto no existe")
                    continue

                cantidad = float(input("Cantidad: "))
                subtotal = cantidad * producto.precio

                detalle = fm_detalle.insert(venta.id, id_producto, cantidad, subtotal)
                print(f"Detalle registrado: {detalle.to_line()}")

                total += subtotal

                continuar = input("\nAgregar otro detalle? (s/n): ")
                if continuar.lower() != "s":
                    break

            # Actualizar total de la venta
            fm_venta.update_total(venta.id, total)
            print(f"\nVenta finalizada. Total: {total}")
            input("Continuar...")

        elif opcion == "2":
            ventas = fm_venta.get_all()
            detalles = fm_detalle.get_all()
            productos = fm_producto.get_all()

            if not ventas:
                print("No hay ventas registradas.")
                return

            for v in ventas.values():
                print(f"\nVenta ID: {v.id} | Cliente ID: {v.id_usuario} | Fecha: {v.fecha} | Total: {v.total}")

                for d in detalles:
                    if d.id_venta == v.id:
                        prod = productos.get(d.id_producto)
                        precio = prod.precio
                        print(f"    Detalle: ProdID={d.id_producto} | Cantidad={d.cantidad} | Precio={precio} | Subtotal={d.subtotal}")

                print("\n")  # 2 saltos

            input("Continuar...")

        elif opcion == "3":
            break