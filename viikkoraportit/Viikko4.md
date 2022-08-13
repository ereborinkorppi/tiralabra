# Viikko 4 raportti

## Tällä viikolla tehty
- Toteutettu Lempel Ziv 78 algoritmi kokonaisuudessaan, niin että sekä pakkaus, että purku toimivat.
- Tehty yksikkötesteusta tuolle LZ78 luokalle.
- Mahdollistettu algoritmien pakkaustuotoksen vertailu ohjelman kautta.
- Muokattu ohjelman toimintaa niin, että sillä voi valita pakkaako vai purkaako. Pakatessa pakataan molemmilla tavoilla ja näytetään vertailua. Purettaussa pitää valita kummalla tavalla pakattu tiedosto halutaan purkuu ja tulostetaan sen sisältö (ajatuksena vain todistaa, että palautus toimii).
- Muokattu määrittely- ja testausdokumentteja ajantasalle
- Aloitettu toteutusdokumentin teko.
- Koodi kommentoitu ja laatu muokattu pylint mukaan virheettömäksi (10/10)

### Ohjelman edistyminen
- Ohjelma on edistynyt paremmin kuin kuvittelin ja nyt molemmat pakkaus/purku -algoritmit toimivat ja näitä voi jopa vähän vertailla karkean käyttöliittymän kautta.

### Tällä viikolla opin
- Lempel Ziv 78 algoritmin python toteutusta
- Tiedostojen koon hakemista pythonilla
- Pickle käyttöä bytes muotoon muuttamiseen ja palautukseen

### Vaikeuksia/epäselvyyksiä
- Huomasin Huffman algoritmissa bugin vain yhtä samaa merkkiä sisältävissä tiedostoissa, jota pitää tutkia.

## Teen seuraavaksi
- Huffman bugin korjaus
- Lisää vertailua, toteutusdokumentin päivitystä (graafejakin ehkä)
- Käyttöliittymään jonkinlaista virheenkäsittelyä tiedostopolkujen osalta yms.

## Aikaa käytetty tällä viikolla

17h