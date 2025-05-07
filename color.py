class color:
    def _init_(self, nombre):
        self._nombre = nombre

    def _str_(self):
        return f'color: {self._dict.str_()}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

if __name__ == '_main_':
    c1 = color('rojo')
    print(c1)

