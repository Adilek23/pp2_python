import pygame as pg
import sys
from random import randint


pg.init()
#создаем экран размером 400 х 600
screen = pg.display.set_mode((400,600))
#загружаем наш задний фон, дорогу
bg = pg.image.load('assets/bg.png')
clock = pg.time.Clock()

#создаем класс нашей машинки
class Person(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('assets/Player.png')
        self.image = pg.transform.scale(self.image, (48,93))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500
    
#создаем физику движения для нашей машинки
    def update(self, x = 0):
        if (self.rect.x <= 0):
            x = 0
            self.rect.x = 1
        if (self.rect.x >= 351):
            x = 0
            self.rect.x = 350
        self.rect.move_ip(x, 0)

#создаем класс машинки соперника
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('assets/Enemy.png')
        self.image = pg.transform.scale(self.image, (48,93))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,360)
        self.rect.y = -100
    
#создаем физику движения для машинки соперника
    def update(self):
        if self.rect.y > 700:
            self.rect.y = -100
            self.rect.x = randint(0,360)
        if cnt < 10:
            self.rect.move_ip(0,10)

        if cnt >= 10:
            self.rect.move_ip(0,12)

        if cnt >= 20:
            self.rect.move_ip(0,15)

#создаем класс монетки

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('assets/coin.png')
        self.image = pg.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,360)
        self.rect.y = -100

#физика движения монетки
    def update(self):
        if self.rect.y > 700:
            self.new_c()
        self.rect.move_ip(0,10)

    def new_c(self):
        self.rect.x = randint(0,360)
        self.rect.y = -100

player = Person()
enemy = Enemy()
coin = Coin()
sprites = pg.sprite.Group()
sprites.add(player)
sprites.add(enemy)
sprites.add(coin)





#шрифт
font = pg.font.Font(None, 40)
cnt = 0




while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()   
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()

    screen.blit(bg, (0,0))
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        if cnt < 10:
            player.update(-5)
        elif cnt >= 10 and cnt < 20:
            player.update(-10)
        else:
            player.update(-15)
    if keys[pg.K_d]:
        if cnt < 10:
            player.update(5)
        elif cnt >= 10 and cnt < 20:
            player.update(10)
        else:
            player.update(15)    


    # если противник ударяется об нашу машинку, конец игры
    if enemy.rect.collideobjects([player]):
        pg.quit()    
        sys.exit()

    # если монетка ударяется об машинку противника, 
    # она получает новые координаты
    if coin.rect.collideobjects([enemy]):
        coin.new_c()
    # если монетка ударяется об нашу монетку,
    #  то мы считаем кол-во собранных монеток
    if coin.rect.collideobjects([player]):
        cnt += 1
        coin.new_c()
        
    screen.blit(font.render(f"Вы набрали {cnt} монет", 0, 'blue'), (0,0))    
    sprites.update()
    sprites.draw(screen)
    pg.display.update()
    clock.tick(60)