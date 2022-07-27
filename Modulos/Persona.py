class ClasePersonas:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
# Métodos get y set

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')


if __name__ == '__main__':
    print("Este código sólo se va a ejecutar si se ejecuta este script")
