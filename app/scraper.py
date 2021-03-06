# source .venv/Scripts/activate - aktywacja środowiska wirtualnego
#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint 
import json

#funkcja do ekstrakcji składowych opinii

def extract_feature(opinion,selector,attribute=None):
    try:
        if attribute:
            return opinion.select(selector).pop(0)[attribute].strip()
        else:
            return opinion.select(selector).pop(0).text.strip()
    except IndexError:
        return None


#słownik z atrybutami i ich selectorami
selectors = {
    "author":["span.user-post__author-name"],
    "recommendation": ["span.user-post_author-recomendation > em"],
    "stars":["span.user-post__score-count"],
    "content":["div.user-post__text"],
    "cons":["div.review-feature__col:has(>div.review-feature__title-negatives"],
    "pros":["div.review-feature__col:has(>div.review-feature__title-positives"],
    "useful":["button.vote-yes > span"],
    "useless":["button.vote-no > span"],
    "opinion_date":["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date":["span.user-post__published > time:nth-child(2)", "datetime"]

}
#mozna tez uzyc div.user-post__body:not(div.js_product-review-hook) > div.user-post_content > jako content 
#pobranie kodu pojedynczej strony z opiniami o produkcie
def scraper(product_id):

    url_prefix = "https://www.ceneo.pl"
    product_id = input("Podaj indentyfikator produktu: ")
    url_postfix = "#tab=reviews"
    url = url_prefix+"/"+product_id+url_postfix
    # opinion = opinions[0]  # 1 opcja
    # opinion = opinions.pop(0) # 2 opcja


    # pusta lista 
    all_opinions = []
    # dla pojedynczej opinii wydobycia jej składowych
    # tutaj było bez pętli i nie potrezba już opinions.pop(0)
    while url:
        # dla wszyskich opinii z danej strony wydobaycie ich składowych 
        respons = requests.get(url)
    # respons.status_code == 200
        page_dom = BeautifulSoup(respons.text, "html.parser")

        # wydobycie z kodu strony fragmentów odpowiadających opiniom konsumentów
        opinions = page_dom.select("div.js_product-review")
        for opinion in opinions:
            features = {key:extract_feature(opinion, *args)
                        for key, args in selectors.items()}
            features["opinion_id"] = int(opinion["data-entry-id"])
            features["useful"] = int(features["useful"])
            features["useless"] = int(features["useless"])
            features["stars"] = float(features["stars"].split("/")[0].replace(",","."))
            features["content"] = features["content"].replace("\n"," ").replace("\r"," ")
            try:
                features["pros"] = features["pros"].replace("\n",", ").replace("\r",", ").replace("Zalety, ", "")
            except AttributeError:
                pass
            try:
                features["cons"] = features["cons"].replace("\n",", ").replace("\r",", ").replace("Wady, ","")
            except AttributeError:
                pass
            all_opinions.append(features)


        try:
            url = url_prefix+page_dom.select("a.pagination__next").pop()["href"]
        except IndexError:
            url = None
        print(len(all_opinions))
        print(url)

    with open("app/opinions_json/"+product_id+".json", "w", encoding="UTF-8") as fp:
        json.dump(all_opinions, fp, indent=4, ensure_ascii=False)

    
# pprint.pprint(all_opinions)

# print(features)
# print(opinion_id, author, recommendation, stars, content, cons, pros, useful, useles, opinion_date, purchase_date)
# pracując na własnych sprzecie mozna przez ssh normalnie lepiej przez http