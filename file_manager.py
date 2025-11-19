import os
from models import usuario

class filemanager:
    def __init__(self, filename = "data.txt", counter_file = "counter.txt"):
        self.filename = filename
        self.counter_file = counter_file

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("")
        
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f:
                f.write("0")

#"w" es write dcumento para escribir ||y|| "r" de read de lectura

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f-read().strip() or  0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        usuario = {}
        with open (self.filename, "r") as f:
            for line in f:
                if line.strip():
                    usuario = usuario.from_line(line)
                    usuarios[usuario.id] = usuario
        return usuarios

    def _write_file(self. usuaios: dict[int, usuarios]):
        with open(self.filename, "w") as f:
            forusuario in usuarios.values():
            f.write(usuario.to_line() + "\n")
    
    def insert(self, nombre: str edad:int) -> usuario:
        usuarios = self._read_file()
        new_id = self._get_next_id()
        usuario = usuario(new_id, nombre, edad)
        usuarios[new_id] = usuario
        self._write_file(usuarios)
        return usuario
#tratarde hacer estos metodos para la siguiente clase
    def update(self, id: int, nombre: str, edad: int):

    def delete(self, id: int):

    def get(self, id: int) -> usuario | none:

    def get_all(self) -> dict[int, usuario]: