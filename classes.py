import pygame
from pygame.locals import *
import settings

class Pokemon(pygame.sprite.Sprite):
  # Define a class to handle pokemon
  def __init__(self, sprite_path, name, *groups):
    super().__init__(*groups)
    self.image = pygame.image.load(sprite_path).convert()
    self.size = self.image.get_size()
    self.image = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
    self.rect = self.image.get_rect()
    self.name = name
    self.enemy = True
    if self.enemy == True: self.rect.center = (40, 60)

  def update(self):
    pressed_keys = pygame.key.get_pressed()
    if self.rect.top > 0:
      if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if self.rect.bottom < settings.SCREEN_HEIGHT:  
      if pressed_keys[K_DOWN]:
          self.rect.move_ip(0,5)
        
    if self.rect.left > 0:
          if pressed_keys[K_LEFT]:
              self.rect.move_ip(-5, 0)
    if self.rect.right < settings.SCREEN_WIDTH:        
          if pressed_keys[K_RIGHT]:
              self.rect.move_ip(5, 0)

  def draw(self, surface):
      surface.blit(self.image, self.rect)