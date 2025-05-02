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
poke_dict['Bulbasaur']['learnset']['TACKLE'] = 1
poke_dict['Bulbasaur']['learnset']['LEECH_SEED'] = 7
poke_dict['Bulbasaur']['learnset']['VINE_WHIP'] = 10
poke_dict['Bulbasaur']['learnset']['POISONPOWDER'] = 15
poke_dict['Bulbasaur']['learnset']['SLEEP_POWDER'] = 15
poke_dict['Bulbasaur']['learnset']['RAZOR_LEAF'] = 20
poke_dict['Bulbasaur']['learnset']['SWEET_SCENT'] = 25
poke_dict['Bulbasaur']['learnset']['GROWTH'] = 32
poke_dict['Bulbasaur']['learnset']['SYNTHESIS'] = 39
poke_dict['Bulbasaur']['learnset']['SOLARBEAM'] = 46

# Ivysaur
poke_dict['Ivysaur']['evolution'] = {}
poke_dict['Ivysaur']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Ivysaur']['evolution']['EVOLVE_LEVEL'][32] = "Venusaur"
poke_dict['Ivysaur']['learnset']['TACKLE'] = 1
poke_dict['Ivysaur']['learnset']['LEECH_SEED'] = 1
poke_dict['Ivysaur']['learnset']['VINE_WHIP'] = 10
poke_dict['Ivysaur']['learnset']['POISONPOWDER'] = 15
poke_dict['Ivysaur']['learnset']['SLEEP_POWDER'] = 15
poke_dict['Ivysaur']['learnset']['RAZOR_LEAF'] = 20
poke_dict['Ivysaur']['learnset']['SWEET_SCENT'] = 25
poke_dict['Ivysaur']['learnset']['GROWTH'] = 32
poke_dict['Ivysaur']['learnset']['SYNTHESIS'] = 39
poke_dict['Ivysaur']['learnset']['SOLARBEAM'] = 46

# Venusaur
poke_dict['Venusaur']['learnset']['TACKLE'] = 1
poke_dict['Venusaur']['learnset']['LEECH_SEED'] = 1
poke_dict['Venusaur']['learnset']['VINE_WHIP'] = 10
poke_dict['Venusaur']['learnset']['POISONPOWDER'] = 15
poke_dict['Venusaur']['learnset']['SLEEP_POWDER'] = 15
poke_dict['Venusaur']['learnset']['RAZOR_LEAF'] = 20
poke_dict['Venusaur']['learnset']['SWEET_SCENT'] = 25
poke_dict['Venusaur']['learnset']['GROWTH'] = 32
poke_dict['Venusaur']['learnset']['SYNTHESIS'] = 39
poke_dict['Venusaur']['learnset']['SOLARBEAM'] = 46

# Charmander
poke_dict['Charmander']['evolution'] = {}
poke_dict['Charmander']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Charmander']['learnset']['SCRATCH'] = 1
poke_dict['Charmander']['learnset']['EMBER'] = 1
poke_dict['Charmander']['learnset']['SMOKESCREEN'] = 13
poke_dict['Charmander']['learnset']['RAGE'] = 19
poke_dict['Charmander']['learnset']['SCARY_FACE'] = 25
poke_dict['Charmander']['learnset']['FLAMETHROWER'] = 31
poke_dict['Charmander']['learnset']['SLASH'] = 37
poke_dict['Charmander']['learnset']['DRAGON_RAGE'] = 43
poke_dict['Charmander']['learnset']['FIRE_SPIN'] = 49

# Charmeleon
poke_dict['Charmeleon']['evolution'] = {}
poke_dict['Charmander']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Charmeleon']['learnset']['SCRATCH'] = 1
poke_dict['Charmeleon']['learnset']['EMBER'] = 1
poke_dict['Charmeleon']['learnset']['SMOKESCREEN'] = 13
poke_dict['Charmeleon']['learnset']['RAGE'] = 19
poke_dict['Charmeleon']['learnset']['SCARY_FACE'] = 25
poke_dict['Charmeleon']['learnset']['FLAMETHROWER'] = 31
poke_dict['Charmeleon']['learnset']['SLASH'] = 37
poke_dict['Charmeleon']['learnset']['DRAGON_RAGE'] = 43
poke_dict['Charmeleon']['learnset']['FIRE_SPIN'] = 49

# Charizard
poke_dict['Charizard']['learnset']['SCRATCH'] = 1
poke_dict['Charizard']['learnset']['EMBER'] = 1
poke_dict['Charizard']['learnset']['SMOKESCREEN'] = 13
poke_dict['Charizard']['learnset']['RAGE'] = 19
poke_dict['Charizard']['learnset']['SCARY_FACE'] = 25
poke_dict['Charizard']['learnset']['FLAMETHROWER'] = 31
poke_dict['Charizard']['learnset']['WING_ATTACK'] = 37
poke_dict['Charizard']['learnset']['SLASH'] = 37
poke_dict['Charizard']['learnset']['DRAGON_RAGE'] = 43
poke_dict['Charizard']['learnset']['FIRE_SPIN'] = 49

# Squirtle
poke_dict['Squirtle']['evolution'] = {}
poke_dict['Squirtle']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Squirtle']['learnset']['TACKLE'] = 1
poke_dict['Squirtle']['learnset']['BUBBLE'] = 1
poke_dict['Squirtle']['learnset']['TAIL_WHIP'] = 1
poke_dict['Squirtle']['learnset']['WITHDRAW'] = 10
poke_dict['Squirtle']['learnset']['WATER_GUN'] = 13
poke_dict['Squirtle']['learnset']['BITE'] = 18
poke_dict['Squirtle']['learnset']['RAPID_SPIN'] = 23
poke_dict['Squirtle']['learnset']['PROTECT'] = 28
poke_dict['Squirtle']['learnset']['RAIN_DANCE'] = 33
poke_dict['Squirtle']['learnset']['SKULL_BASH'] = 40
poke_dict['Squirtle']['learnset']['HYDRO_PUMP'] = 47

# Wartortle
poke_dict['Wartortle']['evolution'] = {}
poke_dict['Wartortle']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Wartortle']['learnset']['TACKLE'] = 1
poke_dict['Wartortle']['learnset']['BUBBLE'] = 1
poke_dict['Wartortle']['learnset']['TAIL_WHIP'] = 1
poke_dict['Wartortle']['learnset']['WITHDRAW'] = 10
poke_dict['Wartortle']['learnset']['WATER_GUN'] = 13
poke_dict['Wartortle']['learnset']['BITE'] = 18
poke_dict['Wartortle']['learnset']['RAPID_SPIN'] = 23
poke_dict['Wartortle']['learnset']['PROTECT'] = 28
poke_dict['Wartortle']['learnset']['RAIN_DANCE'] = 33
poke_dict['Wartortle']['learnset']['SKULL_BASH'] = 40
poke_dict['Wartortle']['learnset']['HYDRO_PUMP'] = 47

# Blastoise
poke_dict['Blastoise']['learnset']['TACKLE'] = 1
poke_dict['Blastoise']['learnset']['BUBBLE'] = 1
poke_dict['Blastoise']['learnset']['TAIL_WHIP'] = 1
poke_dict['Blastoise']['learnset']['WITHDRAW'] = 10
poke_dict['Blastoise']['learnset']['WATER_GUN'] = 13
poke_dict['Blastoise']['learnset']['BITE'] = 18
poke_dict['Blastoise']['learnset']['RAPID_SPIN'] = 23
poke_dict['Blastoise']['learnset']['PROTECT'] = 28
poke_dict['Blastoise']['learnset']['RAIN_DANCE'] = 33
poke_dict['Blastoise']['learnset']['SKULL_BASH'] = 40
poke_dict['Blastoise']['learnset']['HYDRO_PUMP'] = 47

# Caterpie
poke_dict['Caterpie']['evolution'] = {}
poke_dict['Caterpie']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Caterpie']['learnset']['TACKLE'] = 1
poke_dict['Caterpie']['learnset']['STRING_SHOT'] = 1

# Metapod
poke_dict['Metapod']['evolution'] = {}
poke_dict['Metapod']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Metapod']['learnset']['TACKLE'] = 1
poke_dict['Metapod']['learnset']['HARDEN'] = 7

# Butterfree
poke_dict['Butterfree']['learnset']['CONFUSION'] = 1
poke_dict['Butterfree']['learnset']['CONFUSION'] = 10
poke_dict['Butterfree']['learnset']['POISONPOWDER'] = 13
poke_dict['Butterfree']['learnset']['STUN_SPORE'] = 14
poke_dict['Butterfree']['learnset']['SLEEP_POWDER'] = 15
poke_dict['Butterfree']['learnset']['SUPERSONIC'] = 18
poke_dict['Butterfree']['learnset']['WHIRLWIND'] = 23
poke_dict['Butterfree']['learnset']['GUST'] = 28
poke_dict['Butterfree']['learnset']['PSYBEAM'] = 34
poke_dict['Butterfree']['learnset']['SAFEGUARD'] = 40

# Weedle
poke_dict['Weedle']['evolution'] = {}
poke_dict['Weedle']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Weedle']['learnset']['POISON_STING'] = 1
poke_dict['Weedle']['learnset']['STRING_SHOT'] = 1

# Kakuna
poke_dict['Kakuna']['evolution'] = {}
poke_dict['Kakuna']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Kakuna']['learnset']['POISON_STING'] = 1
poke_dict['Kakuna']['learnset']['HARDEN'] = 7

# Beedrill
poke_dict['Beedrill']['learnset']['Leech Life'] = 1
poke_dict['Beedrill']['learnset']['FURY_ATTACK'] = 10
poke_dict['Beedrill']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Beedrill']['learnset']['TWINEEDLE'] = 1
poke_dict['Beedrill']['learnset']['RAGE'] = 1
poke_dict['Beedrill']['learnset']['PURSUIT'] = 1
poke_dict['Beedrill']['learnset']['PIN_MISSILE'] = 1
poke_dict['Beedrill']['learnset']['AGILITY'] = 1

# Pidgey
poke_dict['Pidgey']['evolution'] = {}
poke_dict['Pidgey']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Pidgey']['learnset']['PECK'] = 1
poke_dict['Pidgey']['learnset']['TACKLE'] = 1
poke_dict['Pidgey']['learnset']['SAND_ATTACK'] = 1
poke_dict['Pidgey']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Pidgey']['learnset']['WHIRLWIND'] = 1
poke_dict['Pidgey']['learnset']['WING_ATTACK'] = 1
poke_dict['Pidgey']['learnset']['AGILITY'] = 1
poke_dict['Pidgey']['learnset']['MIRROR_MOVE'] = 1

