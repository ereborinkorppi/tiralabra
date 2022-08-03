from huffman_algo import HuffmanAlgo

def main():
    """Käynnistää sovelluksen ja vastaa nyt sovelluslogiikasta.
    Kovin raakile vielä tässä vaiheessa.
    """

    file_path = str(input("Syötä pakattavan tiedoston polku: "))
    file_huffman = file_path[:-4] + "_huffman" + ".bin"
    print(file_huffman)
    file = open(file_path, "r", encoding="utf-8")
    data = file.read()
    huffman_algo = HuffmanAlgo(data)
    encoding, tree = huffman_algo.huffman_encoding()
    encoded_tree = huffman_algo.encode_tree(tree)
    print("Koodattu puu:", encoded_tree)
    with open(file_huffman, "wb") as binary_file:
        binary_file.write(encoding)
    bytes_from_file = open(file_huffman, "rb")
    encoding_bytes_from_file = bytes_from_file.read()
    print("Purettu teksti:", huffman_algo.huffman_decoding(encoding_bytes_from_file, tree))

if __name__ == "__main__":
    main()
