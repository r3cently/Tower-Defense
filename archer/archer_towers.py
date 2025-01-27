import pygame
from PyFiles.tower import Tower
import os
import math
import time


class Towers(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_images = []
        self.archer_images = []
        self.archer_count = 0
        self.range = 130
        self.inRange = False
        self.right = True
        self.timer = time.time()
        self.damage = 1
        """добавление изображений башен"""
        for x in range(1, 2):
            self.tower_images.append(pygame.transform.scale(
                pygame.image.load(os.path.join("Towers/Tower" + str(x) + ".png")),
                (400, 400)))
        """добавление изображений лучников(нужно найти спрайты)"""
        for x in range(1, 11):
            self.archer_images.append(
                pygame.image.load(os.path.join("archer/atack/Atack" + str(x) + ".png"))
            )

    def draw(self, win):
        # визуализация радиуса атаки
        circle_surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(circle_surface, (128, 128, 128, 90), (self.range, self.range), self.range, 0)
        win.blit(circle_surface, (self.x - self.range, self.y - self.range))
        super().draw(win)

        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_images) * 12:
                self.archer_count = 0
        else:
            self.archer_count = 0
        archer = self.archer_images[self.archer_count // 12]
        if self.right == True:
            add = 0
        else:
            add = -archer.get_width() + 277
        win.blit(archer, (
            (self.x + self.width / 2 + add) - (archer.get_width() / 2) * 1.05, (self.y - archer.get_height() / 1.2)))
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
                enemy_closest.append(enemy)

        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.hit() == True:
                    enemies.remove(first_enemy)
            if first_enemy.x < self.x and not (self.right):
                self.right = True
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)
            elif self.right and first_enemy.x > self.x:
                self.right = False
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)