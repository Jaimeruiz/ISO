import unittest
from buscador import *

class testBuscador(unittest.TestCase):

    def test1(self):
        buscador = Buscador()
        texto = "a"
        self.assertEqual(1, buscador.buscar_texto(texto, "a"))

    def test2(self):
        buscador = Buscador()
        texto = "laura"
        self.assertEqual(2, buscador.buscar_texto(texto, "a"))

    def test3(self):
        buscador = Buscador()
        texto = "Hola buenos días, ¿Qué tal todo?"
        self.assertEqual(4, buscador.buscar_texto(texto, "o"))

    def test4(self):
        buscador = Buscador()
        texto = "hola hola hola. ¿Qué tal todo?. Yo estoy bien. Gracias por preguntar. Hasta pronto."
        self.assertEqual(5, buscador.buscar_texto(texto, "."))

    def test5(self):
        buscador = Buscador()
        texto = "Estoy 100% seguro de que el 10% de un total de 100 es 10, o le que es lo mismo" \
                "restar el 90% al total, Asi se haya el % de algo."
        self.assertEqual(4, buscador.buscar_texto(texto, "%"))

    def test6(self):
        buscador = Buscador()
        texto = "hola ¿como estas?"
        self.assertEqual(1, buscador.buscar_texto(texto, "hola"))

    def test7(self):
        buscador = Buscador()
        texto = "hola, hola, hola ¿como estas?"
        self.assertEqual(3, buscador.buscar_texto(texto, "hola"))

    def test8(self):
        buscador = Buscador()
        texto = "hola, hola, hola ¿como estas?"
        self.assertEqual(2, buscador.buscar_texto(texto, "hola,"))

    def test9(self):
        buscador = Buscador()
        texto = "Hola buenos días, ¿Que tal todo?. Todo bien, ¿Que tal usted?"
        self.assertEqual(2, buscador.buscar_texto(texto, "Que tal"))

    def test10(self):
        buscador = Buscador()
        texto = "Hola buenos días, ¿Que tal, todo bien?. Todo bien, ¿Que tal usted?"
        self.assertEqual(1, buscador.buscar_texto(texto, "¿Que tal,"))

if __name__ == '__main__':
    unittest.main()
