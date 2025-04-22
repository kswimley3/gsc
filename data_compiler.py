# compile all moves for pokemon into .json files
from pathlib import Path
import json

# create path
path = Path(".") / "data"

# create the main dictionary
poke_dict = {}

# read in csv and create an array of the values
file_p_names = open(path / 'names_pokemon.txt', 'r')
pokemon_names = file_p_names.read().split(',')

# initialize pokemon dictionary
count = 0
for name in pokemon_names:
    count +=1
    poke_dict[name.strip()] = {}
    poke_dict[name.strip()]['id'] = count
    poke_dict[name.strip()]['learnset'] = {}


# CREATE LEARNSETS AND LEVELS

# Bulbasaur
poke_dict['Bulbasaur']['learnset']['Tackle'] = 1
poke_dict['Bulbasaur']['learnset']['Absorb'] = 1

# Ivysaur
poke_dict['Ivysaur']['learnset']['Tackle'] = 1
poke_dict['Ivysaur']['learnset']['Absorb'] = 1

# Venusaur
poke_dict['Venusaur']['learnset']['Tackle'] = 1
poke_dict['Venusaur']['learnset']['Absorb'] = 1

# Charmander
poke_dict['Charmander']['learnset']['Scratch'] = 1
poke_dict['Charmander']['learnset']['Ember'] = 1

# Charmeleon
poke_dict['Charmeleon']['learnset']['Scratch'] = 1
poke_dict['Charmeleon']['learnset']['Ember'] = 1

# Charizard
poke_dict['Charizard']['learnset']['Scratch'] = 1
poke_dict['Charizard']['learnset']['Ember'] = 1

# Squirtle
poke_dict['Squirtle']['learnset']['Tackle'] = 1
poke_dict['Squirtle']['learnset']['Bubble'] = 1

# Wartortle
poke_dict['Wartortle']['learnset']['Tackle'] = 1
poke_dict['Wartortle']['learnset']['Bubble'] = 1

# Blastoise
poke_dict['Blastoise']['learnset']['Tackle'] = 1
poke_dict['Blastoise']['learnset']['Bubble'] = 1

# Caterpie

# Metapod

# Butterfree

# Weedle

# Kakuna

# Beedrill

# Pidgey

# Pidgeotto

# Pidgeot

# Rattata

# Raticate

# Spearow

# Fearow

# Ekans

# Arbok

# Pikachu

# Raichu

# Sandshew

# Sandslash

# NOTE UNIQUE CODES FOR NIDORAN!!

# Nidoran♂
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['Tackle'] = 1
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['Poison Sting'] = 1

# Nidorina

# Nidoqueen

# Nidoran♀
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['Tackle'] = 1
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['Poison Sting'] = 1

# Nidorino

# Nidoking



# # write the dictionary
with open(path / 'poke_dict.json', 'w') as outfile:
    json.dump(poke_dict, outfile)


