import turtle



def draw_circle(angie,brad):
    angie.circle(100)
    for i in range(1, 5):
        brad.forward(100)
        brad.right(90)
def draw_art():
    import chicken_turtle_util

    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)
    angie = turtle.Turtle()
    angie.shape('arrow')
    for j in range(1,100):
        draw_circle(angie,brad)


    turtle.exitonclick()




draw_art()