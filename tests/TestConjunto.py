import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunt_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunt_vacio_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(5,conjunto.promedio())

if __name__ == '__main__':
    unittest.main()
