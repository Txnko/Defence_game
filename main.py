# import libraries
import pygame
import os
import time
import random
# import fonts
pygame.font.init()

# define window size
WIDTH, HEIGHT = 750, 750


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Defence simulator")


# import player image
PLAYER = pygame.image.load(os.path.join("assets", "player.png"))

# import enemy image
ENEMY = pygame.image.load(os.path.join("assets", "enemy.png"))
ENEMY2 = pygame.image.load(os.path.join("assets", "enemy2.png"))

# import backgorund image
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

# import bullet image
BULLET = pygame.image.load(os.path.join("assets", "bullet.png"))
ENBULLET = pygame.image.load(os.path.join("assets", "enemybullet.png"))
EN2BULLET = pygame.image.load(os.path.join("assets", "enemy2bullet.png"))


class player: # define base class
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.bullet_img = None
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))
    def get_width(self):
        return self.player_img.get_width()

    def get_height(self):
        return self.player_img.get_height()

class Player(player): # define player class
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_img = PLAYER
        self.bullet_img = BULLET
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health

class Enemy(player): # define enemy class
    SELECTOR_MAP = {
                    "one": (ENEMY, ENBULLET),
                    "two": (ENEMY2, EN2BULLET)
                    }
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_img = ENEMY
        self.bullet_img = ENBULLET
        self.mask = pygame.mask.from_surface(self.player_img)


    def move(self, vel):
        self.y += vel


# main game loop
def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("chiller", 50)

    enemies = []
    wave_length = 5
    enemy_vel = 1


    player_vel = 5

    player = Player(300, 500)

    clock = pygame.time.Clock()

    lost = False

    def redraw_window():
        WIN.blit(BG, (0,0))


        # text on screen
        Lives_UI = main_font.render(f"Lives: {lives}", 1, (211,47,47))
        Level_UI = main_font.render(f"Level: {level}", 1, (211,47,47))

        WIN.blit(Lives_UI, (10, 10))
        WIN.blit(Level_UI, (WIDTH - Level_UI.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)



        pygame.display.update()


    while run:
        clock.tick(FPS)

        if lives <= 0 or player.health <= 0:
            lost = True

        if len(enemies)== 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["one", "two"]))
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        redraw_window()


main()