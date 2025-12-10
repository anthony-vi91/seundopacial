import os
from datetime import datetime
from models import Usuario, Producto, Venta, DetalleVenta

class FileManagerUsuario:
    def __init__(self, filename="usuarios.txt", counter_file="usuarios_counter.txt"):
        self.filename = filename
        self.counter_file = counter_file

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("")

        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f:
                f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        usuarios = {}
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    usuario = Usuario.from_line(line)
                    usuarios[usuario.id] = usuario
        return usuarios

    def _write_file(self, usuarios: dict[int, Usuario]):
        with open(self.filename, "w") as f:
            for usuario in usuarios.values():
                f.write(usuario.to_line() + "\n")

    def _append_file(self, usuario: Usuario):
        with open(self.filename, "a") as f:
            f.write(usuario.to_line() + "\n")

    def insert(self, nombre: str, edad: int) -> Usuario:
        new_id = self._get_next_id()
        usuario = Usuario(new_id, nombre, edad)
        self._append_file(usuario)
        return usuario

    #trata de hacer estos metodos para la siguiente clase
    def update(self, id: int, nombre: str, edad: int) -> bool:
        usuarios = self._read_file()
        if id in usuarios:
            usuarios[id].nombre = nombre
            usuarios[id].edad = edad
            self._write_file(usuarios)
            return True
        return False

    def delete(self, id: int) -> bool:
        usuarios = self._read_file()
        if id in usuarios:
            del usuarios[id]
            self._write_file(usuarios)
            return True
        return False
    
    def get(self, id: int) -> Usuario | None:
        usuarios = self._read_file()
        return usuarios.get(id)
    
    def get_all(self) -> dict[int, Usuario]:
        return self._read_file()

class FileManagerProducto:
    def __init__(self, filename="productos.txt", counter_file="productos_counter.txt"):
        self.filename = filename
        self.counter_file = counter_file

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("")

        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f:
                f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        productos = {}
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    producto = Producto.from_line(line)
                    productos[producto.id] = producto
        return productos

    def _write_file(self, productos: dict[int, Producto]):
        with open(self.filename, "w") as f:
            for producto in productos.values():
                f.write(producto.to_line() + "\n")

    def _append_file(self, producto: Producto):
        with open(self.filename, "a") as f:
            f.write(producto.to_line() + "\n")

    def insert(self, nombre: str, precio: float) -> Producto:
        new_id = self._get_next_id()
        producto = Producto(new_id, nombre, precio)
        self._append_file(producto)
        return producto

    def update(self, id: int, nombre: str, precio: float) -> bool:
        productos = self._read_file()
        if id in productos:
            productos[id].nombre = nombre
            productos[id].precio = precio
            self._write_file(productos)
            return True
        return False

    def delete(self, id: int) -> bool:
        productos = self._read_file()
        if id in productos:
            del productos[id]
            self._write_file(productos)
            return True
        return False
    
    def get(self, id: int) -> Producto | None:
        productos = self._read_file()
        return productos.get(id)
    
    def get_all(self) -> dict[int, Producto]:
        return self._read_file()

class FileManagerVenta:
    def __init__(self, filename="ventas.txt", counter_file="ventas_counter.txt"):
        self.filename = filename
        self.counter_file = counter_file

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("")

        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f:
                f.write("0")

    def _get_next_id(self):
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        ventas = {}
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    venta = Venta.from_line(line)
                    ventas[venta.id] = venta
        return ventas

    def _write_file(self, ventas: dict[int, Venta]):
        with open(self.filename, "w") as f:
            for venta in ventas.values():
                f.write(venta.to_line() + "\n")

    def _append_file(self, venta: Venta):
        with open(self.filename, "a") as f:
            f.write(venta.to_line() + "\n")

    # CRUD:

    def insert(self, id_usuario: int):
        ventas = self.get_all()
        next_id = 1 if not ventas else max(ventas.keys()) + 1

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        venta = Venta(next_id, id_usuario, fecha, 0.0)

        with open(self.filename, "a") as f:
            f.write(venta.to_line() + "\n")

        return venta

    def update_total(self, id: int, total: float):
        ventas = self._read_file()
        if id in ventas:
            ventas[id].total = total
            self._write_file(ventas)
            return True
        return False

    def get(self, id: int) -> Venta | None:
        ventas = self._read_file()
        return ventas.get(id)

    def get_all(self):
        return self._read_file()

class FileManagerDetalleVenta:
    def __init__(self, filename="detalle_ventas.txt"):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("")

    def _read_file(self):
        detalles = []
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    detalles.append(DetalleVenta.from_line(line))
        return detalles

    def _append_file(self, detalle: DetalleVenta):
        with open(self.filename, "a") as f:
            f.write(detalle.to_line() + "\n")

    def _get_next_id(self) -> int:
        count = 0
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    count += 1
        return count + 1

    # Insert SOLO:
    def insert(self, id_venta: int, id_producto: int, cantidad: int, subtotal: float) -> DetalleVenta:
        new_id = self._get_next_id()
        detalle = DetalleVenta(new_id, id_venta, id_producto, cantidad, subtotal)
        self._append_file(detalle)
        return detalle

    def get_by_venta(self, id_venta: int):
        detalles = self._read_file()
        return [d for d in detalles if d.id_venta == id_venta]

    def get_all(self):
        return self._read_file()