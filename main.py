import pygame
import archetypes

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

p1 = archetypes.player(600, 400)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  p1.draw(screen)

  pygame.display.flip()
  clock.tick(60)
