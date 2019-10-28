import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

character = None
maps = None


class Maps:
    def __init__(self):
        self.image = load_image('map02_3.png')
        self.x, self.y = 640,0
        self.frame = 0
    def draw(self):
        self.image.draw(self.x,300)

    def update(self):
        self.x -= 1

class Character:
    def __init__(self):
        self.x, self.y = 90, 90
        self.frame = 0
        self.image = load_image('running1.png')
    def update(self):
        self.image.draw(150, 200)

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)
        self.frame = (self.frame + 1) % 4

    def UPattack(self):
        self.image = load_image('up_attack.png')


    def Usualattack(self):
        self.image = load_image('up_attack.png')
        self.draw(150,90)

def enter():
    global character, maps
    character = Character()
    maps = Maps()
    pass


def exit():
    global character, maps
    del(character)
    del(maps)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:          # 윈도우 창 x를 누르면 종료되게
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:    # 타이틀 상태에서 esc키를 누르면 타이틀로 넘어가게
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            character.UPattack()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_j:
            character.Usualattack()


    pass

#
def update():
    character.update()
    maps.update()
    pass


def draw():
    clear_canvas()
    maps.draw()            # 풀을 그리고..
    character.draw()              # 소년도 그려주고....
    update_canvas()         # 업데이트된 상태도 보여주고....

    delay(0.1)
    pass





