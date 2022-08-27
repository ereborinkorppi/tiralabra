# Testausdokumentti

Unittestin avulla on suoritettu automatisoidusti ohjelman yksikkö- ja integraatiotestausta. Tämän lisäksi järjestelmätason testaus on tehty manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

index.py -moduulia, joka nyt vastaa käyttöliittymästä ja sovelluslogiikasta on testattu vain manuaalisesti erilaisilla tekstitiedostoilla pakkaamista ja niiden pakkausten purkamista. Tiedostosyötteisiin on lisätty kevyttä virheen tarkistusta ja tämän toimivuus testattu.

### Huffman pakkauksesta vastaava luokka

Huffman pakkauksesta vastaava luokkaa `HuffmanAlgo` ja sen käyttöön tarvittavaa `Node` -luokkaa testataan yksikkötestein luokalla [TestHuffmanAlgo](https://github.com/ereborinkorppi/tiralabra/blob/main/src/tests/huffman_algo_test.py). Yksikkötestejä voisi tehdä enemmänkin eri välivaiheille vaikka luokan testikattavuus on hyvä.

### Lempel Ziv 78 pakkausesta vastaava luokka

Lempel Ziv 78 pakkauksesta vastaava luokkaa `LzSeventyeight` testataan yksikkötestein luokalla [TestLzSeventyeight](https://github.com/ereborinkorppi/tiralabra/blob/main/src/tests/lz_seventyeight_test.py).

### Testikattavuus

Testauksen haarautumakattavuus on 96%, vaikka tämä onkin hyvä, niin tarkempaa yksikkötestausta tulisi tehdä.

![](./kuvat/testikattavuus.png)

## Järjestelmätestaus

Sovelluksen järjestelmätestit on suoritettu manuaalisesti.

### Asennus

Sovelluksen toimivuutta testattu sekä omalla koneella, että yliopiston Linux ympäristössä onnistuneesti.

Erilaisia konfiguraatioita ei ole testattu.