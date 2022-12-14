# ohtu-miniprojekti

![Screenshot from 2022-12-14 11-19-17](https://user-images.githubusercontent.com/102189885/207556154-6e9a08bb-c273-41ce-879c-928139e43977.png)

[Backlog](https://docs.google.com/spreadsheets/d/1Otvn0MgeJhJgBoKedaaNOIOoLDglO9RI1a-f7RCdokQ/edit?usp=sharing)

![GHA workflow badge](https://github.com/sohvip/ohtu-miniprojekti/workflows/CI/badge.svg)
## Definition of Done

- User storyille on määritelty hyväksymiskriteerit
- Testikattavuus on noin 70% oleellisen koodin osalta
- Asiakas näkee GitHubista koodin testikattavuuden.
- Koodin ylläpidettävyys on hyvä 


##Asennus- ja käyttöohje

1. Lataa sovelluksen lähdekoodi githubista
2. Varmista, että koneeltasi löytyy PostGreSQL ja tietokantayhteys on auki
3. Siirry terminaalissa projektin sisältävään kansioon ja anna seuraavat käskyt
 - poetry install
 - export DATABASE_URL=postgresql:///{postgreaql_käyttäjänimesi}
 - psql<schema.sql
4. Siirry projektin koodin kansioon src
5. Anna komento Flask run ja seuraa linkkiä
