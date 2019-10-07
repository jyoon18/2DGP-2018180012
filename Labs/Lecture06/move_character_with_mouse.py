from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global x2, y2
    global x3, y3
    global toggle

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            toggle = 1
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x2, y2 = event.x - 25, KPU_HEIGHT - 1 - event.y + 25
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x3, y3 = KPU_WIDTH // 2, KPU_HEIGHT // 2
d=3
x2=x3
y2=y3
frame = 0
hide_cursor()

while running:
    xrun = (x2 - x3)/20
    yrun = (y2 - y3)/20
    x3+=xrun
    y3+=yrun
    if x2-x3<0:
        d=0
    elif(x2-x3>0):
        d=1
    elif(x2-x3==0):
        d=3

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(x, y)
    character.clip_draw(frame*100,100*d,100,100,x3,y3)
    frame = (frame + 1) % 8

    update_canvas()
    delay(0.07)
    handle_events()



close_canvas()




