# Define settings for the game
from pygame import time
import pygame

print(pygame.font.get_fonts())



# screen
# game boy color screen is 160 pix wide and 144 pix tall
SCREEN_MULT = 4
SCREEN_WIDTH = 160 * SCREEN_MULT
SCREEN_HEIGHT = 144 * SCREEN_MULT

# battle screen
BATTLE_SCREEN_WIDTH = SCREEN_WIDTH - (2 * SCREEN_MULT)
BATTLE_SCREEN_HEIGHT = SCREEN_HEIGHT - (36 * SCREEN_MULT)


# colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# time
FPS = 60
FramePerSec = time.Clock()

    