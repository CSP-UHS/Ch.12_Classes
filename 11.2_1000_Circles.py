'''
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
'''

import arcade
import random

arcade.open_window(500, 300, "1000 Circles")
arcade.set_background_color((255, 255, 255))
arcade.start_render()


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw_circle(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)


x_coor = random.randint(0, 500)
y_coor = random.randint(0, 300)
rand_color1 = random.randint(0, 255)
rand_color2 = random.randint(0, 255)
rand_color3 = random.randint(0, 255)

def main():
    x_coor = random.randint(0, 500)
    y_coor = random.randint(0, 300)
    rand_color1 = random.randint(0, 255)
    rand_color2 = random.randint(0, 255)
    rand_color3 = random.randint(0, 255)
    circle1 = Circle(x_coor, y_coor, 10, (rand_color1, rand_color2, rand_color3))
    circle1.draw_circle()


if __name__ == "__main__":
    for i in range(1000):
        main()

arcade.finish_render()
arcade.run()
