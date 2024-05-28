class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError("El nombre debe ser una cadena.")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if isinstance(value, int) and value >= 0:
            self._edad = value
        else:
            raise ValueError("La edad debe ser un entero positivo.")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        if isinstance(value, str):
            self._dni = value
        else:
            raise ValueError("El DNI debe ser una cadena.")

    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

    def es_mayor_de_edad(self):
        return self.edad >= 18
