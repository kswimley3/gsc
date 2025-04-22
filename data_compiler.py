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


# CREATE LEARNSETS, LEVELS AND EVOLUTION LEVLS

# Bulbasaur
poke_dict['Bulbasaur']['evolution'] = {}
poke_dict['Bulbasaur']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Bulbasaur']['evolution']['EVOLVE_LEVEL'][16] = "Ivysaur"
poke_dict['Bulbasaur']['learnset']['Tackle'] = 1
poke_dict['Bulbasaur']['learnset']['Leech Seed'] = 7
poke_dict['Bulbasaur']['learnset']['Vine Whip'] = 10
poke_dict['Bulbasaur']['learnset']['Poison Powder'] = 15
poke_dict['Bulbasaur']['learnset']['Sleep Powder'] = 15
poke_dict['Bulbasaur']['learnset']['Razor Leaf'] = 20
poke_dict['Bulbasaur']['learnset']['Sweet Scent'] = 25
poke_dict['Bulbasaur']['learnset']['Growth'] = 32
poke_dict['Bulbasaur']['learnset']['Synthesis'] = 39
poke_dict['Bulbasaur']['learnset']['Solarbeam'] = 46

# Ivysaur
poke_dict['Ivysaur']['evolution'] = {}
poke_dict['Ivysaur']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Ivysaur']['evolution']['EVOLVE_LEVEL'][32] = "Venusaur"
poke_dict['Ivysaur']['learnset']['Tackle'] = 1
poke_dict['Ivysaur']['learnset']['Leech Seed'] = 1
poke_dict['Ivysaur']['learnset']['Vine Whip'] = 10
poke_dict['Ivysaur']['learnset']['Poison Powder'] = 15
poke_dict['Ivysaur']['learnset']['Sleep Powder'] = 15
poke_dict['Ivysaur']['learnset']['Razor Leaf'] = 20
poke_dict['Ivysaur']['learnset']['Sweet Scent'] = 25
poke_dict['Ivysaur']['learnset']['Growth'] = 32
poke_dict['Ivysaur']['learnset']['Synthesis'] = 39
poke_dict['Ivysaur']['learnset']['Solarbeam'] = 46

# Venusaur
poke_dict['Venusaur']['learnset']['Tackle'] = 1
poke_dict['Venusaur']['learnset']['Absorb'] = 1
poke_dict['Venusaur']['learnset']['Vine Whip'] = 10
poke_dict['Venusaur']['learnset']['Poison Powder'] = 15
poke_dict['Venusaur']['learnset']['Sleep Powder'] = 15
poke_dict['Venusaur']['learnset']['Razor Leaf'] = 20
poke_dict['Venusaur']['learnset']['Sweet Scent'] = 25
poke_dict['Venusaur']['learnset']['Growth'] = 32
poke_dict['Venusaur']['learnset']['Synthesis'] = 39
poke_dict['Venusaur']['learnset']['Solarbeam'] = 46

# Charmander
poke_dict['Charmander']['evolution'] = {}
poke_dict['Charmander']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Charmander']['learnset']['Scratch'] = 1
poke_dict['Charmander']['learnset']['Ember'] = 1

# Charmeleon
poke_dict['Charmeleon']['evolution'] = {}
poke_dict['Charmander']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Charmeleon']['learnset']['Scratch'] = 1
poke_dict['Charmeleon']['learnset']['Ember'] = 1

# Charizard
poke_dict['Charizard']['learnset']['Scratch'] = 1
poke_dict['Charizard']['learnset']['Ember'] = 1

# Squirtle
poke_dict['Squirtle']['evolution'] = {}
poke_dict['Squirtle']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Squirtle']['learnset']['Tackle'] = 1
poke_dict['Squirtle']['learnset']['Bubble'] = 1

# Wartortle
poke_dict['Wartortle']['evolution'] = {}
poke_dict['Wartortle']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Wartortle']['learnset']['Tackle'] = 1
poke_dict['Wartortle']['learnset']['Bubble'] = 1

# Blastoise
poke_dict['Blastoise']['learnset']['Tackle'] = 1
poke_dict['Blastoise']['learnset']['Bubble'] = 1

# Caterpie
poke_dict['Caterpie']['evolution'] = {}
poke_dict['Caterpie']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Caterpie']['learnset']['Tackle'] = 1

# Metapod
poke_dict['Metapod']['evolution'] = {}
poke_dict['Metapod']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Metapod']['learnset']['Tackle'] = 1

# Butterfree
poke_dict['Butterfree']['learnset']['Tackle'] = 1

