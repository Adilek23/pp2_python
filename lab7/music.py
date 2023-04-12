import pygame as pg
import sys
import os
 
pg.init()

class Music:
    def __init__(self, path_to_music, path_to_photo):
        self.path_to_music = path_to_music
        self.photo = pg.image.load('images/images5/' + path_to_photo)
        self.photo = pg.transform.scale(self.photo, (260, 230))
        self.in_pause = False

    def play_music(self, screen):
        self.in_pause = False
        pg.mixer.music.load('music/' + self.path_to_music)
        pg.mixer.stop()
        pg.mixer.music.play()
        screen.blit(self.photo, (20, 18))

music_path = os.listdir('music')
image_path = os.listdir('images/images5')

music_array = []

for i in zip(music_path, image_path):
    music = Music(i[0], i[1])
    music_array.append(music)


screen = pg.display.set_mode((300,400))
bg = pg.image.load('images\Frame1.jpg')
bg = pg.transform.scale(bg, (300,400))
prev_button = pg.Rect(62, 271, 46, 42)
next_button = pg.Rect(194, 271, 46, 42)
stop_button = pg.Rect(127, 268, 47, 47)
screen.blit(bg, (0,0))
cnt = 0
music_array[0].play_music(screen)
music_index = 0

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            position = pg.mouse.get_pos()
            if prev_button.collidepoint(position):
                music_index -= 1
                if(music_index == -1):
                    music_index = len(music_array) - 1
                music_array[music_index].play_music(screen)
                
                
            elif next_button.collidepoint(position):
                music_index += 1
                if(music_index == len(music_array)):
                    music_index = 0
                music_array[music_index].play_music(screen)
            elif stop_button.collidepoint(position):
                if not music_array[music_index].in_pause:
                    music_array[music_index].in_pause = True
                    pg.mixer.music.pause()
                else:
                    music_array[music_index].in_pause = False
                    pg.mixer.music.unpause()
    pg.display.update()