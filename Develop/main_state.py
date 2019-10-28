import random
import json
import os

from pico2d import *

import game_framework
import title_state          # esc키를 눌렀을 때 타이틀 화면으로 넘어가기 위해 타이틀 상태를 받아온다
import pause_two            # p키를 눌렀을 때 반짝거리는 pause상태를 나타내주기 위해 받아온다
#import pause_state


name = "MainState"

boy = None
grass = None
font = None

#
# grass의 클래스를 하나 만들어준다
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')        # 초기값은 grass이미지가 뜨게

    def draw(self):
        self.image.draw(400, 30)                    # 그려준다!


class Boy:                                          # boy class를 생성해줍시다
    def __init__(self):
        self.x, self.y = 0, 90                      # boy의 초기값은 (0,90)에서 시작
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1                                # 거리를 1씩 늘려가며

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir                          #움직이게 해줍니다
        if self.x >= 800:
            self.dir = -1                           # x=800이 되면 반대로 움직이게 해줍니다
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

# 게임에 들어갈 때 초기화를 해준다
# boy와 grass를 초기화 해준다!
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:         # p를 누르면 main_state상태를 유지하면서 pause상태를 불러온다
            game_framework.push_state(pause_two)

    pass

#
def update():
    boy.update()            # 소년을 뛰게 합시다
    pass


def draw():
    clear_canvas()
    grass.draw()            # 풀을 그리고..
    boy.draw()              # 소년도 그려주고....
    update_canvas()         # 업데이트된 상태도 보여주고....
    pass





