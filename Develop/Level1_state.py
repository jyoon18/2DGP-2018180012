
from pico2d import *

import game_framework
import game_world
import title_state

from character1 import Character1
from character2 import Character2
from aim_pty import Aim_Up
from aim_pty import Aim_Down
from map import Maps
from boss_moving import Boss

from jelly_level1 import Small_Jelly_lv1
from jelly_level1 import Big_Jelly_lv1
from jelly_level2 import Small_Jelly_lv2
from jelly_level2 import Big_Jelly_lv2
from life import Life

name = "MainState"

character1 = None
character2 = None
aims = None
maps = None
boss_character = None

Bjelly = None
Sjelly = None

def enter():
    global character1, character2, aim_up, aim_down, maps, boss_character, Bjelly, Sjelly, life
    global jelly
    global life_location

    character1 = Character1()
    character2 = Character2()
    aim_up = Aim_Up()
    aim_down = Aim_Down()
    maps = Maps()
    boss_character = Boss()
    Bjelly = Big_Jelly_lv1()
    Sjelly = Small_Jelly_lv1()
    life = Life()

    game_world.add_object(maps, 0)
    game_world.add_object(aim_up, 0)
    game_world.add_object(aim_down, 0)
    game_world.add_object(character2, 1)
    game_world.add_object(boss_character, 1)

    jelly = [Small_Jelly_lv1() for i in range(10)] + [Big_Jelly_lv1() for n in range(2)]
    game_world.add_objects(jelly, 1)

    life_location = [Life() for k in range(5)]
    game_world.add_objects(life_location, 0)

def exit():
    game_world.clear()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_f or event.key == SDLK_j):
            character2.handle_event(event)

    pass


def update():
    global character2
    global life_location
    for game_object in game_world.all_objects():
        game_object.update()

    for Sjelly in jelly:
        if collide(aim_up, Sjelly):
            print("으악")
        if collide(aim_down, Sjelly):
            print("으악")

    for Bjelly in jelly:
        if collide(aim_up, Bjelly):
            print("으윽")
        if collide(aim_down, Bjelly):
            print("으윽")


    for Sjelly in jelly:
        if collide(character2, Sjelly):
            print("체크쳋크")
            Sjelly.disappear()

        if not collide(character2, Sjelly) and Sjelly.x < 180:
            print("키입력이 없었어요~")
            for life in life_location:
                life_location.remove(life)
                game_world.remove_object(life)

    for Bjelly in jelly:
        if collide(character2, Bjelly):
            print("체크체크")
            Bjelly.disappear()

        if not collide(character2, Bjelly) and Bjelly.x < 180:
            print("키입력이 없었어요~")
            for life in life_location:
                life_location.remove(life)
                game_world.remove_object(life)





def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

    delay(0.1)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True




