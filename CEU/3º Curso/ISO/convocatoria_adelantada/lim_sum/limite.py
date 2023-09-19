

class Limite():
    def __init__(self):
        self.secuencia = []
    """
    CODIGO PARA TEST 1
    def sumar(self, secuencia, limite):
        return f"La suma es 1"
    """
    """
    CODIGO PARA TEST 2
    def sumar(self, secuencia, limite):
        suma = 0
        for i in secuencia:
            suma += i
            if suma <= limite:
                mensaje = f"La suma es {suma}"
        return mensaje
    """
    """
    CODIGO PARA TEST 3
    def sumar(self, secuencia, limite):
        suma = 0
        for i in secuencia:
            suma += i
            if suma == limite:
                mensaje = f"La suma es {suma}"
            else:
                mensaje = f"La suma {suma} ha sobrepasado el limite {limite}"
        return f"{mensaje}"
    """
    #CODIGO PARA TEST 4
    def sumar(self, secuencia, limite):
        suma = 0
        for i in secuencia:
            suma += i
            if suma == limite:
                mensaje = f"La suma es {suma}"
            elif suma < limite:
                mensaje = f"La suma es {suma}, puedes seguir sumando"
            else:
                mensaje = f"La suma {suma} ha sobrepasado el limite {limite}"
                break
        return f"{mensaje}"

    def sumar_2(self, limite):
            suma = 0
            mensaje = ""
            while True:
                try:
                    numero = int(input("Ingrese un número: "))
                    suma += numero
                    if suma == limite:
                        mensaje = f"La suma es {suma}"
                        break  # Detener la suma si se alcanza el límite exacto
                    elif suma < limite:
                        mensaje = f"La suma es {suma}, puedes seguir sumando"
                        print(mensaje)
                    else:
                        mensaje = f"La suma {suma} ha sobrepasado el límite {limite}"
                        break  # Detener la suma si se supera el límite
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            return mensaje
"""
limite = Limite()
limite_esperado = int(input("Ingrese el limite: "))
print(limite.sumar_2(limite_esperado))
"""