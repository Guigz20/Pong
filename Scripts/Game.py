import pygame as pg

from Paddle import *

class Game:
    def __init__(self):
        SCREENSIZE = (800, 600)
        self.screen = pg.display.set_mode(SCREENSIZE)

        self.LeftPaddle = Paddle(50)
        self.RightPaddle = Paddle(750)
        self.PaddleSpeed = 0.5

        self.running = True

    def loop(self):
        while self.running:

            self.draw()

            self.LeftPaddle.move()
            self.RightPaddle.move()

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_s:
                        self.LeftPaddle.should_move = True
                        self.LeftPaddle.direction = self.PaddleSpeed
                    elif event.key == pg.K_w:
                        self.LeftPaddle.should_move = True
                        self.LeftPaddle.direction = -self.PaddleSpeed
                    elif event.key == pg.K_UP:
                        self.RightPaddle.should_move = True
                        self.RightPaddle.direction = -self.PaddleSpeed
                    elif event.key == pg.K_DOWN:
                        self.RightPaddle.should_move = True
                        self.RightPaddle.direction = self.PaddleSpeed
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_s or event.key == pg.K_w:
                        self.LeftPaddle.should_move = False
                    elif event.key == pg.K_DOWN or event.key == pg.K_UP:
                        self.RightPaddle.should_move = False

        pg.QUIT

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.LeftPaddle.draw()
        self.RightPaddle.draw()

if __name__ == '__main__':
    game = Game()
    game.loop()
