from figurageometrica import *
class Cuadrado(figurageometrica):
    def _init_(self, lado):
        super()._init_(lado, lado)

    def area(self):
        return self.alto * self.ancho

    def _str_(self):
        return f"Cuadrado - lado: {self.alto}, área: {self.area()}"
