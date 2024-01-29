import unittest
import libcomplex


#Santiago Coronado Pinzon.
#test de la libreria de complejos

class Prueba(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(libcomplex.sumacomplejos((4,-3),(12,9)), (16, 6))

    def test_resta(self):
        self.assertEqual(libcomplex.restacomplejos((2,3),(4,7)), (-2, -4))

    def test_multiplicacion(self):
        self.assertEqual(libcomplex.multiplicacioncomplejos((2,3),(4,7)), (-13, 26))

    def test_divicion(self):
        self.assertEqual(libcomplex.divicioncomplejos((2,3),(4,7)), (0.4461538461538462, -0.03076923076923077))

    def test_modulo(self):
        self.assertEqual(libcomplex.modulocomplejos((4,4)) , 5.66 )

    def test_conjugado(self):
        self.assertEqual(libcomplex.conjugadocomplejos((4, 4)), (4, -4))

    def test_polar(self):
        self.assertEqual(libcomplex.polar_cartiaciono((64,33)), (-0.85, 63.99))

    def test_fase(self):
        self.assertEqual(libcomplex.fasecomplejos((4,4)), (0.79))



if __name__ == '__main__':
    unittest.main()
