from pico2d import *
open_canvas(1280,600)
grass = load_image('map03_3.png')
character = load_image('running1.png')
heart = load_image('heart2.png')
jump = load_image('up_attack.png')
boss = load_image('boss.png')

frame=0
frame_boss = 0
x=800

def get_event():
    global toggle
    global toggle_j
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            jump = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_f:
                toggle = False
            elif event.key == SDLK_j:
                toggle_j = False


def moving_grass():
    global frame_grass
    frame_grass = 0
    grass.clip_draw(frame_grass*100,0,1600,630,x,300)
    frame_grass = (frame_grass + 1)%8

def heart_display():
    global state
    state =4
    if (state == 4):
        for pos in [940, 1040, 1140, 1240]:
            heart.draw(pos, 550)


#
toggle = True
toggle_j = True

while (x>-800):

    get_events()

    clear_canvas()
    moving_grass()
    x -=1
    heart_display()
    boss.clip_draw(frame_boss * 316, 0, 290, 230, 1050, 200)
    frame_boss = (frame_boss + 1) % 3


    if toggle == False:
        y = 200
        jump.draw(150,y)
        y = 200 + 200 * math.sin(1*math.pi)
        toggle=True
    elif toggle_j == False:
        jump.draw(150, 90)
        toggle_j = True
    elif (toggle == True):
        judge_height = 2
        character.clip_draw(frame * 160, 0, 160, 160, 90, 90)
        frame = (frame + 1) % 4


    update_canvas()

    delay(0.1)

close_canvas()
