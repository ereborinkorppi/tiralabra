from huffman_algo import HuffmanAlgo

def main():
    """Käynnistää sovelluksen ja vastaa nyt sovelluslogiikasta.
    Kovin raakile vielä tässä vaiheessa.
    """

    file_path = str(input("Syötä pakattavan tiedoston polku: "))
    file = open(file_path, "r", encoding="utf-8")
    data = file.read()
    huffman_algo = HuffmanAlgo(data)
    encoding, tree = huffman_algo.huffman_encoding()
    print("Huffman algoritmilla koodattu tuloste:", encoding)
    encoded_tree = huffman_algo.encode_tree(tree)
    print("Koodattu puu:", encoded_tree)
    print("Purettu teksti:", huffman_algo.huffman_decoding(encoding,tree))

if __name__ == "__main__":
    main()