# Pidgeotto
poke_dict['Pidgeotto']['evolution'] = {}
poke_dict['Pidgeotto']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Pidgeotto']['learnset']['PECK'] = 1
poke_dict['Pidgeotto']['learnset']['TACKLE'] = 1
poke_dict['Pidgeotto']['learnset']['SAND_ATTACK'] = 1
poke_dict['Pidgeotto']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Pidgeotto']['learnset']['WHIRLWIND'] = 1
poke_dict['Pidgeotto']['learnset']['WING_ATTACK'] = 1
poke_dict['Pidgeotto']['learnset']['AGILITY'] = 1
poke_dict['Pidgeotto']['learnset']['MIRROR_MOVE'] = 1

# Pidgeot
poke_dict['Pidgeot']['learnset']['PECK'] = 1
poke_dict['Pidgeot']['learnset']['TACKLE'] = 1
poke_dict['Pidgeot']['learnset']['SAND_ATTACK'] = 1
poke_dict['Pidgeot']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Pidgeot']['learnset']['WHIRLWIND'] = 1
poke_dict['Pidgeot']['learnset']['WING_ATTACK'] = 1
poke_dict['Pidgeot']['learnset']['AGILITY'] = 1
poke_dict['Pidgeot']['learnset']['MIRROR_MOVE'] = 1

# Rattata
poke_dict['Rattata']['evolution'] = {}
poke_dict['Rattata']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Rattata']['learnset']['SCRATCH'] = 1
poke_dict['Rattata']['learnset']['TAIL_WHIP'] = 1
poke_dict['Rattata']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Rattata']['learnset']['HYPER_FANG'] = 1
poke_dict['Rattata']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Rattata']['learnset']['PURSUIT'] = 1
poke_dict['Rattata']['learnset']['SUPER_FANG'] = 1

# Raticate
poke_dict['Raticate']['learnset']['SCRATCH'] = 1
poke_dict['Raticate']['learnset']['TAIL_WHIP'] = 1
poke_dict['Raticate']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Raticate']['learnset']['HYPER_FANG'] = 1
poke_dict['Raticate']['learnset']['SCARY_FACE'] = 1
poke_dict['Raticate']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Raticate']['learnset']['PURSUIT'] = 1
poke_dict['Raticate']['learnset']['SUPER_FANG'] = 1


# Spearow
poke_dict['Spearow']['evolution'] = {}
poke_dict['Spearow']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Spearow']['learnset']['PECK'] = 1
poke_dict['Spearow']['learnset']['GROWL'] = 1
poke_dict['Spearow']['learnset']['LEER'] = 1
poke_dict['Spearow']['learnset']['FURY_ATTACK'] = 1
poke_dict['Spearow']['learnset']['PURSUIT'] = 1
poke_dict['Spearow']['learnset']['MIRROR_MOVE'] = 1
poke_dict['Spearow']['learnset']['DRILL_PECK'] = 1
poke_dict['Spearow']['learnset']['AGILITY'] = 1

# Fearow
poke_dict['Fearow']['learnset']['PECK'] = 1
poke_dict['Fearow']['learnset']['GROWL'] = 1
poke_dict['Fearow']['learnset']['LEER'] = 1
poke_dict['Fearow']['learnset']['FURY_ATTACK'] = 1
poke_dict['Fearow']['learnset']['PURSUIT'] = 1
poke_dict['Fearow']['learnset']['MIRROR_MOVE'] = 1
poke_dict['Fearow']['learnset']['DRILL_PECK'] = 1
poke_dict['Fearow']['learnset']['AGILITY'] = 1

# Ekans
poke_dict['Ekans']['evolution'] = {}
poke_dict['Ekans']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Ekans']['learnset']['WRAP'] = 1
poke_dict['Ekans']['learnset']['LEER'] = 1
poke_dict['Ekans']['learnset']['POISON_STING'] = 1
poke_dict['Ekans']['learnset']['BITE'] = 1
poke_dict['Ekans']['learnset']['GLARE'] = 1
poke_dict['Ekans']['learnset']['SCREECH'] = 1
poke_dict['Ekans']['learnset']['ACID'] = 1
poke_dict['Ekans']['learnset']['HAZE'] = 1

# Arbok
poke_dict['Arbok']['learnset']['WRAP'] = 1
poke_dict['Arbok']['learnset']['LEER'] = 1
poke_dict['Arbok']['learnset']['POISON_STING'] = 1
poke_dict['Arbok']['learnset']['BITE'] = 1
poke_dict['Arbok']['learnset']['GLARE'] = 1
poke_dict['Arbok']['learnset']['SCREECH'] = 1
poke_dict['Arbok']['learnset']['ACID'] = 1
poke_dict['Arbok']['learnset']['HAZE'] = 1

# Pikachu
poke_dict['Pikachu']['evolution'] = {}
poke_dict['Pikachu']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Pikachu']['evolution']['EVOLVE_ITEM']['THUNDERSTONE'] = "RAICHU"
poke_dict['Pikachu']['learnset']['THUNDERSHOCK'] = 1
poke_dict['Pikachu']['learnset']['GROWL'] = 1
poke_dict['Pikachu']['learnset']['TAIL_WHIP'] = 1
poke_dict['Pikachu']['learnset']['THUNDER_WAVE'] = 1
poke_dict['Pikachu']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Pikachu']['learnset']['DOUBLE_TEAM'] = 1
poke_dict['Pikachu']['learnset']['SLAM'] = 1
poke_dict['Pikachu']['learnset']['THUNDERBOLT'] = 1
poke_dict['Pikachu']['learnset']['AGILITY'] = 1
poke_dict['Pikachu']['learnset']['THUNDER'] = 1
poke_dict['Pikachu']['learnset']['LIGHT_SCREEN'] = 1

# Raichu
poke_dict['Raichu']['learnset']['THUNDERSHOCK'] = 1
poke_dict['Raichu']['learnset']['GROWL'] = 1
poke_dict['Raichu']['learnset']['TAIL_WHIP'] = 1
poke_dict['Raichu']['learnset']['THUNDER_WAVE'] = 1
poke_dict['Raichu']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Raichu']['learnset']['DOUBLE_TEAM'] = 1
poke_dict['Raichu']['learnset']['SLAM'] = 1
poke_dict['Raichu']['learnset']['THUNDERBOLT'] = 1
poke_dict['Raichu']['learnset']['AGILITY'] = 1
poke_dict['Raichu']['learnset']['THUNDER'] = 1
poke_dict['Raichu']['learnset']['LIGHT_SCREEN'] = 1

# Sandshrew
poke_dict['Sandshrew']['evolution'] = {}
poke_dict['Sandshrew']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Sandshrew']['learnset']['SCRATCH'] = 1
poke_dict['Sandshrew']['learnset']['DEFENSE_CURL'] = 1
poke_dict['Sandshrew']['learnset']['SAND_ATTACK'] = 1
poke_dict['Sandshrew']['learnset']['POISON_STING'] = 1
poke_dict['Sandshrew']['learnset']['SLASH'] = 1
poke_dict['Sandshrew']['learnset']['SWIFT'] = 1
poke_dict['Sandshrew']['learnset']['FURY_SWIPES'] = 1
poke_dict['Sandshrew']['learnset']['SANDSTORM'] = 1

# Sandslash
poke_dict['Sandslash']['learnset']['SCRATCH'] = 1
poke_dict['Sandslash']['learnset']['DEFENSE_CURL'] = 1
poke_dict['Sandslash']['learnset']['SAND_ATTACK'] = 1
poke_dict['Sandslash']['learnset']['POISON_STING'] = 1
poke_dict['Sandslash']['learnset']['SLASH'] = 1
poke_dict['Sandslash']['learnset']['SWIFT'] = 1
poke_dict['Sandslash']['learnset']['FURY_SWIPES'] = 1
poke_dict['Sandslash']['learnset']['SANDSTORM'] = 1

# NOTE UNIQUE CODES FOR NIDORAN!!

# Nidoran♀
poke_dict['Nidoran\u00e2\u2122\u201a']['evolution'] = {}
poke_dict['Nidoran\u00e2\u2122\u201a']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['TACKLE'] = 1
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['GROWL'] = 1
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['DOUBLE_KICK'] = 1
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['POISON_STING'] = 1
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['TAIL_WHIP'] = 1
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['BITE'] = 1
poke_dict['Nidoran\u00e2\u2122\u201a']['learnset']['FURY_SWIPES'] = 1

# Nidorina
poke_dict['Nidorina']['evolution'] = {}
poke_dict['Nidorina']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Nidorina']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Nidoqueen"
poke_dict['Nidorina']['learnset']['TACKLE'] = 1
poke_dict['Nidorina']['learnset']['GROWL'] = 1
poke_dict['Nidorina']['learnset']['DOUBLE_KICK'] = 1
poke_dict['Nidorina']['learnset']['POISON_STING'] = 1
poke_dict['Nidorina']['learnset']['TAIL_WHIP'] = 1
poke_dict['Nidorina']['learnset']['BITE'] = 1
poke_dict['Nidorina']['learnset']['FURY_SWIPES'] = 1

# Nidoqueen
poke_dict['Nidoqueen']['learnset']['TACKLE'] = 1
poke_dict['Nidoqueen']['learnset']['POISON_STING'] = 1
poke_dict['Nidoqueen']['learnset']['GROWL'] = 1
poke_dict['Nidoqueen']['learnset']['DOUBLE_KICK'] = 1
poke_dict['Nidoqueen']['learnset']['BITE'] = 1
poke_dict['Nidoqueen']['learnset']['FURY_SWIPES'] = 1
poke_dict['Nidoqueen']['learnset']['BODY_SLAM'] = 1

# Nidoran♂
poke_dict['Nidoran\u00e2\u2122\u20ac']['evolution'] = {}
poke_dict['Nidoran\u00e2\u2122\u20ac']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['TACKLE'] = 1
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['HORN_ATTACK'] = 1
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['DOUBLE_KICK'] = 1
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['POISON_STING'] = 1
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['FURY_ATTACK'] = 1
poke_dict['Nidoran\u00e2\u2122\u20ac']['learnset']['HORN_DRILL'] = 1

