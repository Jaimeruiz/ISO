import unittest
import math

from botones import *

class TestGrafico(unittest.TestCase):

    def test_abajo(self):
        dibujo = Dibujo()
        dibujo.abajo()
        self.assertTrue(dibujo.lapiz.isdown())

    def test_arriba(self):
        dibujo = Dibujo()
        dibujo.arriba()
        self.assertFalse(dibujo.lapiz.isdown())

    def test_norte(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.norte()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.ycor(), 10)

    def test_sur(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.sur()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.ycor(), -10)

    def test_este(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.este()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), 10)

    def test_oeste(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.oeste()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), -10)

    def test_norte2(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.norte()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.ycor(), 10)

    def test_sur2(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.sur()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.ycor(), -10)

    def test_este2(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.este()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), 10)

    def test_oeste2(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.oeste()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), -10)

    def test_circulo(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.circulo()
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.circle(10), dibujo.circulo())

    def test_circulo2(self):
        dibujo = Dibujo()
        dibujo.abajo()
        dibujo.circulo()
        y_inicial = dibujo.lapiz.ycor()
        dibujo.lapiz.circle(10, extent=180)
        y_final = dibujo.lapiz.ycor()
        radio = (y_final - y_inicial) * 0.5
        area_esperada = math.pi * 10 ** 2
        area_actual = math.pi * radio ** 2
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertAlmostEqual(area_esperada, area_actual, delta=1)


if __name__ == '__main__':
    unittest.main()