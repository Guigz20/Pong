import pygame as pg

class Paddle(pg.sprite.Sprite):
    def __init__(self, x_coord):
        pg.sprite.Sprite.__init__(self)
        self.screen = pg.display.get_surface()

        self.pos = [x_coord, 100]

        self.size = [10, 100]

    def draw(self):
        pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]))