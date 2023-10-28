import pygame
import socket

from CubeAdventure import CubeAdventure
from Game import Game

SINGLE_PLAYER_BUTTON_WIDTH = 270


pygame.init()

server = True

screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

text_color = (0, 0, 0)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
color_background = (255, 255, 255)



# defining a font
smallfont = pygame.font.SysFont('dejavuserif', 30)
print(pygame.font.get_fonts())
text = smallfont.render('Single player', True, text_color)

while True:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if Game.SCREEN_WIDTH / 2-SINGLE_PLAYER_BUTTON_WIDTH/2 <= mouse[0] <= Game.SCREEN_WIDTH / 2 + SINGLE_PLAYER_BUTTON_WIDTH-SINGLE_PLAYER_BUTTON_WIDTH/2 and Game.SCREEN_HEIGHT / 2 <= mouse[1] <= Game.SCREEN_HEIGHT / 2 + 40:
                if server:
                    # create server
                    # listen for connection
                    # receive data
                    # print data
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind(("192.168.50.2", 45001))
                    s.listen()
                    conn, addr = s.accept()
                    print("New client from " + addr[0])
                    data = conn.recv(1024)
                    print("New data from client " + str(data))
                else:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect(("93.182.6.25", 45001))
                    s.sendall(b"hello")
                    # connect to server
                    # send data


                #cubeAdventure = CubeAdventure()
                #cubeAdventure.start_game()
 
    screen.fill(color_background)

    if Game.SCREEN_WIDTH / 2-SINGLE_PLAYER_BUTTON_WIDTH/2 <= mouse[0] <= Game.SCREEN_WIDTH / 2 + SINGLE_PLAYER_BUTTON_WIDTH and Game.SCREEN_HEIGHT / 2 <= mouse[1] <= Game.SCREEN_HEIGHT / 2 + 40:
        pygame.draw.rect(screen, color_light, [Game.SCREEN_WIDTH / 2-SINGLE_PLAYER_BUTTON_WIDTH/2, Game.SCREEN_HEIGHT / 2, SINGLE_PLAYER_BUTTON_WIDTH, 40])
    else:
        pygame.draw.rect(screen, color_dark, [Game.SCREEN_WIDTH / 2-SINGLE_PLAYER_BUTTON_WIDTH/2, Game.SCREEN_HEIGHT / 2, SINGLE_PLAYER_BUTTON_WIDTH, 40])

    screen.blit(text, (Game.SCREEN_WIDTH / 2 + 40-SINGLE_PLAYER_BUTTON_WIDTH/2, Game.SCREEN_HEIGHT / 2))

    pygame.display.update()
