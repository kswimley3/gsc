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

def main():
  # Main set of operations to run the game

  # Load stats
  poke = pd.read_csv("pokemon_gen2.csv")

  # Load sprite paths
  sprite_list = load_sprite_paths()

  # Merge sprite paths into df
  poke["sprite_path"] = sprite_list

  # load move list
  moves = pd.read_csv("./data/moves.csv")

  #PYGAME INITIALIZATION
  pygame.init()
  pygame.font.init()
  my_font = pygame.font.SysFont("consolas" , 16)
  
  DISPLAYSURF = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
  DISPLAYSURF.fill(settings.WHITE)
  pygame.display.set_caption("Pokemon Fiscal")

  P1 = Pokemon(sprite_path = sprite_list[0], name = "Bulbasaur")

  # run the game
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

    P1.update()

    DISPLAYSURF.fill(settings.WHITE)
    P1.draw(DISPLAYSURF)
    text_surface = my_font.render(P1.name, False, settings.BLACK)
    DISPLAYSURF.blit(text_surface, (10, 10))

  
    # update the game state
    pygame.display.update()
    settings.FramePerSec.tick(settings.FPS)



# run the main file
if __name__ == "__main__":
  main()



