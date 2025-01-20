import pygame
from tower import Tower
import os


class Towers(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_images = []
        self.archer_images = []
        self.archer_count = 0
        """добавление изображений башен"""
        for x in range(1, 2):
            self.tower_images.append(pygame.transform.scale(
                pygame.image.load(os.path.join("Towers/Tower" + str(x) + ".png")),
                (64, 64)))
        """добавление изображений лучников(нужно найти спрайты)"""
        # for x in range(2):
        #    self.tower_images.append(pygame.transform.scale(
        #        pygame.image.load(os.path.join("Towers/Tower1", str(x) + ".png")),
        #        (64, 64)))

    def draw(self, win):
        super().draw(win)
        if self.archer_count >= len(self.archer_images):
            self.archer_count = 0

        archer = self.archer_images[self.archer_count]
        win.blit(archer, (
            (self.x + self.width / 2) - (archer.get_width() / 2), (self.y - archer.get_height())))
        self.archer_count += 1

    def attack(self, enemies):
        """атака врагов, находящихся в списке"""
        pass
