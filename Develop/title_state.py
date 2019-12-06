import game_framework               # game_framework와 main_state를 받아온다
from pico2d import *
import character_select_state
import start_state
from map import Level3_Map
from map import Level2_Map
from map import Level1_Map

name = "TitleState"
image = None
title_state_total_time = None

# title_state상태에 접어들 때, 맨 처음 해줄 것들을 초기화 하는 함수
# title의 이미지를 보여줌
def enter():
    global image
    image = load_image('used_image/title.png')

    global lv1, lv2, lv3
    lv1 = Level1_Map()
    lv2 = Level2_Map()
    lv3 = Level3_Map()

    lv1.bgm.stop()
    lv2.bgm.stop()
    lv3.bgm.stop()
    pass

# 게임을 종료할 때, image를 삭제해줌
def exit():
    global image
    global lv1, lv2, lv3
    del image
    del lv1
    del lv2
    del lv3
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
                game_framework.change_state(character_select_state)
    pass
def draw():
    global title_state_total_time
    clear_canvas()
    image.draw(640, 300)         # 메인화면을 그려라!
    title_state_total_time = pico2d.get_time() - start_state.start_state_total_time
    #print("타이틀에서 넘어가는 시간: ", title_state_total_time)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






