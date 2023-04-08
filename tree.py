import turtle 

a = turtle.Turtle()
a.screen.bgcolor('black')
a.pensize(2)
a.color('white')
a.hideturtle()
a.left(90)
a.backward(100)
a.speed(450000)
a.shape('turtle')

def tree(i):
    if i<10:
        return
    else:
        a.forward(i)
        a.color('orange')
        a.circle(2)
        a.color('red')
        a.left(30)

        tree(3*i/4)

        a.right(60)

        tree(3*i/4)

        a.left(30)
        a.backward(i)

tree(100)
turtle.done()