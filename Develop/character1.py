from pico2d import *
import game_world
import Level1_state
from bullet import Bullet
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPPED_KMPH = 20.0
RUN_SPPED_MPM = (RUN_SPPED_KMPH * 1000.0 / 60.0)
RUN_SPPED_MPS = (RUN_SPPED_MPM / 60.0)
RUN_SPPED_PPS = (RUN_SPPED_MPS * PIXEL_PER_METER)

TIMER_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION
FRAME_PER_ACTION = 4
F_DOWN, J_DOWN, F_UP, J_UP, SPACE = range(5)

key_event_table =\
    {
        (SDL_KEYDOWN, SDLK_f): F_DOWN,
        (SDL_KEYDOWN, SDLK_j): J_DOWN,
        (SDL_KEYUP, SDLK_f): F_UP,
        (SDL_KEYUP, SDLK_j): J_UP,
        (SDL_KEYDOWN, SDLK_SPACE): SPACE
    }


class IdleState:
    @staticmethod
    def enter(character1, event):
        if event == F_DOWN:
            character1.x, character1.y = 180, 200
        elif event == J_DOWN:
            character1.x, character1.y = 180, 90

    @staticmethod
    def exit(character1, event):
        if event == SPACE:
            character1.fire()
        pass

    @staticmethod
    def do(character1):
        character1.x, character1.y = 90, 90
        character1.frame = (character1.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if Level1_state.checkk == 1:
            print("ouch")
        Level1_state.checkk = 0

    @staticmethod
    def draw(character1):
        if Level1_state.checkk == 1:
            character1.damaged_image.draw(character1.x, character1.y, 160, 160)
            character1.damage_effect.draw(640, 300, 1300, 640)

        else:
            character1.image.clip_draw(int(character1.frame) * 160, 0, 160, 160, character1.x, character1.y)
        character1.toggle = 0

class AttackState:
    @staticmethod
    def enter(character1, event):
        if event == F_DOWN:
            character1.toggle = 1
            character1.x, character1.y = 180, 200
        elif event == J_DOWN:
            character1.toggle = 2
            character1.x, character1.y = 180, 90

    @staticmethod
    def exit(character1, event):
        if event == SPACE:
            character1.fire()
        pass

    @staticmethod
    def do(character1):
        character1.frame = character1.frame = (character1.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        character1.x, character1.y = 90, 90

        if Level1_state.checkk == 1:
            print("ouch")
        Level1_state.checkk = 0

    @staticmethod
    def draw(character1):
        if Level1_state.checkk == 1:
            character1.damaged_image.draw(character1.x, character1.y, 160, 160)
            character1.damage_effect.draw(640, 300, 1300, 640)

        if character1.toggle == 1:
            character1.image.clip_draw(int(character1.frame) * 160, 0, 160, 160, character1.x, character1.y)
        elif character1.toggle == 2:
            character1.image.clip_draw(int(character1.frame) * 160, 0, 160, 160, character1.x, character1.y)
        else:
            character1.image.clip_draw(int(character1.frame) * 160, 0, 160, 160, character1.x, character1.y)
        character1.toggle = 0

next_state_table = {
    IdleState: {F_DOWN: AttackState, J_DOWN: AttackState, F_UP: AttackState, J_UP: AttackState, SPACE: IdleState},
    AttackState: {F_DOWN: IdleState, J_DOWN: IdleState, F_UP: IdleState, J_UP: IdleState, SPACE: IdleState},
}


class Character1:
    def __init__(self):
        self.x, self.y = 90, 90
        self.frame = 0
        self.velocity = 5
        self.toggle = 0
        self.attack_image = load_image('used_image/up_attack.png')
        self.image = load_image('used_image/running1.png')
        self.damaged_image = load_image('used_image/character1_hit_by_jelly.png')
        self.damage_effect = load_image('used_image/damaged_screen_effect.png')
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire(self):
        bullet = Bullet(self.x, self.y, self.velocity)
        game_world.add_object(bullet, 1)
        if bullet.x > 1050:
            print(bullet.x)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40


