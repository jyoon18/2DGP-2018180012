from pico2d import *

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
    global character
    character = Character()

def exit():
    global character
    del character

def update():
    global character
    character.update()

def draw():
    global character
    character.draw()

def Up():
    global character
    character.Up()

def Down():
    global character
    character.Down()