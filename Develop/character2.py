from pico2d import *
import game_framework

# character event

F_DOWN, J_DOWN = range(2)

key_event_table =\
    {
        (SDL_KEYDOWN, SDLK_f): F_DOWN,
        (SDL_KEYDOWN, SDLK_j): J_DOWN
    }


class IdleState:
    @staticmethod
    def enter(character2, event):
        character2.toggle = 0

    @staticmethod
    def exit(character2, event):
        pass

    @staticmethod
    def do(character2):
        character2.x, character2.y = 90, 160
        character2.frame = (character2.frame + 1) % 8

    @staticmethod
    def draw(character2):
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
    IdleState: {F_DOWN: AttackState, J_DOWN: AttackState},
    AttackState: {F_DOWN: AttackState, J_DOWN: AttackState}
}


class Character2:
    def __init__(self):
        self.x, self.y = 90, 160
        self.frame = 0
        self.attack_image = load_image('used_image/character2_up_attack.png')
        self.image = load_image('used_image/character02_4.png')
        self.damaged_image = load_image('used_image/character2_hit_by_jelly2.png')
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

