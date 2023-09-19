class Cesar():
    def __int__(self):
        self.texto_cifrado = ""
        self.posicion = 0
        self.nueva_posicion = 0

    def cifrar(self, texto, clave):
        texto_cifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        caracteres_especiales = ",.%$€@!¿?¡ºª-:()/ "
        for i in range(len(texto.strip())):
            if texto[i].isupper():
                posicion = alfabeto.index(texto[i].lower())
                nueva_posicion = (posicion + clave) % len(alfabeto) #corrige el desbordamiento del array
                texto_cifrado += alfabeto[nueva_posicion].upper()
            elif texto[i] in caracteres_especiales:
                texto_cifrado += texto[i]
            else:
                posicion = alfabeto.index(texto[i])
                nueva_posicion = (posicion + clave) % len(alfabeto)
                texto_cifrado += alfabeto[nueva_posicion]
        return texto_cifrado
    """
    CODIGO PARA PASAR EL 7 TEST
    def descifrar(self, texto, clave):
        return texto
    """
    """
    CODIGO PARA PASAR EL 8 TEST
    def descifrar(self, texto, clave):
        texto_descifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(texto.strip())):
            posicion = alfabeto.index(texto[i].lower())
            nueva_posicion = posicion - clave
            texto_descifrado += alfabeto[nueva_posicion]
        return texto_descifrado
    """
    """
    CODIGO PARA PASAR EL 9 Y 10 TEST
    def descifrar(self, texto, clave):
        texto_descifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(texto.strip())):
            if texto[i].isupper():
                posicion = alfabeto.index(texto[i].lower())
                nueva_posicion = posicion - clave
                texto_descifrado += alfabeto[nueva_posicion].upper()
            else:
                posicion = alfabeto.index(texto[i])
                nueva_posicion = posicion - clave
                texto_descifrado += alfabeto[nueva_posicion]
        return texto_descifrado
    """
    """
    CODIGO PARA TEST 11 Y 12
    def descifrar(self, texto, clave):
        texto_descifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(texto.strip())):
            if texto[i].isupper():
                posicion = alfabeto.index(texto[i].lower())
                nueva_posicion = (posicion - clave)
                texto_descifrado += alfabeto[nueva_posicion].upper()
            elif texto[i] == " ":
                texto_descifrado += " "
            else:
                posicion = alfabeto.index(texto[i])
                nueva_posicion = (posicion - clave)
                texto_descifrado += alfabeto[nueva_posicion]
        return texto_descifrado
"""
    """
    CODIGO PARA TEST 14
     def descifrar(self, texto, clave):
        texto_descifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(texto.strip())):
            if texto[i].isupper():
                posicion = alfabeto.index(texto[i].lower())
                nueva_posicion = (posicion - clave) % len(alfabeto)
                texto_descifrado += alfabeto[nueva_posicion].upper()
            elif texto[i] == " ":
                texto_descifrado += " "
            else:
                posicion = alfabeto.index(texto[i])
                nueva_posicion = (posicion - clave) % len(alfabeto)
                texto_descifrado += alfabeto[nueva_posicion]
        return texto_descifrado
    """
    #CODIGO PARA TEST 17 Y 18
    def descifrar(self, texto, clave):
        texto_descifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        caracteres_especiales = ",.%$€@!¿?¡ºª-:()/ "
        for i in range(len(texto.strip())):
            if texto[i].isupper():
                posicion = alfabeto.index(texto[i].lower())
                nueva_posicion = (posicion - clave) % len(alfabeto)
                texto_descifrado += alfabeto[nueva_posicion].upper()
            elif texto[i] in caracteres_especiales:
                texto_descifrado += texto[i]
            else:
                posicion = alfabeto.index(texto[i])
                nueva_posicion = (posicion - clave) % len(alfabeto)
                texto_descifrado += alfabeto[nueva_posicion]
        return texto_descifrado

    def cifrar_archivo_cesar(self, nombre_archivo, clave):
        try:
            with open(nombre_archivo, "r")as archivo:
                contenido = archivo.read()
                contenido_cifrado = self.cifrar(contenido, clave)

            nombre_archivo_cifrado = f"{nombre_archivo.split('.')[0]}_cifrado.txt"

            with open(nombre_archivo_cifrado, "w") as archivo_cifrado:
                archivo_cifrado.write(contenido_cifrado)
        except FileNotFoundError:
            print(f"No se encontró el archivo '{nombre_archivo}'.")

    def descifrar_archivo_cesar(self, nombre_archivo_cifrado, clave):
        try:
            with open(nombre_archivo_cifrado, "r")as archivo:
                contenido = archivo.read()
                contenido_descifrado = self.descifrar(contenido, clave)

            nombre_archivo_descifrado = f"{nombre_archivo_cifrado.split('_cifrado.')[0]}_descifrado.txt"

            with open(nombre_archivo_descifrado, "w") as archivo_cifrado:
                archivo_cifrado.write(contenido_descifrado)
        except FileNotFoundError:
            print(f"No se encontró el archivo '{contenido_descifrado}'.")

if __name__ == "__main__":
    cesar = Cesar()
    print(cesar.cifrar("Hola, me llamo Jaime", 16))


