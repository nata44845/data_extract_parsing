import json

# load
with open('steam_games.json', 'r', encoding = 'utf-8') as f1:
  with open('steam_games_short.json', 'w', encoding = 'utf-8') as f2:
        json_file = json.load(f1)
        x=0
        for key in json_file.keys():
            # print(key)
            if x>10000: 
                break
            f2.write(json.dumps(json_file[key]))
            x+=1


