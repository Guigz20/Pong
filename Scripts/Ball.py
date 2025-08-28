import pygame as pg
import random
import math

import pygame.draw


class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.screen = pg.display.get_surface()

        self.initial_speed_coeff = random.random()/4
        self.speed_increase_coeff = 1.1
        self.speed = 600


        self.ball_size = 10

        self.pos = [400, 300]
        self.vel = [random.choice([-1, 1])*self.initial_speed_coeff,
                    random.choice([-1, 1])*(0.25-self.initial_speed_coeff)]
        print(self.vel)

        self.Rect = pg.rect.Rect(400, 300, self.ball_size*2, self.ball_size*2)

        self.last_direction_before_collide = 0
        self.colliding = 0

    def draw(self):
        pg.draw.circle(self.screen, (255,255,255), self.pos, self.ball_size)
        self.Rect.x = self.pos[0] - self.ball_size
        self.Rect.y = self.pos[1] - self.ball_size


    def move(self, padlle_rects, dt):
        self.pos[0] += self.vel[0]*dt*self.speed
        self.pos[1] += self.vel[1]*dt*self.speed

        if self.pos[1] < self.ball_size:
            self.vel[1] = -self.vel[1]
        if self.pos[1] > 600 - self.ball_size:
            self.vel[1] = -self.vel[1]

        if self.pos[0] > 400 - self.ball_size:
            pass

        if self.Rect.collidelist(padlle_rects) != -1:

            if self.colliding == 0:
                self.vel[0] = -self.vel[0]
                self.colliding = 1

        else:
            self.last_direction_before_collide = self.vel[0] / abs(self.vel[0])
            self.colliding = 0


    def increase_speed(self):
        self.vel = [self.vel[0]*self.speed_increase_coeff, self.vel[1]*self.speed_increase_coeff]

    def reset(self):
        self.initial_speed_coeff = random.random() / 4
        self.pos = [400, 300]
        self.vel = [random.choice([-1, 1]) * self.initial_speed_coeff,
                    random.choice([-1, 1]) * (0.25 - self.initial_speed_coeff)]

    def on_death(self):
        self.reset()


