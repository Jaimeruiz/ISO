import socket
import gestor

puerto = int(input('Introduzca el puerto al que desea conectarse: '))
server_addr = ('localhost', puerto)
g = gestor
def cliente():
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect(server_addr)


    print('Elija la operacion que desea llevar a cabo: \n')
    print('1. Conocer la fecha \n')
    print('2. Conocer la hora \n')
    print('3. Apagar el servidor \n')
    opcion = int(input('Opcion:'))
    if opcion == 1:
        solicitud = 'fecha'
        socket_cliente.send(g.codificar(solicitud))
    elif opcion == 2:
        solicitud = 'hora'
        socket_cliente.send(g.codificar(solicitud))
    else:
        solicitud = 'apagar'
        socket_cliente.send(g.codificar(solicitud))

    respuesta = socket_cliente.recv(1024)
    print('Servidor responde a la peticion: \n')
    print(g.decodificar(respuesta))

if __name__ == '__main__':
    cliente()
