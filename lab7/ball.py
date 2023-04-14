import pygame as pg
pg.init()
screen = pg.display.set_mode((1000,1000))
x = y = 500
clock = pg.time.Clock()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        y -= 5
    if keys[pg.K_a]:
        x -= 5
    if keys[pg.K_s]:
        y += 5
    if keys[pg.K_d]:
        x += 5

    if x > 1049:
        x = -49
    if x < 25:
        x = 975
    if y > 1049:
        y = -49
    if y < -49:
        y = 1049
    screen.fill('white')
    pg.draw.circle(surface = screen, color = (255,0,0), center = (x,y), radius = 25)
    pg.display.flip()
    clock.tick(60)