# CeneoScraper
## Etap 1 pracy - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

| Składowa                | Selektor                                         | Nazwa zmiennej |
|-------------------------|--------------------------------------------------|----------------|
| opinia                  |li.js_proctud-review                              |                |
| identyfikator opinii    |["data-entry-id"]                                 |                |
| autor                   |div.reviewer-name-line                            |                |
| rekomendacja            |div.product-review-summary > em                   |                |
| ocena                   |span.review-score-count                           |                |
| treść opini             |p.product-review-body                             |                |
| lista wad               |div.cons-cell > ul                                |                |
| lista zalet             |div.pros-cell > ul                                |                |
| przydatna               |button.vote-yes > span                            |                |
| nieprzydatna            |button.vote-no > span                             |                |
| data wystawienia opinii |span.review-time > time:first-child["datatime"]   |                |
| data zakupu             |span.review-time > time:nth-child(2)["datatime"]  |                |

## Etap 2 - pobranie skłądowych pojednyczej opinii
- pobranie kody jendej storny z opiniami o konkretnym produkcie
- wyciągnięcie kodu strony fragmentów odpowiadających poszczególnym opiniom
- zapisanie do pojednycznych zmiennych wartości poszczególnych składowych opinii