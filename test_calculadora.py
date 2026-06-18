import unittest

from calculadora import calcular_media, dividir, multiplicar, somar, subtrair


class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(10, 5), 15)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 3), 7)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 7), 28)

    def test_dividir(self):
        self.assertEqual(dividir(20, 4), 5.0)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_calcular_media(self):
        self.assertEqual(calcular_media([8, 7, 9, 10, 6]), 8.0)


if __name__ == "__main__":
    unittest.main()
