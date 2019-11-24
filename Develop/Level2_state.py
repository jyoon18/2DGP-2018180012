
from pico2d import *

import game_framework
import game_world
import title_state
import character_select_state
import failure_state
import success_state_Lv2
import random
from bullet import Bullet
from character1 import Character1
from character2 import Character2
from aim_pty import Aim_Up
from aim_pty import Aim_Down
from map import Level2_Map
from boss_moving import Level2_Boss

from jelly_level2 import Small_Jelly_lv2
from jelly_level2 import Big_Jelly_lv2
from life import Life
name = "Level2_state"

character1 = None
character2 = None
maps = None
boss_character = None

Bjelly = None
Sjelly = None

level2_state_check = 1

def enter():
    global character1, character2, aim_up, aim_down, maps, boss_character, Bjelly, Sjelly, life
    global small_jelly, big_jelly
    global life_location, checkk, bullet

    character1 = Character1()
    character2 = Character2()
    aim_up = Aim_Up()
    aim_down = Aim_Down()
    maps = Level2_Map()
    boss_character = Level2_Boss()
    Bjelly = Big_Jelly_lv2()
    Sjelly = Small_Jelly_lv2()
    life = Life()
    bullet = Bullet()

    game_world.add_object(maps, 0)
    game_world.add_object(aim_up, 0)
    game_world.add_object(aim_down, 0)

    if character_select_state.character_select_number == 1:
        game_world.add_object(character1, 1)
    elif character_select_state.character_select_number == 2:
        game_world.add_object(character2, 1)

    game_world.add_object(boss_character, 1)

    small_jelly = [Small_Jelly_lv2() for i in range(15)]
    big_jelly = [Big_Jelly_lv2() for n in range(10)]

    for o in range(15):
        small_jelly[o].x = Sjelly.x
        Sjelly.x += random.randint(70, 75)
    game_world.add_objects(small_jelly, 1)

    for k in range(10):
        big_jelly[k].x = Bjelly.x
        Bjelly.x += random.randint(60, 65)

    life_location = [Life() for k in range(5)]
    for l in range(5):
        life_location[l].x = life.x
        life.x += 65
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
        else:
            if character_select_state.character_select_number == 1:
                character1.handle_event(event)
            elif character_select_state.character_select_number == 2:
                character2.handle_event(event)


def update():
    global character1, character2, Sjelly, Bjelly
    global level2_total_time, small_jelly, big_jelly

    for game_object in game_world.all_objects():
        game_object.update()

    for Sjelly in small_jelly:
        if character_select_state.character_select_number == 1:
            if collide(character1, Sjelly):
                Sjelly.disappear()

        elif character_select_state.character_select_number == 2:
            if collide(character2, Sjelly):
                Sjelly.disappear()

        if Sjelly.x < 180:
            for l in life_location:
                life_location.remove(l)
                game_world.remove_object(l)
                if len(life_location) == 0:
                    game_framework.change_state(failure_state)
                break



    for Bjelly in big_jelly:
        if character_select_state.character_select_number == 1:
            if collide(character1, Bjelly):
                Bjelly.disappear()

        elif character_select_state.character_select_number == 2:
            if collide(character2, Sjelly):
                Bjelly.disappear()

        if Bjelly.x < 170:
            for l in life_location:
                life_location.remove(l)
                game_world.remove_object(l)
                if len(life_location) == 0:
                    game_framework.change_state(failure_state)
                break

    if bullet.x > 600:
        print("over")

def draw():
    global level2_total_time
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

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
