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