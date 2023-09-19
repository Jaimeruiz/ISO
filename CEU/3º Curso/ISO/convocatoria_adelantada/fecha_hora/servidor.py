import socket
import datetime
import gestor
import sys

server_addr = ('localhost', 16073)
g = gestor
def servidor():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind(server_addr)
    socket_servidor.listen(5)
    print('Servidor esperando solicitudes de clientes... \n')

    while True:
        conn, cliente_addr = socket_servidor.accept()
        peticion = conn.recv(1024)
        solicitud = g.decodificar(peticion)
        print('Cliente conectado: ', cliente_addr)

        if solicitud == 'hora':
            hora = datetime.datetime.now().time().strftime('%H:%M:%S')
            respuesta = g.codificar(hora)
            conn.send(respuesta)
        elif solicitud == 'fecha':
            fecha = datetime.datetime.now().date().strftime('%Y-%m-%d')
            respuesta = g.codificar(fecha)
            conn.send(respuesta)
        else:
            respuesta = g.codificar('Cerrando conexion')
            conn.send(respuesta)
            sys.exit(0)
            

if __name__ == '__main__':
    servidor()
