import turtle
from random import randint

#This program creates a small python game using turtle graphics. It ends if the player block collides with the falling block. 
#Control player block with right and left arrow keys. Close window and run again to restart. Good luck!

wn = turtle.Screen();
leo = turtle.Turtle();
wn.setup(500,500);
leo.hideturtle();
wn.tracer(0);
leo.goto(0,0);

#falling rect data
x = randint(-250,-100);
y = 250;

#player block data, p prefix indicates data relating to player block
player = turtle.Turtle();
player.hideturtle();
px, py, pv = -200,-200,4;


def drawSquare(t, sizeH, sizeV, color):
    t.clear();
    t.setheading(0);
    t.color(color);
    t.begin_fill();
    for i in range (2):
        t.forward(sizeH);
        t.right(90);
        t.forward(sizeV);
        t.right(90);
    t.end_fill();

def next_frame():
    global leo, x, y, px, py, pv;
    sizeH=350;
    sizeV=50;
    if(collision(x, y, sizeH, sizeV, px, py)):
        #if true, subsequent calls will also enter loop, return results in no animation
        wn.bgcolor('black');
        return;
    leo.up();
    leo.goto(x,y);
    leo.down();
    drawSquare(leo, sizeH, sizeV, 'red');
    y -= 5;
    if(y==(-250)):
        y=250;
        x=randint(-250,-100);
    player.clear;
    player.up();
    player.goto(px,py);
    player.down();
    drawSquare(player, 50, 50, 'blue');
    if(px<200 and px>-250):
        px += pv;
    else:
        pv = -pv;
        px += pv;
    wn.ontimer(next_frame, 25);
    wn.update();

#selected pv to better adjust for speed of falling blocks
def handle_left():
    global pv;
    pv = -4;

def handle_right():
    global pv;
    pv = 4;

def collision(x, y, sizeH, sizeV, px, py):
#there is a collision if there is not not a collision
    if((px>x and px<x+sizeH and py<y and py>y-sizeV) or (px+50>x and px+50<x+sizeH and py-50<y and py-50>y-sizeV)):
        return True;
    else:
        return False;

wn.onkeypress(handle_left, 'Left');
wn.onkeypress(handle_right, 'Right');
next_frame();

wn.listen();
wn.mainloop();
