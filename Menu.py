import pygame

from CubeAdventure import CubeAdventure
from Game import Game

pygame.init()

screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

text_color = (0, 0, 0)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
color_background = (255, 255, 255)

# defining a font
smallfont = pygame.font.SysFont('dejavuserif', 30)
print(pygame.font.get_fonts())
text = smallfont.render('play', True, text_color)

while True:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if Game.SCREEN_WIDTH / 2-70 <= mouse[0] <= Game.SCREEN_WIDTH / 2 + 140-70 and Game.SCREEN_HEIGHT / 2 <= mouse[1] <= Game.SCREEN_HEIGHT / 2 + 40:
                cubeAdventure = CubeAdventure()
                cubeAdventure.start_game()
 
    screen.fill(color_background)

    if Game.SCREEN_WIDTH / 2-70 <= mouse[0] <= Game.SCREEN_WIDTH / 2 + 140 and Game.SCREEN_HEIGHT / 2 <= mouse[1] <= Game.SCREEN_HEIGHT / 2 + 40:
        pygame.draw.rect(screen, color_light, [Game.SCREEN_WIDTH / 2-70, Game.SCREEN_HEIGHT / 2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [Game.SCREEN_WIDTH / 2-70, Game.SCREEN_HEIGHT / 2, 140, 40])

    screen.blit(text, (Game.SCREEN_WIDTH / 2 + 40-70, Game.SCREEN_HEIGHT / 2))

    pygame.display.update()
