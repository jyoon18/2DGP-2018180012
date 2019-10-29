import game_framework
import pico2d

import start_state


pico2d.open_canvas(1280, 600)        # 피코투디로 캔버스를 열어준다
game_framework.run(start_state)     # start_state 상태로 game_framework가 돌아가게 해준다

pico2d.close_canvas()
