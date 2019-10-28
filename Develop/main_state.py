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
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 1600, 630, self.x, 300)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 1

class Character:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('running1.png')
        

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

# 게임에 들어갈 때 초기화를 해준다
# boy와 grass를 초기화 해준다!
def enter():
    global character, maps
    pass

# 게임이 종료될 때를 위해서
# boy와 grass를 없애준다
def exit():
    global boy, grass
    del(boy)
    del(grass)
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
    pass

#
def update():

    pass


def draw():
    clear_canvas()
    grass.draw()            # 풀을 그리고..
    boy.draw()              # 소년도 그려주고....
    update_canvas()         # 업데이트된 상태도 보여주고....
    pass





