#import bibliotek
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt


#wyświetlnenie zawartości katalogu opinions_json
input_directory = "./opinions_json"
print(*os.listdir(input_directory))

#wczytanie identyfikatora produktu, którego opinie będą analizowane
product_id = input("Podaj identyfikator produktu: ")

opinions = pd.read_json(input_directory+"/"+product_id+".json")
opinions = opinions.set_index("opinion_id")


average_score = opinions.stars.mean().round(2)
pros = opinions.pros.count()
cons = opinions.cons.count()
stars = opinions.stars.value_counts().sort_index()
recommendation = opinions.recommendation.value_counts()

print(f'Średnia ocena: {average_score}\nLiczba opinii z zaletami: {pros}\nLiczba opinii z wadami: {cons}')
fig, ax = plt.subplots()
stars.plot.bar(color = "#f5c2c2")
plt.title("Ranking ocen")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
#plt.show()
plt.savefig("figures_png/"+product_id+"_bar.png")
plt.close()

#udział poszczególnych rekomendacji w ogólnej liczbie opinii
fig, ax = plt.subplots()
recommendation.plot.pie(label="", autopct="%1.1f%%", colors=["#f5c3c2", "#89cff0"])
plt.title("<<Rekomendacja>>")
plt.savefig("figures_png/"+product_id+"_pie.png")
plt.close()

#opinions["purchased"] = opinions['purchase_date'] != None nie wychodziło ponieważ 
opinions["purchased"] = opinions['purchase_date'].apply(lambda x: False if x == None else True)
stars_purchased = pd.crosstab(opinions["stars"], opinions["purchased"])
print(stars_purchased)