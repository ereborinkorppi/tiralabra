from node import Node

class HuffmanAlgo:
    """Huffman algoritmista huolehtiva luokka.
    Koodiin otettu pohja täältä:
    https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
    """

    def __init__(self, data):
        """Luokan konstruktori.

        Args:
            data: str-arvo, pakattava tekstidata.
        """

        self.data = data
        self.nodes = []
        self.symbol_with_probs = self.calculate_probability()
        self.symbols = self.symbol_with_probs.keys()
        #self.probabilities = self.symbol_with_probs.values()
        #print("symbols: ", self.symbols)
        #print("probabilities: ", self.probabilities)

    def huffman_encoding(self):
        """Huffman algoritmi.

        Returns:
            Str muodossa oleva Huffman koodattu data, sekä solmut sisältävä puu.
        """

        for symbol in self.symbols:
            self.nodes.append(Node(self.symbol_with_probs.get(symbol), symbol))

        while len(self.nodes) > 1:
            self.nodes = sorted(self.nodes, key=lambda x: x.prob)

            right = self.nodes[0]
            left = self.nodes[1]

            left.code = 0
            right.code = 1

            new_node = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
            self.nodes.remove(left)
            self.nodes.remove(right)
            self.nodes.append(new_node)

        huffman_encoding = self.calculate_codes(self.nodes[0])
        encoded_output = self.output_encoded(huffman_encoding)

        return encoded_output, self.nodes[0]

    codes = dict()

    def calculate_codes(self, node, val=''):
        """Solmujen koodauksen apufunktio.

        Args:
            node: tämänhetkinen solmu.
            val: edellisen solmun koodi.

        Returns:
            Solmujen koodit dictionary -listana.
        """
        new_val = val + str(node.code)

        if node.left:
            self.calculate_codes(node.left, new_val)
        if node.right:
            self.calculate_codes(node.right, new_val)

        if(not node.left and not node.right):
            self.codes[node.symbol] = new_val

        return self.codes

    def calculate_probability(self):
        """Merkkien esiintyvyyden apufunktio.

        Returns:
            Merkit ja niiden esiintyvyys dictionary -listana.
        """
        symbols = dict()
        for element in self.data:
            if symbols.get(element) == None:
                symbols[element] = 1
            else:
                symbols[element] += 1
        return symbols

    def output_encoded(self, coding):
        """Pakatun datan muodostukseen apufunktio.

        Args:
            coding: dict-tyyppinen lista merkeistä ja koodeista

        Returns:
            Huffman algoritmilla pakattu data str -muodossa.
        """
        encoding_output = []
        for c in self.data:
            encoding_output.append(coding[c])

        string = ''.join([str(item) for item in encoding_output])
        return string
