import re
class Palindromo():
    """
    CODIGO TEST1
    def invertir(self, texto):
        return "a"
    """
    """
    CODIGO TEST 2
        def invertir(self, texto):
        texto_invertido = ""
        for i in range(len(texto)):
            if texto[i] == texto[len(texto)-1-i]:
                texto_invertido += texto[len(texto)-1-i]
        return texto_invertido
    """
    """
    CODIGO PARA PASAR TEST 3 Y 4
        def invertir(self, texto):
        texto_invertido = ""
        for i in range(len(texto)):
            if texto[i] == texto[len(texto)-1-i] and texto[i].isalpha:
                texto_invertido += texto[len(texto)-1-i]
            else:
                return "No es un palindromo"
        return f"{texto_invertido} es un palindromo"
    """
    """
    CODIGO PARA PASAR TEST 5 Y 6
     def invertir(self, texto):
        texto_invertido = ""
        for i in range(len(texto)):
            if texto[i] == texto[len(texto)-1-i] and texto[i].isalpha:
                texto_invertido += texto[len(texto)-1-i]
            elif texto[i] == texto[len(texto) - 1 - i] and texto[i].isdigit():
                texto_invertido += texto[len(texto)-1-i]
            else:
                return "No es un palindromo"
        if texto_invertido.isalpha():
            return f"{texto_invertido} es un palindromo"
        else:
            return f"{texto_invertido} es capicua"
    """
    """
    CODIGO PARA TEST 7
        def invertir(self, texto):
        texto_invertido = ""
        nuevo_texto = texto.replace(" ", "").lower()
        for i in range(len(nuevo_texto)):
            if nuevo_texto[i] == nuevo_texto[len(nuevo_texto)-1-i] and texto.isalpha:
                texto_invertido += nuevo_texto[len(nuevo_texto)-1-i]
            elif nuevo_texto[i] == nuevo_texto[len(nuevo_texto) - 1 - i] and texto.isdigit():
                texto_invertido += nuevo_texto[len(nuevo_texto)-1-i]
            elif nuevo_texto[i] == nuevo_texto[len(nuevo_texto)-1-i] and not texto.isalpha:
                if nuevo_texto[i] == nuevo_texto[len(nuevo_texto) - 1 - i]:
                    texto_invertido += nuevo_texto[len(nuevo_texto)-1-i]
            else:
                return "No es un palindromo"
        if texto.isalpha():
            return f"{texto_invertido} es un palindromo"
        elif texto.isnumeric():
            return f"{texto_invertido} es capicua"
        else:
            return f"{texto} es una oracion palindroma"
    """
    #REFACTOR 1
    """
        def invertir(self, texto):
        texto_invertido = ""
        nuevo_texto = texto.replace(" ", "").lower()
        for i in range(len(nuevo_texto)):
            if nuevo_texto[i] == nuevo_texto[len(nuevo_texto) - 1 - i]:
                texto_invertido += nuevo_texto[i]
            else:
                return "No es un palindromo"
        if texto.isalpha():
            return f"{texto_invertido} es un palindromo"
        elif texto.isnumeric():
            return f"{texto_invertido} es capicua"
        else:
            return f"{texto} es una oracion palindroma"
    """

    #REFACTOR 2 Y codigo para para pasar test 9
    def invertir(self, texto):
        nuevo_texto_2 = re.sub(r'[^a-zA-Z,]', '', texto.lower()) #con esta linea pasa el test 9
        nuevo_texto_3 = re.sub(r'[^a-zA-Z]', '', nuevo_texto_2.lower()) #test10
        if texto.isalpha() and nuevo_texto_2 == nuevo_texto_2[::-1] and nuevo_texto_2.isalpha():
            return f"{texto} es un palindromo"
        elif texto.isnumeric() and texto == texto[::-1]:
            return f"{texto} es capicua"
        elif texto.isnumeric() and not texto == texto[::-1]: #codigo para test 8
            return f"{texto} no es capicua"
        elif not texto.isalpha() and nuevo_texto_2 == nuevo_texto_2[::-1] and nuevo_texto_2.isalpha():
            return f"{texto} es una oracion palindroma"
        elif not texto.isalpha() and nuevo_texto_3 == nuevo_texto_3[::-1] and not nuevo_texto_2.isalpha(): #test 10
            return f"{texto} es un palindromo parcial"
        else:
            return "No es un palindromo"

palindromo = Palindromo()
print(palindromo.invertir("A luna ese anula"))

