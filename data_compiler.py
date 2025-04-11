# compile all moves for pokemon into .json files
from pathlib import Path
import json

# create path
path = Path(".") / "data"

# create the main dictionary
poke_dict = {}
poke_dict['bulbasaur'] = {}
poke_dict['charmander'] = {}
poke_dict['squirtle'] = {}

# create pokemon ids
poke_dict['bulbasaur']['id'] = 1
poke_dict['charmander']['id'] = 4
poke_dict['squirtle']['id'] = 7

# CREATE LEARNSETS AND LEVELS

# bulbasaur
poke_dict['bulbasaur']['learnset'] = {}
poke_dict['bulbasaur']['learnset']['Tackle'] = 1
poke_dict['bulbasaur']['learnset']['Absorb'] = 1

# charmander
poke_dict['charmander']['learnset'] = {}
poke_dict['charmander']['learnset']['Tackle'] = 1
poke_dict['charmander']['learnset']['Ember'] = 1

# squirtle
poke_dict['squirtle']['learnset'] = {}
poke_dict['squirtle']['learnset']['Tackle'] = 1
poke_dict['squirtle']['learnset']['Bubble'] = 1


# write the dictionary
with open(path / 'poke_dict.json', 'w') as outfile:
    json.dump(poke_dict, outfile)


