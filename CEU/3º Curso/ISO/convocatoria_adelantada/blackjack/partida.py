import random
class Partida():
    def __init__(self):
        self.cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.valores = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 10),
               ('Q', 10), ('K', 10), ('A', 11)]


    def obtener_carta(self, cartas):
        """Obtiene una carta aleatoria y la remueve de la lista de cartas."""
        carta = random.choice(cartas)
        cartas.remove(carta)
        return carta


    def calcular_puntaje(self, mano, valores):
        """Calcula el puntaje de una mano de cartas."""
        puntaje = 0
        ases = 0
        for carta in mano:
            for valor_carta, valor in valores:
                if carta == valor_carta:
                    puntaje += valor
                    if carta == 'A':
                        ases += 1
        while ases > 0 and puntaje > 21:
            puntaje -= 10
            ases -= 1
        return puntaje


    def jugar_blackjack(self):
        print("¡Bienvenido al Blackjack!")
        jugador = []
        crupier = []

        # Repartir las primeras dos cartas a cada jugador
        for _ in range(2):
            jugador.append(self.obtener_carta(self.cartas))
            crupier.append(self.obtener_carta(self.cartas))

        while True:
            print(f"\nTus cartas: {jugador}, Puntaje: {self.calcular_puntaje(jugador, self.valores)}")
            print(f"Carta del crupier: {crupier[0]}")

            # Verificar si el jugador ha superado los 21 puntos
            if self.calcular_puntaje(jugador, self.valores) > 21:
                print("Has superado los 21 puntos. ¡Has perdido!")
                break

            # Preguntar al jugador si desea pedir otra carta o plantarse
            opcion = input("¿Deseas pedir otra carta (p) o plantarte (pl)? ").lower()

            if opcion == 'p':
                jugador.append(self.obtener_carta(self.cartas))
            elif opcion == 'pl':
                # El crupier toma cartas hasta alcanzar un puntaje de al menos 17
                while self.calcular_puntaje(crupier, self.valores) < 17:
                    crupier.append(self.obtener_carta(self.cartas))

                print(f"\nTus cartas: {jugador}, Puntaje: {self.calcular_puntaje(jugador, self.valores)}")
                print(f"Cartas del crupier: {crupier}, Puntaje: {self.calcular_puntaje(crupier, self.valores)}")

                # Determinar el resultado
                if self.calcular_puntaje(crupier, self.valores) > 21:
                    print("El crupier ha superado los 21 puntos. ¡Has ganado!")
                elif self.calcular_puntaje(jugador, self.valores) > self.calcular_puntaje(crupier, self.valores):
                    print("¡Has ganado!")
                elif self.calcular_puntaje(jugador, self.valores) < self.calcular_puntaje(crupier, self.valores):
                    print("¡Has perdido!")
                else:
                    print("Es un empate.")

                break
            else:
                print("Opción no válida. Por favor, elige 'p' para pedir carta o 'pl' para plantarte.")


partida = Partida()
partida.jugar_blackjack()
