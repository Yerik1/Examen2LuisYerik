import unittest
from Examen2 import MiClase


class MyTestCase(unittest.TestCase):

    ###YERIK###
    def test_ObtieneValencia1(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneValencia(1234567), 4)  # add assertion here

    def test_ObtieneValencia2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneValencia(13579), 5)  # add assertion here

    def test_DivisibleTempo1(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.DivisibleTempo(10), [1, 2, 5, 10])  # add assertion here
    def test_DivisibleTempo2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.DivisibleTempo(20), [1, 2, 4, 5, 10, 20])  # add assertion here


if __name__ == '__main__':
    unittest.main()
