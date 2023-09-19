import unittest
from tenis import *
import io
import sys
from io import StringIO
from unittest.mock import patch
class testtenis(unittest.TestCase):

    def test28(self):
        partido = Partido()
        output = StringIO()
        sys.stdout = output
        self.assertEqual(False, partido.set_valido(2))

    def test_set_valido(self):
        partido = Partido()
        output = StringIO()
        sys.stdout = output
        self.assertEqual(True, partido.set_valido(3))

    def test1(self):
        partido = Partido()
        marcador = ["A"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "15 - 0", partido.calcular_marcador(marcador))

    def test2(self):
        partido = Partido()
        marcador = ["A", "A"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "30 - 0", partido.calcular_marcador(marcador))

    def test3(self):
        partido = Partido()
        marcador = ["A", "A", "A"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "40 - 0", partido.calcular_marcador(marcador))

    #Poner como test despues de crear y probar el metodo breakA
    def test4(self):
        partido = Partido()
        marcador = ["A", "A", "A", "A"]
        self.assertEqual("0 - 0 \n"
                         "1 - 0 \n"
                         "0 - 0", partido.calcular_marcador(marcador))

    def test5(self):
        partido = Partido()
        marcador = ["B"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "0 - 15", partido.calcular_marcador(marcador))

    def test6(self):
        partido = Partido()
        marcador = ["B", "B", "A", "A"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "30 - 30", partido.calcular_marcador(marcador))

    def test7(self):
        partido = Partido()
        marcador = ["B", "B", "B","A"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "15 - 40", partido.calcular_marcador(marcador))

    # Poner como test despues de crear y probar el metodo breakB
    def test8(self):
        partido = Partido()
        marcador = ["B", "B", "B", "B"]
        self.assertEqual("0 - 0 \n"
                         "0 - 1 \n"
                         "0 - 0", partido.calcular_marcador(marcador))

    def test9(self):
        partido = Partido()
        puntosA = 4
        puntosB = 0
        self.assertEqual(True, partido.breakA(puntosA, puntosB))

    def test10(self):
        partido = Partido()
        puntosA = 4
        puntosB = 2
        self.assertEqual(True, partido.breakA(puntosA, puntosB))

    def test11(self):
        partido = Partido()
        puntosA = 4
        puntosB = 3
        self.assertEqual(False, partido.breakA(puntosA, puntosB))

    def test12(self):
        partido = Partido()
        puntosA = 1
        puntosB = 4
        self.assertEqual(True, partido.breakB(puntosA, puntosB))

    def test13(self):
        partido = Partido()
        puntosA = 2
        puntosB = 4
        self.assertEqual(True, partido.breakB(puntosA, puntosB))

    def test14(self):
        partido = Partido()
        puntosA = 3
        puntosB = 4
        self.assertEqual(False, partido.breakB(puntosA, puntosB))

    #Poner antes de los test breakA y breakB
    def test15(self):
        partido = Partido()
        marcador = ["B", "B", "B","A","A","A","A"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "AD - 40", partido.calcular_marcador(marcador))

    #Poner antes de los test breakA y breakB
    def test16(self):
        partido = Partido()
        marcador = ["B", "B", "B","A","A","A","A","B"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "40 - 40", partido.calcular_marcador(marcador))

    #Poner antes de los test breakA y breakB
    def test17(self):
        partido = Partido()
        marcador = ["B", "B", "B","A","A","A","B"]
        self.assertEqual("0 - 0 \n"
                         "0 - 0 \n"
                         "40 - AD", partido.calcular_marcador(marcador))

    def test18(self):
        partido = Partido()
        breaksA = 6
        breaksB = 2
        self.assertEqual(True, partido.setA(breaksA, breaksB))

    def test19(self):
        partido = Partido()
        breaksA = 4
        breaksB = 6
        self.assertEqual(True, partido.setB(breaksA, breaksB))

    def test20(self):
        partido = Partido()
        breaksA = 5
        breaksB = 6
        self.assertEqual(False, partido.setB(breaksA, breaksB))

    def test21(self):
        partido = Partido()
        breaksA = 6
        breaksB = 6
        self.assertEqual(False, partido.setB(breaksA, breaksB))

    def test22(self):
        partido = Partido()
        breaksA = 7
        breaksB = 5
        self.assertEqual(True, partido.setA(breaksA, breaksB))

    def test23(self):
        partido = Partido()
        breaksA = 6
        breaksB = 6
        self.assertEqual(True, partido.tieBreak(breaksA, breaksB))

    def test24(self):
        partido = Partido()
        breaksA = 6
        breaksB = 6
        puntosTieA = 7
        puntosTieB = 4
        self.assertEqual(True, partido.tieBreakA(puntosTieA, puntosTieB,breaksA, breaksB))

    def test25(self):
        partido = Partido()
        breaksA = 6
        breaksB = 6
        puntosTieA = 6
        puntosTieB = 8
        self.assertEqual(False, partido.tieBreakA(puntosTieA, puntosTieB,breaksA, breaksB))

    def test26(self):
        partido = Partido()
        breaksA = 6
        breaksB = 6
        puntosTieA = 6
        puntosTieB = 7
        self.assertEqual(False, partido.tieBreakA(puntosTieA, puntosTieB,breaksA, breaksB))


    def test27(self):
        partido = Partido()
        marcador = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A",
                    "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A",
                    "B", "B", "B"]
        self.assertEqual("1 - 0 \n"
                         "1 - 0 \n"
                         "0 - 40", partido.calcular_marcador(marcador))

    def test_PartidoAcabadoTresSetsA1(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR A", partido.resultado(2, 1, 3, 0, 0, 0, 0))

    def test_PartidoAcabadoTresSetsB1(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR B", partido.resultado(1, 2, 3, 0, 0, 0, 0))

    def test_PartidoAcabadoTresSetsA2(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR A", partido.resultado(2, 0, 3, 0, 0, 0, 0))

    def test_PartidoAcabadoTresSetsB2(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR B", partido.resultado(0, 2, 3, 0, 0, 0, 0))

    def test_PartidoAcabadoCincoSetsA1(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR A", partido.resultado(3, 0, 5, 0, 0, 0, 0))

    def test_PartidoAcabadoCincoSetsB1(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR B", partido.resultado(0, 3, 5, 0, 0, 0, 0))

    def test_PartidoAcabadoCincoSetsA2(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR A", partido.resultado(3, 1, 5, 0, 0, 0, 0))

    def test_PartidoAcabadoCincoSetsB2(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR B", partido.resultado(1, 3, 5, 0, 0, 0, 0))

    def test_PartidoAcabadoCincoSetsA3(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR A", partido.resultado(3, 2, 5, 0, 0, 0, 0))

    def test_PartidoAcabadoCincoSetsB3(self):
        partido = Partido()
        self.assertEqual("PARTIDO FINALIZADO, GANA EL JUGADOR B", partido.resultado(2, 3, 5, 0, 0, 0, 0))

    def test_PartidoSinAcabarTresSetsA1(self):
        partido = Partido()
        self.assertEqual("EL PARTIDO ESTA EN JUEGO", partido.resultado(1, 0, 3, 0, 0, 0, 0))

    def test_PartidoSinAcabarTresSetsB1(self):
        partido = Partido()
        self.assertEqual("EL PARTIDO ESTA EN JUEGO", partido.resultado(0, 1, 3, 0, 0, 0, 0))

    def test_PartidoSinAcabarCincoSetsA1(self):
        partido = Partido()
        self.assertEqual("EL PARTIDO ESTA EN JUEGO", partido.resultado(2, 0, 5, 3, 0, 0, 0))

    def test_PartidoSinAcabarcincoSetsB1(self):
        partido = Partido()
        self.assertEqual("EL PARTIDO ESTA EN JUEGO", partido.resultado(0, 2, 5, 0, 0, 0, 2))

    def test_PartidoSinAcabarCincoSetsA2(self):
        partido = Partido()
        self.assertEqual("EL PARTIDO ESTA EN JUEGO", partido.resultado(2, 2, 5, 5, 0, 3, 0))

    def test_PartidoSinAcabarcincoSetsB1(self):
        partido = Partido()
        self.assertEqual("EL PARTIDO ESTA EN JUEGO", partido.resultado(1, 2, 5, 0, 0, 0, 0))

    def test_PartidoSinAcabarcincoSetsTieBreak(self):
        partido = Partido()
        self.assertEqual("EL PARTIDO ESTA EN JUEGO", partido.resultado(1, 2, 5, 6, 6, 2, 4))

    def test_MarcadorIncorrecto1(self):
        partido = Partido()
        with self.assertRaises(ValueError):
            partido.resultado(4, 0, 3, 0, 0, 0, 0)

    def test_MarcadorIncorrecto2(self):
        partido = Partido()
        with self.assertRaises(ValueError):
            partido.resultado(2, 1, 3, 1, 0, 0, 0)

    def test_MarcadorIncorrecto3(self):
        partido = Partido()
        with self.assertRaises(ValueError):
            partido.resultado(3, 0, 3, 0, 0, 1, 0)

    def test_MarcadorIncorrecto4(self):
        partido = Partido()
        with self.assertRaises(ValueError):
            partido.resultado(0, 4, 3, 0, 0, 0, 0)

    def test_MarcadorIncorrecto5(self):
        partido = Partido()
        with self.assertRaises(ValueError):
            partido.resultado(0, 3, 3, 0, 1, 0, 0)

    def test_MarcadorIncorrecto6(self):
        partido = Partido()
        with self.assertRaises(ValueError):
            partido.resultado(0, 3, 3, 0, 0, 0, 1)

if __name__ == '__main__':
    unittest.main()



