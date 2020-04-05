# CeneoScraper
## Etap 1 pracy - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

| Składowa                | Selektor                                         | Nazwa zmiennej |
|-------------------------|--------------------------------------------------|----------------|
| opinia                  |li.js_proctud-review                              | opinion        |
| identyfikator opinii    |["data-entry-id"]                                 | opinion_id     |
| autor                   |div.reviewer-name-line                            | author         |
| rekomendacja            |div.product-review-summary > em                   | recommendation |
| ocena                   |span.review-score-count                           | stars          |
| treść opini             |p.product-review-body                             | content        |
| lista wad               |div.cons-cell > ul                                | cons           |
| lista zalet             |div.pros-cell > ul                                | pros           |
| przydatna               |button.vote-yes > span                            | useful         |
| nieprzydatna            |button.vote-no > span                             | useles         |
| data wystawienia opinii |span.review-time > time:first-child["datatime"]   | opinion_date   |
| data zakupu             |span.review-time > time:nth-child(2)["datatime"]  | urchase_date   |

## Etap 2 - pobranie skłądowych pojednyczej opinii
- pobranie kody jendej storny z opiniami o konkretnym produkcie
- wyciągnięcie kodu strony fragmentów odpowiadających poszczególnym opiniom
- zapisanie do pojednycznych zmiennych wartości poszczególnych składowych opinii

## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- zapisanie do złożonej struktury danych składowych wysztkich opoini z podejynczej strony
- przechodzenie po kolejnych stronach z opiniamii
- zapis wszystkich opinii o pojednyczym produkcie do pliku

## Etap 4
- transformacja i wyczyszczenie danych
- refaktoring okdu
- parametryzacja kodu (robienie uniwersalnego kodu)