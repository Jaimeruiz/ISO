import unittest
from vigenere import *
import os
class testVigenere(unittest.TestCase):

    def test1(self):
        vigenere = Vigenere()
        texto = "hello"
        clave = "aaaaa"
        self.assertEqual("hello", vigenere.cifrar(texto, clave))

    def test2(self):
        vigenere = Vigenere()
        texto = "hello"
        clave = "jaime"
        self.assertEqual("qetxs", vigenere.cifrar(texto, clave))

    def test3(self):
        vigenere = Vigenere()
        texto = "oso"
        clave = "dos"
        self.assertEqual("rgg", vigenere.cifrar(texto, clave))

    def test4(self):
        vigenere = Vigenere()
        texto = "Jaime"
        clave = "arbol"
        self.assertEqual("Jrjap", vigenere.cifrar(texto, clave))

    def test5(self):
        vigenere = Vigenere()
        texto = "HOLA"
        clave = "CAMA"
        self.assertEqual("JOXA", vigenere.cifrar(texto, clave))

    def test6(self):
        vigenere = Vigenere()
        frase = "Este Examen esta Aprobado"
        clave = "Este Examen esta Aprobado"
        self.assertEqual("Ikmi Iuayia ikma Aeiccagc", vigenere.cifrar(frase, clave))

    def test7(self):
        vigenere = Vigenere()
        frase = "dragon"
        clave = "lobo"
        self.assertEqual("ofbuzb", vigenere.cifrar(frase, clave))

    def test8(self):
        vigenere = Vigenere()
        texto = "hello"
        clave = "aaaaa"
        self.assertEqual("hello", vigenere.descifrar(texto, clave))

    def test9(self):
        vigenere = Vigenere()
        texto = "qetxs"
        clave = "jaime"
        self.assertEqual("hello", vigenere.descifrar(texto, clave))

    def test10(self):
        vigenere = Vigenere()
        texto = "rgg"
        clave = "dos"
        self.assertEqual("oso", vigenere.descifrar(texto, clave))

    def test11(self):
        vigenere = Vigenere()
        texto = "Jrjap"
        clave = "arbol"
        self.assertEqual("Jaime", vigenere.descifrar(texto, clave))

    def test12(self):
        vigenere = Vigenere()
        texto = "JOXA"
        clave = "CAMA"
        self.assertEqual("HOLA", vigenere.descifrar(texto, clave))

    def test13(self):
        vigenere = Vigenere()
        frase = "Ikmi Iuayia ikma Aeiccagc"
        clave = "Este Examen esta Aprobado"
        self.assertEqual("Este Examen esta Aprobado", vigenere.descifrar(frase, clave))

    def test14(self):
        vigenere = Vigenere()
        frase = "ofbuzb"
        clave = "lobo"
        self.assertEqual("dragon", vigenere.descifrar(frase, clave))


    def test_cifrar_archivo(self):
        vigenere = Vigenere()
        nombre_archivo = "test_archivo.txt"
        clave = "secreta"
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Hola, esto es una prueba.")

        vigenere.cifrar_archivo_vigenere(nombre_archivo, clave)

        nombre_archivo_cifrado = f"{nombre_archivo.split('.')[0]}_cifrado.txt"
        with open(nombre_archivo_cifrado, "r") as archivo_cifrado:
            cifrado = archivo_cifrado.read()
        self.assertTrue(os.path.exists(nombre_archivo_cifrado))
        self.assertEqual("Zsnr, ekxq il mrc tkuwfc.", cifrado)

    def test_descifrar_archivo(self):
        vigenere = Vigenere()
        nombre_archivo_cifrado = "test_archivo_cifrado.txt"
        clave = "secreta"
        with open(nombre_archivo_cifrado, "w") as archivo:
            archivo.write("Zsnr, ekxq il mrc tkuwfc.")

        vigenere.descifrar_archivo_vigenere(nombre_archivo_cifrado, clave)

        nombre_archivo_descifrado = f"{nombre_archivo_cifrado.split('_cifrado.')[0]}_descifrado.txt"

        with open(nombre_archivo_descifrado, "r") as archivo_cifrado:
            descifrado = archivo_cifrado.read()

        self.assertTrue(os.path.exists(nombre_archivo_descifrado))
        self.assertEqual("Hola, esto es una prueba.", descifrado)

if __name__ == '__main__':
    unittest.main()