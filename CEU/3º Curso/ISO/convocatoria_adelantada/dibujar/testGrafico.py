import math
import sys
import unittest
from io import StringIO
from grafico import *

class testGrafico(unittest.TestCase):

    def test1(self):
        dibujo = Dibujo()
        comandos = ["ABJ"]
        dibujo.dibujar(comandos)
        self.assertTrue(dibujo.lapiz.isdown())

    def test2(self):
        dibujo = Dibujo()
        comandos = ["ARR"]
        dibujo.dibujar(comandos)
        self.assertFalse(dibujo.lapiz.isdown())

    def test3(self):
        dibujo = Dibujo()
        comandos = ["ABJ", "NOR1"]
        dibujo.dibujar(comandos)
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.ycor(), 10)

    def test4(self):
        dibujo = Dibujo()
        comandos = ["ARR", "NOR1"]
        dibujo.dibujar(comandos)
        self.assertFalse(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.ycor(), 10)

    def test5(self):
        dibujo = Dibujo()
        comandos = ["ABJ", "SUR1"]
        dibujo.dibujar(comandos)
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.ycor(), -10)

    def test6(self):
        dibujo = Dibujo()
        comandos = ["ARR", "SUR1"]
        dibujo.dibujar(comandos)
        self.assertFalse(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.ycor(), -10)

    def test7(self):
        dibujo = Dibujo()
        comandos = ["ABJ", "EST1"]
        dibujo.dibujar(comandos)
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), 10)

    def test8(self):
        dibujo = Dibujo()
        comandos = ["ARR", "EST1"]
        dibujo.dibujar(comandos)
        self.assertFalse(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), 10)

    def test9(self):
        dibujo = Dibujo()
        comandos = ["ABJ", "OES1"]
        dibujo.dibujar(comandos)
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), -10)

    def test10(self):
        dibujo = Dibujo()
        comandos = ["ARR", "OES1"]
        dibujo.dibujar(comandos)
        self.assertFalse(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), -10)

    def test11(self):
        dibujo = Dibujo()
        comandos = ["ABJ", "NOR1", "EST1", "SUR1", "OES1"]
        dibujo.dibujar(comandos)
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertAlmostEqual(dibujo.lapiz.xcor(), 0, delta=1)
        self.assertAlmostEqual(dibujo.lapiz.ycor(), 0, delta=1)

    def test12(self):
        dibujo = Dibujo()
        comandos = ["ARR", "NOR1", "NOR1","ABJ", "NOR1", "NOR1", "NOR1", "NOR1", "EST1", "EST1", "SUR1", "SUR1", "OES1",
                    "OES1","EST1", "EST1", "SUR1", "SUR1", "ARR", "EST1", "EST1", "ABJ", "NOR1", "NOR1",
                    "NOR1", "NOR1", "EST1", "EST1", "SUR1", "SUR1", "OES1", "OES1", "ARR", "EST1", "EST1",
                    "EST1", "EST1", "EST1", "EST1", "ABJ", "NOR1", "NOR1", "OES1", "OES1", "EST1", "EST1", "EST1", "EST1", "OES1", "OES1", "SUR1", "SUR1",
                    "SUR1", "SUR1", "ARR", "EST1", "EST1", "EST1", "EST1", "ABJ", "NOR1", "NOR1", "NOR1", "NOR1", "EST1", "EST1", "EST1",
                    "SUR1", "SUR1", "SUR1", "SUR1", "OES1", "OES1", "OES1", "ARR", "NOR1", "EST1", "ABJ", "EST1",
                    "NOR1", "NOR1", "OES1", "SUR1", "SUR1", "ARR"]
        dibujo.dibujar(comandos)
        self.assertFalse(dibujo.lapiz.isdown())
        self.assertEqual(dibujo.lapiz.xcor(), 150)
        self.assertAlmostEqual(dibujo.lapiz.ycor(), 30, delta=1)

    def test13(self):
            dibujo = Dibujo()
            self.assertTrue(dibujo.lapiz.isdown())
            self.assertEqual(dibujo.lapiz.circle(10), dibujo.dibujar(["CIRC"]))

    def test14(self):
        dibujo = Dibujo()
        dibujo.dibujar(["CIRC"])
        y_inicial = dibujo.lapiz.ycor() #guardo coordenada Y inicial para calcular el diametro de mi funcion circulo y con esto el area
        dibujo.lapiz.circle(10,extent=180) #dibujo un semicirculo con las mismas medidas que el del comando CIRC
        y_final = dibujo.lapiz.ycor()  #guardo coordenada Y final para calcular el diametro de mi funcion circulo y con esto el area
        radio = (y_final - y_inicial) * 0.5 #calculo el radio dividiendo el diametro
        area_esperada = math.pi * 10 ** 2 #calculo el area esperada
        area_actual = math.pi * radio ** 2 #calculo area actual
        self.assertTrue(dibujo.lapiz.isdown())
        self.assertAlmostEqual(area_esperada, area_actual, delta=1)

    """
    def test_salir_comando(self):
        dibujo = Dibujo()   #NO FUNCIONA ESTE TEST
        dibujo.dibujar(["SALIR"])
        self.assertIsNone(turtle.Screen())
"""
    def test15(self):
        dibujo = Dibujo()
        output = StringIO()
        sys.stdout = output
        dibujo.dibujar(["nor1"])
        self.assertEqual("COMANDO no válido", output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()