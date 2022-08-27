# Viikko 6 raportti

## Tällä viikolla tehty
- Vertaisarviointi nro2
- Käyttöliittymän hienosäätöä
- Huomattu virhe Huffman algoritmin kanssa, ei salli tällä hetkellä ääkkösiä tai ei osaa enää purkaa niitä. Tätä selvitelty tuloksetta pidempäänkin
- LZ78 on myös rajoittunut ennalta alustettavaan dictionaryyn, mutta tämä puutos on huomattavasti helpompi hallita ja mielestäni jopa hyväksyttävä
- Vertailun tekoa algoritmeista
- Toteutusdokumentin ja testausdokumentin päivitystä
- Käyttöohjeen teko
- Testitiedostojen lisääminen projektille
- Koodi kommentoitu ja laatu pidetty pylint mukaan virheettömänä (10/10)

### Ohjelman edistyminen
- Ohjelma toimii muuten kuten toivoisinkin, mutta Huffman bugi ääkkösten kanssa ärsyttää.

### Tällä viikolla opin
- Kertasin aikavertailua ja O notaatioita.
- Tutkin paljon utf-8, latin1 yms. encooding asioita Huffman ongelmaa selvittäessä ja varmaan opinkin jotain mutta en ratkaissut ongelmaa.

### Vaikeuksia/epäselvyyksiä
- Huffman algoritmin kanssa minulla tuli ongelma kun kokeilin (jostain syystä nyt vasta) pakata ääkkösiä sisältäviä tiedostoja. Ongelma tulee kun def encode_tree funktiossa käännän string muotoisen jonon näin: return bytes(encoded_tree_string, 'utf-8'). Tämä menee läpi, mutta myöhemmin kun koittaa purkaa niin def split_tree funktio ei enää osaa hakea noita merkkejä oikein, vaikka siellä on decode samalla 'utf-8'. Kokeilin muitakin encode/decode yhdistelmiä, mutta en saanut tätä toimimaan. En ymmärrä, itse käännän utf-8, mutta silti ohjelma ei osaa palauttaa sieltä Ä:tä ja Ö:tä oikein. Onko Apuja?

## Teen seuraavaksi
- Huffman bugin korjaus jos saan apuja
- Hienosäätöä
- Dokumentaation päivitystä
- Demo

## Aikaa käytetty tällä viikolla

10h