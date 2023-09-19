import unittest
from limite import *
class testLimite(unittest.TestCase):

    def test1(self):
        limite = Limite()
        self.assertEqual("La suma es 1", limite.sumar([1],1))

    def test2(self):
        limite = Limite()
        secuencia = [1,2,3]
        self.assertEqual("La suma es 6", limite.sumar(secuencia,6))

    def test3(self):
        limite = Limite()
        secuencia = [1,2,3]
        self.assertEqual("La suma 6 ha sobrepasado el limite 4", limite.sumar(secuencia,4))

    def test4(self):
        limite = Limite()
        secuencia = [1,5,4,2]
        self.assertEqual("La suma es 12, puedes seguir sumando", limite.sumar(secuencia,14))

    def test5(self):
        limite = Limite()
        secuencia = [1,2,3,4,2]
        self.assertEqual("La suma es 10, puedes seguir sumando", limite.sumar(secuencia[0:4],12))
        self.assertEqual("La suma es 12", limite.sumar(secuencia[0:4] + secuencia[4:5], 12))


if __name__ == '__main__':
    unittest.main()
