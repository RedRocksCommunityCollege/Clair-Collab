import turtle

def Reset():
    turtle.goto(0,150)
    turtle.clear()

def Tangent_Image():
    i = 0
    j = 0
    for i in range(0,36):
        turtle.forward(50)
        for j in range(0,1):
            turtle.backward(500)
            turtle.forward(1000)
            turtle.backward(500)
            j = j + 1
            turtle.left(10)
            i = i + 1

Reset()
Tangent_Image()
