import unittest
from palindromo import *
class testPalindromo(unittest.TestCase):

    def test1(self):
        palindromo = Palindromo()
        self.assertEqual("a es un palindromo", palindromo.invertir("a"))

    def test2(self):
        palindromo = Palindromo()
        self.assertEqual("ana es un palindromo", palindromo.invertir("ana"))

    def test3(self):
        palindromo = Palindromo()
        self.assertEqual("No es un palindromo", palindromo.invertir("hola"))

    def test4(self):
        palindromo = Palindromo()
        self.assertEqual("reconocer es un palindromo", palindromo.invertir("reconocer"))

    def test5(self):
        palindromo = Palindromo()
        self.assertEqual("1 es capicua", palindromo.invertir("1"))

    def test6(self):
        palindromo = Palindromo()
        self.assertEqual("111 es capicua", palindromo.invertir("111"))

    def test7(self):
        palindromo = Palindromo()
        self.assertEqual("12321 es capicua", palindromo.invertir("12321"))

    def test8(self):
        palindromo = Palindromo()
        self.assertEqual("12345 no es capicua", palindromo.invertir("12345"))

    def test9(self):
        palindromo = Palindromo()
        self.assertEqual("A luna ese anula es una oracion palindroma", palindromo.invertir("A luna ese anula"))

    def test10(self):
        palindromo = Palindromo()
        self.assertEqual("A ti no, bonita. es un palindromo parcial", palindromo.invertir("A ti no, bonita."))

if __name__ == '__main__':
    unittest.main()