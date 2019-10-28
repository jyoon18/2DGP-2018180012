class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw



class TestGameState:

    def __init__(self, name):
        self.name = name

    def enter(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def resume(self):
        print("State [%s] Resumed" % self.name)

    def handle_events(self):
        print("State [%s] handle_events" % self.name)

    def update(self):
        print("State [%s] update" % self.name)

    def draw(self):
        print("State [%s] draw" % self.name)



running = None
stack = None


def change_state(state):
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function         # 현재 상태를 삭제
        stack[-1].exit()
        # remove the current state
        stack.pop()
    stack.append(state)                             # 새로운 state를 추가해주고
    state.enter()                                   # state의 enter로 진입시켜준다



def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()                   # 현재 상태를 저장하고 새로운 상태로 넘어간다
    stack.append(state)                     # push_state는 전에 있는 상태가 남아있는 그런 함수임
    state.enter()



def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()



def quit():
    global running
    running = False


def run(start_state):
    global running, stack
    running = True
    stack = [start_state]               # start_state를 담고 있는 스택을 생성시킨다
    start_state.enter()
    while (running):
        stack[-1].handle_events()       # 현재 상태에대한 게임 루프를 진행시킵니다
        stack[-1].update()
        stack[-1].draw()
    # repeatedly delete the top of the stack
    while (len(stack) > 0):             # 스택의 가장 위부터 지워줍니다 stack이 0값보다 크면
        stack[-1].exit()
        stack.pop()


def test_game_framework():
    start_state = TestGameState('StartState')
    run(start_state)



if __name__ == '__main__':
    test_game_framework()