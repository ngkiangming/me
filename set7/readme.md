counter = len([x for x in lines if "M10 P1" in x])

out_file_path = "set4/lasers.pew"
with open(out_file_path, "w", encoding="utf-8") as f:
f.write(str(counter))

in_file_path = "set4/Trispokedevetiles(laser).gcode"
with open(in_file_path, "r", encoding= "utf-8") as f:
lines = f.readlines()

# way 1

counter = 0
for liune in lines:
if "M10 P1" in line:
counter += 1
print(counter)

# way 2

counter = len([x for x in lines if "M10 P1" in x])

out_file_path = "set4/lasers.pew"
with open(out_file_path, "w", encoding="utf-8") as f:
f.write(str(counter))

def get_pokemon(low, high):
some_pokemon_distionaries = []
for id in range(low, high):
url = f"https://pokeapi.co/api/v2/pokemon/{id}"
r = requests.get(url)
if r.status_code is 200:
the_json = json.loads(r.text)
some_pokemon_dictionaries.append(the_json)

tallest_hight = -1
tallest_poke = {}
for p in some_pokemon_dictionaries:
if p["height"] > tallest_hight:
tallest_hight = p["height]
tallest_poke = p

return {"name": tallest_poke["name"], "weight": tallest_poke["weight"], "height": tallest_poke["height"]}

def get_pokemon(low, high):

if os.path.isfile("poke.json"):
with open("poke.json", "r", encoding="utf-8") as f:
data = json.load(f)
else:
data = get_pokemon(2,5)
with open("poke.json", "r", encoding="utf-8") as f:
json.dump(data, f)

print(data)
