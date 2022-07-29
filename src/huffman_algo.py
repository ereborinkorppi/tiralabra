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
            if symbols.get(element) is None:
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
        for char in self.data:
            encoding_output.append(coding[char])

        string = ''.join([str(item) for item in encoding_output])
        return string

    encoded_tree = []

    def encode_tree(self, node):
        """Luodun Huffman puun tallennuksen apufunktio.

        Args:
            node: tämänhetkinen solmu.

        Returns:
            Koodattu Huffmanpuu str -muodossa.
        """
        if node.left is None and node.right is None:
            self.encoded_tree.append(1)
            self.encoded_tree.append(node.symbol)
        else:
            self.encoded_tree.append(0)
            self.encode_tree(node.left)
            self.encode_tree(node.right)

        string = ''.join([str(item) for item in self.encoded_tree])
        return string

    #def decode_tree(self, encoded_tree):

    def huffman_decoding(self, encoded_data, huffman_tree):
        """Huffman pakkauksen purku.

        Args:
            encoded_data: str -muotoinen 1 ja 0 sisältävä merkkijono.
            huffman_tree: solmut sisältävä puu

        Returns:
            Huffman algoritmin pakkauksen purku str -muodossa.
        """
        tree_head = huffman_tree
        decoded_output = []
        for bit in encoded_data:
            if bit == '1':
                huffman_tree = huffman_tree.right
            elif bit == '0':
                huffman_tree = huffman_tree.left
            try:
                if huffman_tree.left.symbol is None and huffman_tree.right.symbol is None:
                    pass
            except AttributeError:
                decoded_output.append(huffman_tree.symbol)
                huffman_tree = tree_head

        string = ''.join([str(item) for item in decoded_output])
        return string
