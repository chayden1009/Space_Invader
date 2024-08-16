import pygame

class player:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self, surface):
    pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, 20, 30))