from figurageometrica import *
class Rectangulo(figurageometrica):
    def _init_(self, alto, ancho):
        super()._init_(alto, ancho)

    def area(self):
        return self.alto * self.ancho

    def _str_(self):
        return f"Rectángulo - alto: {self.alto}, ancho: {self.ancho}, área: {self.area()}"

