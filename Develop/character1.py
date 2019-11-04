from pico2d import *
import game_framework
import game_world

# character event

F_DOWN, F_UP, J_DOWN, J_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_f): F_DOWN,
    (SDL_KEYUP, SDLK_f): F_UP,
    (SDL_KEYDOWN, SDLK_j): J_DOWN,
    (SDL_KEYUP, SDLK_j): J_UP
}

class IdleState:
    @staticmethod
    def enter(character1, event):
        if event == F_DOWN:
            character1.toggle = 1
        elif event == J_DOWN:
            character1.toggle = 2
        elif event == F_UP:
            character1.toggle = 0
        elif event == J_UP:
            character1.toggle = 0

    @staticmethod
    def exit(character1, event):
        pass

    @staticmethod
    def do(character1):
        character1.frame = (character1.frame + 1) % 4

    @staticmethod
    def draw(character1):
        if character1.toggle == 1:
            character1.attack_image(180, 200)
        elif character1.toggle == 2:
            character1.attack_image(180, 90)
        else:
            character1.image.clip_draw(character1.frame * 160, 0, 160, 160, character1.x, character1.y)

class AttackState:
    @staticmethod
    def enter(character1, event):
        if event == F_DOWN:
            character1.toggle = 1
        elif event == J_DOWN:
            character1.toggle = 2
        elif event == F_UP:
            character1.toggle = 0
        elif event == J_UP:
            character1.toggle = 0
    @staticmethod
    def exit(character1, event):
        character1.frame = (character1.frame + 1) % 4
        pass

    @staticmethod
    def do(character1):
        pass

    @staticmethod
    def draw(character1):
        if character1.toggle == 1:
            character1.attack_image(180, 200)
        elif character1.toggle == 2:
            character1.attack_image(180, 90)
        else:
            character1.image.clip_draw(character1.frame * 160, 0, 160, 160, character1.x, character1.y)


next_state_table = {
    IdleState: {F_UP: AttackState, F_DOWN: AttackState,
                J_UP: AttackState, J_DOWN: AttackState},

    AttackState: {F_UP: IdleState, F_DOWN: IdleState,
                  J_UP: IdleState, J_DOWN: IdleState}
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

    def Up(self):
        self.attack_image.draw(180, 200)

    def Down(self):
        self.attack_image.draw(180, 90)