# Weedle
poke_dict['Weedle']['evolution'] = {}
poke_dict['Weedle']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Weedle']['learnset']['Leech Life'] = 1

# Kakuna
poke_dict['Kakuna']['evolution'] = {}
poke_dict['Kakuna']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Kakuna']['learnset']['Leech Life'] = 1

# Beedrill
poke_dict['Beedrill']['learnset']['Leech Life'] = 1

# Pidgey
poke_dict['Pidgey']['evolution'] = {}
poke_dict['Pidgey']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Pidgey']['learnset']['Peck'] = 1

# Pidgeotto
poke_dict['Pidgeotto']['evolution'] = {}
poke_dict['Pidgeotto']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Pidgeotto']['learnset']['Peck'] = 1

# Pidgeot
poke_dict['Pidgeot']['learnset']['Peck'] = 1

# Rattata
poke_dict['Rattata']['evolution'] = {}
poke_dict['Rattata']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Rattata']['learnset']['Scratch'] = 1

# Raticate
poke_dict['Raticate']['learnset']['Scratch'] = 1

# Spearow
poke_dict['Spearow']['evolution'] = {}
poke_dict['Spearow']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Spearow']['learnset']['Peck'] = 1

# Fearow
poke_dict['Fearow']['learnset']['Peck'] = 1

# Ekans
poke_dict['Ekans']['evolution'] = {}
poke_dict['Ekans']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Ekans']['learnset']['Wrap'] = 1

# Arbok
poke_dict['Arbok']['learnset']['Wrap'] = 1

# Pikachu
poke_dict['Pikachu']['evolution'] = {}
poke_dict['Pikachu']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Pikachu']['evolution']['EVOLVE_ITEM']['THUNDERSTONE'] = "RAICHU"
poke_dict['Pikachu']['learnset']['Tackle'] = 1

# Raichu
poke_dict['Raichu']['learnset']['Tackle'] = 1

# Sandshrew
poke_dict['Sandshrew']['evolution'] = {}
poke_dict['Sandshrew']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Sandshrew']['learnset']['Scratch'] = 1

# Sandslash
poke_dict['Sandslash']['learnset']['Scratch'] = 1

# NOTE UNIQUE CODES FOR NIDORAN!!

# Nidoran♀
poke_dict['Nidoran\u00e2\u2122\u201a']['evolution'] = {}
poke_dict['Nidoran\u00e2\u2122\u201a']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['Tackle'] = 1
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['Poison Sting'] = 1

# Nidorina
poke_dict['Nidorina']['evolution'] = {}
poke_dict['Nidorina']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Nidorina']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Nidoqueen"
poke_dict['Nidorina']['learnset']['Tackle'] = 1
poke_dict['Nidorina']['learnset']['Poison Sting'] = 1

# Nidoqueen
poke_dict['Nidoqueen']['learnset']['Tackle'] = 1
poke_dict['Nidoqueen']['learnset']['Poison Sting'] = 1

# Nidoran♂
poke_dict['Nidoran\u00e2\u2122\u20ac']['evolution'] = {}
poke_dict['Nidoran\u00e2\u2122\u20ac']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['Tackle'] = 1
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['Poison Sting'] = 1

# Nidorino
poke_dict['Nidorino']['evolution'] = {}
poke_dict['Nidorino']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Nidorino']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Nidoking"
poke_dict['Nidorino']['learnset']['Tackle'] = 1
poke_dict['Nidorino']['learnset']['Poison Sting'] = 1

# Nidoking
poke_dict['Nidoking']['learnset']['Tackle'] = 1
poke_dict['Nidoking']['learnset']['Poison Sting'] = 1

# Clefairy
poke_dict['Clefairy']['evolution'] = {}
poke_dict['Clefairy']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Clefairy']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Clefable"
poke_dict['Clefairy']['learnset']['Tackle'] = 1

# Clefable
poke_dict['Clefable']['learnset']['Tackle'] = 1

# Vulpix
poke_dict['Vulpix']['evolution'] = {}
poke_dict['Vulpix']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Vulpix']['evolution']['EVOLVE_ITEM']['FIRE_STONE'] = "Ninetails"
poke_dict['Vulpix']['learnset']['Scratch'] = 1

# Ninetales
poke_dict['Ninetales']['learnset']['Scratch'] = 1

# Jigglypuff
poke_dict['Jigglypuff']['evolution'] = {}
poke_dict['Jigglypuff']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Jigglypuff']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Wigglytuff"
poke_dict['Jigglypuff']['learnset']['Pound'] = 1

