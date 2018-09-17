from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_direct1():
    x, y = 203, 535
    x1, y1 = 203, 535
    x2, y2 = 132, 243
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        delay(0.1)

def move_direct2():
    x, y = 132, 243
    x1, y1 = 132, 243
    x2, y2 = 535, 470
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1


    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        delay(0.1)

def move_direct3():
    x, y = 535, 470
    x1, y1 = 535, 470
    x2, y2 = 477, 203
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        delay(0.1)

def move_direct4():
    pass

def move_direct5():
    pass

def move_direct6():
    pass

def move_direct7():
    pass

def move_direct8():
    pass

def move_direct9():
    pass

while True:
    move_direct1()
    move_direct2()
    move_direct3()
    move_direct4()
    move_direct5()
    move_direct6()
    move_direct7()
    move_direct8()
    move_direct9()


close_canvas()