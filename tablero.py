import pyxel

class Tablero:
    def __init__(self):
        self.blanco = (0, 0, 0, 16, 16)
        self.negro = (0, 16, 0, 16, 16)

        self.contador = 0

    def update(self):
        return

    def draw(self):
        for f in range(8):
            for c in range(8):
                self.contador += 1

                if f % 2 == 0:
                    if self.contador % 2 == 0:
                        pyxel.blt(16*c, 16*f, *self.negro)
                    else:
                        pyxel.blt(16*c, 16*f, *self.blanco)
                else:
                    if self.contador % 2 == 0:
                        pyxel.blt(16*c, 16*f, *self.blanco)
                    else:
                        pyxel.blt(16*c, 16*f, *self.negro)

        self.contador = 0