import unittest
from partida import *
class TestPartida(unittest.TestCase):

    def test_obtener_carta(self):
        partida = Partida()
        carta = partida.obtener_carta(partida.cartas)
        self.assertIn(carta, partida.cartas)

    def test_calcular_puntaje(self):
        partida = Partida()
        mano = ['2', 'A']
        puntaje = partida.calcular_puntaje(mano, partida.valores)
        self.assertEqual(puntaje, 13)

    def test_jugar_blackjack_ganar(self):
        partida = Partida()
        partida.cartas = ['2', 'A', 'K', '7']
        resultado = partida.jugar_blackjack()
        self.assertEqual(resultado, "¡Has ganado!")

    def test_jugar_blackjack_perder(self):
        partida = Partida()
        partida.cartas = ['10', 'K', 'A']
        resultado = partida.jugar_blackjack()
        self.assertEqual(resultado, "¡Has perdido!")

    def test_jugar_blackjack_empatar(self):
        partida = Partida()
        partida.cartas = ['10', 'K', '7', '3', '5']
        resultado = partida.jugar_blackjack()
        self.assertEqual(resultado, "Es un empate!")

if __name__ == "__main__":
    unittest.main()
