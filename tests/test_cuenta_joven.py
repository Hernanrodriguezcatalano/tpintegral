import unittest
from models.persona import Persona
from models.cuenta_joven import CuentaJoven

class TestCuentaJoven(unittest.TestCase):
    def test_crear_cuenta_joven(self):
        persona = Persona("Juan", 20, "12345678A")
        cuenta_joven = CuentaJoven(persona, 200.75, 10)
        self.assertEqual(cuenta_joven.titular, persona)
        self.assertEqual(cuenta_joven.cantidad, 200.75)
        self.assertEqual(cuenta_joven.bonificacion, 10)

    def test_es_titular_valido(self):
        persona = Persona("Juan", 20, "12345678A")
        cuenta_joven = CuentaJoven(persona, 200.75, 10)
        self.assertTrue(cuenta_joven.es_titular_valido())

    def test_retirar(self):
        persona = Persona("Juan", 20, "12345678A")
        cuenta_joven = CuentaJoven(persona, 200.75, 10)
        if cuenta_joven.es_titular_valido():
            cuenta_joven.retirar(50)
            self.assertEqual(cuenta_joven.cantidad, 150.75)

if __name__ == "__main__":
    unittest.main()
