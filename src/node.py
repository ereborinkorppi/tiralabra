class Node:
    """Luokka, joka luo puurakenteen Huffman algoritmille.
    Koodiin otettu pohja täältä:
    https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328

    Attributes:
        prob: int-arvo, joka kuvaa merkin esiintyvyyttä datassa.
        symbol: str-arvo joka kertoo mikä merkki on kyseessä.
        left: Node -luokan objekti joka on solmun vasen lapsi.
        right: Node -luokan objekti joka on solmun oikea lapsi.
        code: int-arvo, solmun sijainti puussa.
    """
    def __init__(self, prob, symbol, left=None, right=None):

        self.prob = prob

        self.symbol = symbol

        self.left = left

        self.right = right

        self.code = ''
