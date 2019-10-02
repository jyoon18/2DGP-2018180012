from pico2d import *
open_canvas(1280,600)
grass = load_image('map04_1.png')
character = load_image('running1.png')

#MAP_WIDTH, MAP_HEIGHT = 800, 315

frame=0
x=800

#x, y = MAP_WIDTH, MAP_HEIGHT

while(x<1600):
    clear_canvas()
    grass.draw(x,300)
    character.clip_draw(frame*160,0,160,160,90,90)
    update_canvas()
    frame = (frame + 1) % 4
    x-=2
    delay(0.08)
    get_events()

while(x>0):
    clear_canvas()
    grass.draw(x, 300)
    character.clip_draw(frame*160,0,160,160,90,90)
    update_canvas()
    frame = (frame + 1) % 4
    x += 2
    delay(0.08)
    get_events()

#while (xlen < 1600):
 #   clear_canvas()


close_canvas()