# Wigglytuff
poke_dict['Wigglytuff']['learnset']['Pound'] = 1

# Zubat
poke_dict['Zubat']['evolution'] = {}
poke_dict['Zubat']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Zubat']['learnset']['Leech Life'] = 1

# Golbat
poke_dict['Golbat']['evolution'] = {}
poke_dict['Golbat']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Golbat']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Crobat"
poke_dict['Golbat']['learnset']['Leech Life'] = 1

# Oddish
poke_dict['Oddish']['evolution'] = {}
poke_dict['Oddish']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Oddish']['learnset']['Absorb'] = 1

# Gloom
poke_dict['Gloom']['evolution'] = {}
poke_dict['Gloom']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Gloom']['evolution']['EVOLVE_ITEM']['LEAF_STONE'] = "Vileplume"
poke_dict['Gloom']['evolution']['EVOLVE_ITEM']['SUN_STONE'] = "Bellossom"
poke_dict['Gloom']['learnset']['Absorb'] = 1

# Vileplume
poke_dict['Vileplume']['learnset']['Absorb'] = 1

# Paras
poke_dict['Paras']['evolution'] = {}
poke_dict['Paras']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Paras']['learnset']['Leech Life'] = 1

# Parasect
poke_dict['Parasect']['learnset']['Leech Life'] = 1

# Venonat
poke_dict['Venonat']['evolution'] = {}
poke_dict['Venonat']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Venonat']['learnset']['Leech Life'] = 1

# Venomoth
poke_dict['Venomoth']['learnset']['Leech Life'] = 1

# Diglett
poke_dict['Diglett']['evolution'] = {}
poke_dict['Diglett']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Diglett']['learnset']['Scratch'] = 1

# Dugtrio
poke_dict['Dugtrio']['learnset']['Scratch'] = 1

# Meowth
poke_dict['Meowth']['evolution'] = {}
poke_dict['Meowth']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Meowth']['learnset']['Scratch'] = 1

# Persian
poke_dict['Persian']['learnset']['Scratch'] = 1

# Psyduck
poke_dict['Psyduck']['evolution'] = {}
poke_dict['Psyduck']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Psyduck']['learnset']['Peck'] = 1

# Golduck
poke_dict['Golduck']['learnset']['Peck'] = 1

# Mankey
poke_dict['Mankey']['evolution'] = {}
poke_dict['Mankey']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Mankey']['learnset']['Scratch'] = 1

# Primeape
poke_dict['Primeape']['learnset']['Scratch'] = 1

# Growlithe
poke_dict['Growlithe']['evolution'] = {}
poke_dict['Growlithe']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Growlithe']['evolution']['EVOLVE_ITEM']['FIRE_STONE'] = "Arcanine"
poke_dict['Growlithe']['learnset']['Tackle'] = 1

# Arcanine
poke_dict['Arcanine']['learnset']['Tackle'] = 1

# Poliwag
poke_dict['Poliwag']['evolution'] = {}
poke_dict['Poliwag']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Poliwag']['learnset']['Pound'] = 1

# Poliwhirl
poke_dict['Poliwhirl']['evolution'] = {}
poke_dict['Poliwhirl']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Poliwhirl']['evolution']['EVOLVE_ITEM']["WATER_STONE"] = "Poliwrath"
poke_dict['Poliwhirl']['evolution']['EVOLVE_ITEM']["SUN_STONE"] = "Politoed"
poke_dict['Poliwhirl']['learnset']['Pound'] = 1

# Poliwrath
poke_dict['Poliwrath']['learnset']['Pound'] = 1

# Abra
poke_dict['Abra']['evolution'] = {}
poke_dict['Abra']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Abra']['learnset']['Teleport'] = 1

# Kadabra
poke_dict['Kadabra']['evolution'] = {}
poke_dict['Kadabra']['learnset']['Teleport'] = 1

# Alakazam
poke_dict['Alakazam']['learnset']['Teleport'] = 1

# Machop
poke_dict['Machop']['evolution'] = {}
poke_dict['Machop']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Machop']['learnset']['Pound'] = 1

# Machoke
poke_dict['Machoke']['evolution'] = {}
poke_dict['Machoke']['learnset']['Pound'] = 1

# Machamp
poke_dict['Machamp']['learnset']['Pound'] = 1

# Bellsprout
poke_dict['Bellsprout']['evolution'] = {}
poke_dict['Bellsprout']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Bellsprout']['learnset']['Absorb'] = 1

