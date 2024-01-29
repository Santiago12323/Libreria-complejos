import unittest
import libreria_complejos

#Santiago Coronado Pinzon.
#test de la libreria de complejos

class Prueba(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(libreria_complejos.sumacomplejos((4,-3),(12,9)), (16, 6))
        self.assertEqual(libreria_complejos.sumacomplejos((10,-6),(-2,4)), (8, -2))
        self.assertEqual(libreria_complejos.sumacomplejos((7,41),(1,-6)), (8, 35))

    def test_resta(self):
        self.assertEqual(libreria_complejos.restacomplejos((2,3),(4,7)), (-2, -4))
        self.assertEqual(libreria_complejos.restacomplejos((10, -6), (-2, 4)), (12, -10))
        self.assertEqual(libreria_complejos.restacomplejos((7, 41), (1, -6)), (6, 47))

    def test_multiplicacion(self):
        self.assertEqual(libreria_complejos.multiplicacioncomplejos((2,3),(4,7)), (-13, 26))
        self.assertEqual(libreria_complejos.multiplicacioncomplejos((10, -6), (-2, 4)), (4, 52))
        self.assertEqual(libreria_complejos.multiplicacioncomplejos((7, 41), (1, -6)), (253, -1))

    def test_divicion(self):
        self.assertEqual(libreria_complejos.divicioncomplejos((2,3),(4,7)), (0.4461538461538462, -0.03076923076923077))
        self.assertEqual(libreria_complejos.divicioncomplejos((10, -6), (-2, 4)), (-2.2, -1.4))
        self.assertEqual(libreria_complejos.divicioncomplejos((7, 41), (1, -6)), (-6.45945945945946, 2.2432432432432434))

    def test_modulo(self):
        self.assertEqual(libreria_complejos.modulocomplejos((4,4)) , 5.66 )
        self.assertEqual(libreria_complejos.modulocomplejos((5, 6)), 7.81 )
        self.assertEqual(libreria_complejos.modulocomplejos((7, 4)), 8.06 )

    def test_conjugado(self):
        self.assertEqual(libreria_complejos.conjugadocomplejos((4, 4)), (4, -4))
        self.assertEqual(libreria_complejos.conjugadocomplejos((5, 5)), (5, -5))
        self.assertEqual(libreria_complejos.conjugadocomplejos((3, 1)), (3, -1))

    def test_polar(self):
        self.assertEqual(libreria_complejos.polar_cartiaciono((64,33)), (-0.85, 63.99))
        self.assertEqual(libreria_complejos.polar_cartiaciono((40, 10)), (-33.56, -21.76))
        self.assertEqual(libreria_complejos.polar_cartiaciono((0, 40)), (0.0, 0.0))

    def test_fase(self):
        self.assertEqual(libreria_complejos.fasecomplejos((4,4)), (0.79))
        self.assertEqual(libreria_complejos.fasecomplejos((4, 0)), (0.0))
        self.assertEqual(libreria_complejos.fasecomplejos((1, 8)), (1.45))



if __name__ == '__main__':
    unittest.main()
