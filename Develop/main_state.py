import random
import json
import os

from pico2d import *

import game_framework
import title_state

import character
import aim_pty
import map
import boss_moving

name = "MainState"

Character = None
maps = None
boss = None
aim = None


def enter():

    pass


def exit():
    global Character, maps, boss, aim
    del(Character)
    del(maps)
    del(boss)
    del(aim)
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
            character.Up()
            toggle = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_j:
            character.Down()
            toggle = 2

    pass

#
def update():
    global Character, maps, boss
    character.update()
    maps.update()
    boss.update()
    pass


def draw():
    global toggle

    clear_canvas()
    maps.draw()

    if toggle == 1:
        character.Up()
        toggle = 0

    elif toggle == 2:
        character.Down()
        toggle = 0

    else:
        character.draw()
    boss.draw()
    aim.draw()
    update_canvas()


    delay(0.1)
    pass