# Weepinbell
poke_dict['Weepinbell']['evolution'] = {}
poke_dict['Weepinbell']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Weepinbell']['evolution']['EVOLVE_ITEM']["LEAF_STONE"] = "Victreebel"
poke_dict['Weepinbell']['learnset']['Absorb'] = 1

# Victreebel
poke_dict['Victreebel']['learnset']['Absorb'] = 1

# Tentacool
poke_dict['Tentacool']['evolution'] = {}
poke_dict['Tentacool']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Tentacool']['learnset']['Poison Sting'] = 1

# Tentacruel
poke_dict['Tentacruel']['learnset']['Poison Sting'] = 1

# Geodude
poke_dict['Geodude']['evolution'] = {}
poke_dict['Geodude']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Geodude']['learnset']['Tackle'] = 1

# Graveler
poke_dict['Graveler']['evolution'] = {}
poke_dict['Graveler']['learnset']['Tackle'] = 1

# Golem
poke_dict['Golem']['learnset']['Tackle'] = 1

# Ponyta
poke_dict['Ponyta']['evolution'] = {}
poke_dict['Ponyta']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Ponyta']['learnset']['Tackle'] = 1

# Rapidash
poke_dict['Rapidash']['learnset']['Tackle'] = 1

# Slowpoke
poke_dict['Slowpoke']['evolution'] = {}
poke_dict['Slowpoke']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Slowpoke']['learnset']['Tackle'] = 1

# Slowbro
poke_dict['Slowbro']['learnset']['Tackle'] = 1

# Magnemite
poke_dict['Magnemite']['evolution'] = {}
poke_dict['Magnemite']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Magnemite']['learnset']['Tackle'] = 1

# Magneton
poke_dict['Magneton']['learnset']['Tackle'] = 1

# Farfetch'd
# DATA SPELLING FORMAT: Farfetch\u00e2\u20ac\u2122d
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['Peck'] = 1

# Doduo
poke_dict['Doduo']['evolution'] = {}
poke_dict['Doduo']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Doduo']['learnset']['Peck'] = 1

# Dodrio
poke_dict['Dodrio']['learnset']['Peck'] = 1

# Seel
poke_dict['Seel']['evolution'] = {}
poke_dict['Seel']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Seel']['learnset']['Tackle'] = 1

# Dewgong
poke_dict['Dewgong']['learnset']['Tackle'] = 1

# Grimer
poke_dict['Grimer']['evolution'] = {}
poke_dict['Grimer']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Grimer']['learnset']['Pound'] = 1

# Muk
poke_dict['Muk']['learnset']['Pound'] = 1

# Shellder
poke_dict['Shellder']['evolution'] = {}
poke_dict['Shellder']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Shellder']['learnset']['Tackle'] = 1

# Cloyster
poke_dict['Cloyster']['learnset']['Tackle'] = 1

# Gastly
poke_dict['Gastly']['evolution'] = {}
poke_dict['Gastly']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Gastly']['learnset']['Lick'] = 1

# Haunter
poke_dict['Haunter']['evolution'] = {}
poke_dict['Haunter']['learnset']['Lick'] = 1

# Gengar
poke_dict['Gengar']['learnset']['Lick'] = 1

# Onix
poke_dict['Onix']['evolution'] = {}
poke_dict['Onix']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Onix']['evolution']['EVOLVE_ITEM']['METAL_COAT'] = "Steelix"
poke_dict['Onix']['learnset']['Tackle'] = 1
poke_dict['Onix']['learnset']['Wrap'] = 1

# Drowzee
poke_dict['Drowzee']['evolution'] = {}
poke_dict['Drowzee']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Drowzee']['learnset']['Pound'] = 1

# Hypno
poke_dict['Hypno']['learnset']['Pound'] = 1

# Krabby
poke_dict['Krabby']['evolution'] = {}
poke_dict['Krabby']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Krabby']['learnset']['Scratch'] = 1

# Kingler
poke_dict['Kingler']['learnset']['Scratch'] = 1

# Voltorb
poke_dict['Voltorb']['evolution'] = {}
poke_dict['Voltorb']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Voltorb']['learnset']['Tackle'] = 1

# Electrode
poke_dict['Electrode']['learnset']['Tackle'] = 1

# Exeggcute
poke_dict['Exeggcute']['evolution'] = {}
poke_dict['Exeggcute']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Exeggcute']['learnset']['Tackle'] = 1

# Exeggutor
poke_dict['Exeggutor']['learnset']['Tackle'] = 1

# Cubone
poke_dict['Cubone']['evolution'] = {}
poke_dict['Cubone']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Cubone']['learnset']['Scratch'] = 1

