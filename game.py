import pygame
import os
from enemy_1 import Enemy_1


class Game:
    def __init__(self):
        self.width = 1350
        self.height = 750
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Enemy_1()]
        self.towers = []
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join('game_assets/sistem', 'bg.jpg'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))


    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        for en in self.enemies:
            en.draw(self.win)

        pygame.display.update()

g = Game()
g.run()