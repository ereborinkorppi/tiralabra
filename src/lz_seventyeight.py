import pickle

class LzSeventyeight:
    """LZ78 algoritmista huolehtiva luokka.
    Koodiin otettu pohja täältä:
    https://stackoverflow.com/questions/35029094/implementing-the-lz78-compression-algorithm-in-python
    """

    def __init__(self, data):
        """Luokan konstruktori.

        Args:
            data: str-arvo, pakattava tekstidata.
        """

        self.data = data
        self.dict_size = 256
        self.dictionary = {chr(i): chr(i) for i in range(self.dict_size)}

    def compress(self):
        """LZ78 pakkausalgoritmi.

        Returns:
            Bytes muodossa oleva LZ78 koodattu lista.
        """

        current = ""
        result = []
        for char in self.data:
            new = current + char
            if new in self.dictionary:
                current = new
            else:
                result.append(self.dictionary[current])
                self.dictionary[new] = self.dict_size
                self.dict_size += 1
                current = char
        if current:
            result.append(self.dictionary[current])

        return bytearray(pickle.dumps(result))


    def decompress(self):
        """LZ78 pakkauksen purku.

        Returns:
            LZ78 algoritmin pakkauksen purku str -muodossa.
        """

        compressed = pickle.loads(self.data)
        decoded_output = []
        current = compressed.pop(0)
        decoded_output.append(current)
        for k in compressed:
            if k in self.dictionary:
                entry = self.dictionary[k]
            elif k == self.dict_size:
                entry = current + current[0]
            decoded_output.append(entry)

            self.dictionary[self.dict_size] = current + entry[0]
            self.dict_size += 1
            current = entry

        decoded_output_string = ''.join([str(item) for item in decoded_output])

        return decoded_output_string
