import unittest
from bolos import *
class testbolos(unittest.TestCase):

    def test1(self):
        partida = Partida()
        lanzamientos = ([0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0])
        self.assertEqual(0, partida.marcador(lanzamientos))

    def test2(self):
        partida = Partida()
        lanzamientos = ([0, 5], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(5, partida.marcador(lanzamientos))

    def test3(self):
        partida = Partida()
        lanzamientos = ([0, 5], [0, 0], [0, 8], [0, 0], [0, 0], [4, 2], [0, 0], [1, 0], [4, 0], [0, 0])
        self.assertEqual(24, partida.marcador(lanzamientos))

    def test4(self):
        partida = Partida()
        lanzamientos = ([5, "/"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(10, partida.marcador(lanzamientos))

    def test5(self):
        partida = Partida()
        lanzamientos = ([5, "/"], [7, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(25, partida.marcador(lanzamientos))

    def test6(self):
        partida = Partida()
        lanzamientos = ([5, "/"], [7, 1], [4, "/"], [4, 1], [2, "/"], [6, "/"], [2, 6], [0, 0], [0, 0], [0, 0])
        self.assertEqual(80, partida.marcador(lanzamientos))

    def test7(self):
        partida = Partida()
        lanzamientos = ([5, "/"], [4, "/"], [4, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(34, partida.marcador(lanzamientos))

    def test8(self):
        partida = Partida()
        lanzamientos = ("X", [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(10, partida.marcador(lanzamientos))

    def test9(self):
        partida = Partida()
        lanzamientos = ("X", [5, 4], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(28, partida.marcador(lanzamientos))

    def test10(self):
        partida = Partida()
        lanzamientos = ("X", [5, 4], "X", [6, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(54, partida.marcador(lanzamientos))

    def test11(self):
        partida = Partida()
        lanzamientos = ("X", "X", [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(30, partida.marcador(lanzamientos))

    def test12(self):
        partida = Partida()
        lanzamientos = ("X", "X", [5, 2], [0, 0], [0, 4], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(53, partida.marcador(lanzamientos))

    def test13(self):
        partida = Partida()
        lanzamientos = ("X", "X", "X", [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(60, partida.marcador(lanzamientos))

    def test14(self):
        partida = Partida()
        lanzamientos = ("X", "X", "X", [7, 0], [9, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(90, partida.marcador(lanzamientos))

    def test15(self):
        partida = Partida()
        lanzamientos = ("X", [5, "/"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(30, partida.marcador(lanzamientos))

    def test16(self):
        partida = Partida()
        lanzamientos = ("X", [5, "/"], [5, 4], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(44, partida.marcador(lanzamientos))

    def test17(self):
        partida = Partida()
        lanzamientos = ("X", "X", [5, "/"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(55, partida.marcador(lanzamientos))

    def test18(self):
        partida = Partida()
        lanzamientos = ("X", "X", [5, "/"], [4, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(64, partida.marcador(lanzamientos))

    def test19(self):
        partida = Partida()
        lanzamientos = ([3, "/"], "X", [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(30, partida.marcador(lanzamientos))

    def test20(self):
        partida = Partida()
        lanzamientos = ([8, "/"], "X", [2, 4], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(42, partida.marcador(lanzamientos))

    def test21(self):
        partida = Partida()
        lanzamientos = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], "X", [0, 0])
        self.assertEqual(10, partida.marcador(lanzamientos))

    def test22(self):
        partida = Partida()
        lanzamientos = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], "X", [5, 0])
        self.assertEqual(15, partida.marcador(lanzamientos))

    def test23(self):
        partida = Partida()
        lanzamientos = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], "X", "X", [0, 0])
        self.assertEqual(30, partida.marcador(lanzamientos))

    def test24(self):
        partida = Partida()
        lanzamientos = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], "X", "X", [4, 1])
        self.assertEqual(39, partida.marcador(lanzamientos))

    def test25(self):
        partida = Partida()
        lanzamientos = ([0,  0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], "X", "X", [4, "/"])
        self.assertEqual(44, partida.marcador(lanzamientos))

    def test26(self):
        partida = Partida()
        lanzamientos = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [4, "/"], "X", [0, 0])
        self.assertEqual(30, partida.marcador(lanzamientos))

    def test27(self):
        partida = Partida()
        lanzamientos = ([5, "/"], [4, "/"], "X", [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(44, partida.marcador(lanzamientos))

    def test28(self):
        partida = Partida()
        lanzamientos = ([5, "/"], [4, "/"], "X", [4, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
        self.assertEqual(54, partida.marcador(lanzamientos))

    def test29(self):
        partida = Partida()
        lanzamientos = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [4, "/"], [3, "/"], [0])
        self.assertEqual(23, partida.marcador(lanzamientos))

    def test30(self):
        partida = Partida()
        lanzamientos = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, "/"], [5])
        self.assertEqual(15, partida.marcador(lanzamientos))

    def test31(self):
        partida = Partida()
        lanzamientos = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], "X", [1, "/"], "X")
        self.assertEqual(40, partida.marcador(lanzamientos))

if __name__ == '__main__':
    unittest.main()