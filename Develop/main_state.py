import random
import json
import os

from pico2d import *

import game_framework
import title_state

from character1 import Character1
from character2 import Character2
from aim_pty import Aim
from map import Maps
from boss_moving import Boss

from jelly import Small_Jelly_lv1
from jelly import Big_Jelly_lv1

name = "MainState"

charac = None
aims = None
maps = None
bosses = None

Bjelly = None
Sjelly = None

toggle = 0

def enter():
    global charac2, aims, maps, bosses, Bjelly, Sjelly
    charac2 = Character2()
    aims = Aim()
    maps = Maps()
    bosses = Boss()

    Bjelly = Big_Jelly_lv1()
    Sjelly = Small_Jelly_lv1()
    pass


def exit():
    global charac2, aims, maps, bosses
    global Bjelly, Sjelly

    del (charac2)
    del (maps)
    del (bosses)
    del (aims)

    del Bjelly
    del Sjelly
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
            charac2.Up()
            toggle = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_j:
            charac2.Down()
            toggle = 2
    pass


def update():
    global charac2, aims, maps, bosses
    global Bjelly, Sjelly

    charac2.update()
    maps.update()
    bosses.update()

    Bjelly.update()
    Sjelly.update()
    pass

def draw():
    global toggle

    clear_canvas()
    maps.draw()

    if toggle == 1:
        charac2.Up()
        toggle = 0
    elif toggle == 2:
        charac2.Down()
        toggle = 0
    else:
        charac2.draw()

    Sjelly.draw()
    Bjelly.draw()
    bosses.draw()
    aims.draw()
    update_canvas()


    delay(0.1)
    pass





