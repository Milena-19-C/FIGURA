from figurageometrica import *
class Rectangulo(figurageometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Rectángulo - alto: {self.alto}, ancho: {self.ancho}, área: {self.area()}"

if __name__ == '__main__':
    rectangulo = Rectangulo (16, 6)
    print(rectangulo)