import pygame
import os
from enemies.enemy1 import Enemy_1
from enemies.enemy2 import Enemy_2
from enemies.enemy3 import Enemy_3
from archer.archer_towers import Towers
from menu.menu import Menu
from menu.menu import PlayPauseButton
import time
import random

pygame.init()
waves = [
    [2, 0, 0],
    [5, 0, 0],
    [10, 0, 0],
    [0, 2, 0],
    [0, 5, 1],
    [0, 10, 0],
    [2, 10, 0],
    [5, 10, 0],
    [10, 10, 0],
    [3, 3, 5, ],
    [2, 0, 10],
    [2, 0, 15],
    [20, 10, 20],
]
tower_position = [(895, 645),
                  (1032, 426),
                  (1068, 203),
                  (819, 184),
                  (534, 203),
                  (222, 500),
                  (102, 151),
                  ]
play_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/sistem/play_btn.png")), (75, 75))
pause_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/sistem/pause_btn.png")), (75, 75))


class Game:
    def __init__(self):
        self.width = 1350
        self.height = 750
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tower Defense")  # Заголовок окна
        self.lives_img = pygame.image.load(os.path.join('game_assets', 'heart.png')).convert_alpha()
        self.enemies = []
        self.towers = [Towers(479, 697)]
        self.lives = 3
        self.money = 100
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.bg = pygame.image.load(os.path.join('game_assets/sistem/bg.jpg'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.wave = 0
        self.timer = time.time()
        self.current_wave = waves[self.wave][:]
        self.paused = False
        self.button_color = (0, 128, 0)
        self.button_hover_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont("comicsans", 40)
        self.button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 - 30, 200, 60)
        self.playPauseButton = PlayPauseButton(play_btn, pause_btn, 10, self.height - 85)

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(100)

            if self.paused == False:
                if time.time() - self.timer >= random.randrange(1, 6) / 3:
                    self.timer = time.time()
                    self.gen_enemies()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.paused:
                        if self.button_rect.collidepoint(pos):
                            self.paused = False
                    else:
                        for i in tower_position:
                            for tower in self.towers:
                                if (pos[0] - tower.x) ** 2 + (pos[1] - tower.y) ** 2 < 100 ** 2:
                                    break
                            else:
                                if pos[0] in range(i[0] - 60, i[0] + 60) and pos[1] in range(i[1] - 25, i[1] + 25):
                                    self.towers.append(Towers(i[0], i[1]))

            if not self.paused:
                if time.time() - self.timer >= 2:
                    self.timer = time.time()
                    self.enemies.append(random.choice([Enemy_1(), Enemy_2(), Enemy_3()]))

                to_del = []
                for en in self.enemies:
                    if en.x < -5:
                        to_del.append(en)
                # удаление врагов
                for d in to_del:
                    self.enemies.remove(d)
                    self.hit_player()

                for tw in self.towers:
                    tw.attack(self.enemies)

                if self.lives < 1:
                    return False

                self.draw()
            else:
                self.draw_pause_screen()

        pygame.quit()

    def gen_enemies(self):
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.paused = True
                self.playPauseButton.paused = self.paused
        else:
            wave_enemies = [Enemy_1(), Enemy_2(), Enemy_3()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        text = self.life_font.render(str(self.lives), 1, (255, 255, 255))
        life = pygame.transform.scale(self.lives_img, (50, 50))
        start_x = self.width - life.get_width() - 10
        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))

        """враги"""
        for en in self.enemies:
            if en.draw(self.win):
                self.hit_player()

        """башни"""
        for tw in self.towers:
            tw.draw(self.win)

        pygame.display.update()

    def hit_player(self):
        self.lives -= 1

    def draw_pause_screen(self):
        pos = pygame.mouse.get_pos()

        if self.button_rect.collidepoint(pos):
            button_color = self.button_hover_color
        else:
            button_color = self.button_color

        pygame.draw.rect(self.win, button_color, self.button_rect)
        text_surface = self.button_font.render("Continue", True, self.text_color)
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.win.blit(text_surface, text_rect)
        pygame.display.update()

    def draw_end_screen(self):
        pos = pygame.mouse.get_pos()

        if self.button_rect.collidepoint(pos):
            button_color = self.button_hover_color
        else:
            button_color = self.button_color

        pygame.draw.rect(self.win, button_color, self.button_rect)
        text_surface = self.button_font.render("Restart", True, self.text_color)
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.win.blit(text_surface, text_rect)
        pygame.display.update()