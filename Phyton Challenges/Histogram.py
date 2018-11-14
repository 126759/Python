import turtle

def draw_bar(t, height):
    t.begin_fill()           
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             
    t.forward(10)

tess = turtle.Turtle()       
tess.color("blue", "red")
tess.pensize(3)

xs = [4, 9, 7]

for a in xs:
    draw_bar(tess, a)