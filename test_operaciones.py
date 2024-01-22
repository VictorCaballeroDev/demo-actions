import unittest
from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(multiplicar(0, 5), 0)

        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)
        self.assertEqual(dividir(0, 5), 0)
        self.assertEqual(dividir(5, 0), 'Operacion no permitida')



if __name__ == '__main__':
    unittest.main()