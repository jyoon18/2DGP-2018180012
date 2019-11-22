from pico2d import *
import game_world
import Level1_state
from bullet import Bullet
# character event

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
    def enter(character2, event):
        if event == F_DOWN:
            character2.toggle = 1
            character2.x, character2.y = 180, 320
        elif event == J_DOWN:
            character2.toggle = 2
            character2.x, character2.y = 180, 160

    @staticmethod
    def exit(character2, event):
        pass

    @staticmethod
    def do(character2):
        character2.x, character2.y = 90, 160
        character2.frame = (character2.frame + 1) % 8

        if Level1_state.checkk == 1:
            print("ouch")
        Level1_state.checkk = 0

    @staticmethod
    def draw(character2):
        if Level1_state.checkk == 1:
            character2.damaged_image.draw(character2.x, character2.y)
            character2.damage_effect.draw(640, 300, 1300, 640)
            delay(0.05)
        else:
            character2.image.clip_draw(character2.frame * 320, 0, 320, 320, character2.x, character2.y)


class AttackState:
    @staticmethod
    def enter(character2, event):
        if event == F_DOWN:
            character2.toggle = 1
            character2.x, character2.y = 180, 320

        elif event == J_DOWN:
            character2.toggle = 2
            character2.x, character2.y = 180, 160


    @staticmethod
    def exit(character2, event):
        pass

    @staticmethod
    def do(character2):
       character2.frame = (character2.frame + 1) % 8
       character2.x, character2.y = 90, 160


    @staticmethod
    def draw(character2):
        if character2.toggle == 1:
            character2.attack_image.draw(character2.x, character2.y)
        elif character2.toggle == 2:
            character2.attack_image.draw(character2.x, character2.y)
        else:
            character2.image.clip_draw(character2.frame * 320, 0, 320, 320, character2.x, character2.y)
        character2.toggle = 0



next_state_table = {
    IdleState: {F_DOWN: AttackState, J_DOWN: AttackState, F_UP: AttackState, J_UP: AttackState},
    AttackState: {F_DOWN: IdleState, J_DOWN: IdleState, F_UP: IdleState, J_UP: IdleState}
}


class Character2:
    def __init__(self):
        self.x, self.y = 90, 160
        self.frame = 0
        self.attack_image = load_image('used_image/character2_up_attack.png')
        self.image = load_image('used_image/character02_4.png')
        self.damaged_image = load_image('used_image/character2_hit_by_jelly2.png')
        self.damage_effect = load_image('used_image/damaged_screen_effect.png')
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

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
        return self.x - 40, self.y - 140, self.x + 40, self.y - 40

    def get_damage(self):
        self.damaged_image.draw(self.x, self.y)


