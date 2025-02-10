import os.path
import pygame

class Tower():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.menu = None
        self.tower_images = []
        self.damage = 1
        for x in range(0, 2):
            self.tower_images.append(pygame.transform.scale(
                pygame.image.load(os.path.join("Towers/Tower" + str(x + 1) + ".png")),
                (400 - 200 * x, 400 - 200 * x)))

    def draw(self, win):
        """отрисовка башни"""
        image = self.tower_images[self.level - 1]
        win.blit(image, (self.x - image.get_width() // 2, self.y - image.get_height() // 2))

    def click(self, X, Y):
        """нажатие на башню и выделение данной башни"""
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.width and Y >= self.y:
                return True
        return False

    def sell(self):
        """покупка башни"""
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """улучшение башни на 1 уровень по определнной цене"""
        if self.level < 2:
            self.level += 1
            self.damage += 1

    def get_level(self):
        return self.level

    def get_upgrade_cost(self):
        """возвращает цену улучшения, если она равна нулю, то улучшить нельзя"""
        return self.sell_price[self.level - 1]

    def move(self, x, y):
        self.x = x
        self.y = y