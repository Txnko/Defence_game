import pygame
import os
import time
import random
pygame.font.init()

# define window size
WIDTH, HEIGHT = 750, 750


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie defence simulator")


# import player image
PLAYER = pygame.image.load(os.path.join("assets", "player.png"))

# import enemy image
ENEMY = pygame.image.load(os.path.join("assets", "enemy.png"))

# import backgorund image
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

# import bullet image
BULLET = pygame.image.load(os.path.join("assets", "bullet.png"))
ENBULLET = pygame.image.load(os.path.join("assets", "enemybullet.png"))


class Player:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.bullet_img = None
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))


# main game loop
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("chiller", 50)

    player = Player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))


        # text on screen
        Lives_UI = main_font.render(f"Lives: {lives}", 1, (211,47,47))
        Level_UI = main_font.render(f"Level: {level}", 1, (211,47,47))

        WIN.blit(Lives_UI, (10, 10))
        WIN.blit(Level_UI, (WIDTH - Level_UI.get_width() - 10, 10))

        player.draw(WIN)


        pygame.display.update()
    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()