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
        for i in range(len(comandos)):
            comando = comandos[i]
            if comando == "ABJ":
                self.lapiz.pendown()
            elif comando == "ARR":
                self.lapiz.penup()
            elif comando.startswith("NOR") or comando.startswith("SUR") or comando.startswith(
                    "EST") or comando.startswith("OES"):
                # Buscar un número después del comando y convertirlo en un entero
                distancia = 10  # Valor predeterminado si no se encuentra un número
                match = re.search(r'[0-9]+', comando)
                if match:
                    distancia = int(match.group()) * 10

                if comando.startswith("NOR"):
                    self.lapiz.setheading(90)
                elif comando.startswith("SUR"):
                    self.lapiz.setheading(270)
                elif comando.startswith("EST"):
                    self.lapiz.setheading(0)
                elif comando.startswith("OES"):
                    self.lapiz.setheading(180)

                self.lapiz.forward(distancia)
            elif comando == "CIRC":
                self.lapiz.circle(10)
            elif comando == "SALIR":
                self.ventana_comandos.destroy()
                self.ventana.bye()
            else:
                print(f"COMANDO no válido: {comando}")


if __name__ == '__main__':
    dibujo = Dibujo()
    turtle.done()
