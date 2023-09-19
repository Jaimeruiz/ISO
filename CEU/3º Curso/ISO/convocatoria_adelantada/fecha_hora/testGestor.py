
import gestor
import datetime
import unittest


class TestServidor(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_codificar_palabra(self):
        mensaje = 'hola'
        mensaje_cod = gestor.codificar(mensaje)
        self.assertEqual(mensaje_cod, b'hola')

    def test_codificar_numero(self):
        mensaje = '12345'
        mensaje_cod = gestor.codificar(mensaje)
        self.assertEqual(mensaje_cod, b'12345')

    def test_codificar_vacio(self):
        texto = ""
        resultado = gestor.codificar(texto)
        self.assertEqual(resultado, b'')

    def test_decodificar_vacio(self):
        mensaje_codificado = b''
        resultado = gestor.decodificar(mensaje_codificado)
        self.assertEqual(resultado, '')

    def test_decodificar_palabra(self):
        mensaje_cod = b'adios'
        mensaje = gestor.decodificar(mensaje_cod)
        self.assertEqual(mensaje, 'adios')

    def test_decodificar_numero(self):
        mensaje_cod = b'12345'
        mensaje = gestor.decodificar(mensaje_cod)
        self.assertEqual(mensaje , '12345')

    def test_fecha_actual_es_hoy(self):
        fecha_actual = gestor.obtener_fecha_actual()
        fecha_hoy = datetime.date.today()
        self.assertEqual(fecha_actual, fecha_hoy)


    def test_fecha_actual_formato_correcto(self):
        fecha_actual = gestor.obtener_fecha_actual()
        fecha_str = fecha_actual.strftime("%Y-%m-%d")
        self.assertEqual(fecha_str, str(fecha_actual))
    
    def test_obtener_hora_actual(self):
        hora_actual = gestor.obtener_hora_actual()
        self.assertIsNotNone(hora_actual)
        self.assertIsInstance(hora_actual, datetime.time)

    def test_obtener_hora_actual_formato_correcto(self):
        hora_actual = gestor.obtener_hora_actual()
        formato_esperado = "%H:%M:%S"
        self.assertEqual(hora_actual.strftime(formato_esperado), str(hora_actual.strftime('%H:%M:%S')))


if __name__ == '__main__':
    unittest.main()
