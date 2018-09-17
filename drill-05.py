from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_direct1():
    x, y = 203, 535
    x1, y1 = 203, 535
    x2, y2 = 132, 243
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct2():
    x, y = 132, 243
    x1, y1 = 132, 243
    x2, y2 = 535, 470
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct3():
    x, y = 535, 470
    x1, y1 = 535, 470
    x2, y2 = 477, 203
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct4():
    x, y = 477, 203
    x1, y1 = 477, 203
    x2, y2 = 715, 136
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct5():
    x, y = 715, 236
    x1, y1 = 715, 236
    x2, y2 = 316, 225
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct6():
    x, y = 316, 225
    x1, y1 = 316, 225
    x2, y2 = 510, 92
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct7():
    x, y = 510, 92
    x1, y1 = 510, 92
    x2, y2 = 692, 518
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct8():
    x, y = 692, 518
    x1, y1 = 692, 518
    x2, y2 = 682, 336
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct9():
    x, y = 682, 336
    x1, y1 = 682, 336
    x2, y2 = 712, 349
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

def move_direct10():
    x, y = 712, 349
    x1, y1 = 712, 349
    x2, y2 = 203, 535
    count = 0

    move_x1 = x2 - x1
    move_y1 = y2 - y1

    frame = 0

    while count < 10:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y) 
        update_canvas()
        x = x + move_x1 / 10
        y = y + move_y1 / 10
        count = count + 1
        frame = (frame + 1) % 8 
        update_canvas()
        delay(0.1)
        get_events()

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
    move_direct10()


close_canvas()
