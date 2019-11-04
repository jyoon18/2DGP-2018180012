import random
import json
import os

from pico2d import *

import game_framework
import game_world
import title_state

from character1 import Character1
from character2 import Character2
from aim_pty import Aim
from map import Maps
from boss_moving import Boss

from jelly import Small_Jelly_lv1
from jelly import Big_Jelly_lv1

name = "MainState"

character1 = None
character2 = None
aims = None
maps = None
bosses = None

Bjelly = None
Sjelly = None

up_attack_decision = 0

def enter():
    global character2, aims, maps, bosses, Bjelly, Sjelly
    character2 = Character2()
    aims = Aim()
    maps = Maps()
    bosses = Boss()

    Bjelly = Big_Jelly_lv1()
    Sjelly = Small_Jelly_lv1()

    game_world.add_object(maps, 0)
    game_world.add_object(aims, 0)
    game_world.add_object(character2, 1)
    game_world.add_object(bosses, 1)
    game_world.add_object(Bjelly, 1)
    game_world.add_object(Sjelly, 1)
    pass

def exit():
    #global character_, aims, maps, bosses
    #global Bjelly, Sjelly
    #del character_
    #del maps
    #del bosses
    #del aims
    #del Bjelly
    #del Sjelly

    game_world.clear()
    pass


def handle_events():
    global up_attack_decision

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:          # 윈도우 창 x를 누르면 종료되게
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:    # 타이틀 상태에서 esc키를 누르면 타이틀로 넘어가게
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_f or event.key == SDLK_j):
            character2.handle_event(event)

    pass


def update():
    #global character_, aims, maps, bosses
    #global Bjelly, Sjelly
    #character_.update()
    #maps.update()
    #bosses.update()
    #Bjelly.update()
    #Sjelly.update()

    for game_object in game_world.all_objects():
        game_object.update()
    pass

def draw():
    global up_attack_decision

    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

    delay(0.1)

    pass





