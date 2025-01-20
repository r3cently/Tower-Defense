import pygame
import os
from enemy_1 import Enemy_1
from club import Club
from enemy3 import Enemy_3
from archer_towers import Towers


class Game:
    def __init__(self):
        self.width = 1350
        self.height = 750
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Club()]
        self.towers = [Towers(300, 300)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join('game_assets/sistem', 'bg.jpg'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
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

            for d in to_del:
                self.enemies.remove(d)

            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        """враги"""
        for en in self.enemies:
            en.draw(self.win)

        """башни"""
        for tw in self.towers:
            tw.draw(self.win)

        pygame.display.update()


g = Game()
g.run()
