import pygame
import socket

from Button import Button
from CubeAdventure import CubeAdventure
from Game import Game

pygame.init()


def quit_game():
    pygame.quit()


def create_server():
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


def create_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("93.182.6.25", 45001))
    s.sendall(b"hello")
    # connect to server
    # send data


def start_single_game():
    cubeAdventure = CubeAdventure()
    cubeAdventure.start_game()


buttons_list = [Button('Single player', 400, 300, 270, start_single_game),
                Button('Multiplayer', 400, 400, 270, None),
                Button('Quit', 400, 500, 270, quit_game)]

screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

color_background = (255, 255, 255)

while True:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons_list:
                if button.button_x <= mouse[0] <= button.button_x + button.button_width and button.button_y <= mouse[1] <= button.button_y + button.button_height:
                    button.press_function()

    screen.fill(color_background)

    for button in buttons_list:
        if button.button_x <= mouse[0] <= button.button_x + button.button_width and button.button_y <= mouse[1] <= button.button_y + button.button_height:
            pygame.draw.rect(screen, button.color_light, [button.button_x, button.button_y, button.button_width, button.button_height])
        else:
            pygame.draw.rect(screen, button.color_dark, [button.button_x, button.button_y, button.button_width, button.button_height])
        smallfont = pygame.font.SysFont(button.font_name, button.font_size)
        text = smallfont.render(button.text, True, button.text_color)
        screen.blit(text, (button.button_x, button.button_y))

    pygame.display.update()
