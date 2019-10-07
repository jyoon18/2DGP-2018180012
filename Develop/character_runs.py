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
toggle = True
state = 4


while (x>-800):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            jump = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_f:
                toggle = False

    clear_canvas()
    grass.draw(x,300)

    if(state == 4):
        for pos in [940,1040,1140,1240]:
            heart.draw(pos,550)

    if toggle == False:
        y=250
        jump.draw(90,y)
        #delay(0.1)
        toggle=True
    elif (toggle == True):
        ypos = 200
        judge_height = 2
        character.clip_draw(frame * 160, 0, 160, 160, 90, 90)
        frame = (frame + 1) % 4
    boss.clip_draw(frame_boss * 316, 0, 290, 230, 950, ypos)
    frame_boss = (frame_boss + 1) % 3


    update_canvas()
    x-=2
    get_events()
    delay(0.1)



close_canvas()
