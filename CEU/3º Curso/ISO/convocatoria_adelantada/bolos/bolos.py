class Partida:
    """
    CODIGO TEST 1
    def marcador(self, lanzamientos):
        return 0;
    """

    """
    CODIGO TEST 2 Y 3
    def marcador(self, lanzamientos):
        resultado = 0
        for i in range(0, len(lanzamientos)):
            if type(lanzamientos[i]) == list:
                ronda = lanzamientos[i]
                for bola in range(len(ronda)):
                    resultado += ronda[bola]
        return resultado
    """
    """
    CODIGO TEST 4,5,6 Y 7
    def marcador(self, lanzamientos):
        resultado = 0
        for i in range(0, len(lanzamientos)):
            if type(lanzamientos[i]) == list:
                ronda = lanzamientos[i]
                for bola in range(len(ronda)):
                    if ronda[bola] == "/":
                        tirada_anterior = ronda[bola-1]
                        siguiente_ronda = lanzamientos[i+1]
                        resultado += 10 + siguiente_ronda[0] - tirada_anterior
                    else:
                        resultado += ronda[bola]

        return resultado
    """
    """
    CODIGO TEST 8, 9 Y 10
    def marcador(self, lanzamientos):
        resultado = 0
        for i in range(0, len(lanzamientos)):
            if type(lanzamientos[i]) == list:
                ronda = lanzamientos[i]
                for bola in range(len(ronda)):
                    if ronda[bola] == "/":
                        tirada_anterior = ronda[bola - 1]
                        siguiente_ronda = lanzamientos[i + 1]
                        resultado += 10 + siguiente_ronda[0] - tirada_anterior
                    else:
                        resultado += ronda[bola]
            else:
                if lanzamientos[i] == "X":
                    siguiente_ronda = lanzamientos[i+1]
                    resultado += 10 + siguiente_ronda[0] + siguiente_ronda[1]
        return resultado
    """
    """
    CODIGO TEST 11 Y 12
    def marcador(self, lanzamientos):
        resultado = 0
        for i in range(0, len(lanzamientos)):
            if type(lanzamientos[i]) == list:
                ronda = lanzamientos[i]
                for bola in range(len(ronda)):
                    if ronda[bola] == "/":
                        tirada_anterior = ronda[bola - 1]
                        siguiente_ronda = lanzamientos[i + 1]
                        resultado += 10 + siguiente_ronda[0] - tirada_anterior
                    else:
                        resultado += ronda[bola]
            else:
                if lanzamientos[i] == "X":
                    siguiente_ronda = lanzamientos[i + 1]
                    if siguiente_ronda == "X":
                        siguiente_ronda2 = lanzamientos[i + 2]
                        resultado += 20 + siguiente_ronda2[0]
                    else:
                        resultado += 10 + siguiente_ronda[0] + siguiente_ronda[1]
        return resultado
    """
    """
    CODIGO TEST 13 Y 14
    def marcador(self, lanzamientos):
        resultado = 0
        for i in range(0, len(lanzamientos)):
            if type(lanzamientos[i]) == list:
                ronda = lanzamientos[i]
                for bola in range(len(ronda)):
                    if ronda[bola] == "/":
                        tirada_anterior = ronda[bola - 1]
                        siguiente_ronda = lanzamientos[i + 1]
                        resultado += 10 + siguiente_ronda[0] - tirada_anterior
                    else:
                        resultado += ronda[bola]
            else:
                if lanzamientos[i] == "X":
                    siguiente_ronda = lanzamientos[i + 1]
                    if siguiente_ronda == "X":
                        siguiente_ronda2 = lanzamientos[i + 2]
                        if siguiente_ronda2 == "X":
                            resultado += 30
                        else:
                            resultado += 20 + siguiente_ronda2[0]
                    else:
                        resultado += 10 + siguiente_ronda[0] + siguiente_ronda[1]
        return resultado
    """
    """
    CODIGO TEST 15, 16 17 Y 18
    def marcador(self, lanzamientos):
        resultado = 0
        for i in range(0, len(lanzamientos)):
            if type(lanzamientos[i]) == list:
                ronda = lanzamientos[i]
                for bola in range(len(ronda)):
                    if ronda[bola] == "/":
                        tirada_anterior = ronda[bola - 1]
                        siguiente_ronda = lanzamientos[i + 1]
                        resultado += 10 + siguiente_ronda[0] - tirada_anterior
                    else:
                        resultado += ronda[bola]
            else:
                if lanzamientos[i] == "X":
                    siguiente_ronda = lanzamientos[i + 1]
                    if siguiente_ronda == "X":
                        siguiente_ronda2 = lanzamientos[i + 2]
                        if siguiente_ronda2 == "X":
                            resultado += 30
                        else:
                            resultado += 20 + siguiente_ronda2[0]
                    else:
                        if siguiente_ronda[1] == "/":
                            resultado += 20
                        else:
                            resultado += 10 + siguiente_ronda[0] + siguiente_ronda[1]
        return resultado
    """
    """
    CODIGO TEST 21 ADELANTE
    """
    def marcador(self, lanzamientos):
        resultado = 0
        for i in range(0, len(lanzamientos)):
            if type(lanzamientos[i]) == list:
                ronda = lanzamientos[i]
                if i <= 9:
                    for bola in range(len(ronda)):
                        if ronda[bola] == "/":
                            tirada_anterior = ronda[bola - 1]
                            siguiente_ronda = lanzamientos[i + 1]
                            if siguiente_ronda == "X":
                                resultado += 20 - tirada_anterior
                            else:
                                resultado += 10 + siguiente_ronda[0] - tirada_anterior
                        else:
                            resultado += ronda[bola]
            else:
                if i <= 9 and lanzamientos[i] == "X":
                    siguiente_ronda = lanzamientos[i + 1]
                    if siguiente_ronda == "X":
                        siguiente_ronda2 = lanzamientos[i + 2]
                        if siguiente_ronda2 == "X":
                            resultado += 30
                        else:
                            resultado += 20 + siguiente_ronda2[0]
                    else:
                        if siguiente_ronda[1] == "/":
                            resultado += 20
                        else:
                            resultado += 10 + siguiente_ronda[0] + siguiente_ronda[1]
        return resultado
