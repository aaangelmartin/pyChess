class Posicion:
    def __init__(self, columna: int, fila: int):
        self.columna = columna
        self.fila = fila
    
    @property
    def columna(self):
        return (self.__columna - 1) * 16
    
    @columna.setter
    def columna(self, columna):
        if not isinstance(columna, int):
            raise TypeError("ERROR! Tipo de columna incorrecto.")
        if not 1 <= columna <= 8:
            raise ValueError("ERROR! Valor de columna incorrecto.")
        
        self.__columna = columna

    @property
    def fila(self):
        return (self.__fila - 1) * 16

    @fila.setter
    def fila(self, fila):
        if not isinstance(fila, int):
            raise TypeError("ERROR! Tipo de fila incorrecto.")
        if not 1 <= fila <= 8:
            raise ValueError("ERROR! Valor de fila incorrecto.")

        self.__fila = fila

    def mover_columna(self, direccion: str):
        direcciones = ["izquierda", "derecha"]

        if not direccion.lower() in direcciones:
            raise TypeError("ERROR! Tipo de dirección incorrecta.")

        if direccion.lower() == "izquierda":
            if self.__columna == 1:
                self.__columna = 8
            else:
                self.__columna -= 1
        elif direccion.lower() == "derecha":
            if self.__columna == 8:
                self.__columna = 1
            else:
                self.__columna += 1

    def mover_fila(self, direccion: str):
        direcciones = ["arriba", "abajo"]

        if not direccion.lower() in direcciones:
            raise TypeError("ERROR! Tipo de dirección incorrecta.")

        if direccion.lower() == "arriba":
            if self.__fila == 1:
                self.__fila = 8
            else:
                self.__fila -= 1
        elif direccion.lower() == "abajo":
            if self.__fila == 8:
                self.__fila = 1
            else:
                self.__fila += 1