# Marowak
poke_dict['Marowak']['learnset']['Pound'] = 1

# Hitmonlee
poke_dict['Hitmonlee']['learnset']['Tackle'] = 1

# Hitmonchan
poke_dict['Hitmonchan']['learnset']['Pound'] = 1

# Lickitung
poke_dict['Lickitung']['learnset']['Wrap'] = 1

# Koffing
poke_dict['Koffing']['evolution'] = {}
poke_dict['Koffing']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Koffing']['learnset']['Tackle'] = 1

# Weezing
poke_dict['Weezing']['learnset']['Tackle'] = 1

# Rhyhorn
poke_dict['Rhyhorn']['evolution'] = {}
poke_dict['Rhyhorn']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Rhyhorn']['learnset']['Tackle'] = 1

# Rhydon
poke_dict['Rhydon']['learnset']['Tackle'] = 1

# Chansey
poke_dict['Chansey']['evolution'] = {}
poke_dict['Chansey']['learnset']['Pound'] = 1

# Tangela
poke_dict['Tangela']['learnset']['Absorb'] = 1

# Kangaskhan
poke_dict['Kangaskhan']['learnset']['Pound'] = 1

# Horsea
poke_dict['Horsea']['evolution'] = {}
poke_dict['Horsea']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Horsea']['learnset']['Water Gun'] = 1

# Seadra
poke_dict['Seadra']['evolution'] = {}
poke_dict['Seadra']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Seadra']['learnset']['Water Gun'] = 1

# Goldeen
poke_dict['Goldeen']['evolution'] = {}
poke_dict['Goldeen']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Goldeen']['learnset']['Tackle'] = 1

# Seaking
poke_dict['Seaking']['learnset']['Tackle'] = 1

# Staryu
poke_dict['Staryu']['evolution'] = {}
poke_dict['Staryu']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Staryu']['evolution']['EVOLVE_ITEM']["WATER_STONE"] = "Starmie"
poke_dict['Staryu']['learnset']['Tackle'] = 1

# Starmie
poke_dict['Starmie']['learnset']['Tackle'] = 1

# Mr. Mime
poke_dict['Mr. Mime']['learnset']['Pound'] = 1

# Scyther
poke_dict['Scyther']['evolution'] = {}
poke_dict['Scyther']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Scyther']['evolution']['EVOLVE_ITEM']['METAL_COAT'] = "Scizor"
poke_dict['Scyther']['learnset']['Scratch'] = 1

# Jynx
poke_dict['Jynx']['learnset']['Pound'] = 1

# Electabuzz
poke_dict['Electabuzz']['learnset']['Pound'] = 1

# Magmar
poke_dict['Magmar']['learnset']['Scratch'] = 1

# Pinsir
poke_dict['Pinsir']['learnset']['Scratch'] = 1

# Tauros
poke_dict['Tauros']['learnset']['Tackle'] = 1
poke_dict['Tauros']['learnset']['Stomp'] = 23

# Magikarp
poke_dict['Magikarp']['evolution'] = {}
poke_dict['Magikarp']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Magikarp']['learnset']['Tackle'] = 1

# Gyarados
poke_dict['Gyarados']['learnset']['Tackle'] = 1

# Lapras
poke_dict['Lapras']['learnset']['Tackle'] = 1

# Ditto
poke_dict['Ditto']['learnset']['Transform'] = 1

# Eevee
poke_dict['Eevee']['evolution'] = {}
poke_dict['Eevee']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Eevee']['evolution']['EVOLVE_ITEM']['THUNDERSTONE'] = "Jolteon"
poke_dict['Eevee']['evolution']['EVOLVE_ITEM']['WATER_STONE'] = "Vaporeon"
poke_dict['Eevee']['evolution']['EVOLVE_ITEM']['FIRE_STONE'] = "Flareon"
poke_dict['Eevee']['evolution']['EVOLVE_ITEM']['SUN_STONE'] = "Espeon"
poke_dict['Eevee']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Umbreon"
poke_dict['Eevee']['learnset']['Tackle'] = 1

# Vaporeon
poke_dict['Vaporeon']['learnset']['Tackle'] = 1

# Jolteon
poke_dict['Jolteon']['learnset']['Tackle'] = 1

# Flareon
poke_dict['Flareon']['learnset']['Tackle'] = 1

# Porygon
poke_dict['Porygon']['evolution'] = {}
poke_dict['Porygon']['learnset']['Tackle'] = 1

# Omanyte
poke_dict['Omanyte']['evolution'] = {}
poke_dict['Omanyte']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Omanyte']['learnset']['Tackle'] = 1

