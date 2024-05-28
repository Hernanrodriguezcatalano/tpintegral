import unittest
from models.persona import Persona
from models.cuenta import Cuenta

class TestCuenta(unittest.TestCase):
    def test_crear_cuenta(self):
        persona = Persona("Juan", 20, "12345678A")
        cuenta = Cuenta(persona, 100.50)
        self.assertEqual(cuenta.titular, persona)
        self.assertEqual(cuenta.cantidad, 100.50)

    def test_ingresar_retirar(self):
        persona = Persona("Juan", 20, "12345678A")
        cuenta = Cuenta(persona, 100.50)
        cuenta.ingresar(50)
        self.assertEqual(cuenta.cantidad, 150.50)
        cuenta.retirar(30)
        self.assertEqual(cuenta.cantidad, 120.50)

if __name__ == "__main__":
    unittest.main()
