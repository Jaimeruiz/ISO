import re
class Buscador():
    """
    CODIGO TEST 1
    def buscar_texto(self, texto, caracter):
        return 1
    """
    """
    CODIGO PARA TEST 2, 3, 4 Y 5
    def buscar_texto(self, texto, caracter):
        contador = 0
        for i in range(len(texto)):
            if caracter == texto[i]:
                contador += 1
        return contador
    """
    """
    CODIGOPARA TEST 6
    def buscar_texto(self, texto, caracter):
        contador = 0
        nuevo_texto = texto.split()
        if len(caracter) > 1:
            for i in range(len(nuevo_texto)):
                if caracter == nuevo_texto[i]:
                    contador += 1
        else:
            for i in range(len(texto)):
                if caracter == texto[i]:
                    contador += 1
        return contador
    """
    """
    CODIGO PARA TEST 7
    def buscar_texto(self, texto, caracter):
        contador = 0
        nuevo_texto = re.split(r'[^a-zA-Z]+', texto)
        if len(caracter) > 1:
            for i in range(len(nuevo_texto)):
                if caracter == nuevo_texto[i]:
                    contador += 1
        elif len(caracter) > 1
        else:
            for i in range(len(texto)):
                if caracter == texto[i]:
                    contador += 1
        return contador
    """
    """
    CODIGO PARA TEST 8
    def buscar_texto(self, texto, caracter):
        contador = 0
        if len(caracter) > 1 and caracter.isalpha():
            nuevo_texto = re.split(r'[^a-zA-Z]+', texto)
            for i in range(len(nuevo_texto)):
                if caracter == nuevo_texto[i]:
                    contador += 1
        if len(caracter) > 1 and not caracter.isalpha():
            nuevo_texto = texto.split()
            for i in range(len(nuevo_texto)):
                if caracter == nuevo_texto[i]:
                    contador += 1
        else:
            for i in range(len(texto)):
                if caracter == texto[i]:
                    contador += 1
        return contador
    """
    """
    #codigo para test 9 y 10.
    def buscar_texto(self, texto, caracter):
        contador = 0
        if len(caracter) > 1 and caracter.isalpha():  # Buscar palabra
            nuevo_texto = re.split(r'[^a-zA-Z]+', texto)
            for i in range(len(nuevo_texto)):
                if caracter == nuevo_texto[i]:
                    contador += 1

        elif len(caracter) > 1 and not caracter.isalpha():  # Buscar palabra con caracter especial o frase
            nuevo_texto = texto.split()
            nuevo_caracter = caracter.split(" ")
            if type(nuevo_caracter) == list:
                todos_alpha = all(palabra.isalpha() for palabra in nuevo_caracter) #recorre nuevo_caracter y verifica si cada palabra es alfabetica.(si una no lo es devuelve False)
                if todos_alpha: #para test 9
                    nuevo_texto_2 = [re.sub(r'[^a-zA-Z]', '', palabra) for palabra in texto.split()] #recorre la lista texto que se generea al dividir el texto por espacios, y sustituye con re.sub todo lo que no sean letras por '', con lo que al sustituirlo por '', lo quita
                    for i in range(len(nuevo_texto_2) - len(nuevo_caracter)):  #busca la diferencia entre el texto y lo que buscamos para saber la longitud  de frase que debe buscar para encontrar coincidencia.
                        if nuevo_texto_2[i:i + len(nuevo_caracter)] == nuevo_caracter: #busca si una subsecuencia en texto_2 desde la iteracion actual de i hasta la longitud de la expresion es igual a la propia expresion que busca
                            contador += 1 #ejemplo anterior nuevo_texto_2[0:3], nuevo_texto_2[1:4], nuevo_texto_2[2:5]... 
                else: #para test 10
                    for i in range(len(nuevo_texto) - len(nuevo_caracter)):  # Iterar hasta la longitud posible de coincidencia
                        if nuevo_texto[i:i + len(nuevo_caracter)] == nuevo_caracter:
                            contador += 1
            else:
                for i in range(len(nuevo_texto)):
                    if caracter == nuevo_texto[i]:
                        contador += 1

        else:  # Buscar letra o caracter especial
            for i in range(len(texto)):
                if caracter == texto[i]:
                    contador += 1

        return contador
    
    """
    #REFACTOR
    def buscar_texto(self, texto, caracter):
        contador = texto.count(caracter)
        return contador

buscador = Buscador()
with open(r'C:\Users\jaime\OneDrive\Escritorio\CEU\3º Curso\PED\2022\Examen_ordinaria_2021\frases', 'r') as archivo:
    contenido = archivo.read()
print(buscador.buscar_texto(contenido, 'a'))


