import pygame as pg
from Ball import *
from Paddle import *
import time

class Game:
    def __init__(self):
        SCREENSIZE = (800, 600)
        self.screen = pg.display.set_mode(SCREENSIZE)

        self.LeftPaddle = Paddle(50)
        self.RightPaddle = Paddle(750)


        self.paddle_rects = [self.LeftPaddle.Rect, self.RightPaddle.Rect]

        self.Ball = Ball()

        self.clock = pg.time.Clock()

        self.SpeedIncreaseTimer = pg.event.custom_type()
        pg.time.set_timer(self.SpeedIncreaseTimer, 5000)

        self.running = True

    def loop(self):
        while self.running:

            dt = self.clock.tick(60)/1000
            print(dt)

            self.draw()

            self.LeftPaddle.move(dt)
            self.paddle_rects[0] = self.LeftPaddle.Rect
            self.RightPaddle.move(dt)
            self.paddle_rects[1] = self.RightPaddle.Rect
            self.Ball.move(self.paddle_rects, dt)

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_s:
                        self.LeftPaddle.should_move = True
                        self.LeftPaddle.direction = 1
                    elif event.key == pg.K_w:
                        self.LeftPaddle.should_move = True
                        self.LeftPaddle.direction = -1
                    elif event.key == pg.K_UP:
                        self.RightPaddle.should_move = True
                        self.RightPaddle.direction = -1
                    elif event.key == pg.K_DOWN:
                        self.RightPaddle.should_move = True
                        self.RightPaddle.direction = 1
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_s or event.key == pg.K_w:
                        self.LeftPaddle.should_move = False
                    elif event.key == pg.K_DOWN or event.key == pg.K_UP:
                        self.RightPaddle.should_move = False
                elif event.type == self.SpeedIncreaseTimer:
                    self.Ball.increase_speed()

        pg.QUIT

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.LeftPaddle.draw()
        self.RightPaddle.draw()
        self.Ball.draw()

if __name__ == '__main__':
    game = Game()
    game.loop()
