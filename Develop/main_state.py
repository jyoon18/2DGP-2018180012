import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state

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
    global toggle
    toggle = 0
    def __init__(self):
        self.x, self.y = 90, 90
        self.frame = 0
        self.attack_image = load_image('up_attack.png')
        self.image = load_image('running1.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)

    def Up(self):
        self.attack_image.draw(180, 200)

    def Down(self):

        self.attack_image.draw(180, 90)


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
    character.update()
    maps.update()
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

    update_canvas()


    delay(0.1)
    pass





