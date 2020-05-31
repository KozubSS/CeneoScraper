# CeneoScraper
## Etap 1 pracy - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

| Składowa                | Selektor                                                  | Nazwa zmiennej |
|-------------------------|-----------------------------------------------------------|----------------|
| opinia                  |div.js_proctud-review                                      | opinion        |
| identyfikator opinii    |["data-entry-id"]                                          | opinion_id     |
| autor                   |span.user-post__author-name                                | author         |
| rekomendacja            |span.user-post_author-recomendation> em                    | recommendation |
| ocena                   |span.review-score-count                                    | stars          |
| treść opini             |div.user-post__text                                        | content        |
| lista wad               |div.review-feature__col:has(>div.review-feature__title-negatives                                                       | cons           |
| lista zalet             |div.review-feature__col:has(>div.review-feature__title-positives                                                       | pros           |
| przydatna               |button.vote-yes > span                                     | useful         |
| nieprzydatna            |button.vote-no > span                                      | useles         |
| data wystawienia opinii |span.user-post__published > time:first-child["datatime"]   | opinion_date   |
| data zakupu             |span.user-post__published > time:nth-child(2)["datatime"]  | urchase_date   |

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

## Etap 5 (Pandas, Matpoltlib)
- wczytanie opinii do ramki danych
- policzenie podstawowych statystyk
- narysowanie wykresów funkcji 

## Etap 6 interfejs webowy dla scrapera (Flask)
> /Scrapper  
>>        /run.py  
>>        /config.py  
>>        /app  
>>>            /__init__.py
>>>            /views.py  
>>>            /models.py  #pod jakim adersem jaka akcja bedzie wykonywana
>>>            /static/   #elementy wyświetlane na stronie
>>>>                /figures_png
>>>>                /main.css
>>>            /templates/   # 
>>>>                /layout.html  
>>>>                /extract.html
>>>             /opinions_json
>>>        /requirements.txt  
>>>        /yourappenv