from posicion import Posicion

class Cursor:
    def __init__(self):
        self.posicion = Posicion(1,1)

        self.__estado = "mover"
        self.__sprite = (0, 32, 0, 16,16, 0)

    @property
    def sprite(self):
        if self.__estado.lower() == "mover":
            self.__sprite = (0, 32, 0, 16,16, 0)
        elif self.__estado.lower() == "clic":
            self.__sprite = (0, 64, 0, 16, 16, 0)

        return self.__sprite

    def clic(self):
        self.__estado = "clic"

    def mover(self):
        self.__estado = "mover"