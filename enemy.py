import pygame
import math


class Enemy:
    images = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(34, 250), (144, 250),
                     (250, 287), (409, 302),
                     (585, 299), (675, 256),
                     (703, 160), (751, 91),
                     (817, 65), (886, 85),
                     (930, 142), (949, 207),
                     (982, 271), (1047, 298),
                     (1123, 316), (1162, 364),
                     (1180, 419), (1168, 475),
                     (1132, 519), (1079, 536),
                     (1022, 541), (951, 540),
                     (876, 545), (818, 567),
                     (763, 602), (663, 603),
                     (177, 602), (120, 562),
                     (95, 510), (88, 447),
                     (47, 394), (1, 373)]
        self.path_pos = 0
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        #31 координата
        self.image = None
        self.move_count = 0
        self.move_dis = 0
        self.dis = 0

    def draw(self, win):
        self.animation_count += 1
        if self.animation_count >= len(self.images):
            self.animation_count = 0
        self.image = self.images[self.animation_count]
        win.blit(self.image, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.width and Y >= self.y:
                return True
        return False

    def move(self):
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 373)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.move_count += 1
        dirn = (x2 - x1, y2 - y1)

        move_x, move_y = (self.x + dirn[0] + self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0

        self.x = move_x
        self.y = move_y
        self.path_pos += 1

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True