# Nidorino
poke_dict['Nidorino']['evolution'] = {}
poke_dict['Nidorino']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Nidorino']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Nidoking"
poke_dict['Nidorino']['learnset']['TACKLE'] = 1
poke_dict['Nidorino']['learnset']['POISON_STING'] = 1
poke_dict['Nidorino']['learnset']['HORN_ATTACK'] = 1
poke_dict['Nidorino']['learnset']['DOUBLE_KICK'] = 1
poke_dict['Nidorino']['learnset']['POISON_STING'] = 1
poke_dict['Nidorino']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Nidorino']['learnset']['FURY_ATTACK'] = 1
poke_dict['Nidorino']['learnset']['HORN_DRILL'] = 1

# Nidoking
poke_dict['Nidoking']['learnset']['TACKLE'] = 1
poke_dict['Nidoking']['learnset']['POISON_STING'] = 1
poke_dict['Nidoking']['learnset']['HORN_ATTACK'] = 1
poke_dict['Nidoking']['learnset']['DOUBLE_KICK'] = 1
poke_dict['Nidoking']['learnset']['POISON_STING'] = 1
poke_dict['Nidoking']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Nidoking']['learnset']['FURY_ATTACK'] = 1
poke_dict['Nidoking']['learnset']['THRASH'] = 1
poke_dict['Nidoking']['learnset']['HORN_DRILL'] = 1

# Clefairy
poke_dict['Clefairy']['evolution'] = {}
poke_dict['Clefairy']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Clefairy']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Clefable"
poke_dict['Clefairy']['learnset']['POUND'] = 1
poke_dict['Clefairy']['learnset']['GROWL'] = 1
poke_dict['Clefairy']['learnset']['ENCORE'] = 1
poke_dict['Clefairy']['learnset']['SING'] = 1
poke_dict['Clefairy']['learnset']['DOUBLESLAP'] = 1
poke_dict['Clefairy']['learnset']['MINIMIZE'] = 1
poke_dict['Clefairy']['learnset']['DEFENSE_CURL'] = 1
poke_dict['Clefairy']['learnset']['METRONOME'] = 1
poke_dict['Clefairy']['learnset']['MOONLIGHT'] = 1
poke_dict['Clefairy']['learnset']['LIGHT_SCREEN'] = 1

# Clefable
poke_dict['Clefable']['learnset']['POUND'] = 1
poke_dict['Clefable']['learnset']['GROWL'] = 1
poke_dict['Clefable']['learnset']['ENCORE'] = 1
poke_dict['Clefable']['learnset']['SING'] = 1
poke_dict['Clefable']['learnset']['DOUBLESLAP'] = 1
poke_dict['Clefable']['learnset']['MINIMIZE'] = 1
poke_dict['Clefable']['learnset']['DEFENSE_CURL'] = 1
poke_dict['Clefable']['learnset']['METRONOME'] = 1
poke_dict['Clefable']['learnset']['MOONLIGHT'] = 1
poke_dict['Clefable']['learnset']['LIGHT_SCREEN'] = 1

# Vulpix
poke_dict['Vulpix']['evolution'] = {}
poke_dict['Vulpix']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Vulpix']['evolution']['EVOLVE_ITEM']['FIRE_STONE'] = "Ninetails"
poke_dict['Vulpix']['learnset']['EMBER'] = 1
poke_dict['Vulpix']['learnset']['TAIL_WHIP'] = 1
poke_dict['Vulpix']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Vulpix']['learnset']['ROAR'] = 1
poke_dict['Vulpix']['learnset']['CONFUSE_RAY'] = 1
poke_dict['Vulpix']['learnset']['SAFEGUARD'] = 1
poke_dict['Vulpix']['learnset']['FLAMETHROWER'] = 1
poke_dict['Vulpix']['learnset']['FIRE_SPIN'] = 1

# Ninetales
poke_dict['Ninetales']['learnset']['EMBER'] = 1
poke_dict['Ninetales']['learnset']['TAIL_WHIP'] = 1
poke_dict['Ninetales']['learnset']['QUICK_ATTACK'] = 1
poke_dict['Ninetales']['learnset']['ROAR'] = 1
poke_dict['Ninetales']['learnset']['CONFUSE_RAY'] = 1
poke_dict['Ninetales']['learnset']['SAFEGUARD'] = 1
poke_dict['Ninetales']['learnset']['FLAMETHROWER'] = 1
poke_dict['Ninetales']['learnset']['FIRE_SPIN'] = 1

# Jigglypuff
poke_dict['Jigglypuff']['evolution'] = {}
poke_dict['Jigglypuff']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Jigglypuff']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Wigglytuff"
poke_dict['Jigglypuff']['learnset']['POUND'] = 1
poke_dict['Jigglypuff']['learnset']['SING'] = 1
poke_dict['Jigglypuff']['learnset']['DEFENSE_CURL'] = 1
poke_dict['Jigglypuff']['learnset']['DISABLE'] = 1
poke_dict['Jigglypuff']['learnset']['ROLLOUT'] = 1
poke_dict['Jigglypuff']['learnset']['DOUBLESLAP'] = 1
poke_dict['Jigglypuff']['learnset']['REST'] = 1
poke_dict['Jigglypuff']['learnset']['BODY_SLAM'] = 1
poke_dict['Jigglypuff']['learnset']['DOUBLE_EDGE'] = 1


# Wigglytuff
poke_dict['Wigglytuff']['learnset']['POUND'] = 1
poke_dict['Wigglytuff']['learnset']['SING'] = 1
poke_dict['Wigglytuff']['learnset']['DEFENSE_CURL'] = 1
poke_dict['Wigglytuff']['learnset']['DISABLE'] = 1
poke_dict['Wigglytuff']['learnset']['ROLLOUT'] = 1
poke_dict['Wigglytuff']['learnset']['DOUBLESLAP'] = 1
poke_dict['Wigglytuff']['learnset']['REST'] = 1
poke_dict['Wigglytuff']['learnset']['BODY_SLAM'] = 1
poke_dict['Wigglytuff']['learnset']['DOUBLE_EDGE'] = 1

# Zubat
poke_dict['Zubat']['evolution'] = {}
poke_dict['Zubat']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Zubat']['learnset']['LEECH_LIFE'] = 1
poke_dict['Zubat']['learnset']['SUPERSONIC'] = 1
poke_dict['Zubat']['learnset']['BITE'] = 1
poke_dict['Zubat']['learnset']['CONFUSE_RAY'] = 1
poke_dict['Zubat']['learnset']['WING_ATTACK'] = 1
poke_dict['Zubat']['learnset']['MEAN_LOOK'] = 1
poke_dict['Zubat']['learnset']['HAZE'] = 1

# Golbat
poke_dict['Golbat']['evolution'] = {}
poke_dict['Golbat']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Golbat']['evolution']['EVOLVE_ITEM']['MOON_STONE'] = "Crobat"
poke_dict['Golbat']['learnset']['LEECH_LIFE'] = 1
poke_dict['Golbat']['learnset']['SUPERSONIC'] = 1
poke_dict['Golbat']['learnset']['SCREECH'] = 1
poke_dict['Golbat']['learnset']['BITE'] = 1
poke_dict['Golbat']['learnset']['CONFUSE_RAY'] = 1
poke_dict['Golbat']['learnset']['WING_ATTACK'] = 1
poke_dict['Golbat']['learnset']['MEAN_LOOK'] = 1
poke_dict['Golbat']['learnset']['HAZE'] = 1

# Oddish
poke_dict['Oddish']['evolution'] = {}
poke_dict['Oddish']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Oddish']['learnset']['ABSORB'] = 1
poke_dict['Oddish']['learnset']['SWEET_SCENT'] = 1
poke_dict['Oddish']['learnset']['POISONPOWDER'] = 1
poke_dict['Oddish']['learnset']['STUN_SPORE'] = 1
poke_dict['Oddish']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Oddish']['learnset']['ACID'] = 1
poke_dict['Oddish']['learnset']['MOONLIGHT'] = 1
poke_dict['Oddish']['learnset']['PETAL_DANCE'] = 1

# Gloom
poke_dict['Gloom']['evolution'] = {}
poke_dict['Gloom']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Gloom']['evolution']['EVOLVE_ITEM']['LEAF_STONE'] = "Vileplume"
poke_dict['Gloom']['evolution']['EVOLVE_ITEM']['SUN_STONE'] = "Bellossom"
poke_dict['Gloom']['learnset']['ABSORB'] = 1
poke_dict['Gloom']['learnset']['SWEET_SCENT'] = 1
poke_dict['Gloom']['learnset']['POISONPOWDER'] = 1
poke_dict['Gloom']['learnset']['POISONPOWDER'] = 1
poke_dict['Gloom']['learnset']['STUN_SPORE'] = 1
poke_dict['Gloom']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Gloom']['learnset']['ACID'] = 1
poke_dict['Gloom']['learnset']['MOONLIGHT'] = 1
poke_dict['Gloom']['learnset']['PETAL_DANCE'] = 1

# Vileplume
poke_dict['Vileplume']['learnset']['ABSORB'] = 1
poke_dict['Vileplume']['learnset']['SWEET_SCENT'] = 1
poke_dict['Vileplume']['learnset']['POISONPOWDER'] = 1
poke_dict['Vileplume']['learnset']['POISONPOWDER'] = 1
poke_dict['Vileplume']['learnset']['STUN_SPORE'] = 1
poke_dict['Vileplume']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Vileplume']['learnset']['ACID'] = 1
poke_dict['Vileplume']['learnset']['MOONLIGHT'] = 1
poke_dict['Vileplume']['learnset']['PETAL_DANCE'] = 1

# Paras
poke_dict['Paras']['evolution'] = {}
poke_dict['Paras']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Paras']['learnset']['SCRATCH'] = 1
poke_dict['Paras']['learnset']['STUN_SPORE'] = 1
poke_dict['Paras']['learnset']['POISONPOWDER'] = 1
poke_dict['Paras']['learnset']['LEECH_LIFE'] = 1
poke_dict['Paras']['learnset']['SPORE'] = 1
poke_dict['Paras']['learnset']['SLASH'] = 1
poke_dict['Paras']['learnset']['GROWTH'] = 1
poke_dict['Paras']['learnset']['GIGA_DRAIN'] = 1

# Parasect
poke_dict['Parasect']['learnset']['LEECH_LIFE'] = 1
poke_dict['Parasect']['learnset']['SCRATCH'] = 1
poke_dict['Parasect']['learnset']['STUN_SPORE'] = 1
poke_dict['Parasect']['learnset']['POISONPOWDER'] = 1
poke_dict['Parasect']['learnset']['SPORE'] = 1
poke_dict['Parasect']['learnset']['SLASH'] = 1
poke_dict['Parasect']['learnset']['GROWTH'] = 1
poke_dict['Parasect']['learnset']['GIGA_DRAIN'] = 1

