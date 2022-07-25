from huffman_algo import HuffmanAlgo

def main():
    file_path = str(input("Syötä pakattavan tiedoston polku: "))
    file = open(file_path, "r", encoding="utf-8")
    data = file.read()
    huffman_algo = HuffmanAlgo(data)
    encoding, tree = huffman_algo.huffman_encoding()
    print("Huffman algoritmilla pakattu tuloste:", encoding)

if __name__ == "__main__":
    main()
