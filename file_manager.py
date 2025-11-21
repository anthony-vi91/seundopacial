import os
from models import usuario

class filemanager:
    def __init__(self, filename="data.txt", counter_file="counter.txt"):
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
            current = int(f.read().strip() or  0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        usuarios = {}
        with open (self.filename, "r") as f:
            for line in f:
                if line.strip():
                    user = usuario.from_line(line)
                    usuarios[user.id] = user
        return usuarios

    def _write_file(self, usuarios: dict[int, usuario]):
        with open(self.filename, "w") as f:
            for user in usuarios.values():
                f.write(user.to_line() + "\n")

    """Appends a single user to the file.
        Args:
        user: The user object to append.
    """
    def _append_file(self, user: usuario):
        with open(self.filename, "a") as f:
            f.write(user.to_line() + "\n")
    
    def insert(self, nombre: str, edad:int) -> usuario:
        new_id = self._get_next_id()
        Usuario = usuario(new_id, nombre, edad)
        self._append_file(Usuario)
        return Usuario

#tratar de hacer estos metodos para la siguiente clase
    def update(self, id: int, nombre: str, edad: int) -> bool:
        usuarios = self._read_file()
        if id not in usuarios:   
            usuarios[id].nombre = nombre
            usuarios[id].edad = edad
            self._write_file(usuarios)
            return True
        return False

    def delete(self, id: int):
        usuarios = self._read_file()
        if id not in usuarios:
            del usuarios[id]
            self._write_file(usuarios)
            return True
        return False

    def get(self, id: int) -> usuario | None:
        usuarios = self._read_file()
        return usuarios.get(id)

    def get_all(self) -> dict[int, usuario]:
        return self._read_file()
