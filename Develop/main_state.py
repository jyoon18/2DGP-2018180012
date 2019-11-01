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

charac = None
aims = None
maps = None
bosses = None

def enter():
    global charac, aims, maps, bosses
    charac = Character()
    aims = Aim()
    maps = Maps()
    bosses = Boss()
    pass


def exit():
    global charac, aims, maps, bosses

    del (charac)
    del (maps)
    del (bosses)
    del (aims)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global toggle
    toggle = 0
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:          # 윈도우 창 x를 누르면 종료되게
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:    # 타이틀 상태에서 esc키를 누르면 타이틀로 넘어가게
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            charac.Up()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_j:
            charac.Down()

    pass


def update():
    global charac, aims, maps, bosses

    charac.update()
    maps.update()
    bosses.update()
    pass


def draw():
    global toggle
    toggle = 0

    clear_canvas()
    maps.draw()

    
    charac.draw()

    bosses.draw()
    aims.draw()
    update_canvas()


    delay(0.1)
    pass





