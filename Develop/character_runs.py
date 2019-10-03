from pico2d import *
open_canvas(1280,600)
grass = load_image('map03_3.png')
character = load_image('running1.png')

frame=0
x=800
toggle = True

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
    if toggle == False:
        y=250
        character.clip_draw(frame * 160, 0, 160, 160, 90, y)
        frame = (frame + 1) % 4
        toggle=True
    elif (toggle == True):
        character.clip_draw(frame * 160, 0, 160, 160, 90, 90)
        frame = (frame + 1) % 4
    update_canvas()
    x-=2
    get_events()
    delay(0.1)



close_canvas()
