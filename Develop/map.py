from pico2d import *
import game_framework

class Ready:
    def __init__(self):
        self.tbgm = load_music('title_character.mp3')
        self.tbgm.set_volume(64)
        self.tbgm.repeat_play()

class Level1_Map:
    def __init__(self):
        self.image = load_image('used_image/map03_3.png')
        self.image2 = load_image('used_image/map03_3.png')
        self.x, self.y = 640, 300
        self.x2, self.y2 = 1920, 300
        self.frame = 0
        self.velocity = 100
        self.bgm = load_music('Level1.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.sbgm = load_wav('trumpet1.wav')
        self.sbgm.set_volume(64)
        self.fbgm = load_wav('fate2.wav')
        self.fbgm.set_volume(64)

    def update(self):
        self.x -= self.velocity * game_framework.frame_time
        self.x2 -= self.velocity * game_framework.frame_time
        if self.x <= -640:
            self.x = 1920
        if self.x2 <= -640:
            self.x2 = 1920
    def draw(self):
        self.image.draw(self.x, self.y)
        self.image2.draw(self.x2, self.y2)


class Level2_Map:
    def __init__(self):
        self.image = load_image('used_image/map02_4.png')
        self.image2 = load_image('used_image/map02_4.png')

        self.x, self.y = 640, 300
        self.x2, self.y2 = 1920, 300
        self.frame = 0
        self.velocity = 100

        self.bgm = load_music('Level2.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.sbgm = load_wav('trumpet1.wav')
        self.sbgm.set_volume(64)
        self.fbgm = load_wav('fate2.wav')
        self.fbgm.set_volume(64)

    def update(self):
        self.x -= self.velocity * game_framework.frame_time
        self.x2 -= self.velocity * game_framework.frame_time
        if self.x < -640:
            self.x = 1920
        if self.x2 <= -640:
            self.x2 = 1920

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image2.draw(self.x2, self.y2)


class Level3_Map:
    def __init__(self):
        self.image = load_image('used_image/map04.png')
        self.image2 = load_image('used_image/map04.png')
        self.x, self.y = 640, 300
        self.x2, self.y2 = 1920, 300
        self.frame = 0
        self.velocity = 100

        self.bgm = load_music('Level3.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.sbgm = load_wav('clap.wav')
        self.sbgm.set_volume(64)
        self.fbgm = load_wav('fate2.wav')
        self.fbgm.set_volume(64)

    def update(self):
        self.x -= self.velocity * game_framework.frame_time
        self.x2 -= self.velocity * game_framework.frame_time
        if self.x <= -640:
            self.x = 1920
        if self.x2 <= -640:
            self.x2 = 1920

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image2.draw(self.x2, self.y2)
