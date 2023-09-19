import datetime
def codificar(texto):
    mensaje_cod = texto.encode('UTF-8')
    return mensaje_cod

def decodificar(mensaje_cod):
    mensaje_decod = mensaje_cod.decode('UTF-8')
    return mensaje_decod

def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now().date()
    return fecha_actual

def obtener_hora_actual():
    hora_actual = datetime.datetime.now().time()
    return hora_actual



