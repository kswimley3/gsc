import pygame
from pygame.locals import *
import settings

class Pokemon(pygame.sprite.Sprite):
      # Define a class to handle pokemon
      def __init__(self, sprite_path, name, enemy=True, level=1,
                   stats=(1, 1, 1, 1, 1, 1),
                   moves=(None, None, None, None),
                   *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(sprite_path).convert()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(
            self.image, (int(self.size[0] * settings.SCREEN_MULT), int(self.size[1] * settings.SCREEN_MULT))
        )
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.name = name
        self.enemy = enemy
        if self.enemy: self.rect.center = (int(self.size[0]/2), int(self.size[1]/2))
        if not self.enemy: self.rect.center = (int(self.size[0]/2) + 2*settings.SCREEN_MULT,
                                               settings.BATTLE_SCREEN_HEIGHT - int(self.size[1]/2))
        self.stats = stats
        self.HP = int((stats[0] * 2 * level) / 100 + level + 10)
        self.ATK = int((stats[1] * 2) / 100 + 5)
        self.DEF = int((stats[2] * 2) / 100 + 5)
        self.SPATK = int((stats[3] * 2) / 100 + 5)
        self.SPDEF = int((stats[4] * 2) / 100 + 5)
        self.SPD = int((stats[5] * 2) / 100 + 5)

        self.health = self.HP
        self.move_1 = moves[0]
        self.move_2 = moves[1]
        self.move_3 = moves[2]
        self.move_4 = moves[3]

      def update(self):
        # Update all information related to self
        if self.enemy:
          if self.rect.right < settings.BATTLE_SCREEN_WIDTH - settings.SCREEN_MULT:
            self.rect.move_ip(5, 0)

      def draw(self, surface):
          surface.blit(self.image, self.rect)

