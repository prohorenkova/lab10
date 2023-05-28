import json

with open('1.json') as f:
    t = json.load(f)

for i in t['products']:
    print("Название: ", i["name"], "\n Цена: ", i["price"], "\n Вес: ", i["weight"],
          "\n В наличии" if i["available"] else "Нет в наличии!", "\n")
