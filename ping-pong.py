from random import randint
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
    # def point(self):
    #     point_l = global
    #     point_r = global


class Player(GameSprite):
    def move_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 650:
            self.rect.y += self.speed
    def move_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 650:
            self.rect.y += self.speed


mw = display.set_mode((700, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('pole.jpg'), (700, 500))
clock = time.Clock()

speed_x = 4
speed_y = 4

point_l = 0
point_r = 0

Dio = Player('Dio_Brando.png', 10, 200, 15, 70, 170)
Jorno = Player('jorno.png', 600, 200, 15, 70, 170)

josuke = GameSprite('josuke.png', 350,250,4,50,50)

font.init()
font = font.Font(None, 36)

win_right = font.render('Golden Experience are Winner!!!', 1, (255,255,255))
win_left = font.render('The World are Winner!!!', 1, (255,255,255))

game = True
finish = False
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        mw.blit(background, (0,0))
        josuke.reset()
        Dio.reset()
        Jorno.reset()
        josuke.rect.x += speed_x
        josuke.rect.y += speed_y
        Dio.move_l()
        Jorno.move_r()
        text_l = font.render('Счёт Dio:' + str(point_l), 1, (255,255,255))
        mw.blit(text_l, (10,20))
        text_r = font.render('Счёт Jorno:' + str(point_l), 1, (255,255,255))
        mw.blit(text_r, (525, 20))

        if sprite.collide_rect(Dio, josuke) or sprite.collide_rect(Jorno ,josuke):
            speed_x *= -1
            speed_y *= 1
        if josuke.rect.y > 450 or josuke.rect.y < 0:
            speed_y *= -1
        if josuke.rect.x < 0:
            point_r += 1
            if point_r == 3:
                finish = True
                mw.blit(win_right, (200, 200))
        if josuke.rect.x > 650:
            point_l += 1
            if point_l == 3:
                finish = True
                mw.blit(win_left, (200, 200))


    display.update()
    clock.tick(FPS)