# Venonat
poke_dict['Venonat']['evolution'] = {}
poke_dict['Venonat']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Venonat']['learnset']['LEECH_LIFE'] = 1
poke_dict['Venonat']['learnset']['DISABLE'] = 1
poke_dict['Venonat']['learnset']['FORESIGHT'] = 1
poke_dict['Venonat']['learnset']['SUPERSONIC'] = 1
poke_dict['Venonat']['learnset']['CONFUSION'] = 1
poke_dict['Venonat']['learnset']['POISONPOWDER'] = 1
poke_dict['Venonat']['learnset']['STUN_SPORE'] = 1
poke_dict['Venonat']['learnset']['PSYBEAM'] = 1
poke_dict['Venonat']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Venonat']['learnset']['PSYCHIC_M'] = 1

# Venomoth
poke_dict['Venomoth']['learnset']['LEECH_LIFE'] = 1
poke_dict['Venomoth']['learnset']['DISABLE'] = 1
poke_dict['Venomoth']['learnset']['FORESIGHT'] = 1
poke_dict['Venomoth']['learnset']['SUPERSONIC'] = 1
poke_dict['Venomoth']['learnset']['CONFUSION'] = 1
poke_dict['Venomoth']['learnset']['POISONPOWDER'] = 1
poke_dict['Venomoth']['learnset']['STUN_SPORE'] = 1
poke_dict['Venomoth']['learnset']['GUST'] = 1
poke_dict['Venomoth']['learnset']['PSYBEAM'] = 1
poke_dict['Venomoth']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Venomoth']['learnset']['PSYCHIC_M'] = 1

# Diglett
poke_dict['Diglett']['evolution'] = {}
poke_dict['Diglett']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Diglett']['learnset']['SCRATCH'] = 1
poke_dict['Diglett']['learnset']['GROWL'] = 1
poke_dict['Diglett']['learnset']['MAGNITUDE'] = 1
poke_dict['Diglett']['learnset']['DIG'] = 1
poke_dict['Diglett']['learnset']['SAND_ATTACK'] = 1
poke_dict['Diglett']['learnset']['SLASH'] = 1
poke_dict['Diglett']['learnset']['EARTHQUAKE'] = 1
poke_dict['Diglett']['learnset']['FISSURE'] = 1

# Dugtrio
poke_dict['Dugtrio']['learnset']['SCRATCH'] = 1
poke_dict['Dugtrio']['learnset']['TRI_ATTACK'] = 1
poke_dict['Dugtrio']['learnset']['GROWL'] = 1
poke_dict['Dugtrio']['learnset']['MAGNITUDE'] = 1
poke_dict['Dugtrio']['learnset']['DIG'] = 1
poke_dict['Dugtrio']['learnset']['SAND_ATTACK'] = 1
poke_dict['Dugtrio']['learnset']['SLASH'] = 1
poke_dict['Dugtrio']['learnset']['EARTHQUAKE'] = 1
poke_dict['Dugtrio']['learnset']['FISSURE'] = 1

# Meowth
poke_dict['Meowth']['evolution'] = {}
poke_dict['Meowth']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Meowth']['learnset']['SCRATCH'] = 1
poke_dict['Meowth']['learnset']['GROWL'] = 1
poke_dict['Meowth']['learnset']['BITE'] = 1
poke_dict['Meowth']['learnset']['PAY_DAY'] = 1
poke_dict['Meowth']['learnset']['FAINT_ATTACK'] = 1
poke_dict['Meowth']['learnset']['SCREECH'] = 1
poke_dict['Meowth']['learnset']['FURY_SWIPES'] = 1
poke_dict['Meowth']['learnset']['SLASH'] = 1

# Persian
poke_dict['Persian']['learnset']['SCRATCH'] = 1
poke_dict['Persian']['learnset']['GROWL'] = 1
poke_dict['Persian']['learnset']['BITE'] = 1
poke_dict['Persian']['learnset']['PAY_DAY'] = 1
poke_dict['Persian']['learnset']['FAINT_ATTACK'] = 1
poke_dict['Persian']['learnset']['SCREECH'] = 1
poke_dict['Persian']['learnset']['FURY_SWIPES'] = 1
poke_dict['Persian']['learnset']['SLASH'] = 1

# Psyduck
poke_dict['Psyduck']['evolution'] = {}
poke_dict['Psyduck']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Psyduck']['learnset']['PECK'] = 1
poke_dict['Psyduck']['learnset']['TAIL_WHIP'] = 1
poke_dict['Psyduck']['learnset']['DISABLE'] = 1
poke_dict['Psyduck']['learnset']['CONFUSION'] = 1
poke_dict['Psyduck']['learnset']['SCREECH'] = 1
poke_dict['Psyduck']['learnset']['PSYCH_UP'] = 1
poke_dict['Psyduck']['learnset']['FURY_SWIPES'] = 1
poke_dict['Psyduck']['learnset']['HYDRO_PUMP'] = 1


# Golduck
poke_dict['Golduck']['learnset']['PECK'] = 1
poke_dict['Golduck']['learnset']['TAIL_WHIP'] = 1
poke_dict['Golduck']['learnset']['DISABLE'] = 1
poke_dict['Golduck']['learnset']['CONFUSION'] = 1
poke_dict['Golduck']['learnset']['SCREECH'] = 1
poke_dict['Golduck']['learnset']['PSYCH_UP'] = 1
poke_dict['Golduck']['learnset']['FURY_SWIPES'] = 1
poke_dict['Golduck']['learnset']['HYDRO_PUMP'] = 1

# Mankey
poke_dict['Mankey']['evolution'] = {}
poke_dict['Mankey']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Mankey']['learnset']['SCRATCH'] = 1
poke_dict['Mankey']['learnset']['LEER'] = 1
poke_dict['Mankey']['learnset']['LOW_KICK'] = 1
poke_dict['Mankey']['learnset']['KARATE_CHOP'] = 1
poke_dict['Mankey']['learnset']['FURY_SWIPES'] = 1
poke_dict['Mankey']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Mankey']['learnset']['SEISMIC_TOSS'] = 1
poke_dict['Mankey']['learnset']['CROSS_CHOP'] = 1
poke_dict['Mankey']['learnset']['SCREECH'] = 1
poke_dict['Mankey']['learnset']['THRASH'] = 1

# Primeape
poke_dict['Primeape']['learnset']['SCRATCH'] = 1
poke_dict['Primeape']['learnset']['LEER'] = 1
poke_dict['Primeape']['learnset']['LOW_KICK'] = 1
poke_dict['Primeape']['learnset']['RAGE'] = 1
poke_dict['Primeape']['learnset']['KARATE_CHOP'] = 1
poke_dict['Primeape']['learnset']['FURY_SWIPES'] = 1
poke_dict['Primeape']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Primeape']['learnset']['SEISMIC_TOSS'] = 1
poke_dict['Primeape']['learnset']['CROSS_CHOP'] = 1
poke_dict['Primeape']['learnset']['SCREECH'] = 1
poke_dict['Primeape']['learnset']['THRASH'] = 1

# Growlithe
poke_dict['Growlithe']['evolution'] = {}
poke_dict['Growlithe']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Growlithe']['evolution']['EVOLVE_ITEM']['FIRE_STONE'] = "Arcanine"
poke_dict['Growlithe']['learnset']['BITE'] = 1
poke_dict['Growlithe']['learnset']['ROAR'] = 1
poke_dict['Growlithe']['learnset']['EMBER'] = 1
poke_dict['Growlithe']['learnset']['LEER'] = 1
poke_dict['Growlithe']['learnset']['TAKE_DOWN'] = 1
poke_dict['Growlithe']['learnset']['FLAME_WHEEL'] = 1
poke_dict['Growlithe']['learnset']['AGILITY'] = 1
poke_dict['Growlithe']['learnset']['FLAMETHROWER'] = 1

# Arcanine
poke_dict['Arcanine']['learnset']['BITE'] = 1
poke_dict['Arcanine']['learnset']['ROAR'] = 1
poke_dict['Arcanine']['learnset']['EMBER'] = 1
poke_dict['Arcanine']['learnset']['LEER'] = 1
poke_dict['Arcanine']['learnset']['TAKE_DOWN'] = 1
poke_dict['Arcanine']['learnset']['FLAME_WHEEL'] = 1
poke_dict['Arcanine']['learnset']['AGILITY'] = 1
poke_dict['Arcanine']['learnset']['FLAMETHROWER'] = 1
poke_dict['Arcanine']['learnset']['EXTREMESPEED'] = 1

# Poliwag
poke_dict['Poliwag']['evolution'] = {}
poke_dict['Poliwag']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Poliwag']['learnset']['BUBBLE'] = 1
poke_dict['Poliwag']['learnset']['HYPNOSIS'] = 1
poke_dict['Poliwag']['learnset']['WATER_GUN'] = 1
poke_dict['Poliwag']['learnset']['DOUBLESLAP'] = 1
poke_dict['Poliwag']['learnset']['RAIN_DANCE'] = 1
poke_dict['Poliwag']['learnset']['BODY_SLAM'] = 1
poke_dict['Poliwag']['learnset']['BELLY_DRUM'] = 1
poke_dict['Poliwag']['learnset']['HYDRO_PUMP'] = 1

# Poliwhirl
poke_dict['Poliwhirl']['evolution'] = {}
poke_dict['Poliwhirl']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Poliwhirl']['evolution']['EVOLVE_ITEM']["WATER_STONE"] = "Poliwrath"
poke_dict['Poliwhirl']['evolution']['EVOLVE_ITEM']["SUN_STONE"] = "Politoed"
poke_dict['Poliwhirl']['learnset']['BUBBLE'] = 1
poke_dict['Poliwhirl']['learnset']['HYPNOSIS'] = 1
poke_dict['Poliwhirl']['learnset']['WATER_GUN'] = 1
poke_dict['Poliwhirl']['learnset']['DOUBLESLAP'] = 1
poke_dict['Poliwhirl']['learnset']['RAIN_DANCE'] = 1
poke_dict['Poliwhirl']['learnset']['BODY_SLAM'] = 1
poke_dict['Poliwhirl']['learnset']['BELLY_DRUM'] = 1
poke_dict['Poliwhirl']['learnset']['HYDRO_PUMP'] = 1


