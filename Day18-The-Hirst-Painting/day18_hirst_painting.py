import turtle as t
import colorgram
import random


tim = t.Turtle()
t.colormode(255)

extracted_colors = colorgram.extract('./Day18-The-Hirst-Painting/image.jpg', 36)
colors = []
for num in range(0, len(extracted_colors)):
    r = (extracted_colors[num].rgb).r
    g = (extracted_colors[num].rgb).g
    b = (extracted_colors[num].rgb).b
    colors.append((r, g, b))

x_cor = -240
y_cor = -240
count = 0

while count <= 6:
    tim.penup()
    tim.setposition(x_cor, y_cor)
    tim.pendown()
    for _ in range(12):
        turtle_color = random.choice(colors)
        tim.dot(25, turtle_color)
        tim.penup()
        tim.forward(45)
        tim.pendown()
    y_cor += 45
    count += 1


screen = t.Screen()
screen.exitonclick()
