import random
import json
import os

from pico2d import *

import game_framework
import title_state

from character import Character
from aim_pty import Aim
from map import Maps
from boss_moving import Boss

name = "MainState"



def enter():
    Character()
    Aim()
    Maps()
    Boss()
    pass


def exit():

    del (Character)
    del (Maps)
    del (Boss)
    del (Aim)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global toggle
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:          # 윈도우 창 x를 누르면 종료되게
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:    # 타이틀 상태에서 esc키를 누르면 타이틀로 넘어가게
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            Character().Up()
            toggle = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_j:
            Character().Down()
            toggle = 2

    pass

#
def update():
    Character().update()
    Maps().update()
    Boss().update()
    pass


def draw():
    global toggle

    clear_canvas()
    Maps().draw()

    if toggle == 1:
        Character().Up()
        toggle = 0

    elif toggle == 2:
        Character().Down()
        toggle = 0

    else:
        Character().draw()
    Boss().draw()
    Aim().draw()
    update_canvas()


    delay(0.1)
    pass





