from pico2d import *

import game_framework
import main_state


image = None

def enter():
    global image
    image = load_image('character_select_window.png')


def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                game_framework.change_state(main_state)

def draw():
    clear_canvas()
    image.draw(640,300)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass


