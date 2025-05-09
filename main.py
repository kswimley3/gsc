from pathlib import Path
import pandas as pd
import pygame
from pygame.locals import *
import sys
import settings
from classes import Pokemon


# FUNCTIONS
def load_sprite_paths():

    # create sprite path
    sprite_path = Path('.') / 'sprites' / 'sprites' / 'pokemon' / 'versions' / 'generation-ii' / 'silver'

    # create a sorted list of sprite files
    # indexed from 0 = bulbasaur to 250 = celebi, # only unknown a available
    sprite_list = []
    for num in range(1,252):
      temp_name = str(num) + ".png"
      sprite_list.append(sprite_path / temp_name)

    return sprite_list

def load_back_sprite_paths():

    # create sprite path
    sprite_path = Path('.') / 'sprites' / 'sprites' / 'pokemon' / 'versions' / 'generation-ii' / 'silver' / 'back'

    # create a sorted list of sprite files
    # indexed from 0 = bulbasaur to 250 = celebi, # only unknown a available
    sprite_list = []
    for num in range(1, 252):
      temp_name = str(num) + ".png"
      sprite_list.append(sprite_path / temp_name)

    return sprite_list


def get_pokemon_stats(poke_id, poke_pd):
    # get stats from pokemon data
    HP = poke_pd["HP"][poke_id]
    ATK = poke_pd["Attack"][poke_id]
    DEF = poke_pd["Defense"][poke_id]
    SPATK = poke_pd["Sp. Atk"][poke_id]
    SPDEF = poke_pd["Sp. Def"][poke_id]
    SPD = poke_pd["Sp. Def"][poke_id]
    return (HP, ATK, DEF, SPATK, SPDEF, SPD)


def main():
    # Main set of operations to run the game

    # Define global states
    glob_intro_battle_state = 1
    glob_move_selection = 0
    glob_move_ally = 0
    glob_move_enemy= 0

    # Load stats
    poke = pd.read_csv("pokemon_gen2.csv")

    # Load sprite paths
    sprite_list = load_sprite_paths()
    backsprite_list = load_back_sprite_paths()

    # Merge sprite paths into df
    poke["sprite_path"] = sprite_list

    # load move list
    # moves = pd.read_csv("./data/moves.csv")

    # PYGAME INITIALIZATION
    pygame.init()
    pygame.font.init()

    # define font and size
    my_font = pygame.font.SysFont("consolas", 8 * settings.SCREEN_MULT)
    font_moves = pygame.font.SysFont("consolas", 8 * settings.SCREEN_MULT)
  
    DISPLAYSURF = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    DISPLAYSURF.fill(settings.WHITE)
    pygame.display.set_caption("Pokemon Fiscal")

    P1 = Pokemon(sprite_path=sprite_list[2], name="Venusaur",
                 level=50, stats=get_pokemon_stats(2, poke_pd=poke)
                 )
    P2 = Pokemon(sprite_path=backsprite_list[5], name="Charizard",
                 level=50, enemy=False, stats=get_pokemon_stats(5, poke_pd=poke),
                 moves=("Ember", "Growl", "Wing Attack", "Dragon Breath")
                 )

    # establish the move indicator sprite
    MOVE_INDICATOR = pygame.image.load(Path('.') / 'sprites' / 'gsc_custom' / 'Menu_Indicator.png').convert()
    MOVE_INDICATOR_SIZE = MOVE_INDICATOR.get_size()
    MOVE_INDICATOR = pygame.transform.scale(
        MOVE_INDICATOR, (int(MOVE_INDICATOR_SIZE[0] * settings.SCREEN_MULT), int(MOVE_INDICATOR_SIZE[1] * settings.SCREEN_MULT))
    )
    MOVE_INDICATOR_rect = MOVE_INDICATOR.get_rect()
    MOVE_INDICATOR_rect.left = 0
    MOVE_INDICATOR_rect.bottom = 544

    # run the game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        P1.update()
        P2.update()

        DISPLAYSURF.fill(settings.WHITE)
        P1.draw(DISPLAYSURF)
        P2.draw(DISPLAYSURF)

        # Draw the enemy information
        text_enemy_name = my_font.render(P1.name, False, settings.BLACK)
        DISPLAYSURF.blit(text_enemy_name, (5*settings.SCREEN_MULT, 5*settings.SCREEN_MULT))

        text_enemy_hp = my_font.render("HP: " + str(P1.health), False, settings.BLACK)
        DISPLAYSURF.blit(text_enemy_hp, (50*settings.SCREEN_MULT, 5*settings.SCREEN_MULT))

        # Draw ally information
        text_ally_name = my_font.render(P2.name, False, settings.BLACK)
        DISPLAYSURF.blit(text_ally_name,
                         (settings.BATTLE_SCREEN_WIDTH - settings.SCREEN_MULT * 82,
                          settings.BATTLE_SCREEN_HEIGHT - settings.SCREEN_MULT * 6)
                         )

        text_ally_hp = my_font.render("HP: " + str(P2.health), False, settings.BLACK)
        DISPLAYSURF.blit(text_ally_hp,
                         (settings.BATTLE_SCREEN_WIDTH - settings.SCREEN_MULT * 32,
                          settings.BATTLE_SCREEN_HEIGHT - settings.SCREEN_MULT * 6)
                         )

        # Create the Moves screen
        pygame.draw.rect(
            DISPLAYSURF,
            settings.BLACK,
            (0,                                                         # left
                settings.BATTLE_SCREEN_HEIGHT+1*settings.SCREEN_MULT,   # top
                settings.BATTLE_SCREEN_WIDTH,                           # width
                settings.SCREEN_HEIGHT - settings.BATTLE_SCREEN_HEIGHT  # height
             ),
            2 * settings.SCREEN_MULT  # width
        )

        text_move1 = font_moves.render(P2.move_1, False, settings.BLACK)
        text_move2 = font_moves.render(P2.move_2, False, settings.BLACK)
        text_move3 = font_moves.render(P2.move_3, False, settings.BLACK)
        text_move4 = font_moves.render(P2.move_4, False, settings.BLACK)

        DISPLAYSURF.blit(text_move1,
                         (settings.SCREEN_MULT * 8,
                          settings.SCREEN_HEIGHT - settings.SCREEN_MULT * 30)
                         )

        DISPLAYSURF.blit(text_move2,
                         (settings.SCREEN_WIDTH/2,
                          settings.SCREEN_HEIGHT - settings.SCREEN_MULT * 30)
                         )

        DISPLAYSURF.blit(text_move3,
                         (settings.SCREEN_MULT * 8,
                          settings.SCREEN_HEIGHT - settings.SCREEN_MULT * 15)
                         )

        DISPLAYSURF.blit(text_move4,
                         (settings.SCREEN_WIDTH/2,
                          settings.SCREEN_HEIGHT - settings.SCREEN_MULT * 15)
                         )

        if P2.in_position == True:
            glob_intro_battle_state = 0
            glob_move_selection = 1

        if glob_move_selection == True:
            DISPLAYSURF.blit(MOVE_INDICATOR, MOVE_INDICATOR_rect)





        # update the game state
        pygame.display.update()
        settings.FramePerSec.tick(settings.FPS)



# run the main file
if __name__ == "__main__":
    main()



