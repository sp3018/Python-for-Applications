import upc
import turtle

"""
barcode_maker.py
=====
1. Ask the user for a barcode
2. Check if the barcode is valid
3. If the barcode is valid, draw a barcode!
4. If the barcode is not valid:
    * ask for another barcode
    * the text on the prompt should display an error message
"""
wn = turtle.Screen();
t = turtle.Turtle();
wn.setup(500,500);
wn.bgcolor('white');
wn.setworldcoordinates(0,0,500,500);
wn.bgcolor('black');
t.pensize(1);
t.fillcolor('black');
wn.bgcolor('white');
t.hideturtle();
wn.tracer(0);

#Keep asking for barcodes until a valid one is provided!
barcode_number=wn.textinput('barcode', 'Please enter a bar code.');
while(upc.valid_barcode(barcode_number) == False):
    barcode_number=wn.textinput('barcode', 'NOT A VALID BARCODE \n\n Please enter another barcode');

#barcode is now valid, draw the barcode
bar_widths = upc.generate_bar_widths(barcode_number);
t.up();
t.goto(50, 400);
t.down();

"""
Draw a single bar based on arguments.
l and w are ints indicating the length and width.
Black is a boolean indicating whether or not the bar is shaded black.
"""
def draw_bar(l, w, black):
    if(black):
        t.begin_fill();
    t.setheading(0);
    for i in range(2):
        t.forward(w);
        t.right(90);
        t.forward(l);
        t.right(90);
    if(black):
        t.end_fill();
        
"""
Sets the turtle to the top right corner of drawn barcode.
w is an int indicating the width of the bar.
"""
def setup_next(w):
    t.setheading(0);
    t.up();
    t.forward(w);
    t.down();

#Draw the barcode
for i in range(len(bar_widths)):
    length = 200;
    blackBar = ((i % 2) == 0);
    if(blackBar == False):
        t.up();
    #items in positions for start, middle, end segments are extended
    if((i<3) or (i>27 and i<33) or i>=56):
        length = 220;
    width = int(bar_widths[i])*3;
    draw_bar(length, width, blackBar);
    setup_next(width);
    if(blackBar == False):
        t.down();

wn.update();
wn.mainloop();

