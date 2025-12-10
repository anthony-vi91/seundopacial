#Clase Usuario
class Usuario:
    def __init__(self, id: int, nombre: str, edad: int):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "edad": self.edad}

    @staticmethod
    def from_dict(data):
        return Usuario(data["id"], data["nombre"], data["edad"])

    def to_line(self) -> str:
        return f"{self.id}|{self.nombre}|{self.edad}"

    @staticmethod
    def from_line(line: str):
        parts = line.strip().split("|")
        return Usuario(int(parts[0]), parts[1], int(parts[2]))

#Clase Producto
class Producto:
    def __init__(self, id: int, nombre: str, precio: float):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["precio"])

    def to_line(self) -> str:
        return f"{self.id}|{self.nombre}|{self.precio}"

    @staticmethod
    def from_line(line: str):
        parts = line.strip().split("|")
        return Producto(int(parts[0]), parts[1], float(parts[2]))

#Clase Venta
class Venta:
    def __init__(self, id: int, fecha: str, id_usuario: int, total: float):
        self.id = id
        self.fecha = fecha
        self.id_usuario = id_usuario
        self.total = total

    def to_dict(self):
        return {"id": self.id, "fecha": self.fecha, "id_usuario": self.id_usuario, "total": self.total}

    @staticmethod
    def from_dict(data):
        return Venta(data["id"], data["fecha"], data["id_usuario"], data["total"])

    def to_line(self) -> str:
        return f"{self.id}|{self.fecha}|{self.id_usuario}|{self.total}"

    @staticmethod
    def from_line(line: str):
        parts = line.strip().split("|")
        return Venta(int(parts[0]), int(parts[1]), parts[2], float(parts[3]))

#Clase Detalle Venta
class DetalleVenta:
    def __init__(self, id: int, id_venta: int, id_producto: int, cantidad: int, subtotal: float):
        self.id = id
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.subtotal = subtotal

    def to_dict(self):
        return {"id": self.id, "id_venta": self.id_venta, "id_producto": self.id_producto, "cantidad": self.cantidad, "subtotal": self.subtotal}

    @staticmethod
    def from_dict(data):
        return DetalleVenta(data["id"], data["id_venta"], data["id_producto"], data["cantidad"], data["subtotal"])

    def to_line(self) -> str:
        return f"{self.id}|{self.id_venta}|{self.id_producto}|{self.cantidad}|{self.subtotal}"

    @staticmethod
    def from_line(line: str):
        parts = line.strip().split("|")
        return DetalleVenta(int(parts[0]), int(parts[1]), int(parts[2]), float(parts[3]), float(parts[4]))