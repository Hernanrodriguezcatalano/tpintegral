from models.cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, value):
        if isinstance(value, (int, float)) and 0 <= value <= 100:
            self._bonificacion = value
        else:
            raise ValueError("La bonificación debe ser un número entre 0 y 100.")

    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        return f"Cuenta Joven - Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%"
