import pyxel

from tablero import Tablero
from piezas_blancas import PiezasBlancas
from piezas_negras import PiezasNegras
from posicion import Posicion
from cursor import Cursor

class App:
    def __init__(self):

        self.turno = None
        self.tablero = Tablero()
        self.piezasBlancas = PiezasBlancas()
        self.piezasNegras = PiezasNegras()
        self.cursor = Cursor()

        self.posicion = Posicion(1,1)

        pyxel.init(128, 128, title="pyChess", fps=30)
        pyxel.load("assets/assets.pyxres")
        pyxel.run(self.__update, self.__draw)

    def __update(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.cursor.mover()
            self.posicion.mover_fila("arriba")
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.cursor.mover()
            self.posicion.mover_fila("abajo")
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.cursor.mover()
            self.posicion.mover_columna("izquierda")
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.cursor.mover()
            self.posicion.mover_columna("derecha")
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.cursor.clic()


    def __draw(self):
        self.tablero.draw()
        self.piezasBlancas.draw()
        self.piezasNegras.draw()

        pyxel.blt(self.posicion.columna, self.posicion.fila, *self.cursor.sprite)