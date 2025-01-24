import pygame
from tower import Tower
import os
import math

class Towers(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_images = []
        self.archer_images = []
        self.archer_count = 0
        self.range = 50
        self.inRange = False
        """добавление изображений башен"""
        for x in range(1, 2):
            self.tower_images.append(pygame.transform.scale(
                pygame.image.load(os.path.join("Towers/Tower" + str(x) + ".png")),
                (400, 400)))
        """добавление изображений лучников(нужно найти спрайты)"""
        for x in range(1, 6):
            self.archer_images.append(
                pygame.image.load(os.path.join("archer/atack/Atack" + str(x) + ".png"))
            )

    def draw(self, win):
        super().draw(win)
        if self.archer_count >= len(self.archer_images) * 12:
            self.archer_count = 0
        archer = self.archer_images[self.archer_count // 12]
        win.blit(archer, (
            (self.x + self.width / 2) - (archer.get_width() / 2) * 1.05, (self.y - archer.get_height() / 1.2)))
        self.archer_count += 1

    def change_range(self, r):
        """Радиус атаки"""

    def attack(self, enemies):
        """атака врагов, находящихся в списке"""
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dis < self.range:
                self.inRange = True