# Poliwrath
poke_dict['Poliwrath']['learnset']['BUBBLE'] = 1
poke_dict['Poliwrath']['learnset']['HYPNOSIS'] = 1
poke_dict['Poliwrath']['learnset']['WATER_GUN'] = 1
poke_dict['Poliwrath']['learnset']['DOUBLESLAP'] = 1
poke_dict['Poliwrath']['learnset']['SUBMISSION'] = 1
poke_dict['Poliwrath']['learnset']['RAIN_DANCE'] = 1
poke_dict['Poliwrath']['learnset']['BODY_SLAM'] = 1
poke_dict['Poliwrath']['learnset']['BELLY_DRUM'] = 1
poke_dict['Poliwrath']['learnset']['MIND_READER'] = 1
poke_dict['Poliwrath']['learnset']['HYDRO_PUMP'] = 1

# Abra
poke_dict['Abra']['evolution'] = {}
poke_dict['Abra']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Abra']['learnset']['TELEPORT'] = 1

# Kadabra
poke_dict['Kadabra']['evolution'] = {}
poke_dict['Kadabra']['learnset']['TELEPORT'] = 1
poke_dict['Kadabra']['learnset']['KINESIS'] = 1
poke_dict['Kadabra']['learnset']['CONFUSION'] = 1
poke_dict['Kadabra']['learnset']['DISABLE'] = 1
poke_dict['Kadabra']['learnset']['PSYBEAM'] = 1
poke_dict['Kadabra']['learnset']['RECOVER'] = 1
poke_dict['Kadabra']['learnset']['FUTURE_SIGHT'] = 1
poke_dict['Kadabra']['learnset']['PSYCHIC_M'] = 1
poke_dict['Kadabra']['learnset']['REFLECT'] = 1

# Alakazam
poke_dict['Alakazam']['learnset']['TELEPORT'] = 1
poke_dict['Alakazam']['learnset']['KINESIS'] = 1
poke_dict['Alakazam']['learnset']['CONFUSION'] = 1
poke_dict['Alakazam']['learnset']['DISABLE'] = 1
poke_dict['Alakazam']['learnset']['PSYBEAM'] = 1
poke_dict['Alakazam']['learnset']['RECOVER'] = 1
poke_dict['Alakazam']['learnset']['FUTURE_SIGHT'] = 1
poke_dict['Alakazam']['learnset']['PSYCHIC_M'] = 1
poke_dict['Alakazam']['learnset']['REFLECT'] = 1

# Machop
poke_dict['Machop']['evolution'] = {}
poke_dict['Machop']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Machop']['learnset']['POUND'] = 1
poke_dict['Machop']['learnset']['LOW_KICK'] = 1
poke_dict['Machop']['learnset']['LEER'] = 1
poke_dict['Machop']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Machop']['learnset']['KARATE_CHOP'] = 1
poke_dict['Machop']['learnset']['SEISMIC_TOSS'] = 1
poke_dict['Machop']['learnset']['FORESIGHT'] = 1
poke_dict['Machop']['learnset']['VITAL_THROW'] = 1
poke_dict['Machop']['learnset']['CROSS_CHOP'] = 1
poke_dict['Machop']['learnset']['SCARY_FACE'] = 1
poke_dict['Machop']['learnset']['SUBMISSION'] = 1

# Machoke
poke_dict['Machoke']['evolution'] = {}
poke_dict['Machoke']['learnset']['POUND'] = 1
poke_dict['Machoke']['learnset']['LOW_KICK'] = 1
poke_dict['Machoke']['learnset']['LEER'] = 1
poke_dict['Machoke']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Machoke']['learnset']['KARATE_CHOP'] = 1
poke_dict['Machoke']['learnset']['SEISMIC_TOSS'] = 1
poke_dict['Machoke']['learnset']['FORESIGHT'] = 1
poke_dict['Machoke']['learnset']['VITAL_THROW'] = 1
poke_dict['Machoke']['learnset']['CROSS_CHOP'] = 1
poke_dict['Machoke']['learnset']['SCARY_FACE'] = 1
poke_dict['Machoke']['learnset']['SUBMISSION'] = 1

# Machamp
poke_dict['Machamp']['learnset']['POUND'] = 1
poke_dict['Machamp']['learnset']['LOW_KICK'] = 1
poke_dict['Machamp']['learnset']['LEER'] = 1
poke_dict['Machamp']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Machamp']['learnset']['KARATE_CHOP'] = 1
poke_dict['Machamp']['learnset']['SEISMIC_TOSS'] = 1
poke_dict['Machamp']['learnset']['FORESIGHT'] = 1
poke_dict['Machamp']['learnset']['VITAL_THROW'] = 1
poke_dict['Machamp']['learnset']['CROSS_CHOP'] = 1
poke_dict['Machamp']['learnset']['SCARY_FACE'] = 1
poke_dict['Machamp']['learnset']['SUBMISSION'] = 1

# Bellsprout
poke_dict['Bellsprout']['evolution'] = {}
poke_dict['Bellsprout']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Bellsprout']['learnset']['VINE_WHIP'] = 1
poke_dict['Bellsprout']['learnset']['GROWTH'] = 1
poke_dict['Bellsprout']['learnset']['WRAP'] = 1
poke_dict['Bellsprout']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Bellsprout']['learnset']['POISONPOWDER'] = 1
poke_dict['Bellsprout']['learnset']['STUN_SPORE'] = 1
poke_dict['Bellsprout']['learnset']['ACID'] = 1
poke_dict['Bellsprout']['learnset']['SWEET_SCENT'] = 1
poke_dict['Bellsprout']['learnset']['RAZOR_LEAF'] = 1
poke_dict['Bellsprout']['learnset']['SLAM'] = 1

# Weepinbell
poke_dict['Weepinbell']['evolution'] = {}
poke_dict['Weepinbell']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Weepinbell']['evolution']['EVOLVE_ITEM']["LEAF_STONE"] = "Victreebel"
poke_dict['Weepinbell']['learnset']['VINE_WHIP'] = 1
poke_dict['Weepinbell']['learnset']['GROWTH'] = 1
poke_dict['Weepinbell']['learnset']['WRAP'] = 1
poke_dict['Weepinbell']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Weepinbell']['learnset']['POISONPOWDER'] = 1
poke_dict['Weepinbell']['learnset']['STUN_SPORE'] = 1
poke_dict['Weepinbell']['learnset']['ACID'] = 1
poke_dict['Weepinbell']['learnset']['SWEET_SCENT'] = 1
poke_dict['Weepinbell']['learnset']['RAZOR_LEAF'] = 1
poke_dict['Weepinbell']['learnset']['SLAM'] = 1

# Victreebel
poke_dict['Victreebel']['learnset']['VINE_WHIP'] = 1
poke_dict['Victreebel']['learnset']['GROWTH'] = 1
poke_dict['Victreebel']['learnset']['WRAP'] = 1
poke_dict['Victreebel']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Victreebel']['learnset']['POISONPOWDER'] = 1
poke_dict['Victreebel']['learnset']['STUN_SPORE'] = 1
poke_dict['Victreebel']['learnset']['ACID'] = 1
poke_dict['Victreebel']['learnset']['SWEET_SCENT'] = 1
poke_dict['Victreebel']['learnset']['RAZOR_LEAF'] = 1
poke_dict['Victreebel']['learnset']['SLAM'] = 1

# Tentacool
poke_dict['Tentacool']['evolution'] = {}
poke_dict['Tentacool']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Tentacool']['learnset']['POISON_STING'] = 1
poke_dict['Tentacool']['learnset']['SUPERSONIC'] = 1
poke_dict['Tentacool']['learnset']['CONSTRICT'] = 1
poke_dict['Tentacool']['learnset']['ACID'] = 1
poke_dict['Tentacool']['learnset']['BUBBLEBEAM'] = 1
poke_dict['Tentacool']['learnset']['WRAP'] = 1
poke_dict['Tentacool']['learnset']['BARRIER'] = 1
poke_dict['Tentacool']['learnset']['SCREECH'] = 1
poke_dict['Tentacool']['learnset']['HYDRO_PUMP'] = 1

# Tentacruel
poke_dict['Tentacruel']['learnset']['POISON_STING'] = 1
poke_dict['Tentacruel']['learnset']['SUPERSONIC'] = 1
poke_dict['Tentacruel']['learnset']['CONSTRICT'] = 1
poke_dict['Tentacruel']['learnset']['ACID'] = 1
poke_dict['Tentacruel']['learnset']['BUBBLEBEAM'] = 1
poke_dict['Tentacruel']['learnset']['WRAP'] = 1
poke_dict['Tentacruel']['learnset']['BARRIER'] = 1
poke_dict['Tentacruel']['learnset']['SCREECH'] = 1
poke_dict['Tentacruel']['learnset']['HYDRO_PUMP'] = 1

# Geodude
poke_dict['Geodude']['evolution'] = {}
poke_dict['Geodude']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Geodude']['learnset']['TACKLE'] = 1
poke_dict['Geodude']['learnset']['HARDEN'] = 1
poke_dict['Geodude']['learnset']['ROCK_THROW'] = 1
poke_dict['Geodude']['learnset']['MAGNITUDE'] = 1
poke_dict['Geodude']['learnset']['SELFDESTRUCT'] = 1
poke_dict['Geodude']['learnset']['ROLLOUT'] = 1
poke_dict['Geodude']['learnset']['EARTHQUAKE'] = 1
poke_dict['Geodude']['learnset']['EXPLOSION'] = 1

# Graveler
poke_dict['Graveler']['evolution'] = {}
poke_dict['Graveler']['learnset']['TACKLE'] = 1
poke_dict['Graveler']['learnset']['HARDEN'] = 1
poke_dict['Graveler']['learnset']['ROCK_THROW'] = 1
poke_dict['Graveler']['learnset']['MAGNITUDE'] = 1
poke_dict['Graveler']['learnset']['SELFDESTRUCT'] = 1
poke_dict['Graveler']['learnset']['ROLLOUT'] = 1
poke_dict['Graveler']['learnset']['EARTHQUAKE'] = 1
poke_dict['Graveler']['learnset']['EXPLOSION'] = 1

# Golem
poke_dict['Golem']['learnset']['TACKLE'] = 1
poke_dict['Golem']['learnset']['HARDEN'] = 1
poke_dict['Golem']['learnset']['ROCK_THROW'] = 1
poke_dict['Golem']['learnset']['MAGNITUDE'] = 1
poke_dict['Golem']['learnset']['SELFDESTRUCT'] = 1
poke_dict['Golem']['learnset']['ROLLOUT'] = 1
poke_dict['Golem']['learnset']['EARTHQUAKE'] = 1
poke_dict['Golem']['learnset']['EXPLOSION'] = 1

