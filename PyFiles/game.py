import pygame
import os
from enemies.enemy1 import Enemy_1
from enemies.enemy2 import Enemy_2
from enemies.enemy3 import Enemy_3
from archer.archer_towers import Towers
import time
import random
lives_img = pygame.image.load(os.path.join('game_assets', 'heart.png'))


class Game:
    def __init__(self):
        self.width = 1350
        self.height = 750
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Enemy_2()]
        self.towers = [Towers(479, 697)]
        self.lives = 3
        self.money = 100
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.bg = pygame.image.load(os.path.join('game_assets/sistem/bg.jpg'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            if time.time() - self.timer >= 2:
                self.timer = time.time()
                self.enemies.append(random.choice([Enemy_1(), Enemy_2(), Enemy_3()]))
            #pygame.time.delay(500)
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pos)
            to_del = []
            for en in self.enemies:
                if en.x < -5:
                    to_del.append(en)
            #удаление врагов
            for d in to_del:
                self.enemies.remove(d)

            for tw in self.towers:
                tw.attack(self.enemies)

            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        text = self.life_font.render(str(self.lives), 1, (255, 255, 255))
        life = pygame.transform.scale(lives_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))

        """враги"""
        for en in self.enemies:
            en.draw(self.win)

        """башни"""
        for tw in self.towers:
            tw.draw(self.win)

        pygame.display.update()


g = Game()
g.run()