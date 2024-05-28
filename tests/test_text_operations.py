import unittest
from Utils.text_operations import contar_palabras, palabra_mas_frecuente

class TestTextOperations(unittest.TestCase):
    def test_contar_palabras(self):
        self.assertEqual(contar_palabras("Hola mundo mundo"), {"Hola": 1, "mundo": 2})

    def test_palabra_mas_frecuente(self):
        frecuencia = {"Hola": 1, "mundo": 2}
        self.assertEqual(palabra_mas_frecuente(frecuencia), ("mundo", 2))

if __name__ == "__main__":
    unittest.main()
