
from pico2d import *

import game_framework
import game_world
import title_state
import success_state_Lv1
import character_select_state

from character1 import Character1
from character2 import Character2
from aim_pty import Aim_Up
from aim_pty import Aim_Down
from map import Level1_Map
from boss_moving import Boss

from jelly_level1 import Small_Jelly_lv1
from jelly_level1 import Big_Jelly_lv1
from life import Life
import failure_state
name = "Level1_state"

character1 = None
character2 = None
aims = None
maps = None
boss_character = None
hit = None

Bjelly = None
Sjelly = None

level1_total_time = None

checkk = 0

def enter():
    global character1, character2, aim_up, aim_down, maps, boss_character, Bjelly, Sjelly, life
    global jelly
    global life_location, checkk

    character1 = Character1()
    character2 = Character2()
    aim_up = Aim_Up()
    aim_down = Aim_Down()
    maps = Level1_Map()
    boss_character = Boss()
    Bjelly = Big_Jelly_lv1()
    Sjelly = Small_Jelly_lv1()
    life = Life()

    game_world.add_object(maps, 0)
    game_world.add_object(aim_up, 0)
    game_world.add_object(aim_down, 0)

    if character_select_state.character_select_number == 1:
        game_world.add_object(character1, 1)
    elif character_select_state.character_select_number == 2:
        game_world.add_object(character2, 1)

    game_world.add_object(boss_character, 1)

    jelly = [Small_Jelly_lv1() for i in range(10)] + [Big_Jelly_lv1() for n in range(1)]
    game_world.add_objects(jelly, 1)

    life_location = [Life() for k in range(5)]
    for l in range(5):
        life_location[l].x = life.x
        life.x += 65
    game_world.add_objects(life_location, 0)
    checkk = 0

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
        else: #event.type == SDL_KEYDOWN and (event.key == SDLK_f or event.key == SDLK_j or event.key == SDLK_SPACE):
            if character_select_state.character_select_number == 1:
                character1.handle_event(event)
            elif character_select_state.character_select_number == 2:
                character2.handle_event(event)


def update():
    global character1, character2, Sjelly, Bjelly
    global level1_total_time, damaged_effect, checkk

    for game_object in game_world.all_objects():
        game_object.update()

    #for Sjelly in jelly:
        #if collide(aim_up, Sjelly):
         #   print("으악")
        #if collide(aim_down, Sjelly):
         #   print("으악")

    #for Bjelly in jelly:
        #if collide(aim_up, Bjelly):
         #   print("으윽")
        #if collide(aim_down, Bjelly):
         #   print("으윽")


    for Sjelly in jelly:
        if character_select_state.character_select_number == 1:
            if collide(character1, Sjelly):
                Sjelly.disappear()
        elif character_select_state.character_select_number == 2:
            if collide(character2, Sjelly):
                Sjelly.disappear()
        if Sjelly.x < 171:
            for l in life_location:
                life_location.remove(l)
                game_world.remove_object(l)
                checkk = 1
                if len(life_location) == 0:
                    game_framework.change_state(failure_state)
                break

    for Bjelly in jelly:
        if character_select_state.character_select_number == 1:
            if collide(character1, Bjelly):
                Bjelly.disappear()

        elif character_select_state.character_select_number == 2:
            if collide(character2, Bjelly):
                Bjelly.disappear()

        if Bjelly.x < 171:
            for l in life_location:
                life_location.remove(l)
                game_world.remove_object(l)
                checkk = 1
                if len(life_location) == 0:
                    game_framework.change_state(failure_state)
                break

    level1_total_time = pico2d.get_time() - character_select_state.character_state_total_time
    if level1_total_time > 30:
        game_framework.change_state(success_state_Lv1)

def draw():
    global level1_total_time, damaged_effect

    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    level1_total_time = pico2d.get_time() - character_select_state.character_state_total_time
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