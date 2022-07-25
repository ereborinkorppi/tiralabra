from huffmanAlgo import HuffmanAlgo

def main():
    filePath = str(input("Syötä pakattavan tiedoston polku: "))
    file = open(filePath, "r")
    data = file.read()
    encoding, tree = HuffmanAlgo.Huffman_Encoding(data)
    print("Encoded output", encoding)

if __name__ == "__main__":
    main()