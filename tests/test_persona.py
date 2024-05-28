import unittest
from models.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", 20, "12345678A")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.edad, 20)
        self.assertEqual(persona.dni, "12345678A")

    def test_es_mayor_de_edad(self):
        persona = Persona("Juan", 20, "12345678A")
        self.assertTrue(persona.es_mayor_de_edad())

if __name__ == "__main__":
    unittest.main()
