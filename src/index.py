from huffman_algo import HuffmanAlgo

def main():
    """Käynnistää sovelluksen ja vastaa nyt sovelluslogiikasta.
    Kovin raakile vielä tässä vaiheessa.
    """

    selection = str(input("Haluatko pakata vai purkaa tiedoston?" +
                          "\n1 = pakkaa\n2 = pura\nmuu lopettaa ohjelman\n"))
    #Huffman testaus
    if selection == "1":
        file_path = str(input("Syötä pakattavan tiedoston polku: "))
        file = open(file_path, "r", encoding="utf-8")
        data = file.read()
        file_huffman = file_path[:-4] + "_huffman" + ".bin"
        huffman_algo = HuffmanAlgo(data)
        encoding, tree = huffman_algo.huffman_encoding()
        with open(file_huffman, "wb") as binary_file:
            binary_file.write(tree)
            binary_file.write(encoding)
        print("Pakattu tiedosto löytyy polusta:\n" + file_huffman)
    elif selection == "2":
        file_path = str(input("Syötä purettavan tiedoston polku: "))
        huffman_bytes_from_file = open(file_path, "rb")
        data = huffman_bytes_from_file.read()
        huffman_algo = HuffmanAlgo(data)
        print("Huffman koodauksella purettu teksti:")
        print(huffman_algo.huffman_decoding())
    else:
        quit()

if __name__ == "__main__":
    main()