# Ponyta
poke_dict['Ponyta']['evolution'] = {}
poke_dict['Ponyta']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Ponyta']['learnset']['TACKLE'] = 1
poke_dict['Ponyta']['learnset']['GROWL'] = 1
poke_dict['Ponyta']['learnset']['TAIL_WHIP'] = 1
poke_dict['Ponyta']['learnset']['EMBER'] = 1
poke_dict['Ponyta']['learnset']['STOMP'] = 1
poke_dict['Ponyta']['learnset']['FIRE_SPIN'] = 1
poke_dict['Ponyta']['learnset']['TAKE_DOWN'] = 1
poke_dict['Ponyta']['learnset']['AGILITY'] = 1
poke_dict['Ponyta']['learnset']['FIRE_BLAST'] = 1

# Rapidash
poke_dict['Rapidash']['learnset']['TACKLE'] = 1
poke_dict['Rapidash']['learnset']['GROWL'] = 1
poke_dict['Rapidash']['learnset']['TAIL_WHIP'] = 1
poke_dict['Rapidash']['learnset']['EMBER'] = 1
poke_dict['Rapidash']['learnset']['STOMP'] = 1
poke_dict['Rapidash']['learnset']['FIRE_SPIN'] = 1
poke_dict['Rapidash']['learnset']['TAKE_DOWN'] = 1
poke_dict['Rapidash']['learnset']['AGILITY'] = 1
poke_dict['Rapidash']['learnset']['FIRE_BLAST'] = 1

# Slowpoke
poke_dict['Slowpoke']['evolution'] = {}
poke_dict['Slowpoke']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Slowpoke']['learnset']['TACKLE'] = 1
poke_dict['Slowpoke']['learnset']['CURSE'] = 1
poke_dict['Slowpoke']['learnset']['GROWL'] = 1
poke_dict['Slowpoke']['learnset']['WATER_GUN'] = 1
poke_dict['Slowpoke']['learnset']['CONFUSION'] = 1
poke_dict['Slowpoke']['learnset']['DISABLE'] = 1
poke_dict['Slowpoke']['learnset']['HEADBUTT'] = 1
poke_dict['Slowpoke']['learnset']['AMNESIA'] = 1
poke_dict['Slowpoke']['learnset']['PSYCHIC_M'] = 1

# Slowbro
poke_dict['Slowbro']['learnset']['TACKLE'] = 1
poke_dict['Slowbro']['learnset']['CURSE'] = 1
poke_dict['Slowbro']['learnset']['GROWL'] = 1
poke_dict['Slowbro']['learnset']['WATER_GUN'] = 1
poke_dict['Slowbro']['learnset']['CONFUSION'] = 1
poke_dict['Slowbro']['learnset']['DISABLE'] = 1
poke_dict['Slowbro']['learnset']['HEADBUTT'] = 1
poke_dict['Slowbro']['learnset']['AMNESIA'] = 1
poke_dict['Slowbro']['learnset']['PSYCHIC_M'] = 1

# Magnemite
poke_dict['Magnemite']['evolution'] = {}
poke_dict['Magnemite']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Magnemite']['learnset']['TACKLE'] = 1
poke_dict['Magnemite']['learnset']['THUNDERSHOCK'] = 1
poke_dict['Magnemite']['learnset']['SUPERSONIC'] = 1
poke_dict['Magnemite']['learnset']['SONICBOOM'] = 1
poke_dict['Magnemite']['learnset']['THUNDER_WAVE'] = 1
poke_dict['Magnemite']['learnset']['LOCK_ON'] = 1
poke_dict['Magnemite']['learnset']['SWIFT'] = 1
poke_dict['Magnemite']['learnset']['SCREECH'] = 1
poke_dict['Magnemite']['learnset']['ZAP_CANNON'] = 1

# Magneton
poke_dict['Magneton']['learnset']['TACKLE'] = 1
poke_dict['Magneton']['learnset']['THUNDERSHOCK'] = 1
poke_dict['Magneton']['learnset']['SUPERSONIC'] = 1
poke_dict['Magneton']['learnset']['SONICBOOM'] = 1
poke_dict['Magneton']['learnset']['THUNDER_WAVE'] = 1
poke_dict['Magneton']['learnset']['LOCK_ON'] = 1
poke_dict['Magneton']['learnset']['SWIFT'] = 1
poke_dict['Magneton']['learnset']['SCREECH'] = 1
poke_dict['Magneton']['learnset']['ZAP_CANNON'] = 1

# Farfetch'd
# DATA SPELLING FORMAT: Farfetch\u00e2\u20ac\u2122d
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['PECK'] = 1
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['SAND_ATTACK'] = 1
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['LEER'] = 1
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['FURY_ATTACK'] = 1
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['SWORDS_DANCE'] = 1
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['AGILITY'] = 1
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['SLASH'] = 1
poke_dict['Farfetch\u00e2\u20ac\u2122d']['learnset']['FALSE_SWIPE'] = 1

# Doduo
poke_dict['Doduo']['evolution'] = {}
poke_dict['Doduo']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Doduo']['learnset']['PECK'] = 1
poke_dict['Doduo']['learnset']['GROWL'] = 1
poke_dict['Doduo']['learnset']['PURSUIT'] = 1
poke_dict['Doduo']['learnset']['FURY_ATTACK'] = 1
poke_dict['Doduo']['learnset']['PURSUIT'] = 1
poke_dict['Doduo']['learnset']['FURY_ATTACK'] = 1
poke_dict['Doduo']['learnset']['TRI_ATTACK'] = 1
poke_dict['Doduo']['learnset']['RAGE'] = 1
poke_dict['Doduo']['learnset']['DRILL_PECK'] = 1
poke_dict['Doduo']['learnset']['AGILITY'] = 1

# Dodrio
poke_dict['Dodrio']['learnset']['PECK'] = 1
poke_dict['Dodrio']['learnset']['GROWL'] = 1
poke_dict['Dodrio']['learnset']['PURSUIT'] = 1
poke_dict['Dodrio']['learnset']['FURY_ATTACK'] = 1
poke_dict['Dodrio']['learnset']['PURSUIT'] = 1
poke_dict['Dodrio']['learnset']['FURY_ATTACK'] = 1
poke_dict['Dodrio']['learnset']['TRI_ATTACK'] = 1
poke_dict['Dodrio']['learnset']['RAGE'] = 1
poke_dict['Dodrio']['learnset']['DRILL_PECK'] = 1
poke_dict['Dodrio']['learnset']['AGILITY'] = 1


# Seel
poke_dict['Seel']['evolution'] = {}
poke_dict['Seel']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Seel']['learnset']['HEADBUTT'] = 1
poke_dict['Seel']['learnset']['GROWL'] = 1
poke_dict['Seel']['learnset']['AURORA_BEAM'] = 1
poke_dict['Seel']['learnset']['REST'] = 1
poke_dict['Seel']['learnset']['TAKE_DOWN'] = 1
poke_dict['Seel']['learnset']['ICE_BEAM'] = 1
poke_dict['Seel']['learnset']['SAFEGUARD'] = 1

# Dewgong
poke_dict['Dewgong']['learnset']['HEADBUTT'] = 1
poke_dict['Dewgong']['learnset']['GROWL'] = 1
poke_dict['Dewgong']['learnset']['AURORA_BEAM'] = 1
poke_dict['Dewgong']['learnset']['REST'] = 1
poke_dict['Dewgong']['learnset']['TAKE_DOWN'] = 1
poke_dict['Dewgong']['learnset']['ICE_BEAM'] = 1
poke_dict['Dewgong']['learnset']['SAFEGUARD'] = 1

# Grimer
poke_dict['Grimer']['evolution'] = {}
poke_dict['Grimer']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Grimer']['learnset']['POUND'] = 1
poke_dict['Grimer']['learnset']['POISON_GAS'] = 1
poke_dict['Grimer']['learnset']['HARDEN'] = 1
poke_dict['Grimer']['learnset']['DISABLE'] = 1
poke_dict['Grimer']['learnset']['SLUDGE'] = 1
poke_dict['Grimer']['learnset']['MINIMIZE'] = 1
poke_dict['Grimer']['learnset']['SCREECH'] = 1
poke_dict['Grimer']['learnset']['ACID_ARMOR'] = 1
poke_dict['Grimer']['learnset']['SLUDGE_BOMB'] = 1


# Muk
poke_dict['Muk']['learnset']['POUND'] = 1
poke_dict['Muk']['learnset']['POISON_GAS'] = 1
poke_dict['Muk']['learnset']['HARDEN'] = 1
poke_dict['Muk']['learnset']['DISABLE'] = 1
poke_dict['Muk']['learnset']['SLUDGE'] = 1
poke_dict['Muk']['learnset']['MINIMIZE'] = 1
poke_dict['Muk']['learnset']['SCREECH'] = 1
poke_dict['Muk']['learnset']['ACID_ARMOR'] = 1
poke_dict['Muk']['learnset']['SLUDGE_BOMB'] = 1

# Shellder
poke_dict['Shellder']['evolution'] = {}
poke_dict['Shellder']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Shellder']['learnset']['TACKLE'] = 1
poke_dict['Shellder']['learnset']['WITHDRAW'] = 1
poke_dict['Shellder']['learnset']['SUPERSONIC'] = 1
poke_dict['Shellder']['learnset']['AURORA_BEAM'] = 1
poke_dict['Shellder']['learnset']['PROTECT'] = 1
poke_dict['Shellder']['learnset']['SPIKES'] = 1
poke_dict['Shellder']['learnset']['CLAMP'] = 1
poke_dict['Shellder']['learnset']['SPIKE_CANNON'] = 1
poke_dict['Shellder']['learnset']['ICE_BEAM'] = 1

# Cloyster
poke_dict['Cloyster']['learnset']['TACKLE'] = 1
poke_dict['Shellder']['learnset']['WITHDRAW'] = 1
poke_dict['Shellder']['learnset']['SUPERSONIC'] = 1
poke_dict['Shellder']['learnset']['AURORA_BEAM'] = 1
poke_dict['Shellder']['learnset']['PROTECT'] = 1
poke_dict['Shellder']['learnset']['SPIKES'] = 1
poke_dict['Shellder']['learnset']['CLAMP'] = 1
poke_dict['Shellder']['learnset']['SPIKE_CANNON'] = 1
poke_dict['Shellder']['learnset']['ICE_BEAM'] = 1

