import turtle
import tkinter as tk

class Dibujo():
    def __init__(self):
        # Configurar la ventana de dibujo
        self.ventana = turtle.Screen()
        self.ventana.title("Dibujando con botones")
        self.ventana.bgcolor("white")
        self.lapiz = turtle.Turtle()
        self.lapiz.speed(1)
        self.lapiz.penup()

        # Crear una ventana emergente de tkinter para los botones
        self.ventana_botones = tk.Tk()
        self.ventana_botones.title("Botones")
        self.boton_abajo = tk.Button(self.ventana_botones, text="Abajo", command=self.abajo)
        self.boton_arriba = tk.Button(self.ventana_botones, text="Arriba", command=self.arriba)
        self.boton_norte = tk.Button(self.ventana_botones, text="Norte", command=self.norte)
        self.boton_sur = tk.Button(self.ventana_botones, text="Sur", command=self.sur)
        self.boton_este = tk.Button(self.ventana_botones, text="Este", command=self.este)
        self.boton_oeste = tk.Button(self.ventana_botones, text="Oeste", command=self.oeste)
        self.boton_circulo = tk.Button(self.ventana_botones, text="Círculo", command=self.circulo)

        # Colocar los botones en la ventana
        self.boton_abajo.pack()
        self.boton_arriba.pack()
        self.boton_norte.pack()
        self.boton_sur.pack()
        self.boton_este.pack()
        self.boton_oeste.pack()
        self.boton_circulo.pack()

    def abajo(self):
        self.lapiz.pendown()

    def arriba(self):
        self.lapiz.penup()

    def norte(self):
        self.lapiz.setheading(90)
        self.lapiz.forward(10)

    def sur(self):
        self.lapiz.setheading(270)
        self.lapiz.forward(10)

    def este(self):
        self.lapiz.setheading(0)
        self.lapiz.forward(10)

    def oeste(self):
        self.lapiz.setheading(180)
        self.lapiz.forward(10)

    def circulo(self):
        self.lapiz.circle(10)

if __name__ == "__main__":
    dibujo = Dibujo()
    turtle.done()
