import pygame as pg

class Paddle(pg.sprite.Sprite):
    def __init__(self, x_coord):
        pg.sprite.Sprite.__init__(self)
        self.screen = pg.display.get_surface()

        self.pos = [x_coord, 100]

        self.size = [10, 100]

        self.should_move = False
        self.direction = 1

    def draw(self):
        pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]))

    def move(self):
        if self.should_move:
            if self.pos[1] < 0:
                self.pos[1] = 0

            elif self.pos[1] > 600 - self.size[1]:
                self.pos[1] = 600 - self.size[1]

            else:
                self.pos[1] += self.direction
