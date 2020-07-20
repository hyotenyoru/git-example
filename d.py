import json
with open("data.json",mode="r",encoding="utf-8") as file:
    data = json.load(file)
for x in data:
    if x['id'] in '巴哈':
        print('name:'+x['name'])