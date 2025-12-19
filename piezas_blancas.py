import pyxel

class PiezasBlancas:
    def __init__(self):
        self.pieza_activa = 0

    def draw(self):
        tile = (16, 16)

        # Peon
        p = (0, 0, 16, *tile, 0, 0)
        # Caballo
        c = (0, 0, 32, *tile, 0, 0)
        # Alfil
        a = (0, 0, 48, *tile, 0, 0)
        # Torre
        t = (0, 0, 64, *tile, 0, 0)
        # Dame
        d = (0, 0, 80, *tile, 0, 0)
        # Rey
        r = (0, 0, 96, *tile, 0, 0)

        tablero = (
            (p, p, p, p, p, p, p, p),
            (t, c, a, d, r, a, c, t)
        )

        for f in range(len(tablero)):
            for c in range(len(tablero[f])):
                pyxel.blt(c*16, (6+f)*16, *tablero[f][c])