# ohtu-miniprojekti

![Screenshot from 2022-12-14 11-19-17](https://user-images.githubusercontent.com/102189885/207556154-6e9a08bb-c273-41ce-879c-928139e43977.png)

[Backlog](https://docs.google.com/spreadsheets/d/1Otvn0MgeJhJgBoKedaaNOIOoLDglO9RI1a-f7RCdokQ/edit?usp=sharing)

[Raportti](https://docs.google.com/document/d/1EYoOaevRcciSkLH4vtv1HQykKb-BRuH5I-jmM93S-hg/edit?usp=sharing)

![GHA workflow badge](https://github.com/sohvip/ohtu-miniprojekti/workflows/CI/badge.svg)
## Definition of Done

- User storyille on määritelty hyväksymiskriteerit
- Testikattavuus on noin 70% oleellisen koodin osalta
- Asiakas näkee GitHubista koodin testikattavuuden.
- Koodin ylläpidettävyys on hyvä 


## Asennus- ja käyttöohje

1. Lataa sovelluksen lähdekoodi githubista
2. Varmista, että koneeltasi löytyy PostGreSQL ja tietokantayhteys on auki
3. Siirry terminaalissa projektin sisältävään kansioon ja anna seuraavat käskyt
```bash
poetry install
```
```bash
 export DATABASE_URL=postgresql:///{postgresql_käyttäjänimesi}
 ```
 ```bash
 psql<schema.sql
 ```
4. Siirry projektin kansioon src
5. Anna komento Flask run ja seuraa linkkiä