# Gastly
poke_dict['Gastly']['evolution'] = {}
poke_dict['Gastly']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Gastly']['learnset']['LICK'] = 1
poke_dict['Gastly']['learnset']['HYPNOSIS'] = 1
poke_dict['Gastly']['learnset']['SPITE'] = 1
poke_dict['Gastly']['learnset']['MEAN_LOOK'] = 1
poke_dict['Gastly']['learnset']['CURSE'] = 1
poke_dict['Gastly']['learnset']['NIGHT_SHADE'] = 1
poke_dict['Gastly']['learnset']['CONFUSE_RAY'] = 1
poke_dict['Gastly']['learnset']['DREAM_EATER'] = 1
poke_dict['Gastly']['learnset']['DESTINY_BOND'] = 1

# Haunter
poke_dict['Haunter']['evolution'] = {}
poke_dict['Haunter']['learnset']['LICK'] = 1
poke_dict['Haunter']['learnset']['HYPNOSIS'] = 1
poke_dict['Haunter']['learnset']['SPITE'] = 1
poke_dict['Haunter']['learnset']['MEAN_LOOK'] = 1
poke_dict['Haunter']['learnset']['CURSE'] = 1
poke_dict['Haunter']['learnset']['NIGHT_SHADE'] = 1
poke_dict['Haunter']['learnset']['CONFUSE_RAY'] = 1
poke_dict['Haunter']['learnset']['DREAM_EATER'] = 1
poke_dict['Haunter']['learnset']['DESTINY_BOND'] = 1

# Gengar
poke_dict['Gengar']['learnset']['LICK'] = 1
poke_dict['Gengar']['learnset']['HYPNOSIS'] = 1
poke_dict['Gengar']['learnset']['SPITE'] = 1
poke_dict['Gengar']['learnset']['MEAN_LOOK'] = 1
poke_dict['Gengar']['learnset']['CURSE'] = 1
poke_dict['Gengar']['learnset']['NIGHT_SHADE'] = 1
poke_dict['Gengar']['learnset']['CONFUSE_RAY'] = 1
poke_dict['Gengar']['learnset']['DREAM_EATER'] = 1
poke_dict['Gengar']['learnset']['DESTINY_BOND'] = 1

# Onix
poke_dict['Onix']['evolution'] = {}
poke_dict['Onix']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Onix']['evolution']['EVOLVE_ITEM']['METAL_COAT'] = "Steelix"
poke_dict['Onix']['learnset']['TACKLE'] = 1
poke_dict['Onix']['learnset']['WRAP'] = 1
poke_dict['Onix']['learnset']['BIND'] = 1
poke_dict['Onix']['learnset']['ROCK_THROW'] = 1
poke_dict['Onix']['learnset']['HARDEN'] = 1
poke_dict['Onix']['learnset']['RAGE'] = 1
poke_dict['Onix']['learnset']['SANDSTORM'] = 1
poke_dict['Onix']['learnset']['SLAM'] = 1

# Drowzee
poke_dict['Drowzee']['evolution'] = {}
poke_dict['Drowzee']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Drowzee']['learnset']['POUND'] = 1
poke_dict['Drowzee']['learnset']['HYPNOSIS'] = 1
poke_dict['Drowzee']['learnset']['DISABLE'] = 1
poke_dict['Drowzee']['learnset']['CONFUSION'] = 1
poke_dict['Drowzee']['learnset']['HEADBUTT'] = 1
poke_dict['Drowzee']['learnset']['POISON_GAS'] = 1
poke_dict['Drowzee']['learnset']['MEDITATE'] = 1
poke_dict['Drowzee']['learnset']['PSYCHIC_M'] = 1
poke_dict['Drowzee']['learnset']['PSYCH_UP'] = 1
poke_dict['Drowzee']['learnset']['FUTURE_SIGHT'] = 1

# Hypno
poke_dict['Hypno']['learnset']['POUND'] = 1
poke_dict['Hypno']['learnset']['HYPNOSIS'] = 1
poke_dict['Hypno']['learnset']['DISABLE'] = 1
poke_dict['Hypno']['learnset']['CONFUSION'] = 1
poke_dict['Hypno']['learnset']['HEADBUTT'] = 1
poke_dict['Hypno']['learnset']['POISON_GAS'] = 1
poke_dict['Hypno']['learnset']['MEDITATE'] = 1
poke_dict['Hypno']['learnset']['PSYCHIC_M'] = 1
poke_dict['Hypno']['learnset']['PSYCH_UP'] = 1
poke_dict['Hypno']['learnset']['FUTURE_SIGHT'] = 1

# Krabby
poke_dict['Krabby']['evolution'] = {}
poke_dict['Krabby']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Krabby']['learnset']['BUBBLE'] = 1
poke_dict['Krabby']['learnset']['LEER'] = 1
poke_dict['Krabby']['learnset']['VICEGRIP'] = 1
poke_dict['Krabby']['learnset']['HARDEN'] = 1
poke_dict['Krabby']['learnset']['STOMP'] = 1
poke_dict['Krabby']['learnset']['GUILLOTINE'] = 1
poke_dict['Krabby']['learnset']['PROTECT'] = 1
poke_dict['Krabby']['learnset']['CRABHAMMER'] = 1

# Kingler
poke_dict['Kingler']['learnset']['BUBBLE'] = 1
poke_dict['Kingler']['learnset']['LEER'] = 1
poke_dict['Kingler']['learnset']['VICEGRIP'] = 1
poke_dict['Kingler']['learnset']['HARDEN'] = 1
poke_dict['Kingler']['learnset']['STOMP'] = 1
poke_dict['Kingler']['learnset']['GUILLOTINE'] = 1
poke_dict['Kingler']['learnset']['PROTECT'] = 1
poke_dict['Kingler']['learnset']['CRABHAMMER'] = 1

# Voltorb
poke_dict['Voltorb']['evolution'] = {}
poke_dict['Voltorb']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Voltorb']['learnset']['TACKLE'] = 1
poke_dict['Voltorb']['learnset']['SCREECH'] = 1
poke_dict['Voltorb']['learnset']['SONICBOOM'] = 1
poke_dict['Voltorb']['learnset']['SELFDESTRUCT'] = 1
poke_dict['Voltorb']['learnset']['ROLLOUT'] = 1
poke_dict['Voltorb']['learnset']['LIGHT_SCREEN'] = 1
poke_dict['Voltorb']['learnset']['SWIFT'] = 1
poke_dict['Voltorb']['learnset']['EXPLOSION'] = 1
poke_dict['Voltorb']['learnset']['MIRROR_COAT'] = 1

# Electrode
poke_dict['Electrode']['learnset']['TACKLE'] = 1
poke_dict['Electrode']['learnset']['SCREECH'] = 1
poke_dict['Electrode']['learnset']['SONICBOOM'] = 1
poke_dict['Electrode']['learnset']['SELFDESTRUCT'] = 1
poke_dict['Electrode']['learnset']['ROLLOUT'] = 1
poke_dict['Electrode']['learnset']['LIGHT_SCREEN'] = 1
poke_dict['Electrode']['learnset']['SWIFT'] = 1
poke_dict['Electrode']['learnset']['EXPLOSION'] = 1
poke_dict['Electrode']['learnset']['MIRROR_COAT'] = 1

# Exeggcute
poke_dict['Exeggcute']['evolution'] = {}
poke_dict['Exeggcute']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Exeggcute']['learnset']['BARRAGE'] = 1
poke_dict['Exeggcute']['learnset']['HYPNOSIS'] = 1
poke_dict['Exeggcute']['learnset']['REFLECT'] = 1
poke_dict['Exeggcute']['learnset']['LEECH_SEED'] = 1
poke_dict['Exeggcute']['learnset']['CONFUSION'] = 1
poke_dict['Exeggcute']['learnset']['STUN_SPORE'] = 1
poke_dict['Exeggcute']['learnset']['POISONPOWDER'] = 1
poke_dict['Exeggcute']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Exeggcute']['learnset']['SOLARBEAM'] = 1

# Exeggutor
poke_dict['Exeggutor']['learnset']['BARRAGE'] = 1
poke_dict['Exeggutor']['learnset']['HYPNOSIS'] = 1
poke_dict['Exeggutor']['learnset']['REFLECT'] = 1
poke_dict['Exeggutor']['learnset']['LEECH_SEED'] = 1
poke_dict['Exeggutor']['learnset']['CONFUSION'] = 1
poke_dict['Exeggutor']['learnset']['EGG_BOMB'] = 1
poke_dict['Exeggutor']['learnset']['STUN_SPORE'] = 1
poke_dict['Exeggutor']['learnset']['POISONPOWDER'] = 1
poke_dict['Exeggutor']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Exeggutor']['learnset']['SOLARBEAM'] = 1

# Cubone
poke_dict['Cubone']['evolution'] = {}
poke_dict['Cubone']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Cubone']['learnset']['POUND'] = 1
poke_dict['Cubone']['learnset']['TAIL_WHIP'] = 1
poke_dict['Cubone']['learnset']['BONE_CLUB'] = 1
poke_dict['Cubone']['learnset']['HEADBUTT'] = 1
poke_dict['Cubone']['learnset']['LEER'] = 1
poke_dict['Cubone']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Cubone']['learnset']['BONEMERANG'] = 1
poke_dict['Cubone']['learnset']['RAGE'] = 1
poke_dict['Cubone']['learnset']['FALSE_SWIPE'] = 1
poke_dict['Cubone']['learnset']['THRASH'] = 1
poke_dict['Cubone']['learnset']['BONE_RUSH'] = 1

# Marowak
poke_dict['Marowak']['learnset']['POUND'] = 1
poke_dict['Marowak']['learnset']['TAIL_WHIP'] = 1
poke_dict['Marowak']['learnset']['BONE_CLUB'] = 1
poke_dict['Marowak']['learnset']['HEADBUTT'] = 1
poke_dict['Marowak']['learnset']['LEER'] = 1
poke_dict['Marowak']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Marowak']['learnset']['BONEMERANG'] = 1
poke_dict['Marowak']['learnset']['RAGE'] = 1
poke_dict['Marowak']['learnset']['FALSE_SWIPE'] = 1
poke_dict['Marowak']['learnset']['THRASH'] = 1
poke_dict['Marowak']['learnset']['BONE_RUSH'] = 1

