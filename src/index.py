from huffman_algo import HuffmanAlgo
from lz_seventyeight import LzSeventyeight

def main():
    """Käynnistää sovelluksen ja vastaa nyt sovelluslogiikasta.
    Kovin raakile vielä tässä vaiheessa.
    """

    selection = str(input("Haluatko pakata vai purkaa tiedoston?" +
                          "\n1 = pakkaa\n2 = pura\nmuu lopettaa ohjelman\n"))
    if selection == "1":
        file_path = str(input("Syötä pakattavan tiedoston polku: "))
        file = open(file_path, "r", encoding="utf-8")
        data = file.read()
        #huffman pakkaus
        file_huffman = file_path[:-4] + "_huffman" + ".bin"
        huffman_algo = HuffmanAlgo(data)
        encoding, tree = huffman_algo.huffman_encoding()
        with open(file_huffman, "wb") as binary_file:
            binary_file.write(tree)
            binary_file.write(encoding)
        print("Huffman algoritmilla pakattu tiedosto löytyy polusta:\n" + file_huffman)
        #lz78 pakkaus
        file_lz = file_path[:-4] + "_lz" + ".bin"
        lz_seventyeight = LzSeventyeight(data)
        compressed = lz_seventyeight.compress()
        with open(file_lz, "wb") as binary_file:
            binary_file.write(compressed)
        print("Lempel Ziv 78 algoritmilla pakattu tiedosto löytyy polusta:\n" + file_lz)

    elif selection == "2":
        decompress_algo = str(input("Puretaanko Huffman vai LZ78 algoritmilla pakattu tiedosto" +
                          "\n1 = Huffman\n2 = LZ78\n"))
        file_path = str(input("Syötä purettavan tiedoston polku: "))
        file = open(file_path, "rb")
        data = file.read()
        #Huffman purku
        if decompress_algo == "1":
            huffman_algo = HuffmanAlgo(data)
            print("Huffman pakkauksesta purettu teksti:")
            print(huffman_algo.huffman_decoding())
        #lz78 purku
        elif decompress_algo == "2":
            lz_seventyeight = LzSeventyeight(data)
            print("LZ78 pakkauksesta purettu teksti:")
            print(lz_seventyeight.decompress())

    else:
        quit()

if __name__ == "__main__":
    main()