# Omastar
poke_dict['Omastar']['learnset']['Tackle'] = 1

# Kabuto
poke_dict['Kabuto']['evolution'] = {}
poke_dict['Kabuto']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Kabuto']['learnset']['Tackle'] = 1

# Kabutops
poke_dict['Kabutops']['learnset']['Tackle'] = 1

# Aerodactyl
poke_dict['Aerodactyl']['learnset']['Tackle'] = 1

# Snorlax 
poke_dict['Snorlax']['learnset']['Pound'] = 1

# Articuno
poke_dict['Articuno']['learnset']['Icy Wind'] = 1

# Zapdos
poke_dict['Zapdos']['learnset']['Thundershock'] = 1

# Moltres
poke_dict['Moltres']['learnset']['Ember'] = 1

# Dratini
poke_dict['Dratini']['evolution'] = {}
poke_dict['Dratini']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Dratini']['learnset']['Tackle'] = 1

# Dragonair
poke_dict['Dragonair']['evolution'] = {}
poke_dict['Dragonair']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Dragonair']['learnset']['Tackle'] = 1

# Dragonite
poke_dict['Dragonite']['learnset']['Tackle'] = 1

# Mewtwo 
poke_dict['Mewtwo']['learnset']['Confusion'] = 1

# Mew
poke_dict['Mew']['learnset']['Confusion'] = 1

# =================================================
# GEN 2
# =================================================

# Chikorita
poke_dict['Chikorita']['evolution'] = {}
poke_dict['Chikorita']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Chikorita']['learnset']['Tackle'] = 1
poke_dict['Chikorita']['learnset']['Absorb'] = 1

# Bayleef
poke_dict['Bayleef']['evolution'] = {}
poke_dict['Bayleef']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Bayleef']['learnset']['Tackle'] = 1
poke_dict['Bayleef']['learnset']['Absorb'] = 1

# Meganium
poke_dict['Meganium']['learnset']['Tackle'] = 1
poke_dict['Meganium']['learnset']['Absorb'] = 1

# Cyndaquil
poke_dict['Cyndaquil']['evolution'] = {}
poke_dict['Cyndaquil']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Cyndaquil']['learnset']['Scratch'] = 1
poke_dict['Cyndaquil']['learnset']['Ember'] = 1

# Quilava
poke_dict['Quilava']['evolution'] = {}
poke_dict['Quilava']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Quilava']['learnset']['Scratch'] = 1
poke_dict['Quilava']['learnset']['Ember'] = 1

# Typhlosion
poke_dict['Typhlosion']['learnset']['Scratch'] = 1
poke_dict['Typhlosion']['learnset']['Ember'] = 1

# Totodile
poke_dict['Totodile']['evolution'] = {}
poke_dict['Totodile']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Totodile']['learnset']['Scratch'] = 1
poke_dict['Totodile']['learnset']['Bubble'] = 1

# Croconaw
poke_dict['Croconaw']['evolution'] = {}
poke_dict['Croconaw']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Croconaw']['learnset']['Scratch'] = 1
poke_dict['Croconaw']['learnset']['Bubble'] = 1

# Feraligatr
poke_dict['Feraligatr']['learnset']['Scratch'] = 1
poke_dict['Feraligatr']['learnset']['Bubble'] = 1

# Sentret
poke_dict['Sentret']['evolution'] = {}
poke_dict['Sentret']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Sentret']['learnset']['Scratch'] = 1

# Furret
poke_dict['Furret']['learnset']['Scratch'] = 1

# Hoothoot
poke_dict['Hoothoot']['evolution'] = {}
poke_dict['Hoothoot']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Hoothoot']['learnset']['Peck'] = 1

# Noctowl
poke_dict['Noctowl']['learnset']['Peck'] = 1

# Ledyba
poke_dict['Ledyba']['evolution'] = {}
poke_dict['Ledyba']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Ledyba']['learnset']['Pound'] = 1

# Ledian
poke_dict['Ledian']['learnset']['Pound'] = 1

# Spinarak
poke_dict['Spinarak']['evolution'] = {}
poke_dict['Spinarak']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Spinarak']['learnset']['Leech Life'] = 1

# Ariados
poke_dict['Ariados']['learnset']['Leech Life'] = 1

# Crobat
poke_dict['Crobat']['learnset']['Leech Life'] = 1

# Chinchou
poke_dict['Chinchou']['evolution'] = {}
poke_dict['Chinchou']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Chinchou']['learnset']['Water Gun'] = 1

