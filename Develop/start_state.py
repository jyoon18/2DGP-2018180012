import game_framework               # game_framework를 import함
import title_state                  # title_state를 쓰기위해 import함
from pico2d import *

# 초기화 시켜줌
name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('kpu_credit.png')
    pass

# 게임 상태에서 나갈 때 종료화
# image를 삭제시켜줌
def exit():
    global image
    del(image)
    pass

# 게임을 갱신시켜줌
# 여기서는 맨 처음 로고 화면을 1초 동안 보여줬다가 title_state로 넘어가게 해놨음
def update():
    global logo_time

    if(logo_time>1.0):          # 로고 타임이 1 이상이 되면
        logo_time = 0
        game_framework.change_state(title_state)    # import한 title_state로 게임의 상태를 완전히 바꿔줌
    delay(0.01)
    logo_time += 0.01           # 그게 아니라면 계속 로고화면을 보여주기 위한 시간을 0.01초 씩 늘려준당당
    pass


def draw():
    global image           # kpu_credit을 보여줌
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




