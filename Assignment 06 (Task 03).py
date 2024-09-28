import abc
import tkinter as tk

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def draw(self, canvas, x, y):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self, canvas, x, y):
        canvas.create_rectangle(x, y, x + self.width, y + self.height, outline="black", fill="purple")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def draw(self, canvas, x, y):
        canvas.create_oval(x, y, x + 2 * self.radius, y + 2 * self.radius, outline="black", fill="red")

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Oval(Circle):
    def __init__(self, radius1, radius2):
        super().__init__(radius1)
        self.radius2 = radius2

    def area(self):
        return 3.14 * self.radius * self.radius2

    def draw(self, canvas, x, y):
        canvas.create_oval(x, y, x + 2 * self.radius, y + 2 * self.radius2, outline="black", fill="green")

def main():
    name = tk.Tk()
    name.title("Shapes Drawing")

    canvas = tk.Canvas(name, width=500, height=500)
    canvas.pack()

    rectangle = Rectangle(100, 50)
    rectangle.draw(canvas, 10, 10)

    circle = Circle(50)
    circle.draw(canvas, 120, 10)

    square = Square(200)
    square.draw(canvas, 10, 120)

    oval = Oval(80, 50)
    oval.draw(canvas, 220, 220)

    name.mainloop()

if __name__=="__main__":
    main()