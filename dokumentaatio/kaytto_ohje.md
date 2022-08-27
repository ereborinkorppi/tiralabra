# Käyttöohje

## Ohjelman suorittaminen

### Viimeisin release

Release tulossa...

### Asennus

Ohjelman käyttämät riippuvuudet asennetaan komennolla:

```bash
poetry install
```

### Ohjelman suorittaminen

Ohjelma käynnistetään komennolla:

```bash
poetry run invoke start
```

Tämän jälkeen ohjelmassa valitaan tekstikäyttöliittymää seuraten ollaanko 1 pakkaamassa .txt -tiedostoa, vai 2 purkamassa .bin -tiedostoa. Pakkausta varten syötetään halutun tiedoston polku. Purku toimii muuten samoin, mutta ensin on valittava puretaanko 1 Huffman algoritmilla pakattu tiedosto vai 2 LZ78 algoritmilla pakattu tiedosto.

### Testaus

Testaus suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti luodaan komennolla:

```bash
poetry run invoke coverage-report
```

Raportti löytyy htmlcov kansiosta index.html nimellä.

### Koodinlaatu

Laaturaportti luodaan komennolla:

```bash
poetry run invoke lint
```

## Testitiedostot

Ohjelman pakkaustoimintaa voi testata omilla tekstitiedostoilla tai kansiosta [testitiedostot](./testitiedostot) löytyvillä tiedostoilla. Kun on pakannut jotain, voi tämän luomia pakattuja tiedostoja käyttää purun testaukseen.