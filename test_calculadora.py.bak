import unittest
from calculadora import somar, subtrair, multiplicar, dividir, calcular_media


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
        # Espera que seja tratado, mas a função não trata — vai lançar ZeroDivisionError
        resultado = dividir(10, 0)
        self.assertIsNone(resultado)

    def test_calcular_media(self):
        # Vai falhar por causa do bug em calcular_media
        self.assertEqual(calcular_media([8, 7, 9, 10, 6]), 8.0)


if __name__ == "__main__":
    unittest.main()
