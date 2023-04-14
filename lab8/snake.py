import pygame as pg
import random
pg.init()

#создаем класс нашей змейки, ее тело и голова
class Snake(pg.sprite.Sprite):
    head = (100, 0) #координаты для головы 
    body = [(50, 0),(0, 0)] # координаты для тела

#создаем физику движения змейки
    def update(self, dx, dy):
        self.body.insert(0, self.head) # добавляем голову змейки в начало тела
        self.body.pop() # удаляем последний элемент из тела

        #преобразуем кортеж головы в список, чтобы можно было изменить координаты
        self.head = list(self.head)
        #изменяем координаты тела в соответствии с dx и dy
        self.head[0] += dx * 50
        self.head[1] += dy * 50
        #преобразуем список головы обратно в кортеж
        self.head = tuple(self.head)


    def draw(self, screen):
    #при каждой еде будем дорисовывать к телу квадраты
        for i in self.body:
            pg.draw.rect(screen, 'white', [*i,49,49])
    # рисуем голову змейки
        pg.draw.rect(screen, 'red', (*self.head, 49, 49))

    def has_colise(self, apple, dx, dy):
        # создаем прямоугольник для головы змейки
        head_rect = pg.Rect(*self.head, 49, 49)
        # проверяем, пересекаются ли голова змейки с яблоком
        if head_rect.collideobjects([apple]):
            # добавляем новый элемент тела в конец
            self.body.append((self.body[-1][0] - 5000 * dx, self.body[-1][1] - 5000 * dy))
            return True # если произошло столкновение
        return False # если не произошло


    # проверяем, умерла ли змейка
    def isDead(self):
        # если голова пересекается с телом
        if self.head in self.body: 
            return True
        # если голова змейки вышла за пределы экрана
        if self.head[0] > 799 or self.head[0] < 0 or self.head[1] > 599 or self.head[1] < 0:
            return True # умерла, если вышла
        return False # не умерла

# создаем класс яблока

class Apple(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50)) # создаем яблоко, как отдельный экран
        self.rect = self.image.get_rect() # получаем прямоугольник яблока
        # размещаем на позиции функции
        self.PlaceApple()

    # размещаем яблоко на рандомной позиции
    def PlaceApple(self):
        x, y = random.randrange(0, 750, 50), random.randrange(0, 550, 50)
        self.rect.x = x
        self.rect.y = y

    # рисуем яблоко
    def draw(self, screen):
        pg.draw.rect(screen, 'green', self.rect)

# создаем экран размером 800 х 600
screen = pg.display.set_mode((800, 600))


snake = Snake() # создание экземпляра змеи
apple = Apple() # создание экземпляра яблока


cnt = 0
# dict клавишей куда мы можем двигаться, если наверх, 
# то одновременно вниз не можем двигаться
our_keyses = {'W': True, 'S': True, 'D': True, 'A': False}

clock = pg.time.Clock()
dx = 1
dy = 0
speed_count = 1
speed = 10
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    #проверка на столкновение с яблоком
    if snake.has_colise(apple, dx, dy):
        apple.PlaceApple()
        cnt += 1
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and our_keyses['W']:
        dx = 0
        dy = -1
        our_keyses = {'W': True, 'S': False, 'D': True, 'A': True}
    if keys[pg.K_s] and our_keyses['S']:
        dx = 0
        dy = 1
        our_keyses = {'W': False, 'S': True, 'D': True, 'A': True}
    if keys[pg.K_a] and our_keyses['A']:
        dx = -1
        dy = 0
        our_keyses = {'W': True, 'S': True, 'D': False, 'A': True}
    if keys[pg.K_d] and our_keyses['D']:
        dx = 1
        dy = 0
        our_keyses = {'W': True, 'S': True, 'D': True, 'A': False}
    screen.fill('black')
    speed_count += 1
    if cnt >= 4 and cnt < 10:
        speed = 8
    if cnt >= 10:
        speed = 5
    # Обновление позиции змеи каждые `speed` итераций цикла
    if speed_count % speed == 0:
        snake.update(dx, dy)
    snake.draw(screen)
    apple.draw(screen)
    pg.display.flip()
    if snake.isDead():
        exit()
    clock.tick(60)