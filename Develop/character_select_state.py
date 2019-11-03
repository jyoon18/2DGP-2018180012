from pico2d import *

import game_framework
import main_state


image = None
character1 = None
character2 = None

class Select1:
    def __init__(self):
        self.x, self.y = 400, 200
        self.frame = 0
        self.image = load_image('used_image/character1_select_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 168, 0 , 160, 160, self.x, self.y)

class Select2:
    def __init__(self):
        self.x, self.y = 800, 300
        self.frame = 0
        self.image = load_image('used_image/character2_select_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 363, 0, 363, 363, self.x, self.y)


def enter():
    global image, character1, character2
    image = load_image('used_image/character_select_window.png')
    character1 = Select1()
    character2 = Select2()

def exit():
    global image, character1, character2
    del image
    del character1
    del character2


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

def update():
    global character1, character2
    character1.update()
    character2.update()
    pass

def draw():
    clear_canvas()
    image.draw(640,300)

    character1.draw()
    character2.draw()


    update_canvas()
    delay(0.1)
    pass





def pause():
    pass


def resume():
    pass


