import pygame
import math
from archer.archer_towers import Towers


class Enemy:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(335, 749), (405, 613), (482, 607), (558, 605), (736, 603),
                     (769, 596), (964, 549), (1076, 538), (1133, 519), (1157, 490),
                     (1173, 444), (1173, 404), (1121, 325), (1006, 281),
                     (949, 206), (834, 73), (747, 85),
                     (724, 112), (715, 134), (693, 213), (619, 290), (567, 303),
                     (510, 305), (444, 300), (255, 294), (162, 255),
                     (108, 246), (78, 245), (58, 246), (27, 250), (1, 250), (-100, 373)]
        self.path_pos = 0
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        # 31 координата
        self.image = None
        self.move_count = 0
        self.move_dis = 0
        self.images = []
        self.dis = 0
        self.flipped = False
        self.max_health = 0

    def draw(self, win):
        self.animation_count += 1
        if self.animation_count >= len(self.images) * 5:
            self.animation_count = 0
        self.image = self.images[self.animation_count // 5]
        win.blit(self.image, (self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2))
        self.draw_health_bar(win)
        return self.move()


    def draw_health_bar(self, win):
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255, 0, 0), (self.x - 35, self.y - 40, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 35, self.y - 40, health_bar, 10), 0)

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.width and Y >= self.y:
                return True
        return False

    def move(self):
        will_hit = False
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-100, 373)
            will_hit = True

        else:
            x2, y2 = self.path[self.path_pos + 1]

        dirn = ((x2 - x1) * 2, (y2 - y1) * 2)
        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2)
        dirn = (dirn[0] / length, dirn[1] / length)


        if dirn[0] < 0 and not self.flipped:
            self.flipped = True
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = (self.x + dirn[0], self.y + dirn[1])

        self.x = move_x
        self.y = move_y
        if dirn[0] >= 0:
            if dirn[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:
            if dirn[1] >= 0:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y <= y2:
                    self.path_pos += 1
        return will_hit

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
        return False