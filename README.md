# Tiralabra harjoitustyö

Tämä on tiralabra -kurssin harjoitustyöni, jossa käsittelen pakkausalgoritmeja.

## Dokumentaatio

- [Määrittelydokumentti](./dokumentaatio/maarittelydokumentti.md)
- [Testausdokumentti](./dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](./dokumentaatio/toteutusdokumentti.md)
- [Käyttöohje](./dokumentaatio/kaytto_ohje.md)

## Viikkoraportit

- [Viikko 1](./viikkoraportit/Viikko1.md)
- [Viikko 2](./viikkoraportit/Viikko2.md)
- [Viikko 3](./viikkoraportit/Viikko3.md)
- [Viikko 4](./viikkoraportit/Viikko4.md)
- [Viikko 5](./viikkoraportit/Viikko5.md)
- [Viikko 6](./viikkoraportit/Viikko6.md)

## Komentorivitoiminnot

### Asennus

Riippuvuudet asennetaan komennolla:

```bash
poetry install
```

### Ohjelman suorittaminen

Ohjelma käynnistetään komennolla:

```bash
poetry run invoke start
```

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

### Koodinlaatu

Laaturaportti luodaan komennolla:

```bash
poetry run invoke lint
```