import game_framework               # game_framework와 main_state를 받아온다
import main_state
from pico2d import *


name = "TitleState"
image = None

# title_state상태에 접어들 때, 맨 처음 해줄 것들을 초기화 하는 함수
# title의 이미지를 보여줌
def enter():
    global image
    image = load_image('title.png')
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
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):            # title화면이었을 때도 esc키를 눌렀을 때도 게임이 끝나게 설정
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):           # space키를 누르면 main_state로 넘겨줌
                game_framework.change_state(main_state)
    pass
def draw():
    clear_canvas()
    image.draw(400,300)         # 메인화면을 그려라!
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






