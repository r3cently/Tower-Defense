import pygame
import os
from enemies.enemy import Enemy


class Enemy_3(Enemy):
    def __init__(self):
        super().__init__()
        self.images = []
        self.max_health = 4
        self.health = self.max_health
        for x in range(8):
            add_str = str(x)
            if x < 10:
                add_str = "0" + add_str
            self.images.append(pygame.transform.scale(
                pygame.image.load(os.path.join("enemies/enemy3", "7_enemies_1_attack_0" + add_str + ".png")),
                (64, 64)))