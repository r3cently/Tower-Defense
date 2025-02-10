from PyFiles.game import Game
import pygame
import os


class MainMenu:
    def __init__(self, win):
        self.width = 1350
        self.height = 700
        self.bg = pygame.image.load(os.path.join("game_assets/sistem" + "/bg.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.start_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/sistem" + "/button_play.png")).convert_alpha(), (500, 400))
        self.logo = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/sistem" + "/logo.png")).convert_alpha(), (500, 500))
        self.win = win
        self.btn = (self.width/2 - self.start_btn.get_width()/2, 350, self.start_btn.get_width(), self.start_btn.get_height())

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game()
                            game.run()

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(self.logo, (self.width/2 - self.logo.get_width()/2, 0))
        self.win.blit(self.start_btn, (self.btn[0], self.btn[1]))
        pygame.display.update()

