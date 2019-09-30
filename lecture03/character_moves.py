from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=90
y=90
gak=0

while True:
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x+=20
        delay(0.01)
    

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(798,y)
        y+=2
        delay(0.01)

    while(x>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,598)
        x-=2
        delay(0.01)

    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(90,y)
        y-=2
        delay(0.01)

    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x+=2
        delay(0.01)

    
    while(gak<270):
        x=400
        y=300
        clear_canvas_now()
        grass.draw_now(400,30)
        x=x+200*math.cos(gak/360*2*math.pi)
        y=y+200*math.sin(gak/360*2*math.pi)
        character.draw_now(x,y)
        gak+=2
        delay(0.01)

close_canvas()

