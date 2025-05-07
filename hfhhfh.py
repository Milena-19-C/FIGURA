class figurageometrica:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
@property
def alto(self):
    return self._alto
@alto.setter
def alto(self, valor):
    self._alto = valor
@property
def ancho(self):
    return self._ancho
@ancho.setter
def ancho(self, valor):
    self._ancho = valor

def __int__(self):
    return self.alto,
from figurageometrica import *
class Cuadrado(figurageometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Cuadrado - lado: {self.alto}, área: {self.area()}"
from figurageometrica import *
class Rectangulo(figurageometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Rectángulo - alto: {self.alto}, ancho: {self.ancho}, área: {self.area()}"

    if __name__ == '_main_':
        cuadrado = Cuadrado (8)
        print(cuadrado)
        rectangulo = Rectangulo (16, 6)
        print(rectangulo)