# Lanturn
poke_dict['Lanturn']['learnset']['Water Gun'] = 1

# Pichu
poke_dict['Pichu']['evolution'] = {}
poke_dict['Pichu']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Pichu']['learnset']['Thundershock'] = 1

# Cleffa
poke_dict['Cleffa']['evolution'] = {}
poke_dict['Cleffa']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Cleffa']['learnset']['Pound'] = 1

# Igglybuff
poke_dict['Igglybuff']['evolution'] = {}
poke_dict['Igglybuff']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Igglybuff']['learnset']['Pound'] = 1

# Togepi
poke_dict['Togepi']['evolution'] = {}
poke_dict['Togepi']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Togepi']['learnset']['Tackle'] = 1

# Togetic
poke_dict['Togetic']['learnset']['Tackle'] = 1

# Natu
poke_dict['Natu']['evolution'] = {}
poke_dict['Natu']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Natu']['learnset']['Peck'] = 1

# Xatu
poke_dict['Natu']['learnset']['Peck'] = 1

# Mareep
poke_dict['Mareep']['evolution'] = {}
poke_dict['Mareep']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Mareep']['learnset']['Tackle'] = 1

# Flaaffy
poke_dict['Flaaffy']['evolution'] = {}
poke_dict['Flaaffy']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Flaaffy']['learnset']['Tackle'] = 1

# Ampharos
poke_dict['Ampharos']['learnset']['Tackle'] = 1

# Bellossom
poke_dict['Bellossom']['learnset']['Absorb'] = 1

# Marill
poke_dict['Marill']['evolution'] = {}
poke_dict['Marill']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Marill']['learnset']['Pound'] = 1

# Azumarill
poke_dict['Azumarill']['learnset']['Pound'] = 1

# Sudowoodo
poke_dict['Sudowoodo']['learnset']['Pound'] = 1

# Politoed
poke_dict['Politoed']['learnset']['Water Gun'] = 1

# Hoppip
poke_dict['Hoppip']['evolution'] = {}
poke_dict['Hoppip']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Hoppip']['learnset']['Tackle'] = 1

# Skiploom
poke_dict['Skiploom']['evolution'] = {}
poke_dict['Skiploom']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Skiploom']['learnset']['Tackle'] = 1

# Jumpluff
poke_dict['Jumpluff']['learnset']['Tackle'] = 1

# Aipom
poke_dict['Aipom']['learnset']['Scratch'] = 1

# Sunkern
poke_dict['Sunkern']['evolution'] = {}
poke_dict['Sunkern']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Sunkern']['learnset']['Tackle'] = 1

# Sunflora
poke_dict['Sunflora']['learnset']['Tackle'] = 1

# Yanma
poke_dict['Yanma']['learnset']['Tackle'] = 1

# Wooper
poke_dict['Wooper']['learnset']['Tackle'] = 1

# Quagsire
poke_dict['Quagsire']['learnset']['Tackle'] = 1

# Espeon
poke_dict['Espeon']['learnset']['Tackle'] = 1

# Umbreon
poke_dict['Umbreon']['learnset']['Tackle'] = 1

# Murkrow
poke_dict['Murkrow']['learnset']['Peck'] = 1

# Slowking
poke_dict['Slowking']['learnset']['Tackle'] = 1

# Misdreavus
poke_dict['Misdreavus']['learnset']['Lick'] = 1

# Unown
poke_dict['Unown']['learnset']['Confusion'] = 1

# Wobbuffet
poke_dict['Wobbuffet']['learnset']['Counter'] = 1

# Girafarig
poke_dict['Girafarig']['learnset']['Tackle'] = 1

# Pineco
poke_dict['Sunkern']['evolution'] = {}
poke_dict['Sunkern']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Pineco']['learnset']['Tackle'] = 1

# Forretress
poke_dict['Forretress']['learnset']['Tackle'] = 1

# Dunsparce
poke_dict['Dunsparce']['learnset']['Tackle'] = 1

# Gligar
poke_dict['Gligar']['learnset']['Scratch'] = 1

# Steelix
poke_dict['Steelix']['learnset']['Wrap'] = 1

# Snubbull
poke_dict['Snubbull']['evolution'] = {}
poke_dict['Snubbull']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Snubbull']['learnset']['Tackle'] = 1

# Granbull
poke_dict['Granbull']['learnset']['Pound'] = 1

# Qwilfish
poke_dict['Qwilfish']['learnset']['Tackle'] = 1

# Scizor
poke_dict['Scizor']['learnset']['Scratch'] = 1

