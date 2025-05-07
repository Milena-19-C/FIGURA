from color import Color
from figurageometrica import figurageometrica

class Cuadrado(figurageometrica,Color):
    def __init__(self, lado=0.color=None):
        figurageometrica.__init__(self,ancho=lado,alto=lado)
        Color

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Cuadrado - lado: {self.alto}, área: {self.area()}"
if __name__ == '__main__':
    cuadrado = Cuadrado(8)
    print(cuadrado)


























