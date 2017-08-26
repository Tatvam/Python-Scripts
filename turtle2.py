import turtle



def draw_circle(brad):
    brad.right(10)
    for i in range(1, 5):
        brad.forward(100)
        brad.right(90)
def draw_art():

    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)
    for j in range(1,100):
        draw_circle(brad)


    turtle.exitonclick()




draw_art()