import pygame as pg

from Paddle import *

class Game:
    def __init__(self):
        SCREENSIZE = (800, 600)
        self.screen = pg.display.set_mode(SCREENSIZE)

        self.LeftPaddle = Paddle(100)
        self.RightPaddle = Paddle(700)

        self.running = True

    def loop(self):
        while self.running:

            self.draw()

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

        pg.QUIT

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.LeftPaddle.draw()
        self.RightPaddle.draw()

if __name__ == '__main__':
    game = Game()
    game.loop()
