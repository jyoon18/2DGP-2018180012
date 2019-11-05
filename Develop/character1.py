from pico2d import *
import game_framework

# character event

F_DOWN, J_DOWN = range(2)

key_event_table =\
    {
        (SDL_KEYDOWN, SDLK_f): F_DOWN,
        (SDL_KEYDOWN, SDLK_j): J_DOWN,
    }


class IdleState:
    @staticmethod
    def enter(character1, event):
        character1.toggle = 0

    @staticmethod
    def exit(character1, event):
        pass

    @staticmethod
    def do(character1):
        character1.x, character1.y = 90, 90
        character1.frame = (character1.frame + 1) % 4

    @staticmethod
    def draw(character1):
        character1.image.clip_draw(character1.frame * 160, 0, 160, 160, character1.x, character1.y)


class AttackState:
    @staticmethod
    def enter(character1, event):
        if event == F_DOWN:
            character1.toggle = 1
        elif event == J_DOWN:
            character1.toggle = 2

    @staticmethod
    def exit(character1, event):
        pass

    @staticmethod
    def do(character1):
        character1.frame = (character1.frame + 1) % 4

    @staticmethod
    def draw(character1):
        if character1.toggle == 1:
            character1.attack_image.draw(180, 200)
        elif character1.toggle == 2:
            character1.attack_image.draw(180, 90)
        else:
            character1.image.clip_draw(character1.frame * 160, 0, 160, 160, character1.x, character1.y)
        character1.toggle = 0



next_state_table = {
    IdleState: {F_DOWN: AttackState, J_DOWN: AttackState},
    AttackState: {F_DOWN: AttackState, J_DOWN: AttackState}
}


class Character1:
    def __init__(self):
        self.x, self.y = 90, 90
        self.frame = 0
        self.toggle = 0
        self.attack_image = load_image('used_image/up_attack.png')
        self.image = load_image('used_image/running1.png')
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

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


