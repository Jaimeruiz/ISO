import unittest
from cesar import *
import os
class testCifradoCesar(unittest.TestCase):

    def test1(self):
        cesar = Cesar()
        frase = "hello"
        clave = 0
        self.assertEqual("hello", cesar.cifrar(frase, clave))

    def test2(self):
        cesar = Cesar()
        frase = "hello"
        clave = 5
        self.assertEqual("mjqqt", cesar.cifrar(frase, clave))

    def test3(self):
        cesar = Cesar()
        frase = "hola mundo"
        clave = 3
        self.assertEqual("krod pxqgr", cesar.cifrar(frase, clave))

    def test4(self):
        cesar = Cesar()
        frase = "Jaime"
        clave = 4
        self.assertEqual("Nemqi", cesar.cifrar(frase, clave))

    def test5(self):
        cesar = Cesar()
        frase = "HOLA"
        clave = 7
        self.assertEqual("OVSH", cesar.cifrar(frase, clave))

    def test6(self):
        cesar = Cesar()
        frase = "Este Examen esta Aprobado"
        clave = 1
        self.assertEqual("Ftuf Fybnfo ftub Bqspcbep", cesar.cifrar(frase, clave))

    def test13(self):
        cesar = Cesar()
        frase = "Z"
        clave = 1
        self.assertEqual("A", cesar.cifrar(frase,clave))

    def test15(self):
        cesar = Cesar()
        frase = "-"
        clave = 12
        self.assertEqual("-", cesar.cifrar(frase, clave))

    def test16(self): #prueba cifrado, mayusculas, caracteres especiales, espacio y desbordamiento.
        cesar = Cesar()
        frase = "Hola, me llamo Jaime."
        clave = 12
        self.assertEqual("Taxm, yq xxmya Vmuyq.", cesar.cifrar(frase, clave))


    def test7(self):
        cesar = Cesar()
        frase = "hello"
        clave = 1
        self.assertEqual("gdkkn", cesar.descifrar(frase, clave))

    def test8(self):
        cesar = Cesar()
        frase = "mjqqt"
        clave = 5
        self.assertEqual("hello", cesar.descifrar(frase, clave))

    def test9(self):
        cesar = Cesar()
        frase = "Nemqi"
        clave = 4
        self.assertEqual("Jaime", cesar.descifrar(frase, clave))

    def test10(self):
        cesar = Cesar()
        frase = "OVSH"
        clave = 7
        self.assertEqual("HOLA", cesar.descifrar(frase, clave))

    def test11(self):
        cesar = Cesar()
        frase = "krod pxqgr"
        clave = 3
        self.assertEqual("hola mundo", cesar.descifrar(frase, clave))

    def test12(self):
        cesar = Cesar()
        frase = "Ftuf FYBNFO ftub bqspcbep"
        clave = 1
        self.assertEqual("Este EXAMEN esta aprobado", cesar.descifrar(frase, clave))

    def test14(self):
        cesar = Cesar()
        frase = "A"
        clave = 1
        self.assertEqual("Z", cesar.descifrar(frase, clave))

    def test17(self):
        cesar = Cesar()
        frase = "¿?"
        clave = 12
        self.assertEqual("¿?", cesar.descifrar(frase, clave))

    def test18(self):
        cesar = Cesar()
        frase = "Taxm, yq xxmya Vmuyq."
        clave = 12
        self.assertEqual("Hola, me llamo Jaime.", cesar.descifrar(frase, clave))

    def test_cifrar_archivo(self):
        cesar = Cesar()
        nombre_archivo = "test_archivo.txt"
        clave = 1
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Este examen esta aprobado")

        cesar.cifrar_archivo_cesar(nombre_archivo, clave)

        nombre_archivo_cifrado = f"{nombre_archivo.split('.')[0]}_cifrado.txt"
        with open(nombre_archivo_cifrado, "r") as archivo_cifrado:
            cifrado = archivo_cifrado.read()
        self.assertTrue(os.path.exists(nombre_archivo_cifrado))
        self.assertEqual("Ftuf fybnfo ftub bqspcbep", cifrado)

    def test_descifrar_archivo(self):
        cesar = Cesar()
        nombre_archivo_cifrado = "test_archivo_cifrado.txt"
        clave = 1
        with open(nombre_archivo_cifrado, "w") as archivo:
            archivo.write("Ftuf fybnfo ftub bqspcbep")

        cesar.descifrar_archivo_cesar(nombre_archivo_cifrado, clave)

        nombre_archivo_descifrado = f"{nombre_archivo_cifrado.split('_cifrado.')[0]}_descifrado.txt"

        with open(nombre_archivo_descifrado, "r") as archivo_cifrado:
            descifrado = archivo_cifrado.read()

        self.assertTrue(os.path.exists(nombre_archivo_descifrado))
        self.assertEqual("Este examen esta aprobado", descifrado)

if __name__ == '__main__':
    unittest.main()