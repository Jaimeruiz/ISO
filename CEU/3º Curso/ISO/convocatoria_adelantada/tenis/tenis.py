import math
class Partido():
    def __init__(self):
        self.puntosA = 0
        self.puntosB = 0
        self.breaksA = 0
        self.breaksB = 0
        self.setsA = 0
        self.setsB = 0
        self.puntuacion = ["0", "15", "30", "40", "AD"]
        self.sets = 0
        self.marcador = ""
    """
    def calcular_marcador(self, marcador):
        for punto in marcador:
            if punto == "A":
                self.puntosA += 1
                if self.puntosA == 1:
                    self.marcadorA = 15 #Test 1
                elif self.puntosA == 2:
                    self.marcadorA = 30 #Test2
                elif self.puntosA == 3:
                    self.marcadorA = 40 #Test3
                else:
                    if self.puntosA == 4 and self.puntosB == 3:
                        self.marcadorA = "AD" #Test15
                    elif self.puntosA == 4 and self.puntosB == 4:
                        self.marcadorA = 40
                        self.marcadorB = 40
                        self.puntosA = 3
                        self.puntosB = 3 #Test16
                    else:
                        self.marcadorA = 0 #Test4
                        self.marcadorB = 0
            else:
                self.puntosB += 1
                if self.puntosB == 1:
                    self.marcadorB = 15 #Test5
                elif self.puntosB == 2:
                    self.marcadorB = 30 #Test6
                elif self.puntosB == 3:
                    self.marcadorB = 40 #Test7
                else:
                    if self.puntosA == 4 and self.puntosB == 3:
                        self.marcadorB = "AD"
                        elif self.puntosA == 4 and self.puntosB == 4:
                        self.marcadorA = 40
                        self.marcadorB = 40
                        self.puntosA = 3
                        self.puntosB = 3 #Test17
                    else:
                        self.marcadorA = 0  # Test8
                        self.marcadorB = 0

        return f"{self.setsA} - {self.setsB} \n" \
                   f"{self.breaksA} - {self.breaksB} \n" \
                   f"{self.puntuacion[self.puntosA]} - {self.puntuacion[self.puntosB]}"
    """
    def set_valido(self, sets):
        return sets % 2 == 1 and sets < 5

    def introducir_sets(self):
        while True:
            try:
                self.sets = int(input("Introduce el número de sets (debe ser impar y menor que 5): "))
                if self.sets % 2 != 1 or self.sets > 5:
                    raise ValueError("El número de sets debe ser impar y menor o igual que 5.")
                break
            except ValueError as e:
                print(f"Error: {e}", end="")
        if self.set_valido(self.sets):
            secuencia = str(input("Introduzca la secuencia de puntos del partido: \n"))
            self.marcador = list(secuencia)

  #REFACTOR1 METODO CALCULAR
    def calcular_marcador(self, marcador):
        for punto in marcador:
            if punto == "A" and not self.tieBreak(self.breaksA, self.breaksB):
                self.puntosA += 1
                if self.breakA(self.puntosA, self.puntosB):
                    self.puntosA = 0
                    self.puntosB = 0
                    self.breaksA += 1
                if self.puntosA == self.puntosB == 4:
                    self.puntosA -= 1
                    self.puntosB -= 1
                if self.setA(self.breaksA, self.breaksB):
                    self.breaksA = 0
                    self.breaksB = 0
                    self.setsA += 1
            elif punto == "B" and not self.tieBreak(self.breaksA, self.breaksB):
                self.puntosB += 1
                if self.breakB(self.puntosA, self.puntosB):
                    self.puntosA = 0
                    self.puntosB = 0
                    self.breaksB += 1
                if self.puntosA == self.puntosB == 4:
                    self.puntosA -= 1
                    self.puntosB -= 1
                if self.setB(self.breaksA, self.breaksB):
                    self.breaksA = 0
                    self.breaksB = 0
                    self.setsB += 1
            elif self.tieBreak(self.breaksA, self.breaksB):
                if punto == "A":
                    self.puntosA += 1
                    if self.tieBreakA(self.puntosA, self.puntosB, self.breaksA, self.breaksB):
                        self.puntosA = 0
                        self.puntosB = 0
                        self.setsA += 1
                        self.breaksA = 0
                        self.breaksB = 0
                else:
                    self.puntosB += 1
                    if self.tieBreakB(self.puntosA, self.puntosB, self.breaksA, self.breaksB):
                        self.puntosA = 0
                        self.puntosB = 0
                        self.setsB += 1
                        self.breaksA = 0
                        self.breaksB = 0
        if self.tieBreak(self.breaksA, self.breaksB):
            return f"{self.setsA} - {self.setsB} \n" \
               f"{self.breaksA} - {self.breaksB} \n" \
               f"{self.puntosA} - {self.puntosB}"
        else:
            return f"{self.setsA} - {self.setsB} \n" \
                   f"{self.breaksA} - {self.breaksB} \n" \
                   f"{self.puntuacion[self.puntosA]} - {self.puntuacion[self.puntosB]}"

    def breakA(self, puntosA, puntosB):
        return puntosA >= 4 and puntosA - puntosB >= 2  #Test9 a 11

    def breakB(self, puntosA, puntosB):
        return puntosB >= 4 and puntosB - puntosA >= 2 #Test 12 a 14

    def setA(self, breaksA, breaksB):
        return breaksA >= 6 and breaksA - breaksB >= 2 #Test 18 y 22 (cambiar == por >= del 19 al 21)

    def setB(self, breaksA, breaksB):
        return breaksB >= 6 and breaksB - breaksA >= 2 #Test 19 a 21 (cambiar == por >= del 19 al 21)

    def tieBreak(self, breaksA, breaksB):
        return breaksA == breaksB == 6 #Test 23

    def tieBreakA(self, puntosTieA, puntosTieB, breaksA, breaksB):
        return breaksA == breaksB == 6 and puntosTieA >= 7 and puntosTieA - puntosTieB >= 2 #Test 24

    def tieBreakB(self, puntosTieA, puntosTieB, breaksA, breaksB):
        return breaksA == breaksB == 6 and puntosTieB >=7 and puntosTieB - puntosTieA >= 2 #Test 25 y 26

    def resultado(self, setsA, setsB, sets, breaksA, breaksB, puntosA, puntosB):
        setsJ = setsA + setsB
        breaks = breaksA + breaksB
        puntos = puntosA + puntosB
        if (setsJ > sets) or (setsJ == sets and breaks > 0) or (setsJ == sets and puntos > 0):
            raise ValueError("RESULTADO INCORRECTO")
        elif setsJ < sets:
            sorted_sets = sorted([setsA, setsB], reverse=True)
            if math.ceil(sets / 2) > sorted_sets[0]:
               return "EL PARTIDO ESTA EN JUEGO"
            elif math.ceil(sets / 2) == sorted_sets[0] and breaks == puntos == 0:
                if setsA > setsB:
                    return "PARTIDO FINALIZADO, GANA EL JUGADOR A"
                else:
                    return "PARTIDO FINALIZADO, GANA EL JUGADOR B"
            else:
                raise ValueError("RESULTADO INCORRECTO")
        else:
            if setsA > setsB:
                return "PARTIDO FINALIZADO, GANA EL JUGADOR A"
            else:
                return "PARTIDO FINALIZADO, GANA EL JUGADOR B"

if __name__ == "__main__":
    partido = Partido()
    partido.introducir_sets()
    print(partido.calcular_marcador(partido.marcador))
    print(partido.resultado(partido.setsA,partido.setsB,partido.sets,partido.breaksA,
          partido.breaksB,partido.puntosA,partido.puntosB))