# Shuckle
poke_dict['Shuckle']['learnset']['Tackle'] = 1

# Heracross
poke_dict['Heracross']['learnset']['Pound'] = 1

# Sneasel
poke_dict['Sneasel']['learnset']['Scratch'] = 1

# Teddiursa
poke_dict['Teddiursa']['evolution'] = {}
poke_dict['Teddiursa']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Teddiursa']['learnset']['Pound'] = 1

# Ursaring
poke_dict['Ursaring']['learnset']['Pound'] = 1

# Slugma
poke_dict['Slugma']['evolution'] = {}
poke_dict['Slugma']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Slugma']['learnset']['Ember'] = 1

# Magcargo
poke_dict['Magcargo']['learnset']['Ember'] = 1

# Swinub
poke_dict['Swinub']['evolution'] = {}
poke_dict['Swinub']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Swinub']['learnset']['Tackle'] = 1

# Piloswine
poke_dict['Piloswine']['learnset']['Tackle'] = 1

# Corsola
poke_dict['Corsola']['learnset']['Tackle'] = 1

# Remoraid
poke_dict['Remoraid']['evolution'] = {}
poke_dict['Remoraid']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Remoraid']['learnset']['Tackle'] = 1

# Octillery
poke_dict['Octillery']['learnset']['Tackle'] = 1
poke_dict['Octillery']['learnset']['Wrap'] = 10

# Delibird
poke_dict['Delibird']['learnset']['Peck'] = 1

# Mantine
poke_dict['Mantine']['learnset']['Water Gun'] = 1

# Skarmory
poke_dict['Skarmory']['learnset']['Peck'] = 1

# Houndour
poke_dict['Houndour']['evolution'] = {}
poke_dict['Houndour']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Houndour']['learnset']['Scratch'] = 1

# Houndoom
poke_dict['Houndoom']['learnset']['Scratch'] = 1

# Kingdra
poke_dict['Kingdra']['learnset']['Bubblebeam'] = 1

# Phanpy
poke_dict['Phanpy']['evolution'] = {}
poke_dict['Phanpy']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Phanpy']['learnset']['Tackle'] = 1

# Donphan
poke_dict['Donphan']['learnset']['Tackle'] = 1

# Porygon2
poke_dict['Porygon2']['learnset']['Tackle'] = 1

# Stantler
poke_dict['Stantler']['learnset']['Tackle'] = 1

# Smeargle
poke_dict['Smeargle']['learnset']['Tackle'] = 1
poke_dict['Smeargle']['learnset']['Sketch'] = 1

# Tyrogue
poke_dict['Tyrogue']['evolution'] = {}
poke_dict['Tyrogue']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Tyrogue']['learnset']['Pound'] = 1

# Hitmontop
poke_dict['Hitmontop']['learnset']['Pound'] = 1

# Smoochum
poke_dict['Smoochum']['evolution'] = {}
poke_dict['Smoochum']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Smoochum']['learnset']['Pound'] = 1

# Elekid
poke_dict['Elekid']['evolution'] = {}
poke_dict['Elekid']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Elekid']['learnset']['Pound'] = 1

# Magby
poke_dict['Magby']['evolution'] = {}
poke_dict['Magby']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Magby']['learnset']['Scratch'] = 1

# Miltank
poke_dict['Miltank']['learnset']['Tackle'] = 1

# Blissey
poke_dict['Blissey']['learnset']['Pound'] = 1

# Raikou
poke_dict['Raikou']['learnset']['Shock Wave'] = 1

# Entei
poke_dict['Entei']['learnset']['Flame Wheel'] = 1

# Suicune
poke_dict['Suicune']['learnset']['Water Gun'] = 1
poke_dict['Suicune']['learnset']['Aurora Beam'] = 41

# Larvitar
poke_dict['Larvitar']['evolution'] = {}
poke_dict['Larvitar']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Larvitar']['learnset']['Tackle'] = 1

# Pupitar
poke_dict['Pupitar']['evolution'] = {}
poke_dict['Pupitar']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Pupitar']['learnset']['Tackle'] = 1

# Tyranitar
poke_dict['Tyranitar']['learnset']['Tackle'] = 1

# Lugia
poke_dict['Lugia']['learnset']['Confusion'] = 1

# Ho-Oh
poke_dict['Ho-Oh']['learnset']['Wing Attack'] = 1

# Celebi
poke_dict['Celebi']['learnset']['Absorb'] = 1



# # write the dictionary
with open(path / 'poke_dict.json', 'w') as outfile:
    json.dump(poke_dict, outfile)


