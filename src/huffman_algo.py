from node import Node

class HuffmanAlgo:
    """Huffman algoritmista huolehtiva luokka.
    Koodiin otettu pohja täältä:
    https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
    """

    def __init__(self, data):
        """Luokan konstruktori.

        Args:
            data: Joko pakattava str- data tai purettava bytes- data.
        """

        self.data = data
        self.nodes = []

    def huffman_encoding(self):
        """Huffman algoritmi.

        Returns:
            Bytes muodossa oleva Huffman koodattu data, sekä koodattu puu.
        """
        symbol_with_probs = self.calculate_probability()
        symbols = symbol_with_probs.keys()
        for symbol in symbols:
            self.nodes.append(Node(symbol_with_probs.get(symbol), symbol))

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
        encoded_string = self.output_encoded(huffman_encoding)
        encoded_tree = self.encode_tree(self.nodes[0])
        encoded_output = self.encoding_to_bytes(encoded_string)
        return encoded_output, encoded_tree

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
            Koodattu Huffmanpuu bytes -muodossa.
        """
        if node.left is None and node.right is None:
            self.encoded_tree.append(1)
            self.encoded_tree.append(node.symbol)
        else:
            self.encoded_tree.append(0)
            self.encode_tree(node.left)
            self.encode_tree(node.right)

        encoded_tree_string = ''.join([str(item) for item in self.encoded_tree])
        encoded_tree_string = encoded_tree_string + "  "
        return bytes(encoded_tree_string, 'utf-8')

    i = 0

    def decode_tree(self, coded_tree):
        """Luo uuden puun koodatusta datasta.

        Args:
            coded_tree: str- muotoinen koodattu puu.

        Returns:
            Huffman puu node -objekteina.
        """
        if coded_tree[self.i] == "1":
            self.i += 1
            new_node = Node(0, coded_tree[self.i])
            self.nodes.append(new_node)

        else:
            self.i += 1
            left_child = self.decode_tree(coded_tree)
            self.i += 1
            right_child = self.decode_tree(coded_tree)
            new_node = Node(0, "0", left_child, right_child)
            self.nodes.append(new_node)

        return new_node

    def huffman_decoding(self):
        """Huffman pakkauksen purku.

        Returns:
            Huffman algoritmin pakkauksen purku str -muodossa.
        """
        #huffman_bytes_from_file = self.data
        string_tree, counter = self.split_tree_coding(self.data)
        coding_bytes = self.data[counter:]
        encoded_data = self.bytes_to_string(coding_bytes)
        huffman_tree = self.decode_tree(string_tree)
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

        decoded_output_string = ''.join([str(item) for item in decoded_output])
        return decoded_output_string

    def encoding_to_bytes(self, encoded_string):
        """Str -Koodauksen muuttaminen tavuiksi apufunktio.

        Args:
            encoded_string: str -muotoinen 1 ja 0 sisältävä merkkijono.

        Returns:
            Huffman koodaus tavuiksi muutettuna.
        """
        encoding_bytes = bytearray()
        extra_bits = 8 - (len(encoded_string) % 8)
        for i in range(0, len(encoded_string), 8):
            encoding_bytes.append(int(encoded_string[i:i+8], 2))
        encoding_bytes.insert(0, extra_bits)
        return bytes(encoding_bytes)

    def bytes_to_string(self, encoding_bytes):
        """Huffman koodin muuttaminen str -muotoon purun apufunktio.

        Args:
            encoding_bytes: Bytes -muotoinen Huffman koodaus.

        Returns:
            Str- muotoinen Huffman koodi.
        """
        extra_bits = encoding_bytes[0]
        bytes_as_bits = ''.join(format(byte, '08b') for byte in encoding_bytes[1:])
        bytes_as_string = str(bytes_as_bits)
        replace_list = []
        i = extra_bits
        while i > 0:
            replace_list.append(bytes_as_string[-i])
            i -= 1
        replace_string = ''.join(replace_list)
        for char in replace_string:
            if char == '1':
                replace_string = replace_string[replace_string.index(char):]
                break
        removable = extra_bits + len(replace_string)
        string_wihtout_extra_bits = bytes_as_string[:-removable]
        huffman_output = string_wihtout_extra_bits + replace_string
        return huffman_output

    def split_tree_coding(self, huffman_bytes_from_file):
        """Puun irroittaminen bytes -tiedostosta purun apufunktio.

        Args:
            huffman_bytes_from_file: Bytes -muotoinen puu ja Huffman koodaus.

        Returns:
            Str- muotoinen koodattu puu, sekä int- muotoinen osoitin.
        """
        string_tree = ''
        counter = 0
        for current_char in huffman_bytes_from_file:
            current_char = huffman_bytes_from_file[counter:counter+1].decode('utf-8')
            counter += 1
            if current_char == " ":
                next_char = huffman_bytes_from_file[counter:counter+1].decode('utf-8')
                if next_char == " ":
                    break
            string_tree = string_tree + current_char
        counter += 1
        return string_tree, counter
