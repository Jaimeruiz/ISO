import math
import sys
import unittest
from io import StringIO
from grafico_FactoryMethod import *
# Clase Dibujo y DibujoFactory aquí ...

class testGrafico(unittest.TestCase):

    def setUp(self):
        self.dibujo = Dibujo()

    def test1(self):
        comandos = ["ABJ"]
        self.dibujo.dibujar(comandos)
        self.assertTrue(self.dibujo.lapiz.isdown())

    def test2(self):
        comandos = ["ARR"]
        self.dibujo.dibujar(comandos)
        self.assertFalse(self.dibujo.lapiz.isdown())

    def test3(self):
        comandos = ["ABJ", "NOR1"]
        self.dibujo.dibujar(comandos)
        self.assertTrue(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.ycor(), 10)

    def test4(self):
        comandos = ["ARR", "NOR1"]
        self.dibujo.dibujar(comandos)
        self.assertFalse(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.ycor(), 10)

    def test5(self):
        comandos = ["ABJ", "SUR1"]
        self.dibujo.dibujar(comandos)
        self.assertTrue(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.ycor(), -10)

    def test6(self):
        comandos = ["ARR", "SUR1"]
        self.dibujo.dibujar(comandos)
        self.assertFalse(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.ycor(), -10)

    def test7(self):
        comandos = ["ABJ", "EST1"]
        self.dibujo.dibujar(comandos)
        self.assertTrue(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.xcor(), 10)

    def test8(self):
        comandos = ["ARR", "EST1"]
        self.dibujo.dibujar(comandos)
        self.assertFalse(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.xcor(), 10)

    def test9(self):
        comandos = ["ABJ", "OES1"]
        self.dibujo.dibujar(comandos)
        self.assertTrue(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.xcor(), -10)

    def test10(self):
        comandos = ["ARR", "OES1"]
        self.dibujo.dibujar(comandos)
        self.assertFalse(self.dibujo.lapiz.isdown())
        self.assertEqual(-10, self.dibujo.lapiz.xcor())

    def test11(self):
        comandos = ["ABJ", "NOR1", "EST1", "SUR1", "OES1"]
        self.dibujo.dibujar(comandos)
        self.assertTrue(self.dibujo.lapiz.isdown())
        self.assertAlmostEqual(self.dibujo.lapiz.xcor(), 0, delta=1)
        self.assertAlmostEqual(self.dibujo.lapiz.ycor(), 0, delta=1)

    def test12(self):
        comandos = ["ARR", "NOR1", "NOR1", "ABJ", "NOR1", "NOR1", "NOR1", "NOR1", "EST1", "EST1", "SUR1", "SUR1", "OES1",
                    "OES1", "EST1", "EST1", "SUR1", "SUR1", "ARR", "EST1", "EST1", "ABJ", "NOR1", "NOR1",
                    "NOR1", "NOR1", "EST1", "EST1", "SUR1", "SUR1", "OES1", "OES1", "ARR", "EST1", "EST1",
                    "EST1", "EST1", "EST1", "EST1", "ABJ", "NOR1", "NOR1", "OES1", "OES1", "EST1", "EST1", "EST1", "EST1", "OES1", "OES1", "SUR1", "SUR1",
                    "SUR1", "SUR1", "ARR", "EST1", "EST1", "EST1", "EST1", "ABJ", "NOR1", "NOR1", "NOR1", "NOR1", "EST1", "EST1", "EST1",
                    "SUR1", "SUR1", "SUR1", "SUR1", "OES1", "OES1", "OES1", "ARR", "NOR1", "EST1", "ABJ", "EST1",
                    "NOR1", "NOR1", "OES1", "SUR1", "SUR1", "ARR"]
        self.dibujo.dibujar(comandos)
        self.assertFalse(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.xcor(), 150)
        self.assertAlmostEqual(self.dibujo.lapiz.ycor(), 30, delta=1)

    def test13(self):
        comandos = ["CIRC"]
        self.dibujo.dibujar(comandos)
        self.assertTrue(self.dibujo.lapiz.isdown())
        self.assertEqual(self.dibujo.lapiz.circle(10), self.dibujo.dibujar(["CIRC"]))

    def test14(self):
        comandos = ["CIRC"]
        self.dibujo.dibujar(comandos)
        y_inicial = self.dibujo.lapiz.ycor()
        self.dibujo.lapiz.circle(10, extent=180)
        y_final = self.dibujo.lapiz.ycor()
        radio = (y_final - y_inicial) * 0.5
        area_esperada = math.pi * 10 ** 2
        area_actual = math.pi * radio ** 2
        self.assertTrue(self.dibujo.lapiz.isdown())
        self.assertAlmostEqual(area_esperada, area_actual, delta=1)

    def test15(self):
        output = StringIO()
        sys.stdout = output
        comandos = ["nor1"]
        self.dibujo.dibujar(comandos)
        self.assertEqual("COMANDO no válido", output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
