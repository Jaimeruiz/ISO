import re
import turtle
import tkinter as tk
class Dibujo():

    def __init__(self):
        # Configurar la ventana de dibujo
        self.ventana = turtle.Screen()
        self.ventana.title("Dibujando con comandos")
        self.ventana.bgcolor("white")
        self.lapiz = turtle.Turtle()
        self.lapiz.speed(1)

        # Crear una ventana emergente de tkinter para la entrada de comandos
        self.ventana_comandos = tk.Tk()
        self.ventana_comandos.title("Comandos")
        self.entrada_comandos = tk.Entry(self.ventana_comandos)
        self.entrada_comandos.pack()
        self.entrada_comandos.bind('<Return>', self.ejecutar_comandos)  # Bind Enter key
        self.boton_ejecutar = tk.Button(self.ventana_comandos, text="Ejecutar", command=self.ejecutar_comandos)
        self.boton_ejecutar.pack()

    def ejecutar_comandos(self, event=None):
        comandos = self.entrada_comandos.get()
        # Dividir los comandos en una lista de comandos individuales
        comandos = comandos.split()

        # Ejecutar los comandos uno por uno en la ventana de dibujo
        self.dibujar(comandos)
        self.entrada_comandos.delete(0, 'end')

    def dibujar(self, comandos):
        for i in comandos:
            if i == "ABJ":
                self.lapiz.pendown()
            elif i == "ARR":
                self.lapiz.penup()
            elif i == "NOR1":
                self.lapiz.setheading(90)
                self.lapiz.forward(10)
            elif i == "SUR1":
                self.lapiz.setheading(270)
                self.lapiz.forward(10)
            elif i == "EST1":
                self.lapiz.setheading(0)
                self.lapiz.forward(10)
            elif i == "OES1":
                self.lapiz.setheading(180)
                self.lapiz.forward(10)
            elif i == "CIRC":
                self.lapiz.circle(10)
            elif i == "SALIR":
                self.ventana_comandos.destroy()
                self.ventana.bye()
            else:
                print("COMANDO no válido")
"""
dibujo = Dibujo()
turtle.done()
"""
