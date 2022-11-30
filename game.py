import pygame

running = True


pygame.init()

size = (400, 400)
Game = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

pygame.display.flip()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False 