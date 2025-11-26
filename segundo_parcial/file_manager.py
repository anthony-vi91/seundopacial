import os
from models import Usuario

class FileManager:
    def __init__(self, filename="data.txt", counter_file="counter.txt"):
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