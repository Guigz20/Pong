import pygame as pg
import random

class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.screen = pg.display.get_surface()

        initial_speed_coeff = random.random()/2
        print("Initial Speed Coeff: ", initial_speed_coeff)
        self.ball_size = 10

        self.pos = [400, 300]
        self.vel = [random.choice([-1, 1])*initial_speed_coeff, random.choice([-1, 1])*(0.5-initial_speed_coeff)]
        print(self.vel)

        self.Rect = pg.rect.Rect(400, 300, self.ball_size*2, self.ball_size*2)

    def draw(self):
        pg.draw.circle(self.screen, (255,255,255), self.pos, self.ball_size)
        self.Rect.x = self.pos[0] - self.ball_size
        self.Rect.y = self.pos[1] - self.ball_size

    def move(self, padlle_rects):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[1] < self.ball_size:
            self.vel[1] = -self.vel[1]
        if self.pos[1] > 600 - self.ball_size:
            self.vel[1] = -self.vel[1]

        if self.Rect.collidelist(padlle_rects) != -1:
            self.vel[0] = -self.vel[0]
            self.pos[0] += self.vel[0]*2

