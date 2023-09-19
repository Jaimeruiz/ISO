import re
import turtle
import tkinter as tk

class Figura:
    def dibujar(self, lapiz):
        pass

class Linea(Figura):
    def __init__(self, direccion):
        self.direccion = direccion

    def dibujar(self, lapiz):
        if self.direccion == "NOR1":
            lapiz.setheading(90)
        elif self.direccion == "SUR1":
            lapiz.setheading(270)
        elif self.direccion == "EST1":
            lapiz.setheading(0)
        elif self.direccion == "OES1":
            lapiz.setheading(180)
        lapiz.forward(10)

class LevantarLapiz(Figura):
    def dibujar(self, lapiz):
        lapiz.penup()

class BajarLapiz(Figura):
    def dibujar(self, lapiz):
        lapiz.pendown()

class Circulo(Figura):
    def dibujar(self, lapiz):
        lapiz.circle(10)

class Cuadrado(Figura):
    def dibujar(self, lapiz):
        for _ in range(4):
            lapiz.forward(10)
            lapiz.left(90)

class FiguraFactory:
    def crear_figura(self, comando):
        if comando in ["NOR1", "SUR1", "EST1", "OES1"]:
            return Linea(comando)
        elif comando == "CIRC":
            return Circulo()
        elif comando == "CUAD":
            return Cuadrado()
        elif comando == "ABJ":
            return BajarLapiz()
        elif comando == "ARR":
            return LevantarLapiz()
        else:
            return None

class Dibujo():
    def __init__(self):
        self.ventana = turtle.Screen()
        self.ventana.title("Dibujando con comandos")
        self.ventana.bgcolor("white")
        self.lapiz = turtle.Turtle()
        self.lapiz.speed(1)

        self.ventana_comandos = tk.Tk()
        self.ventana_comandos.title("Comandos")
        self.entrada_comandos = tk.Entry(self.ventana_comandos)
        self.entrada_comandos.pack()
        self.entrada_comandos.bind('<Return>', self.ejecutar_comandos)
        self.boton_ejecutar = tk.Button(self.ventana_comandos, text="Ejecutar", command=self.ejecutar_comandos)
        self.boton_ejecutar.pack()

        self.factory = FiguraFactory()

    def ejecutar_comandos(self, event=None):
        comandos = self.entrada_comandos.get()
        comandos = comandos.split()

        self.dibujar(comandos)
        self.entrada_comandos.delete(0, 'end')

    def dibujar(self, comandos):
        for comando in comandos:
            figura = self.factory.crear_figura(comando)
            if figura:
                figura.dibujar(self.lapiz)
            else:
                print("COMANDO no válido")
"""
dibujo = Dibujo()
turtle.done()
"""