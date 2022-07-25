from node import Node

class HuffmanAlgo:
    """Huffman algoritmista huolehtiva luokka.
    Koodiin otettu pohja täältä: https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
    """
        
    def Huffman_Encoding(data):
        """Huffman algoritmi.

        Args:
            data: str-arvo, pakattava data.

        Returns:
            Str muodossa oleva Huffman koodattu data, sekä solmut siltävä puu.
        """
        symbol_with_probs = HuffmanAlgo.Calculate_Probability(data)
        symbols = symbol_with_probs.keys()
    
        nodes = []
    
        for symbol in symbols:
            nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.prob)

            right = nodes[0]
            left = nodes[1]
    
            left.code = 0
            right.code = 1
    
            newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(newNode)
            
        huffman_encoding = HuffmanAlgo.Calculate_Codes(nodes[0])
        encoded_output = HuffmanAlgo.Output_Encoded(data,huffman_encoding)

        return encoded_output, nodes[0]  

    codes = dict()

    def Calculate_Codes(node, val=''):
        """Solmujen koodauksen apufunktio.

        Args:
            node: tämänhetkinen solmu.
            val: edellisen solmun koodi.

        Returns:
            Koodit dictionary -listana.
        """
        newVal = val + str(node.code)

        if(node.left):
            HuffmanAlgo.Calculate_Codes(node.left, newVal)
        if(node.right):
            HuffmanAlgo.Calculate_Codes(node.right, newVal)

        if(not node.left and not node.right):
            HuffmanAlgo.codes[node.symbol] = newVal
         
        return HuffmanAlgo.codes  

    def Calculate_Probability(data):
        """Merkkien esiintyvyyden apufunktio.

        Args:
            data: str-arvo, pakattava data.

        Returns:
            Merkit dictionary -listana.
        """
        symbols = dict()
        for element in data:
            if symbols.get(element) == None:
                symbols[element] = 1
            else: 
                symbols[element] += 1     
        return symbols

    def Output_Encoded(data, coding):
        """Pakatun datan muodostukseen apufunktio.

        Args:
            data: str-arvo, pakattava data.
            coding: dict-tyyppinen lista symboleista ja koodeista

        Returns:
            Huffman algoritmilla pakattu data str -muodossa.
        """
        encoding_output = []
        for c in data:
            encoding_output.append(coding[c])
        
        string = ''.join([str(item) for item in encoding_output])    
        return string

huffmanAlgo = HuffmanAlgo()