# Hitmonlee
poke_dict['Hitmonlee']['learnset']['DOUBLE_KICK'] = 1
poke_dict['Hitmonlee']['learnset']['MEDITATE'] = 1
poke_dict['Hitmonlee']['learnset']['ROLLING_KICK'] = 1
poke_dict['Hitmonlee']['learnset']['JUMP_KICK'] = 1
poke_dict['Hitmonlee']['learnset']['FOCUS_ENERGY'] = 1
poke_dict['Hitmonlee']['learnset']['HI_JUMP_KICK'] = 1
poke_dict['Hitmonlee']['learnset']['MIND_READER'] = 1
poke_dict['Hitmonlee']['learnset']['FORESIGHT'] = 1
poke_dict['Hitmonlee']['learnset']['ENDURE'] = 1
poke_dict['Hitmonlee']['learnset']['MEGA_KICK'] = 1
poke_dict['Hitmonlee']['learnset']['REVERSAL'] = 1

# Hitmonchan
poke_dict['Hitmonchan']['learnset']['COMET_PUNCH'] = 1
poke_dict['Hitmonchan']['learnset']['AGILITY'] = 1
poke_dict['Hitmonchan']['learnset']['PURSUIT'] = 1
poke_dict['Hitmonchan']['learnset']['THUNDERPUNCH'] = 1
poke_dict['Hitmonchan']['learnset']['ICE_PUNCH'] = 1
poke_dict['Hitmonchan']['learnset']['FIRE_PUNCH'] = 1
poke_dict['Hitmonchan']['learnset']['MACH_PUNCH'] = 1
poke_dict['Hitmonchan']['learnset']['MEGA_PUNCH'] = 1
poke_dict['Hitmonchan']['learnset']['DETECT'] = 1
poke_dict['Hitmonchan']['learnset']['COUNTER'] = 1

# Lickitung
poke_dict['Lickitung']['learnset']['LICK'] = 1
poke_dict['Lickitung']['learnset']['TACKLE'] = 1
poke_dict['Lickitung']['learnset']['SUPERSONIC'] = 1
poke_dict['Lickitung']['learnset']['DEFENSE_CURL'] = 1
poke_dict['Lickitung']['learnset']['STOMP'] = 1
poke_dict['Lickitung']['learnset']['WRAP'] = 1
poke_dict['Lickitung']['learnset']['DISABLE'] = 1
poke_dict['Lickitung']['learnset']['SLAM'] = 1
poke_dict['Lickitung']['learnset']['SCREECH'] = 1

# Koffing
poke_dict['Koffing']['evolution'] = {}
poke_dict['Koffing']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Koffing']['learnset']['POISON_GAS'] = 1
poke_dict['Koffing']['learnset']['TACKLE'] = 1
poke_dict['Koffing']['learnset']['SMOG'] = 1
poke_dict['Koffing']['learnset']['SELFDESTRUCT'] = 1
poke_dict['Koffing']['learnset']['SLUDGE'] = 1
poke_dict['Koffing']['learnset']['SMOKESCREEN'] = 1
poke_dict['Koffing']['learnset']['HAZE'] = 1
poke_dict['Koffing']['learnset']['EXPLOSION'] = 1
poke_dict['Koffing']['learnset']['DESTINY_BOND'] = 1

# Weezing
poke_dict['Weezing']['learnset']['TACKLE'] = 1
poke_dict['Weezing']['learnset']['POISON_GAS'] = 1
poke_dict['Weezing']['learnset']['SMOG'] = 1
poke_dict['Weezing']['learnset']['SELFDESTRUCT'] = 1
poke_dict['Weezing']['learnset']['SLUDGE'] = 1
poke_dict['Weezing']['learnset']['SMOKESCREEN'] = 1
poke_dict['Weezing']['learnset']['HAZE'] = 1
poke_dict['Weezing']['learnset']['EXPLOSION'] = 1
poke_dict['Weezing']['learnset']['DESTINY_BOND'] = 1

# Rhyhorn
poke_dict['Rhyhorn']['evolution'] = {}
poke_dict['Rhyhorn']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Rhyhorn']['learnset']['HORN_ATTACK'] = 1
poke_dict['Rhyhorn']['learnset']['TAIL_WHIP'] = 1
poke_dict['Rhyhorn']['learnset']['STOMP'] = 1
poke_dict['Rhyhorn']['learnset']['FURY_ATTACK'] = 1
poke_dict['Rhyhorn']['learnset']['SCARY_FACE'] = 1
poke_dict['Rhyhorn']['learnset']['HORN_DRILL'] = 1
poke_dict['Rhyhorn']['learnset']['TAKE_DOWN'] = 1
poke_dict['Rhyhorn']['learnset']['EARTHQUAKE'] = 1

# Rhydon
poke_dict['Rhydon']['learnset']['HORN_ATTACK'] = 1
poke_dict['Rhydon']['learnset']['TAIL_WHIP'] = 1
poke_dict['Rhydon']['learnset']['STOMP'] = 1
poke_dict['Rhydon']['learnset']['FURY_ATTACK'] = 1
poke_dict['Rhydon']['learnset']['SCARY_FACE'] = 1
poke_dict['Rhydon']['learnset']['HORN_DRILL'] = 1
poke_dict['Rhydon']['learnset']['TAKE_DOWN'] = 1
poke_dict['Rhydons']['learnset']['EARTHQUAKE'] = 1

# Chansey
poke_dict['Chansey']['evolution'] = {}
poke_dict['Chansey']['learnset']['POUND'] = 1
poke_dict['Chansey']['learnset']['GROWL'] = 1
poke_dict['Chansey']['learnset']['TAIL_WHIP'] = 1
poke_dict['Chansey']['learnset']['SOFTBOILED'] = 1
poke_dict['Chansey']['learnset']['DOUBLESLAP'] = 1
poke_dict['Chansey']['learnset']['MINIMIZE'] = 1
poke_dict['Chansey']['learnset']['SING'] = 1
poke_dict['Chansey']['learnset']['EGG_BOMB'] = 1
poke_dict['Chansey']['learnset']['DEFENSE_CURL'] = 1
poke_dict['Chansey']['learnset']['LIGHT_SCREEN'] = 1
poke_dict['Chansey']['learnset']['DOUBLE_EDGE'] = 1

# Tangela
poke_dict['Tangela']['learnset']['CONSTRICT'] = 1
poke_dict['Tangela']['learnset']['SLEEP_POWDER'] = 1
poke_dict['Tangela']['learnset']['ABSORB'] = 1
poke_dict['Tangela']['learnset']['POISONPOWDER'] = 1
poke_dict['Tangela']['learnset']['VINE_WHIP'] = 1
poke_dict['Tangela']['learnset']['BIND'] = 1
poke_dict['Tangela']['learnset']['MEGA_DRAIN'] = 1
poke_dict['Tangela']['learnset']['STUN_SPORE'] = 1
poke_dict['Tangela']['learnset']['SLAM'] = 1
poke_dict['Tangela']['learnset']['GROWTH'] = 1

# Kangaskhan
poke_dict['Kangaskhan']['learnset']['COMET_PUNCH'] = 1
poke_dict['Kangaskhan']['learnset']['LEER'] = 1
poke_dict['Kangaskhan']['learnset']['BITE'] = 1
poke_dict['Kangaskhan']['learnset']['TAIL_WHIP'] = 1
poke_dict['Kangaskhan']['learnset']['MEGA_PUNCH'] = 1
poke_dict['Kangaskhan']['learnset']['RAGE'] = 1
poke_dict['Kangaskhan']['learnset']['ENDURE'] = 1
poke_dict['Kangaskhan']['learnset']['DIZZY_PUNCH'] = 1
poke_dict['Kangaskhan']['learnset']['REVERSAL'] = 1

# Horsea
poke_dict['Horsea']['evolution'] = {}
poke_dict['Horsea']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Horsea']['learnset']['BUBBLE'] = 1
poke_dict['Horsea']['learnset']['SMOKESCREEN'] = 1
poke_dict['Horsea']['learnset']['LEER'] = 1
poke_dict['Horsea']['learnset']['WATER_GUN'] = 1
poke_dict['Horsea']['learnset']['TWISTER'] = 1
poke_dict['Horsea']['learnset']['AGILITY'] = 1
poke_dict['Horsea']['learnset']['HYDRO_PUMP'] = 1

# Seadra
poke_dict['Seadra']['evolution'] = {}
poke_dict['Seadra']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Seadra']['learnset']['BUBBLE'] = 1
poke_dict['Seadra']['learnset']['SMOKESCREEN'] = 1
poke_dict['Seadra']['learnset']['LEER'] = 1
poke_dict['Seadra']['learnset']['WATER_GUN'] = 1
poke_dict['Seadra']['learnset']['TWISTER'] = 1
poke_dict['Seadra']['learnset']['AGILITY'] = 1
poke_dict['Seadra']['learnset']['HYDRO_PUMP'] = 1

# Goldeen
poke_dict['Goldeen']['evolution'] = {}
poke_dict['Goldeen']['evolution']['EVOLVE_LEVEL'] = {}
poke_dict['Goldeen']['learnset']['PECK'] = 1
poke_dict['Goldeen']['learnset']['TAIL_WHIP'] = 1
poke_dict['Goldeen']['learnset']['SUPERSONIC'] = 1
poke_dict['Goldeen']['learnset']['HORN_ATTACK'] = 1
poke_dict['Goldeen']['learnset']['FLAIL'] = 1
poke_dict['Goldeen']['learnset']['FURY_ATTACK'] = 1
poke_dict['Goldeen']['learnset']['WATERFALL'] = 1
poke_dict['Goldeen']['learnset']['HORN_DRILL'] = 1
poke_dict['Goldeen']['learnset']['AGILITY'] = 1

# Seaking
poke_dict['Seaking']['learnset']['PECK'] = 1
poke_dict['Seaking']['learnset']['TAIL_WHIP'] = 1
poke_dict['Seaking']['learnset']['SUPERSONIC'] = 1
poke_dict['Seaking']['learnset']['HORN_ATTACK'] = 1
poke_dict['Seaking']['learnset']['FLAIL'] = 1
poke_dict['Seaking']['learnset']['FURY_ATTACK'] = 1
poke_dict['Seaking']['learnset']['WATERFALL'] = 1
poke_dict['Seaking']['learnset']['HORN_DRILL'] = 1
poke_dict['Seaking']['learnset']['AGILITY'] = 1

# Staryu
poke_dict['Staryu']['evolution'] = {}
poke_dict['Staryu']['evolution']['EVOLVE_ITEM'] = {}
poke_dict['Staryu']['evolution']['EVOLVE_ITEM']["WATER_STONE"] = "Starmie"
poke_dict['Staryu']['learnset']['TACKLE'] = 1

# Starmie
poke_dict['Starmie']['learnset']['TACKLE'] = 1

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


