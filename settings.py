# Define settings for the game
from pygame import time
import pygame

print(pygame.font.get_fonts())

# screen
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 288

# colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# time
FPS = 60
FramePerSec = time.Clock()

    