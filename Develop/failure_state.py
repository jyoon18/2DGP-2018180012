import game_framework               # game_framework와 main_state를 받아온다
from pico2d import *
import character_select_state


name = "TitleState"
image = None

# title_state상태에 접어들 때, 맨 처음 해줄 것들을 초기화 하는 함수
# title의 이미지를 보여줌
def enter():
    global image
    image = load_image('used_image/.png')
    pass

# 게임을 종료할 때, image를 삭제해줌
def exit():
    global image
    del(image)
    pass

# 사용자 입력을 받아오는 함수
# 사용자가 window창의 종료 버튼을 눌렀을 때는 아예 game_framework가 끝나게 함, 게임자체가 끝나게
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(character_select_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass

def draw():
    clear_canvas()
    image.draw(640,300)         # 메인화면을 그려라!
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






