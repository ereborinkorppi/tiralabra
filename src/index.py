import sys
import os
from huffman_algo import HuffmanAlgo
from lz_seventyeight import LzSeventyeight

def main():
    """Käynnistää sovelluksen ja vastaa nyt sovelluslogiikasta.
    Kovin raakile vielä tässä vaiheessa, ei esim. virheen tarkistusta.
    """

    selection = str(input("Haluatko pakata vai purkaa tiedoston?" +
                          "\n1 = pakkaa\n2 = pura\nmuu lopettaa ohjelman\n"))
    file_found = False
    if selection == "1":
        while not file_found:
            file_path = str(input("Syötä pakattavan tiedoston polku: "))
            file_found = check_file(file_path, ".txt")
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
        #huffman pakkaus
        file_huffman = file_path[:-4] + "_huffman" + ".bin"
        huffman_algo = HuffmanAlgo(data)
        encoding, tree = huffman_algo.huffman_encoding()
        with open(file_huffman, "wb") as binary_file:
            binary_file.write(tree)
            binary_file.write(encoding)
        print("\nHuffman algoritmilla pakattu tiedosto löytyy polusta:\n" + file_huffman)
        #lz78 pakkaus
        file_lz = file_path[:-4] + "_lz" + ".bin"
        lz_seventyeight = LzSeventyeight(data)
        with open(file_lz, "wb") as binary_file:
            binary_file.write(lz_seventyeight.compress())
        print("\nLempelZiv78 algoritmilla pakattu tiedosto löytyy polusta:\n" + file_lz)
        #vertailu
        org_size = os.path.getsize(file_path)
        huff_size = os.path.getsize(file_huffman)
        lz_size = os.path.getsize(file_lz)
        print("\nAlkuperäisen tiedoston koko on:", org_size, "tavua")
        print("Huffman algoritmilla pakatun tiedoston koko on:", huff_size, "tavua")
        print("Huffman -tiedosto on kooltaan", round((huff_size/org_size)*100, 2),
              "prosenttia alkuperäisestä tiedostosta")
        print("LempelZiv78 algoritmilla pakatun tiedoston koko on:", lz_size, "tavua")
        print("LempelZiv78 -tiedosto on kooltaan", round((lz_size/org_size)*100, 2),
              "prosenttia alkuperäisestä tiedostosta")

    elif selection == "2":
        selection = str(input("Puretaanko Huffman vai LZ78 algoritmilla pakattu tiedosto" +
                          "\n1 = Huffman\n2 = LZ78\n"))
        if selection not in ("1", "2"):
            sys.exit()
        while not file_found:
            file_path = str(input("Syötä purettavan tiedoston polku: "))
            file_found = check_file(file_path, ".bin")
        with open(file_path, "rb") as file:
            data = file.read()
        #huffman purku
        if selection == "1":
            huffman_algo = HuffmanAlgo(data)
            print("\nHuffman pakkauksesta purettu teksti:")
            print(huffman_algo.huffman_decoding())
        #lz78 purku
        elif selection == "2":
            lz_seventyeight = LzSeventyeight(data)
            print("\nLZ78 pakkauksesta purettu teksti:")
            print(lz_seventyeight.decompress())

    else:
        sys.exit()

def check_file(file_path, file_type):
    """Tarkistaa löytyykö annettu polku ja onko johtaako se .txt tiedostoon.

    Args:
        file_path: tiedoston polku.
        file_type: str -muotoinen syöte osoittamaan millaista tiedostoa haetaan.

    Returns:
        True jos polku oikea ja se päättyy .txt, false jos ei.
    """

    if not os.path.exists(file_path):
        print("Tiedostoa ei löydy")
        return False
    if file_path[-4:] != file_type:
        print("Tiedosto ei ole " + file_type + " -muotoinen")
        return False
    return True

if __name__ == "__main__":
    main()
