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