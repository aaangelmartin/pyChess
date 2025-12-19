import pyxel

class PiezasNegras:
    def __init__(self):
        self.pieza_activa = 0

    def draw(self):
        tile = (16, 16)

        # Peon
        p = (0, 16, 16, *tile, 0, 0)
        # Caballo
        c = (0, 16, 32, *tile, 0, 0)
        # Alfil
        a = (0, 16, 48, *tile, 0, 0)
        # Torre
        t = (0, 16, 64, *tile, 0, 0)
        # Dame
        d = (0, 16, 80, *tile, 0, 0)
        # Rey
        r = (0, 16, 96, *tile, 0, 0)

        tablero = (
            (p, p, p, p, p, p, p, p),
            (t, c, a, d, r, a, c, t)
        )

        for f in range(len(tablero)):
            for c in range(len(tablero[f])):
                pyxel.blt(c*16, f*16, *tablero[f][c])