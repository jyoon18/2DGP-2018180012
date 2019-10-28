import game_framework
import pico2d

import start_state


pico2d.open_canvas()        # 피코투디로 캔버스를 열어준다
game_framework.run(start_state)     # start_state 상태로 game_framework가 돌아가게 해준다
                                    # 그럼 start_state -> title_state-> main_state상태로 접어들고 main_state에서 pause이벤트가 일어나게 해줌
pico2d.close_canvas()
