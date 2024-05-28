from models.persona import Persona

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, value):
        if isinstance(value, Persona):
            self._titular = value
        else:
            raise ValueError("El titular debe ser una instancia de la clase Persona.")

    @property
    def cantidad(self):
        return self._cantidad

    def mostrar(self):
        return f"Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        self._cantidad -= cantidad

