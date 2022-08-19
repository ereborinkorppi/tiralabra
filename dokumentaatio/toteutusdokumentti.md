# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman käyttöliittymästä ja sovelluslogiikasta vastaa index.py, täällä tapahtuu tiedostojen lukeminen ja kirjoittaminen. Huffman pakkaus/purku -algoritmia varten on oma luokka [HuffmanAlgo](https://github.com/ereborinkorppi/tiralabra/blob/main/src/huffman_algo.py) ja Lempel Ziv 78 pakkaus/purku -algoritmia varten on oma luokka [LzSeventyeight](https://github.com/ereborinkorppi/tiralabra/blob/main/src/lz_seventyeight.py). Lisäksi Huffman algoritmin puun toteuttamista varten on luokka [Node](https://github.com/ereborinkorppi/tiralabra/blob/main/src/node.py).

## Saavutetut aika- ja tilavaativuudet

## Suorituskyky vertailu pakkausten osalta

Pakkauskyvyn vertailu on aloitettu muutamilla erilaisilla tiedostoilla: 
- Pienellä 6 merkin tiedostolla kumpikin algoritmi tuottaa alkuperäistä suuremman pakkauksen. Huffman tiedoston koko on 217% alkuperäisestä ja LZ78 tiedoston koko on 617% alkuperäisestä.
- 788 tavun kokoisen The 69 Eyes - Feel Berlin lyrics tiedoston kohdalla Huffman tiedoston koko on 74% alkuperäisestä (hieman pienempi) ja LZ78 tiedoston koko on 180% alkuperäisestä.
- 2 megan vaihtuvasisältöisellä teksti tiedostolla pakkaus alkaa olla jo hyödyksi. Huffman tiedoston koko on 53% alkuperäisestä ja LZ78 tiedoston koko on 33% alkuperäisestä.
- 2022 tavua sisältävä toisteisen (kaikki merkit a) tiedoston kohdalla Huffman tiedoston koko on 13% alkuperäisestä ja LZ78 tiedoston koko on 10% alkuperäisestä.
- Äkkiseltään näyttää siltä, että Huffman pakkauksella saadaan hyötyä myös hieman pienempien tiedostojen kanssa, mutta LZ78 näyttää tehokkaammalta suurien tiedostojen kanssa. 
- Pakkauskykytestaus jatkuu...

## Työn puutteet ja parannusehdotukset

- Huffman algoritmin voisi varmasti suorittaa tehokkaamminkin. 
- Vaikka käyttöliittymään on otettu virhekäsittelyä, ei tiedostoja oikeasti tarkasteta, että onko pakkaustekniikka ollut se millä yritetään purkaa.

## Lähteet

- https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
- https://en.wikipedia.org/wiki/Huffman_coding
- https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
- https://medium.com/swlh/how-data-compression-works-exploring-lz78-e97e539138