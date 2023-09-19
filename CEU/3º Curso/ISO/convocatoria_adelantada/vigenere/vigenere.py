
class Vigenere():
    """
    codigo test1
    def cifrar(self, texto, clave):
        return "hello"
    """
    """
    CODIGO PARA TEST 2
    def cifrar(self, texto, clave):
        texto_cifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(texto)):
            if texto[i] in alfabeto:
                posicion_deesplazada = alfabeto.index(clave[i])
                nueva_letra = alfabeto.index(texto[i])
                desplazamiento = posicion_deesplazada + nueva_letra
                texto_cifrado += alfabeto[desplazamiento]

        return texto_cifrado
    """

    """
    CODIGO TEST 3
    def cifrar(self, texto, clave):
        texto_cifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(texto)):
            if texto[i] in alfabeto:
                posicion_deesplazada = alfabeto.index(clave[i])
                nueva_letra = alfabeto.index(texto[i])
                desplazamiento = (posicion_deesplazada + nueva_letra) % len(alfabeto)
                texto_cifrado += alfabeto[desplazamiento]

        return texto_cifrado
    """
    """
    def cifrar(self, texto, clave):
        texto_cifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(texto)):
                if texto[i].isupper() and texto[i].lower() in alfabeto: 
                    posicion_desplazada = alfabeto.index(clave[i].lower())
                    nueva_letra = alfabeto.index(texto[i].lower())
                    desplazamiento = (posicion_desplazada + nueva_letra) % len(alfabeto)
                    texto_cifrado += alfabeto[desplazamiento].upper()
                else:
                    posicion_desplazada = alfabeto.index(clave[i])
                    nueva_letra = alfabeto.index(texto[i].lower())
                    desplazamiento = (posicion_desplazada + nueva_letra) % len(alfabeto)
                    texto_cifrado += alfabeto[desplazamiento]
        return texto_cifrado
    """
    def cifrar(self, texto, clave):
        texto_cifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        clave = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)] #la añado para pasar test7
        for i in range(len(texto)):
            if texto[i].isalpha() and clave[i].isalpha(): #añadido para pasar test6
                if texto[i].isupper() and texto[i].lower() in alfabeto:
                    posicion_desplazada = alfabeto.index(clave[i].lower())
                    nueva_letra = alfabeto.index(texto[i].lower())
                    desplazamiento = (nueva_letra + posicion_desplazada) % len(alfabeto)
                    texto_cifrado += alfabeto[desplazamiento].upper()
                else:
                    posicion_desplazada = alfabeto.index(clave[i])
                    nueva_letra = alfabeto.index(texto[i].lower())
                    desplazamiento = (nueva_letra + posicion_desplazada) % len(alfabeto)
                    texto_cifrado += alfabeto[desplazamiento]
            else: #añadido para pasar test6
                texto_cifrado += texto[i]
        return texto_cifrado

    def descifrar(self, texto, clave):
        texto_descifrado = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        clave = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)] #la añado para pasar test7
        for i in range(len(texto)):
            if texto[i].isalpha() and clave[i].isalpha(): #añadido para pasar test6
                if texto[i].isupper() and texto[i].lower() in alfabeto:
                    posicion_desplazada = alfabeto.index(clave[i].lower())
                    nueva_letra = alfabeto.index(texto[i].lower())
                    desplazamiento = (nueva_letra - posicion_desplazada) % len(alfabeto)
                    texto_descifrado += alfabeto[desplazamiento].upper()
                else:
                    posicion_desplazada = alfabeto.index(clave[i])
                    nueva_letra = alfabeto.index(texto[i].lower())
                    desplazamiento = (nueva_letra - posicion_desplazada) % len(alfabeto)
                    texto_descifrado += alfabeto[desplazamiento]
            else: #añadido para pasar test6
                texto_descifrado += texto[i]
        return texto_descifrado

    def cifrar_archivo_vigenere(self, nombre_archivo, clave):
        try:
            with open(nombre_archivo, "r")as archivo:
                contenido = archivo.read()
                contenido_cifrado = self.cifrar(contenido, clave)

            nombre_archivo_cifrado = f"{nombre_archivo.split('.')[0]}_cifrado.txt"

            with open(nombre_archivo_cifrado, "w") as archivo_cifrado:
                archivo_cifrado.write(contenido_cifrado)
        except FileNotFoundError:
            print(f"No se encontró el archivo '{nombre_archivo}'.")

    def descifrar_archivo_vigenere(self, nombre_archivo_cifrado, clave):
        try:
            with open(nombre_archivo_cifrado, "r")as archivo:
                contenido = archivo.read()
                contenido_descifrado = self.descifrar(contenido, clave)

            nombre_archivo_descifrado = f"{nombre_archivo_cifrado.split('_cifrado.')[0]}_descifrado.txt"

            with open(nombre_archivo_descifrado, "w") as archivo_cifrado:
                archivo_cifrado.write(contenido_descifrado)
        except FileNotFoundError:
            print(f"No se encontró el archivo '{contenido_descifrado}'.")